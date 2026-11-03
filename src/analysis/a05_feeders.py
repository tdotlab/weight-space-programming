"""Step 5: who feeds the L22 'Wait' writers?
Target neurons: L22 columns with the largest post-training write along u (d . dW_j > 0, i.e. post-training made them write 'Wait').
Their input side: gate rows (and up rows) of those neurons, scaled by L22's (1+w) post-attention norm.
v_in = top singular direction of the weighted gate-row matrix (the residual direction that best switches them on).
Then: which upstream layers' MLPs (instruct, and post-training delta) write along v_in, and is the delta aligned?"""
import json
import torch
from safetensors import safe_open
from transformers import AutoTokenizer
from common import *

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
BASE = safe_open(str(BASE_WEIGHTS), "pt")
Wb = lambda name, L: BASE.get_tensor(P + f"layers.{L}." + name).float()
u = torch.load(LOGS / "a04_directions.pt")["u"]
L22 = 22

dW = W("mlp.down_proj.weight", L22) - Wb("mlp.down_proj.weight", L22)
c = u @ dW
K = 64
tgt = torch.topk(c, K).indices          # post-training made these write +u ('Wait')
w = c[tgt]
n22 = 1.0 + W("post_attention_layernorm.weight", L22)
G = W("mlp.gate_proj.weight", L22)[tgt] * n22[None]   # (K, 1024)
Uu = W("mlp.up_proj.weight", L22)[tgt] * n22[None]
# sign: SiLU(gate) * up writes along down column; neuron writes +c*u when silu(g)*up > 0. Use gate*sign(up-alignment)
_, Sg, Vg = torch.linalg.svd(G * w[:, None], full_matrices=False)
v_in = Vg[0]
if (G @ v_in).mean() < 0:
    v_in = -v_in
print("gate-row matrix singular values:", [round(x, 3) for x in Sg[:6].tolist()])
print("frac of target gates with positive v_in drive:", ((G @ v_in) > 0).float().mean().item())
hi, lo = top_tokens(v_in, tok, 12)
print("v_in logit lens  + :", hi)
print("                 - :", lo)

rows = []
for L in range(L22):
    Wi = W("mlp.down_proj.weight", L)
    dWL = Wi - Wb("mlp.down_proj.weight", L)
    pi = v_in @ Wi
    pd = v_in @ dWL
    rows.append(dict(layer=L, full_attn=L in FULL_ATTN,
                     inst_top64=round(torch.topk(pi.abs(), 64).values.sum().item(), 3),
                     delta_top64=round(torch.topk(pd.abs(), 64).values.sum().item(), 4),
                     delta_signed_top64=round(torch.topk(pd, 64).values.sum().item() - torch.topk(-pd, 64).values.sum().item(), 4),
                     delta_energy_share=round(((pd ** 2).sum() / (dWL ** 2).sum()).item() * 1024, 3)))
for r in sorted(rows, key=lambda r: -r["delta_energy_share"])[:10]:
    print(r)
print("--- by layer order (delta_energy_share: 1.0 = random) ---")
print([(r["layer"], r["delta_energy_share"]) for r in rows])

torch.save(dict(v_in=v_in, targets=tgt), LOGS / "a05_vin.pt")
json.dump(dict(sv=Sg[:8].tolist(), v_in_promotes=hi, v_in_suppresses=lo, layers=rows),
          open(LOGS / "a05_feeders.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
