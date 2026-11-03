"""a08: a weight-only guess at the sign of the u edits (a06's gate/up cosine proxy was noise).

If the residual entering L22's MLP already points toward 'Wait' (x = alpha * u), neuron j's write back along u is
    c_j(alpha) = silu(alpha * g_j . u~) * (alpha * up_j . u~) * (u . W_down[:, j]),   u~ = (1 + w_norm) * u
(RMS scale folded into alpha). Summed over a set of columns, c < 0 means that set brakes 'Wait' once it is coming,
c > 0 means it feeds it. An edit that scales those columns' u-component by (1 + s) changes the u-write by s * c.
This is a bilinear readout of the weights at one chosen input direction, not a forward pass.

Calibration on 0.8B, where evals give the answer: the top-64 |u.W| columns were a strong net brake (P64 removed them,
'Wait' x33; A64 doubled them, 'Wait' / 13), and post-training's u-delta across L22 was a weak net promoter
(D_full reverted it, 'Wait' 3.22 -> 2.51). Two bits; a coin agrees with both 25% of the time.
Output: LOGS/a08_self_gain.json
"""
import json

import torch
import torch.nn.functional as F
from safetensors import safe_open

from common import BASE_WEIGHTS, LOGS, MODEL, P, W

torch.set_grad_enabled(False)
L = 22
d = torch.load(LOGS / "a04_directions.pt")
u, r = d["u"].float(), d["r"].float()
u, r = u / u.norm(), r / r.norm()

Wd = W("mlp.down_proj.weight", L)
G = W("mlp.gate_proj.weight", L)
Up = W("mlp.up_proj.weight", L)
nw = 1.0 + W("post_attention_layernorm.weight", L)
Wd_b = safe_open(str(BASE_WEIGHTS), "pt").get_tensor(P + f"layers.{L}.mlp.down_proj.weight").float()

# alpha: put the typical |gate pre-activation| at a realistic size. A residual of RMS 1 has norm sqrt(hidden);
# alpha = sqrt(hidden) means "the whole normalized residual points along u" (upper bound); smaller = partial.
H = Wd.shape[0]


def gains(x, coef, alpha):
    xt = nw * x
    gz, uz = alpha * (G @ xt), alpha * (Up @ xt)
    return F.silu(gz) * uz * coef  # per column


coef = u @ Wd          # u-write of each column (what P64/A64 scale)
coef_dW = u @ (Wd - Wd_b)  # post-training's u-write (what D_full reverts)
top64 = torch.topk(coef.abs(), 64).indices
k_prop = round(64 * Wd.shape[1] / 3584)  # same column fraction as 64 of 0.8B's 3584
topk_prop = torch.topk(coef.abs(), k_prop).indices
gen = torch.Generator().manual_seed(1)

out = dict(model=MODEL, layer=L, hidden=H, columns=Wd.shape[1], k_prop=k_prop, by_alpha={})
for frac in (0.1, 0.25, 0.5, 1.0):
    alpha = frac * H ** 0.5
    c = gains(u, coef, alpha)
    c_dW = gains(u, coef_dW, alpha)
    # Random 64-column sets: the per-column gains are heavy-tailed (a few columns carry most of it), so a z-score
    # against random sets is unstable. Report the 2.5/50/97.5 percentiles instead, and how concentrated top64 is.
    rnd = torch.stack([c[torch.randperm(len(c), generator=gen)[:64]].sum() for _ in range(2000)])
    q = torch.quantile(rnd, torch.tensor([0.025, 0.5, 0.975]))
    by_size = c[top64].abs().sort(descending=True).values
    rec = dict(
        top64_sum=c[top64].sum().item(),
        top64_neg_frac=(c[top64] < 0).float().mean().item(),
        top64_share_of_layer=(c[top64].sum() / c.sum()).item(),
        top5_share_of_top64_abs=(by_size[:5].sum() / by_size.sum()).item(),
        topk_prop_sum=c[topk_prop].sum().item(),
        random64_p2_5=q[0].item(), random64_median=q[1].item(), random64_p97_5=q[2].item(),
        random64_below_top64=(rnd <= c[top64].sum()).float().mean().item(),
        all_columns_sum=c.sum().item(),
        post_training_delta_sum=c_dW.sum().item(),  # D_full removes this; >0 means post-training's u-delta fed Wait
        control_r_top64_sum=gains(r, r @ Wd, alpha)[torch.topk((r @ Wd).abs(), 64).indices].sum().item(),
    )
    out["by_alpha"][f"{frac}*sqrt(H)"] = {k: round(v, 5) for k, v in rec.items()}
    print(f"alpha {frac:4}*sqrt(H): top64 {rec['top64_sum']:+.4f} = {rec['top64_share_of_layer']:.0%} of layer "
          f"(neg {rec['top64_neg_frac']:.2f}, top5 carry {rec['top5_share_of_top64_abs']:.0%}); random64 95% "
          f"[{rec['random64_p2_5']:+.4f}, {rec['random64_p97_5']:+.4f}]  top{k_prop} {rec['topk_prop_sum']:+.4f}  "
          f"post-training delta {rec['post_training_delta_sum']:+.4f}  r-control {rec['control_r_top64_sum']:+.4f}")

# Which neurons carry it. rank = position by |u.W_j| (what the top-k edits select on); cos = row direction vs u~.
alpha = 0.25 * H ** 0.5
c = gains(u, coef, alpha)
ut = nw * u
rank = torch.empty_like(coef, dtype=torch.long)
rank[torch.argsort(coef.abs(), descending=True)] = torch.arange(len(coef))
carriers = []
print(f"\ncarriers at alpha 0.25*sqrt(H) (layer sum {c.sum().item():+.4f}):")
for j in torch.argsort(c.abs(), descending=True)[:8].tolist():
    rec = dict(col=j, coef_rank=rank[j].item(), coef=coef[j].item(), c=c[j].item(), share=(c[j] / c.sum()).item(),
               gate_u=(G[j] @ ut).item(), up_u=(Up[j] @ ut).item(),
               cos_gate_u=F.cosine_similarity(G[j], ut, 0).item(), cos_up_u=F.cosine_similarity(Up[j], ut, 0).item(),
               cos_down_u=F.cosine_similarity(Wd[:, j], u, 0).item())
    carriers.append({k: round(v, 5) if isinstance(v, float) else v for k, v in rec.items()})
    print(f"  col {j:5d} (|u.W| rank {rec['coef_rank']:3d})  c {rec['c']:+.4f} ({rec['share']:.0%})  "
          f"cos(gate,u) {rec['cos_gate_u']:+.3f}  cos(up,u) {rec['cos_up_u']:+.3f}  cos(down,u) {rec['cos_down_u']:+.3f}")
out["carriers"] = carriers
typical = F.cosine_similarity(G, ut[None], 1).abs()
out["typical_abs_cos_gate_u"] = dict(median=typical.median().item(), p99=torch.quantile(typical, 0.99).item())
print(f"  typical |cos(gate,u)|: median {out['typical_abs_cos_gate_u']['median']:.3f}, "
      f"p99 {out['typical_abs_cos_gate_u']['p99']:.3f}")
json.dump(out, open(LOGS / "a08_self_gain.json", "w"), indent=1)
