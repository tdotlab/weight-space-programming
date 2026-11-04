"""a11: the stop machinery. Which MLP neurons brake '</think>' (and the commit words), and where did they come from?

a08's readout, aimed at a token instead of u. For token t, r_t = (1 + g_final) * (E[t] - mean(E)) is the residual
direction that raises t's centered logit fastest. If the residual entering layer L's MLP leans toward t (x = alpha *
r_t / |r_t|), neuron j writes
    c_j(alpha) = silu(alpha * gate_j . x~) * (alpha * up_j . x~) * (r_t . W_down[:, j]),   x~ = (1 + w_norm) * x
into t's logit. Summed over the layer: c < 0 means the layer brakes t once it is coming, c > 0 means it feeds it.
Weight math at one chosen input direction, not a forward pass.

Calibration: for 'Wait' this must find the a08/a09 brake (0.8B L22 col 573, 2B L22 col 5041) without using u.
Then for each carrier of the '</think>' brake: is it a pretraining feature (as the Wait brake was, a09) or did
post-training build it? And did post-training change the '</think>' embedding row itself (tied embeddings)?
Output: LOGS/a11_stop_gain.json. The chosen brake columns are saved by a12 (LOGS/a12_directions.pt).
"""
import json

import torch
import torch.nn.functional as F
from safetensors import safe_open
from transformers import AutoTokenizer

from common import BASE_WEIGHTS, LOGS, MODEL, MODEL_DIR, N_LAYERS, P, ROOT, TOK, W, top_tokens, token_z

torch.set_grad_enabled(False)
tok = AutoTokenizer.from_pretrained(str(MODEL_DIR))
_b = safe_open(str(BASE_WEIGHTS), "pt")
bkeys = set(_b.keys())


def Wb(name, layer=None):
    k = P + (f"layers.{layer}." if layer is not None else "") + name
    return _b.get_tensor(k if k in bkeys else k.replace(P, "model.")).float()


E, g = W("embed_tokens.weight"), 1.0 + W("norm.weight")
mu = E.mean(0)
TOKENS = ["Wait", "</think>", " Therefore", "Therefore", "Final", " Final"]
for t in TOKENS:
    if t not in TOK:
        TOK[t] = tok.convert_tokens_to_ids(tok.tokenize(t))[0]
R = {t: g * (E[TOK[t]] - mu) for t in TOKENS}  # raw readout: logit write of a column v is R[t] @ v
H = E.shape[1]
ALPHAS = (0.1, 0.25, 0.5)


def gains(m, t, alpha):
    x = m["nw"] * (R[t] / R[t].norm())
    return F.silu(alpha * (m["G"] @ x)) * (alpha * (m["Up"] @ x)) * (R[t] @ m["Wd"])


def layer(L, base=False):
    f = Wb if base else W
    return dict(G=f("mlp.gate_proj.weight", L), Up=f("mlp.up_proj.weight", L), Wd=f("mlp.down_proj.weight", L),
                nw=1.0 + f("post_attention_layernorm.weight", L))


