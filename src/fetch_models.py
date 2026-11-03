"""Download a Qwen instruct + base pair into ~/tools/models (or $WSP_TOOLS/models) and check sha256 against the Hub.

Usage: uv run python src/fetch_models.py Qwen3.5-2B Qwen3.5-2B-Base
"""
import hashlib, os, sys
from pathlib import Path

from huggingface_hub import HfApi, snapshot_download

TOOLS = Path(os.environ.get("WSP_TOOLS", Path.home() / "tools"))
MODELS = TOOLS / "models"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 24), b""):
            h.update(b)
    return h.hexdigest()


def main():
    api = HfApi()
    for name in sys.argv[1:]:
        repo = f"Qwen/{name}"
        dest = MODELS / name
        print(f"== {repo} -> $WSP_TOOLS/models/{name}", flush=True)  # no absolute paths: logs are public
        snapshot_download(repo, local_dir=dest)
        info = api.model_info(repo, files_metadata=True)
        for s in info.siblings:
            if s.lfs:
                got = sha256(dest / s.rfilename)
                ok = got == s.lfs.sha256
                print(f"  {s.rfilename}: {'OK' if ok else 'MISMATCH'} {got}", flush=True)
                if not ok:
                    sys.exit(f"sha256 mismatch for {repo}/{s.rfilename}")
        print(f"  revision {info.sha}", flush=True)


if __name__ == "__main__":
    main()
