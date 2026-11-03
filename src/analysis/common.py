"""Shared weight loading. Weight math only: nothing here runs the network."""
import os
from functools import lru_cache
from pathlib import Path

import torch
from safetensors import safe_open

TOOLS = Path(os.environ.get("WSP_TOOLS", Path.home() / "tools"))  # models, llama.cpp, sources
MODEL_DIR = TOOLS / "models" / "Qwen3.5-0.8B"
BASE_WEIGHTS = TOOLS / "models" / "Qwen3.5-0.8B-Base" / "model.safetensors-00001-of-00001.safetensors"
WEIGHTS = MODEL_DIR / "model.safetensors-00001-of-00001.safetensors"
ROOT = Path(__file__).resolve().parents[2]
LOGS = ROOT / "logs"
P = "model.language_model."
N_LAYERS = 24
FULL_ATTN = {3, 7, 11, 15, 19, 23}

TOK = {
    "</think>": 248069, "<think>": 248068, "<|im_end|>": 248046,
    "Wait": 13784, " Wait": 13428, "wait": 11158, " wait": 3655,
    "Hmm": 77264, " Hmm": 85152, "Actually": 50821, " Actually": 32645, "Hold": 45847,
    "Therefore": 52971, " Therefore": 14833, "Thus": 43022, "So": 4272, " So": 1987, "Final": 18770,
    "No": 2665, " No": 2233, "\n\n": 271,
}
RESTART = ["Wait", " Wait", "wait", " wait", "Hmm", " Hmm", "Actually", " Actually", "Hold"]
COMMIT = ["Therefore", " Therefore", "Thus", "So", " So", "Final"]


@lru_cache(None)
def _f():
    return safe_open(str(WEIGHTS), "pt")


def W(name, layer=None):
    key = P + (f"layers.{layer}." if layer is not None else "") + name
    return _f().get_tensor(key).float()


@lru_cache(None)
def unembed_stats():
    """Tied unembedding E, effective final-norm scale (1+g), embedding mean and covariance.
    Logit of residual direction x (pre-norm, ignoring the shared RMS scale) = E @ ((1+g) * x)."""
    E = W("embed_tokens.weight")
    g = 1.0 + W("norm.weight")
    mu = E.mean(0)
    Ec = E - mu
    cov = (Ec.T @ Ec) / E.shape[0]
    return E, g, mu, cov


def token_z(U, ids):
    """U: (1024, k) residual-space write vectors. Returns z-scores (len(ids), k) of each token's logit
    relative to that vector's logit distribution over the whole vocab."""
    E, g, mu, cov = unembed_stats()
    V = g[:, None] * U
    sd = torch.sqrt(torch.einsum("ik,ij,jk->k", V, cov, V)).clamp_min(1e-8)
    return (E[ids] @ V - (mu @ V)[None]) / sd[None]


def top_tokens(v, tok, k=15):
    E, g, mu, cov = unembed_stats()
    lg = E @ (g * v)
    hi = torch.topk(lg, k).indices.tolist()
    lo = torch.topk(-lg, k).indices.tolist()
    dec = lambda ids: [tok.decode([i]) for i in ids]
    return dec(hi), dec(lo)