out = dict(model=MODEL, tokens={}, alphas=ALPHAS)
A = 0.25 * H ** 0.5
cache = {L: layer(L) for L in range(N_LAYERS)}
for t in TOKENS:
    rec = dict(token_id=TOK[t], layers=[], carriers=[])
    tot = 0.0
    for L in range(N_LAYERS):
        m = cache[L]
        c = gains(m, t, A)
        tot += c.sum().item()
        rec["layers"].append(dict(layer=L, sum=round(c.sum().item(), 4), neg=round(c[c < 0].sum().item(), 4),
                                  pos=round(c[c > 0].sum().item(), 4)))
        for j in torch.topk(c.abs(), 3).indices.tolist():
            rec["carriers"].append(dict(layer=L, col=j, c=c[j].item(), layer_sum=c.sum().item()))
    rec["carriers"].sort(key=lambda r: -abs(r["c"]))
    rec["carriers"] = rec["carriers"][:10]
    rec["all_layers_sum"] = round(tot, 4)
    out["tokens"][t] = rec
    print(f"\n{MODEL} {t!r} (id {TOK[t]}): self-gain at alpha 0.25*sqrt(H), all layers {tot:+.3f}; "
          f"by layer (L18-23): " + "  ".join(f"L{r['layer']} {r['sum']:+.3f}" for r in rec["layers"][18:]))
    for r in rec["carriers"][:6]:
        m = cache[r["layer"]]
        d = m["Wd"][:, r["col"]]
        z = token_z(d[:, None] * (1 if r["c"] < 0 else 1), [TOK[t]])[0, 0].item()
        hi, lo = top_tokens(d, tok, 6)
        r.update(z_down=round(z, 2), down_promotes=hi, down_suppresses=lo,
                 share_of_layer=round(r["c"] / r["layer_sum"], 3) if r["layer_sum"] else None)
        print(f"  L{r['layer']:2d} col {r['col']:5d}  c {r['c']:+.4f} ({'brake' if r['c'] < 0 else 'feeds'}, "
              f"{r['share_of_layer']:.0%} of its layer)  z(down) {z:+.1f}  down + {hi[:4]}  - {lo[:4]}")

# Alpha robustness for the top carrier of each token.
for t in TOKENS:
    r0 = out["tokens"][t]["carriers"][0]
    m = cache[r0["layer"]]
    r0["by_alpha"] = {f"{a}*sqrt(H)": dict(c=round(gains(m, t, a * H ** 0.5)[r0["col"]].item(), 5),
                                            layer=round(gains(m, t, a * H ** 0.5).sum().item(), 5)) for a in ALPHAS}

# Origin of the '</think>' brakes: base vs instruct, per neuron (a09-style), and the token rows themselves.
print("\norigin (base vs instruct):")
Eb = Wb("embed_tokens.weight")
for t in ["</think>", "Wait", " Therefore"]:
    i = TOK[t]
    print(f"  embedding row {t!r}: |E| instruct {E[i].norm():.3f} base {Eb[i].norm():.3f} "
          f"(median row {E.norm(dim=1).median():.3f}), cos(instruct, base) {F.cosine_similarity(E[i], Eb[i], 0):+.3f}")
    out["tokens"][t]["embedding"] = dict(norm_instruct=E[i].norm().item(), norm_base=Eb[i].norm().item(),
                                         cos_instruct_base=F.cosine_similarity(E[i], Eb[i], 0).item())
for t in ["</think>", " Therefore"]:
    for r in [x for x in out["tokens"][t]["carriers"] if x["c"] < 0][:3]:
        L, j = r["layer"], r["col"]
        mi, mb = cache[L], layer(L, base=True)
        ci, cb = gains(mi, t, A), gains(mb, t, A)
        rel = lambda a, b: ((a - b).norm() / b.norm()).item()
        r["origin"] = dict(c_base=cb[j].item(), layer_sum_base=cb.sum().item(),
                           rel_change_gate=rel(mi["G"][j], mb["G"][j]), rel_change_up=rel(mi["Up"][j], mb["Up"][j]),
                           rel_change_down=rel(mi["Wd"][:, j], mb["Wd"][:, j]),
                           median_rel_change_down=((mi["Wd"] - mb["Wd"]).norm(dim=0) / mb["Wd"].norm(dim=0)).median().item())
        o = r["origin"]
        print(f"  {t!r} L{L} col {j}: c instruct {r['c']:+.4f}, base {o['c_base']:+.4f}; layer instruct "
              f"{r['layer_sum']:+.4f}, base {o['layer_sum_base']:+.4f}; rel change gate {o['rel_change_gate']:.3f} "
              f"up {o['rel_change_up']:.3f} down {o['rel_change_down']:.3f} (median down {o['median_rel_change_down']:.3f})")

json.dump(out, open(LOGS / "a11_stop_gain.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
