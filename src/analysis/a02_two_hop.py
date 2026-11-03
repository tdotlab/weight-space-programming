"""Step 2: two-hop circuit trace, weights only.

Hop 2 (late, direct): which neurons in layers 16-23 push restart tokens over </think> ("doubt writers")
and which push </think>/end tokens ("closers")?  Score = z(restart) - z(</think>) from the logit lens.
Hop 1 (upstream): for every neuron j in layers 0..L'-1, path weight into a late neuron k at layer L' =
  W_down[L][:, j] . ((1 + w_postnorm[L']) * gate_k[L'])     (gate pre-activation; up ignored for sign)
Upstream neurons that excite doubt writers and inhibit closers get a high 'doubt-feeding' score.
Then: the dominant shared direction of the top doubt-feeders' write vectors, and which layers own it.
Ignores attention mixing and RMS scale (approximation, logged)."""
import json
import torch
from transformers import AutoTokenizer
from common import *

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
R = [TOK[t] for t in ["Wait", " Wait", "Hmm", " Hmm", "Actually", " Actually", "Hold"]]
END = [TOK["</think>"]]

# Hop 2: late neurons scored by direct effect
late = []
for L in range(14, N_LAYERS):
    D = W("mlp.down_proj.weight", L)
    s = token_z(D, R).mean(0) - token_z(D, END)[0]
    late.append(s)
late = torch.stack(late)  # (10, 3584)
flat = late.flatten()
K = 40
doubt_idx = torch.topk(flat, K).indices
close_idx = torch.topk(-flat, K).indices
to_lj = lambda i: (14 + i // 3584, i % 3584)
doubters = [to_lj(i.item()) + (flat[i].item(),) for i in doubt_idx]
closers = [to_lj(i.item()) + (flat[i].item(),) for i in close_idx]

# reader vectors (gate rows scaled by that layer's (1+w) post-attn norm), weighted by |direct score|
def readers(group):
    out = []
    for L, k, sc in group:
        n = 1.0 + W("post_attention_layernorm.weight", L)
        out.append((L, n * W("mlp.gate_proj.weight", L)[k], abs(sc)))
    return out

RD, RC = readers(doubters), readers(closers)

# Hop 1: every upstream neuron's path score
feed = {}
for L in range(0, 23):
    D = W("mlp.down_proj.weight", L)  # (1024, 3584)
    Dn = D / D.norm(dim=0, keepdim=True)
    sc = torch.zeros(D.shape[1])
    for (Lk, r, w) in RD:
        if Lk > L:
            sc += w * (r / r.norm()) @ Dn
    for (Lk, r, w) in RC:
        if Lk > L:
            sc -= w * (r / r.norm()) @ Dn
    feed[L] = sc

allsc = torch.cat([feed[L] for L in range(23)])
mu, sd = allsc.mean(), allsc.std()
per_layer = []
for L in range(23):
    z = (feed[L] - mu) / sd
    per_layer.append(dict(layer=L, full_attn=L in FULL_ATTN, n_z_gt3=int((z.abs() > 3).sum()),
                          max_abs_z=round(z.abs().max().item(), 2), top64_mean_abs_z=round(torch.topk(z.abs(), 64).values.mean().item(), 2)))
    print(per_layer[-1])

# Shared direction among top doubt-feeders (by |z|, sign-aligned)
cands = []
for L in range(23):
    z = (feed[L] - mu) / sd
    for j in torch.topk(z.abs(), 64).indices.tolist():
        cands.append((z[j].item(), L, j))
cands.sort(key=lambda t: -abs(t[0]))
top = cands[:256]
V = torch.stack([torch.sign(torch.tensor(zz)) * W("mlp.down_proj.weight", L)[:, j] for zz, L, j in top], 1)
U, S, _ = torch.linalg.svd(V, full_matrices=False)
d = U[:, 0]
print("singular values of top-256 feeder write matrix:", [round(x, 3) for x in S[:8].tolist()])
hi, lo = top_tokens(d, tok, 15)
print("direction d logit lens  + :", hi)
print("                        - :", lo)

# Which layers' MLPs write d? share of each layer's top-64 |projection| mass
own = []
for L in range(N_LAYERS):
    D = W("mlp.down_proj.weight", L)
    p = (d @ D).abs()
    own.append(dict(layer=L, top64_proj_sum=round(torch.topk(p, 64).values.sum().item(), 3),
                    max_proj=round(p.max().item(), 4)))
own.sort(key=lambda r: -r["top64_proj_sum"])
print("layers writing d most strongly:", own[:8])

torch.save(dict(d=d, top=top), LOGS / "a02_direction.pt")
json.dump(dict(doubters=doubters[:15], closers=closers[:15], per_layer=per_layer, sv=S[:16].tolist(),
               d_promotes=hi, d_suppresses=lo, owners=own), open(LOGS / "a02_two_hop.json", "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
