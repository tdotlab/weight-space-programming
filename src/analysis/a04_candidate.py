"""Step 4: pin down candidate direction u = top left singular vector of (W_down_instruct - W_down_base) at L22,
check how concentrated its writing is across columns, and save u plus a seeded random control direction."""
import json
import torch
from safetensors import safe_open
from transformers import AutoTokenizer
from common import *

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
BASE = safe_open(str(BASE_WEIGHTS), "pt")
L = 22
Wi = W("mlp.down_proj.weight", L)
Wbase = BASE.get_tensor(P + f"layers.{L}.mlp.down_proj.weight").float()
U, S, Vh = torch.linalg.svd(Wi - Wbase, full_matrices=False)
u = U[:, 0]
# fix sign so u promotes 'Wait'
E, g, mu, cov = unembed_stats()
if (E[TOK["Wait"]] @ (g * u)) < 0:
    u = -u

ids = {t: TOK[t] for t in ["Wait", " Wait", "Hmm", "Actually", "</think>", "<|im_end|>", "Therefore", " So", "\n\n"]}
z = token_z(u[:, None], list(ids.values()))[:, 0]
print("u z-scores:", {k: round(v, 2) for k, v in zip(ids, z.tolist())})

proj = u @ Wi  # per-column write along u
tot = (proj ** 2).sum()
frac = lambda k: (torch.topk(proj.abs(), k).values ** 2).sum() / tot
share_of_layer = (tot / (Wi ** 2).sum()).item()
print(f"share of L22 down_proj energy along u: {share_of_layer:.5f} (random expectation {1/Wi.shape[0]:.5f})")
for k in (16, 64, 256, Wi.shape[0]):
    print(f"  top-{k} columns hold {frac(k).item():.3f} of the u-writing")

# base model's writing along u, for comparison
pb = u @ Wbase
print(f"base L22 energy along u: {((pb**2).sum()/(Wbase**2).sum()).item():.5f}")

gen = torch.Generator().manual_seed(0)
r = torch.randn(Wi.shape[0], generator=gen)
r = r / r.norm()
zr = token_z(r[:, None], list(ids.values()))[:, 0]
print("random r z-scores:", {k: round(v, 2) for k, v in zip(ids, zr.tolist())})

torch.save(dict(u=u, r=r, layer=L), LOGS / "a04_directions.pt")
json.dump(dict(layer=L, u_z={k: round(v, 3) for k, v in zip(ids, z.tolist())},
               r_z={k: round(v, 3) for k, v in zip(ids, zr.tolist())}, share_of_layer=share_of_layer,
               top64_frac=frac(64).item(), top256_frac=frac(256).item()),
          open(LOGS / "a04_candidate.json", "w"), indent=1)
