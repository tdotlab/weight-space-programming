"""a12: does a11's self-gain readout predict what an edit does to its token? Calibrate it on every evaluated edit,
then use it to set round 2's doses.

For each built edit of $WSP_MODEL (edited/*/EDIT.json) the self-gain of each watched token is recomputed, summed
over all 24 layers (a11's c at alpha 0.25*sqrt(H)), and set beside the change in that token's rate per 1000
reasoning chars in the edit's eval, against the baseline run on the same problems. Edits only touch down_proj and c
is linear in the down column, so gate/up activations are computed once from the original.
If the readout orders the evaluated edits the way the evals did (P64 removed the Wait brake and 'Wait' ran away;
A64h..A64x5 added to it), it can pick doses for new edits before any eval. Candidate edits are read out
analytically: scaling column j of layer L by f adds (f - 1) * c_j to every token's gain.
Also saves LOGS/a12_directions.pt: the down columns of the chosen commit brakes (brake_Final, brake_Therefore and
their _where), for make_edit.py --kind project --k 1 (scale s multiplies the column by 1 - s).
Output: LOGS/a12_edit_readout.json, LOGS/a12_directions.pt
"""
import json, re

import torch
import torch.nn.functional as F
from safetensors import safe_open

from common import LOGS, MODEL, N_LAYERS, P, ROOT, TOK, W

torch.set_grad_enabled(False)
SIZE = MODEL.split("-")[-1]
E, g = W("embed_tokens.weight"), 1.0 + W("norm.weight")
mu = E.mean(0)
H = E.shape[1]
A = 0.25 * H ** 0.5
TOKENS = ["Wait", "No", "Final", "Therefore"]
MARK = {"Wait": r"(?<![A-Za-z])[Ww]ait", "No": r"(?<![A-Za-z])No[,.]", "Final": r"(?<![A-Za-z])Final",
        "Therefore": r"(?<![A-Za-z])Therefore"}
R = {t: g * (E[TOK[t]] - mu) for t in TOKENS}
FN = "model.safetensors-00001-of-00001.safetensors"
# Commit brakes from a11 (largest negative c for 'Final' / 'Therefore'); checked against the readout below.
BRAKES = {"Qwen3.5-0.8B": {"Final": (23, 1238), "Therefore": (22, 2001)},
          "Qwen3.5-2B": {"Final": (23, 6022), "Therefore": (22, 3895)}}[MODEL]
WAIT_BRAKE = {"Qwen3.5-0.8B": (22, 573), "Qwen3.5-2B": (22, 5041)}[MODEL]


def acts(L):
    nw = 1.0 + W("post_attention_layernorm.weight", L)
    G, Up = W("mlp.gate_proj.weight", L), W("mlp.up_proj.weight", L)
    out = {}
    for t, r in R.items():
        x = nw * (r / r.norm())
        out[t] = F.silu(A * (G @ x)) * (A * (Up @ x))  # neuron activations when the residual leans toward t
    return out


ACT = {L: acts(L) for L in range(N_LAYERS)}
ORIG = {L: W("mlp.down_proj.weight", L) for L in range(N_LAYERS)}


def c_of(down, L):
    """Per-neuron self-gain c_j of layer L for every token, given that layer's down_proj."""
    return {t: ACT[L][t] * (R[t] @ down) for t in TOKENS}


def readout(down):
    tot = {t: 0.0 for t in TOKENS}
    for L in range(N_LAYERS):
        for t, c in c_of(down[L], L).items():
            tot[t] += c.sum().item()
    return tot


def rates(run, ids):
    rows = {json.loads(l)["id"]: json.loads(l) for l in open(run / "results.jsonl", encoding="utf-8")}
    kch = sum(len(rows[i]["reasoning"]) for i in ids) / 1000
    return {t: sum(len(re.findall(MARK[t], rows[i]["reasoning"])) for i in ids) / kch for t in TOKENS}


def observed(name):
    """Marker rates per kchar in the edit's eval and in the baseline on the same problems."""
    mdir = ROOT / "runs" / SIZE / "math500"
    stem = {"D_full": "Dfull"}.get(name, name[3:] if name.startswith("2B_") else name)
    run = mdir / (stem + ("_8k_q8" if SIZE == "2B" else "_q8"))
    base = mdir / ("base_8k_q8" if SIZE == "2B" else "base_q8")
    if not (run / "results.jsonl").exists():
        return None
    ids = {json.loads(l)["id"] for l in open(run / "results.jsonl", encoding="utf-8")} & \
          {json.loads(l)["id"] for l in open(base / "results.jsonl", encoding="utf-8")}
    e, b = rates(run, ids), rates(base, ids)
    return dict(run=run.name, n=len(ids), edit={t: round(v, 3) for t, v in e.items()},
                base={t: round(v, 3) for t, v in b.items()})


