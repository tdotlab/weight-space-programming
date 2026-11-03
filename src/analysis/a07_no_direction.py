"""a07: is there a weight-space direction behind 'No,' the way u (L22) is behind 'Wait'?

A64 cut 'Wait' 13x but 'No,' stayed at baseline and the remaining loops run on 'No, ...'.
For L14-L23, take the top-16 left singular vectors of the post-training delta of down_proj (instruct - base),
score each by logit-lens z for 'No'/' No' (and 'Wait', commit tokens for reference), and report the best.
Also scores u itself and the unembedding-derived 'No' direction. Weight math only.
Output: logs/a07_no_direction.json, logs/a07_no_direction.pt
"""
import json

import torch
from safetensors import safe_open

from common import LOGS, P, TOK, W, token_z, unembed_stats

torch.set_grad_enabled(False)
BASE = safe_open(str(BASE_WEIGHTS), "pt")
PROBE = ["No", " No", "Wait", " Wait", "Hmm", "Actually", "Therefore", " So", "</think>", "\n\n"]
ids = [TOK[t] for t in PROBE]
K = 16

u = torch.load(LOGS / "a04_directions.pt")["u"].float()
u = u / u.norm()
out = dict(probe=PROBE, u_z=dict(zip(PROBE, [round(v, 2) for v in token_z(u[:, None], ids)[:, 0].tolist()])), layers={})

best = []
for L in range(14, 24):
    Wi = W("mlp.down_proj.weight", L)
    Wb = BASE.get_tensor(P + f"layers.{L}.mlp.down_proj.weight").float()
    U, S, _ = torch.linalg.svd(Wi - Wb, full_matrices=False)
    U = U[:, :K]
    Z = token_z(U, ids)  # (len(PROBE), K)
    # orient each singular vector so it promotes 'No'
    sgn = torch.sign(Z[0]).clamp_min(0) * 2 - 1
    sgn[sgn == 0] = 1
    Z = Z * sgn[None]
    U = U * sgn[None]
    energy = (S[:K] ** 2 / (S ** 2).sum()).tolist()
    rows = []
    for k in range(K):
        z = dict(zip(PROBE, [round(v, 2) for v in Z[:, k].tolist()]))
        rows.append(dict(k=k, energy=round(energy[k], 4), cos_u=round(abs((U[:, k] @ u).item()), 3), z=z))
        best.append((Z[0, k].item(), L, k, U[:, k].clone(), z, energy[k]))
    out["layers"][L] = rows

best.sort(key=lambda t: -t[0])
out["top_no_directions"] = [dict(layer=L, k=k, energy=round(e, 4), z=z) for _, L, k, _, z, e in best[:12]]

# unembedding-side 'No' direction: the residual direction whose logit lens most favors 'No' (through final norm)
E, g, mu, cov = unembed_stats()
d = (E[TOK["No"]] - mu) / g
d = d / d.norm()
out["unembed_No_z"] = dict(zip(PROBE, [round(v, 2) for v in token_z(d[:, None], ids)[:, 0].tolist()]))
out["cos_u_unembedNo"] = round((u @ d).item(), 3)

json.dump(out, open(LOGS / "a07_no_direction.json", "w"), indent=1)
torch.save(dict(best=[(L, k, v) for _, L, k, v, _, _ in best[:12]], unembed_No=d), LOGS / "a07_no_direction.pt")
print("u:", out["u_z"])
print("unembed No dir:", out["unembed_No_z"], "cos with u", out["cos_u_unembedNo"])
for r in out["top_no_directions"]:
    print(r)
