"""Build an edited copy of $WSP_MODEL (default Qwen3.5-0.8B) in edited/<name>/ and convert it to gguf/<name>-f16.gguf.
The original model directory is only read. Every edit is recorded in edited/<name>/EDIT.json and logs/edits.jsonl.

Edit kinds (all on layer L mlp.down_proj, residual-space unit direction d):
  project  : for the k columns with largest |d . W[:, j]|, W[:, j] -= d (d . W[:, j])          (MIT-style)
  revert   : for the k columns with largest |d . dW[:, j]| (dW = instruct - base), W[:, j] -= d (d . dW[:, j])
             k=all reverts post-training's component along d in the whole matrix (rank-1).
Usage: uv run python src/make_edit.py --name D_full --kind revert --dir u --k all
Stacking: --start A64 applies the edit on top of edited/A64/. --dirfile picks the direction file (default a04).
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

import torch
from safetensors import safe_open
from safetensors.torch import save_file

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(os.environ.get("WSP_TOOLS", Path.home() / "tools"))  # models, llama.cpp, sources
MODEL = os.environ.get("WSP_MODEL", "Qwen3.5-0.8B")
ORIG = TOOLS / "models" / MODEL
BASE = TOOLS / "models" / (MODEL + "-Base")
LOGDIR = "logs" if MODEL == "Qwen3.5-0.8B" else "logs/" + MODEL.split("-")[-1]
FNAME = "model.safetensors-00001-of-00001.safetensors"
CONVERT = str(TOOLS / "source-code-of-open-source" / "llama.cpp-b11804" / "convert_hf_to_gguf.py")
P = "model.language_model."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--kind", choices=["project", "revert"], required=True)
    ap.add_argument("--dir", default="u", help="key in --dirfile (u or r in a04; v_in in a05)")
    ap.add_argument("--dirfile", default=LOGDIR + "/a04_directions.pt", help="torch file holding the direction")
    ap.add_argument("--start", default="", help="stack on an existing edit in edited/<start>/ instead of the original")
    ap.add_argument("--layers", default="22")
    ap.add_argument("--k", default="64")
    ap.add_argument("--scale", type=float, default=1.0, help="1.0 = full removal; >1 overshoots")
    a = ap.parse_args()

    out = ROOT / "edited" / a.name
    if out.exists():
        sys.exit(f"{out} exists; pick a new name")
    out.mkdir(parents=True)
    for f in ORIG.iterdir():
        if f.is_file() and f.name != FNAME and not f.name.startswith("."):
            shutil.copy2(f, out / f.name)

    dirs = torch.load(ROOT / a.dirfile)
    d = dirs[a.dir].float()
    d = d / d.norm()

    start = ROOT / "edited" / a.start if a.start else ORIG
    src = safe_open(str(start / FNAME), "pt")
    tensors = {k: src.get_tensor(k) for k in src.keys()}
    meta = src.metadata()
    base = safe_open(str(BASE / FNAME), "pt") if a.kind == "revert" else None

    record = dict(name=a.name, model=MODEL, kind=a.kind, dir=a.dir, dirfile=a.dirfile, start=a.start or "original",
                  layers=a.layers, k=a.k, scale=a.scale,
                  time=time.strftime("%Y-%m-%d %H:%M:%S"), per_layer=[])
    changed = 0
    for L in [int(x) for x in a.layers.split(",")]:
        key = P + f"layers.{L}.mlp.down_proj.weight"
        Wt = tensors[key].float()
        ref = Wt - base.get_tensor(key).float() if base else Wt
        coef = d @ ref  # (3584,)
        k = Wt.shape[1] if a.k == "all" else int(a.k)
        cols = torch.topk(coef.abs(), k).indices
        Wn = Wt.clone()
        Wn[:, cols] -= a.scale * d[:, None] * coef[cols][None, :]
        tensors[key] = Wn.to(tensors[key].dtype)
        diff = (tensors[key].float() != Wt).sum().item()
        changed += diff
        record["per_layer"].append(dict(layer=L, columns=sorted(cols.tolist()) if k <= 256 else f"{k} columns",
                                        weights_changed=int(diff),
                                        rel_change=round(((Wn - Wt).norm() / Wt.norm()).item(), 6)))
    record["weights_changed_total"] = int(changed)
    save_file(tensors, str(out / FNAME), metadata=meta)
    record["sha256"] = hashlib.sha256((out / FNAME).read_bytes()).hexdigest()
    json.dump(record, open(out / "EDIT.json", "w"), indent=1)
    with open(ROOT / "logs" / "edits.jsonl", "a") as f:
        f.write(json.dumps({k: v for k, v in record.items()}) + "\n")
    print(json.dumps({k: v for k, v in record.items() if k != "per_layer"}, indent=1))
    for pl in record["per_layer"]:
        print(f"  L{pl['layer']}: {pl['weights_changed']} weights changed, rel change {pl['rel_change']}")

    gg = ROOT / "gguf" / f"{a.name}-f16.gguf"
    subprocess.run([sys.executable, CONVERT, str(out), "--outtype", "f16", "--outfile", str(gg)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("gguf:", gg, gg.stat().st_size)


if __name__ == "__main__":
    main()
