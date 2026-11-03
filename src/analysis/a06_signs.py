"""a06: why did projecting u out of 64 L22 columns (P64) make 'Wait' 33x more frequent?

Weight math only. A SwiGLU neuron's activation is silu(gate.x) * (up.x). When it fires (gate.x > 0),
its sign follows up.x, which tends to share the sign of gate.x if the gate and up rows point the same way.
So sign(cos(gate_j, up_j)) * (u . W_down[:, j]) is a weight-only proxy for whether neuron j pushes
toward (+) or away from (-) 'Wait' when it fires.
Output: logs/a06_signs.json
"""
import json

import torch
from safetensors import safe_open

from common import BASE_WEIGHTS, LOGS, W

BASE = str(BASE_WEIGHTS)
L = 22

u = torch.load(LOGS / "a04_directions.pt")["u"].float()
u = u / u.norm()
r = torch.load(LOGS / "a04_directions.pt")["r"].float()
r = r / r.norm()

Wd = W("mlp.down_proj.weight", L)  # (1024, 3584)
G = W("mlp.gate_proj.weight", L)   # (3584, 1024)
U = W("mlp.up_proj.weight", L)
base = safe_open(BASE, "pt")
Wd_b = base.get_tensor(f"model.language_model.layers.{L}.mlp.down_proj.weight").float()

coef = u @ Wd
coef_b = u @ Wd_b
cos_gu = torch.nn.functional.cosine_similarity(G, U, dim=1)
eff = torch.sign(cos_gu) * coef  # + : pushes toward Wait when it fires

p64 = torch.topk(coef.abs(), 64).indices
r64 = torch.topk((r @ Wd).abs(), 64).indices


def summ(idx, label):
    c, e, cg = coef[idx], eff[idx], cos_gu[idx]
    return dict(
        set=label, n=len(idx),
        coef_pos=int((c > 0).sum()), coef_neg=int((c < 0).sum()),
        cos_gu_mean=round(cg.mean().item(), 3), cos_gu_abs_mean=round(cg.abs().mean().item(), 3),
        eff_pos=int((e > 0).sum()), eff_neg=int((e < 0).sum()),
        eff_sum=round(e.sum().item(), 4), eff_abs_sum=round(e.abs().sum().item(), 4),
        coef_sum=round(c.sum().item(), 4),
        post_training_coef_change_sum=round((coef[idx] - coef_b[idx]).sum().item(), 4),
    )


out = dict(
    note="eff = sign(cos(gate_j, up_j)) * u.W_down[:, j]; positive = pushes toward Wait when firing",
    all_L22=dict(cos_gu_mean=round(cos_gu.mean().item(), 3), cos_gu_abs_mean=round(cos_gu.abs().mean().item(), 3),
                 frac_cos_gt_0p1=round((cos_gu > 0.1).float().mean().item(), 3),
                 frac_cos_lt_m0p1=round((cos_gu < -0.1).float().mean().item(), 3),
                 eff_sum=round(eff.sum().item(), 4)),
    P64=summ(p64, "P64 columns (top |u.W|)"),
    top64_promoters=summ(torch.topk(eff, 64).indices, "top-64 by eff (Wait promoters)"),
    top64_suppressors=summ(torch.topk(-eff, 64).indices, "top-64 by -eff (Wait suppressors)"),
)
out["P64_overlap_with_promoters"] = len(set(p64.tolist()) & set(torch.topk(eff, 64).indices.tolist()))
out["P64_overlap_with_suppressors"] = len(set(p64.tolist()) & set(torch.topk(-eff, 64).indices.tolist()))
json.dump(out, open(LOGS / "a06_signs.json", "w"), indent=1)
print(json.dumps(out, indent=1))
torch.save(dict(eff=eff, cos_gu=cos_gu, coef=coef), LOGS / "a06_signs.pt")