g0 = readout(ORIG)
rows = [dict(name="original", gain=g0, observed=None)]
starts = {"original": ORIG}
for d in sorted((ROOT / "edited").iterdir()):
    if not (d / "EDIT.json").exists():
        continue
    spec = json.load(open(d / "EDIT.json"))
    if spec.get("model", "Qwen3.5-0.8B") != MODEL:
        continue
    f = safe_open(str(d / FN), "pt")
    down = {}
    for L in range(N_LAYERS):
        t = f.get_tensor(P + f"layers.{L}.mlp.down_proj.weight").float()
        down[L] = ORIG[L] if torch.equal(t, ORIG[L]) else t
    starts[d.name] = down
    rows.append(dict(name=d.name, spec={k: spec.get(k) for k in ("kind", "dir", "start", "layers", "k", "scale")},
                     changed_layers=[L for L in range(N_LAYERS) if down[L] is not ORIG[L]],
                     gain=readout(down), observed=observed(d.name)))

print(f"{MODEL}: all-layer self-gain at alpha 0.25*sqrt(H) (negative = the token brakes itself), change vs original,")
print("and the token's rate per kchar in the edit's eval / baseline on the same problems (n).")
print(f"{'edit':12s} {'n':>4s}" + "".join(f"{t:>30s}" for t in TOKENS))
print(f"{'original':12s} {'':>4s}" + "".join(f"{g0[t]:+9.3f}{'':21s}" for t in TOKENS))
for r in rows[1:]:
    o = r["observed"]
    s = f"{r['name']:12s} {o['n'] if o else '-':>4}"
    for t in TOKENS:
        dg = r["gain"][t] - g0[t]
        if o:
            ratio = o["edit"][t] / o["base"][t] if o["base"][t] else float("nan")
            s += f"{r['gain'][t]:+9.3f} ({dg:+7.3f}) {o['edit'][t]:6.2f}/{o['base'][t]:5.2f}"
        else:
            s += f"{r['gain'][t]:+9.3f} ({dg:+7.3f}) {'not run':>12s}"
    print(s)

# Candidate commit-brake edits, read out analytically on top of a start model.
start = "2B_A64x3" if SIZE == "2B" else "A64x3"
print(f"\ncommit brakes ({MODEL}); per-token c of each brake neuron in the original:")
dirs = {}
for name, (L, j) in BRAKES.items():
    c = c_of(ORIG[L], L)
    rank = (c[name] < c[name][j]).sum().item()
    print(f"  {name:9s} L{L} col {j}: c " + "  ".join(f"{t} {c[t][j].item():+.4f}" for t in TOKENS) +
          f"   (rank {rank} most negative in its layer for {name!r})")
    dirs["brake_" + name] = ORIG[L][:, j].clone()
    dirs["brake_" + name + "_where"] = torch.tensor([L, j])
    # make_edit picks the top-|coef| column for this direction; in the start models round 2 builds on it must be
    # j itself, unchanged from the original (D_full rewrites all of L22 a little; nothing builds on it).
    for sname in ("original", start):
        down = starts[sname]
        u = dirs["brake_" + name] / dirs["brake_" + name].norm()
        top = torch.topk((u @ down[L]).abs(), 2)
        assert top.indices[0].item() == j and torch.equal(down[L][:, j], ORIG[L][:, j]), (sname, name, top)
        print(f"    {sname}: make_edit selects col {top.indices[0].item()} (coef {top.values[0]:.3f}; "
              f"runner-up col {top.indices[1].item()} at {top.values[1]:.3f})")
torch.save(dirs, LOGS / "a12_directions.pt")
print("  saved", (LOGS / "a12_directions.pt").relative_to(ROOT).as_posix())

gs = next(r["gain"] for r in rows if r["name"] == start)
CANDS = [("Final x0.5", {"Final": 0.5}), ("Final x0", {"Final": 0.0}), ("Final x-1", {"Final": -1.0}),
         ("Therefore x0", {"Therefore": 0.0}), ("Final x0 + Therefore x0", {"Final": 0.0, "Therefore": 0.0})]
cand_out = []
for base_name, bg in (("original", g0), (start, gs)):
    print(f"\ncandidates on {base_name}: all-layer self-gain after the edit (change)")
    for label, fs in CANDS:
        new = dict(bg)
        for name, fac in fs.items():
            L, j = BRAKES[name]
            c = c_of(starts[base_name][L], L)
            for t in TOKENS:
                new[t] += (fac - 1.0) * c[t][j].item()
        cand_out.append(dict(start=base_name, edit=label, factors=fs, gain=new))
        print(f"  {label:26s}" + "".join(f"  {t} {new[t]:+8.3f} ({new[t] - bg[t]:+7.3f})" for t in TOKENS))

json.dump(dict(model=MODEL, alpha="0.25*sqrt(H)", marker_regex=MARK, brakes=BRAKES, rows=rows,
               candidates=cand_out), open(LOGS / "a12_edit_readout.json", "w"), indent=1)
