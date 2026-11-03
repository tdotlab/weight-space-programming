"""Step 3: what did post-training write? Diff instruct vs base MLP down_proj per layer.
For each layer: relative delta norm, effective rank, and logit lens of top singular directions of dW_down
(left singular vectors live in residual space = what post-training made the MLP write)."""
import json
import torch
from safetensors import safe_open
from transformers import AutoTokenizer
from common import *

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
BASE = safe_open(str(BASE_WEIGHTS), "pt")
bkeys = set(BASE.keys())

def Wb(name, L):
    k = P + f"layers.{L}." + name
    if k not in bkeys:
        k = "model." + f"layers.{L}." + name  # base may use text-only naming
    return BASE.get_tensor(k).float()

R = [TOK[t] for t in ["Wait", " Wait", "Hmm", " Hmm", "Actually", " Actually", "Hold"]]
END = [TOK["</think>"]]
C = [TOK[t] for t in COMMIT]

layers, dirs = [], []
for L in range(N_LAYERS):
    rec = dict(layer=L, full_attn=L in FULL_ATTN)
    for m in ["mlp.down_proj.weight", "mlp.gate_proj.weight", "mlp.up_proj.weight"]:
        A, B = W(m, L), Wb(m, L)
        rec[m.split(".")[1] + "_rel"] = round(((A - B).norm() / B.norm()).item(), 5)
    dW = W("mlp.down_proj.weight", L) - Wb("mlp.down_proj.weight", L)
    U, S, Vh = torch.linalg.svd(dW, full_matrices=False)
    e = (S ** 2) / (S ** 2).sum()
    rec["top1_energy"] = round(e[0].item(), 4)
    rec["top4_energy"] = round(e[:4].sum().item(), 4)
    zr = token_z(U[:, :8], R).mean(0)
    ze = token_z(U[:, :8], END)[0]
    zc = token_z(U[:, :8], C).mean(0)
    sc = (zr - ze)
    rec["sv_doubt_scores"] = [round(x, 2) for x in sc.tolist()]
    rec["sv_endthink_z"] = [round(x, 2) for x in ze.tolist()]
    layers.append(rec)
    print({k: v for k, v in rec.items() if k not in ("sv_endthink_z",)}, flush=True)
    for i in range(8):
        dirs.append(dict(layer=L, sv=i, s=S[i].item(), energy=e[i].item(), doubt=sc[i].item(),
                         z_restart=zr[i].item(), z_end=ze[i].item(), z_commit=zc[i].item()))

dirs.sort(key=lambda r: -abs(r["doubt"]))
print("\nTop singular directions of post-training delta by |restart - </think>| z:")
for r in dirs[:16]:
    U = torch.linalg.svd(W("mlp.down_proj.weight", r["layer"]) - Wb("mlp.down_proj.weight", r["layer"]), full_matrices=False)[0]
    hi, lo = top_tokens(U[:, r["sv"]], tok, 10)
    r["promotes"], r["suppresses"] = hi, lo
    print(f"L{r['layer']:2d} sv{r['sv']} energy {r['energy']:.3f} doubt {r['doubt']:+6.2f} zR {r['z_restart']:+5.2f} "
          f"zEnd {r['z_end']:+5.2f} | + {hi[:7]} | - {lo[:7]}")

json.dump(dict(layers=layers, top_dirs=dirs[:40]), open(LOGS / "a03_base_diff.json", "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
