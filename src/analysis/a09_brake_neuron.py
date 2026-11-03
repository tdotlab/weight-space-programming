"""a09: the L22 'Wait brake' neuron found by a08, compared between base and instruct.

a08 found one L22 MLP neuron carrying ~95% of the layer's self-gain along u (0.8B col 573, 2B col 5041): its gate and
up rows and its down column all line up with u, so it fires when the residual points toward 'Wait' and writes -u back.
Questions: does the base model already have it, did post-training weaken it, and how much of u (the top singular
vector of post-training's down_proj delta) is this one column's change?
Output: LOGS/a09_brake_neuron.json
"""
import json

import torch
import torch.nn.functional as F
from safetensors import safe_open

from common import BASE_WEIGHTS, LOGS, MODEL, P, W

torch.set_grad_enabled(False)
L = 22
d = torch.load(LOGS / "a04_directions.pt")
u = d["u"].float()
u = u / u.norm()
_b = safe_open(str(BASE_WEIGHTS), "pt")


def Wb(name):
    return _b.get_tensor(P + f"layers.{L}.{name}").float()


inst = dict(G=W("mlp.gate_proj.weight", L), Up=W("mlp.up_proj.weight", L), Wd=W("mlp.down_proj.weight", L),
            nw=1.0 + W("post_attention_layernorm.weight", L))
base = dict(G=Wb("mlp.gate_proj.weight"), Up=Wb("mlp.up_proj.weight"), Wd=Wb("mlp.down_proj.weight"),
            nw=1.0 + Wb("post_attention_layernorm.weight"))
H = inst["Wd"].shape[0]
alpha = 0.25 * H ** 0.5


def neuron(m, j):
    ut = m["nw"] * u
    gz, uz, cf = alpha * (m["G"][j] @ ut), alpha * (m["Up"][j] @ ut), u @ m["Wd"][:, j]
    return dict(cos_gate_u=F.cosine_similarity(m["G"][j], ut, 0).item(),
                cos_up_u=F.cosine_similarity(m["Up"][j], ut, 0).item(),
                cos_down_u=F.cosine_similarity(m["Wd"][:, j], u, 0).item(),
                gate_norm=m["G"][j].norm().item(), up_norm=m["Up"][j].norm().item(),
                down_norm=m["Wd"][:, j].norm().item(), u_write=cf.item(),
                self_gain=(F.silu(gz) * uz * cf).item())


def layer_gain(m):
    ut = m["nw"] * u
    return (F.silu(alpha * (m["G"] @ ut)) * (alpha * (m["Up"] @ ut)) * (u @ m["Wd"])).sum().item()


c_inst = F.silu(alpha * (inst["G"] @ (inst["nw"] * u))) * (alpha * (inst["Up"] @ (inst["nw"] * u))) * (u @ inst["Wd"])
j = c_inst.abs().argmax().item()
dW = inst["Wd"] - base["Wd"]
proj = u @ dW  # u-component of each column's post-training change; sum of squares = sigma_0^2
out = dict(model=MODEL, layer=L, col=j, alpha="0.25*sqrt(H)",
           instruct=neuron(inst, j), base=neuron(base, j),
           layer_self_gain=dict(instruct=layer_gain(inst), base=layer_gain(base)),
           share_of_sigma0_sq=(proj[j] ** 2 / (proj ** 2).sum()).item(),
           sigma0_sq_rank=(proj.abs() > proj[j].abs()).sum().item(),
           cos_dW_col_u=F.cosine_similarity(dW[:, j], u, 0).item(),
           rel_change=dict(gate=((inst["G"][j] - base["G"][j]).norm() / base["G"][j].norm()).item(),
                           up=((inst["Up"][j] - base["Up"][j]).norm() / base["Up"][j].norm()).item(),
                           down=(dW[:, j].norm() / base["Wd"][:, j].norm()).item(),
                           down_layer_median=(dW.norm(dim=0) / base["Wd"].norm(dim=0)).median().item()))

print(f"{MODEL} L{L} col {j}")
for k in ("instruct", "base"):
    n = out[k]
    print(f"  {k:8s} cos(gate,u) {n['cos_gate_u']:+.3f}  cos(up,u) {n['cos_up_u']:+.3f}  "
          f"cos(down,u) {n['cos_down_u']:+.3f}  u-write {n['u_write']:+.4f}  self-gain {n['self_gain']:+.4f}  "
          f"|g| {n['gate_norm']:.3f} |up| {n['up_norm']:.3f} |down| {n['down_norm']:.3f}")
g = out["layer_self_gain"]
print(f"  layer self-gain along u: instruct {g['instruct']:+.4f}, base {g['base']:+.4f}")
print(f"  this column's share of sigma_0^2 (post-training delta along u): {out['share_of_sigma0_sq']:.1%} "
      f"(rank {out['sigma0_sq_rank']}); cos(delta column, u) {out['cos_dW_col_u']:+.3f}")
rc = out["rel_change"]
print(f"  relative post-training change: gate {rc['gate']:.3f}  up {rc['up']:.3f}  down {rc['down']:.3f} "
      f"(median down column {rc['down_layer_median']:.3f})")
json.dump(out, open(LOGS / "a09_brake_neuron.json", "w"), indent=1)
