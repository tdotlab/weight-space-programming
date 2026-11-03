"""The repo is public: keep the machine's home path (C:\\Users\\<name>, any slash or case) out of it.
Tool output (llama-quantize prints its DLL paths, huggingface prints download dirs) carries it otherwise.

  uv run python src/scrub_paths.py --check        scan tracked + untracked files, list hits, exit 1 if any
  uv run python src/scrub_paths.py FILE [FILE...]  replace the home path with ~ in place
"""
import re, subprocess, sys
from pathlib import Path

home = str(Path.home())
# C:\Users\name, C:/Users/name, /c/Users/name, JSON-escaped C:\\Users\\name; any case
pat = re.compile(r"(?i)(?:[a-z]:|/[a-z])[\\/]+" + r"[\\/]+".join(map(re.escape, re.split(r"[\\/]", home)[1:])))


def read(p):
    return p.read_text(encoding="utf-8", errors="surrogateescape")


if sys.argv[1:] == ["--check"]:
    root = Path(__file__).resolve().parents[1]
    files = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=root,
                           capture_output=True, text=True, check=True).stdout.splitlines()
    hits = [f for f in files if (root / f).is_file() and pat.search(read(root / f))]
    print("\n".join(hits) if hits else "clean")
    sys.exit(1 if hits else 0)

for f in sys.argv[1:]:
    p = Path(f)
    s = read(p)
    n = len(pat.findall(s))
    if n:
        p.write_text(pat.sub("~", s), encoding="utf-8", errors="surrogateescape")
    print(f"{f}: {n} replaced")
