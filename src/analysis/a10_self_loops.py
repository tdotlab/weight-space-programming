"""a10: is the L22 'Wait' brake (a08/a09) one of a class? Scan every MLP neuron in every layer for a self-loop.

A SwiGLU neuron j reads its own write direction d = W_down[:, j] when its gate and up rows (times the RMSNorm gain)
line up with d. Feed it s*d, where s = sign(cos(gate, d)) is the side that opens the gate. Then
act = silu(|.|) * (s * up.d) and the write along d has sign s * sign(up.d). So it is a brake (writes against its
input) iff up.d < 0, and an amplifier iff up.d > 0, whatever the gate's sign. Strength ~ |cos(gate,d)| * |cos(up,d)|.
The concept it brakes or amplifies is s*d, read through the unembedding (logit-lens convention, as in a03/a04).
Output: LOGS/a10_self_loops.json
"""
import json

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer

from common import LOGS, MODEL, MODEL_DIR, N_LAYERS, ROOT, TOK, W, token_z, top_tokens

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
WATCH = ["Wait", " Wait", "No", " No", "Hmm", " Actually", "</think>", " Therefore", "\n\n"]
ids = [TOK[t] for t in WATCH]

rows, strengths, Z, BRAKE = [], [], [], []
for L in range(N_LAYERS):
    nw = 1.0 + W("post_attention_layernorm.weight", L)
    G, Up, Wd = W("mlp.gate_proj.weight", L) * nw, W("mlp.up_proj.weight", L) * nw, W("mlp.down_proj.weight", L)
    D = Wd / Wd.norm(dim=0, keepdim=True)
    cg = F.cosine_similarity(G, D.T, dim=1)
    cu = F.cosine_similarity(Up, D.T, dim=1)
    st = cg.abs() * cu.abs()
    strengths.append(st)
    Z.append(token_z(D * torch.sign(cg)[None], ids))  # z of each watched token for each neuron's concept s*d
    BRAKE.append(cu < 0)
    for j in torch.topk(st, 5).indices.tolist():
        rows.append(dict(layer=L, col=j, strength=st[j].item(), cos_gate=cg[j].item(), cos_up=cu[j].item(),
                         kind="brake" if cu[j] < 0 else "amplifier", side=1 if cg[j] > 0 else -1,
                         down_norm=Wd[:, j].norm().item()))

allst = torch.cat(strengths)
med, p999 = allst.median().item(), torch.quantile(allst, 0.999).item()
rows.sort(key=lambda r: -r["strength"])
top = rows[:20]
for r in top:
    L, j = r["layer"], r["col"]
    v = r["side"] * W("mlp.down_proj.weight", L)[:, j]
    z = token_z(v[:, None], ids)[:, 0]
    r["z"] = {t: round(z[i].item(), 2) for i, t in enumerate(WATCH)}
    r["top_tokens"] = top_tokens(v, tok, 6)[0]

print(f"{MODEL}: self-loop strength |cos(gate,d)|*|cos(up,d)| over {len(allst)} neurons: "
      f"median {med:.4f}, p99.9 {p999:.4f}")
print("top 20 (the concept is s*d; a brake writes against it, an amplifier with it):")
for r in top:
    zs = "  ".join(f"{t.strip() or repr(t)} {v:+.1f}" for t, v in r["z"].items() if abs(v) >= 3)
    print(f"  L{r['layer']:2d} col {r['col']:5d}  {r['strength']:.3f} {r['kind']:9s} cos g {r['cos_gate']:+.2f} "
          f"up {r['cos_up']:+.2f}  top {r['top_tokens']}  |z|>=3: {zs}")
# Search by token, without u: which self-braking neuron's concept writes this token hardest (z * strength)?
# If 'Wait' finds the L22 neuron a08 found through u, the search works, and its answer for 'No' means something.
ST, ZZ, BR = torch.stack(strengths), torch.stack(Z), torch.stack(BRAKE)  # (L, cols), (L, tok, cols), (L, cols)
Lidx = torch.arange(N_LAYERS)[:, None].expand_as(ST)
by_token = {}
print("\nbest self-braking neuron per token (score = z * strength, brakes only, any layer):")
for i, t in enumerate(WATCH):
    sc = torch.where(BR, ZZ[:, i] * ST, torch.tensor(-1e9))
    best = torch.topk(sc.flatten(), 5).indices
    lst = []
    for b in best.tolist():
        L, j = divmod(b, ST.shape[1])
        lst.append(dict(layer=L, col=j, z=round(ZZ[L, i, j].item(), 2), strength=round(ST[L, j].item(), 3),
                        rank_by_strength=int((allst > ST[L, j]).sum())))
    by_token[t] = lst
    print(f"  {t!r:12s} " + "  ".join(f"L{r['layer']} c{r['col']} z {r['z']:+.1f} s {r['strength']:.2f}" for r in lst))
json.dump(dict(model=MODEL, median=med, p99_9=p999, top=top, by_token=by_token),
          open(LOGS / "a10_self_loops.json", "w"), indent=1)
# Each token's best brake as a direction for make_edit.py: its own down column, so a project edit with k=1 at that
# layer selects that column and scale -2 triples it. Keys: brake_Wait, brake_No, ...
dirs = {}
for t in ["Wait", "No", " Actually", " Therefore", "</think>"]:
    b = by_token[t][0]
    key = "brake_" + t.strip().replace("</", "").replace(">", "")
    dirs[key] = W("mlp.down_proj.weight", b["layer"])[:, b["col"]].clone()
    dirs[key + "_where"] = torch.tensor([b["layer"], b["col"]])
torch.save(dirs, LOGS / "a10_directions.pt")
print("saved", (LOGS / "a10_directions.pt").relative_to(ROOT).as_posix(), {k: v.tolist() for k, v in dirs.items() if k.endswith("_where")})
