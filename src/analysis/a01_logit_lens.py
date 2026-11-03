"""Step 1: logit lens over every MLP neuron's write vector (down_proj column), all layers.
Score = z(restart tokens) - z(</think>): neurons that push 'Wait/Hmm/Actually' over ending the thought."""
import json
import torch
from transformers import AutoTokenizer
from common import *

tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
R = [TOK[t] for t in RESTART]
C = [TOK[t] for t in COMMIT]
END = [TOK["</think>"]]

rows = []
per_layer = []
for L in range(N_LAYERS):
    D = W("mlp.down_proj.weight", L)  # (1024, 3584)
    zR = token_z(D, R).mean(0)
    zE = token_z(D, END)[0]
    zC = token_z(D, C).mean(0)
    score = zR - zE
    norms = D.norm(dim=0)
    for j in range(D.shape[1]):
        rows.append((L, j, score[j].item(), zR[j].item(), zE[j].item(), zC[j].item(), norms[j].item()))
    s = score.abs()
    per_layer.append(dict(layer=L, full_attn=L in FULL_ATTN, max_abs=round(s.max().item(), 2),
                          n_abs_gt6=int((s > 6).sum()), n_abs_gt10=int((s > 10).sum()),
                          mean_col_norm=round(norms.mean().item(), 4)))
    print(per_layer[-1], flush=True)

rows.sort(key=lambda r: -abs(r[2]))
top = []
for L, j, sc, zr, ze, zc, nm in rows[:40]:
    D = W("mlp.down_proj.weight", L)
    hi, lo = top_tokens(D[:, j], tok, 10)
    top.append(dict(layer=L, neuron=j, score=round(sc, 2), z_restart=round(zr, 2), z_endthink=round(ze, 2),
                    z_commit=round(zc, 2), col_norm=round(nm, 4), promotes=hi, suppresses=lo))
    print(f"L{L:2d} n{j:4d} score {sc:+6.2f} zR {zr:+5.2f} zEnd {ze:+5.2f} norm {nm:.3f} | + {hi[:6]} | - {lo[:6]}")

json.dump(dict(per_layer=per_layer, top=top), open(LOGS / "a01_logit_lens.json", "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
