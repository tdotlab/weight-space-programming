"""Is every model we evaluated the model we meant to evaluate? This desktop's RAM corrupts data (docs/STATUS.md,
Gotchas), so each stage rebuilds or rehashes an artifact and compares it bit for bit with what is on disk.

  A  originals: each read-only weight file against Hugging Face's SHA-256 (kept in the download cache's metadata).
  B  edits: each edited/<name>/ file against the SHA-256 recorded when it was built (did the disk copy change?), and
     against a fresh in-memory rebuild from its start with make_edit's own apply_edit (was the build faithful?).
  C  GGUFs (--gguf): each evaluated Q8_0 file against a fresh f16 conversion + Q8_0 quantization of its safetensors.
  D  evals: server and console logs of every run for errors, and each run's finish reasons.
  E  RAM screen (--ram-gb N): write and read back N GB in several patterns. User space only: it sees the pages
     Windows hands it. MemTest86 from a USB stick is the real test.

The check runs on the same RAM, so every hash is computed from cache-bypassing reads (FILE_FLAG_NO_BUFFERING), and
every tensor mismatch is judged on cache-bypassing bytes. "On disk" means the build file really differs from what its
recipe gives; "this check" means the file is fine and the fault was in this process's memory or Windows' cached copy.
A GGUF mismatch gets a second rebuild before it counts.

Usage: uv run python src/verify_artifacts.py [--gguf] [--ram-gb 12] [--only NAME,...]  | tee logs/verify_artifacts.txt
Weight math and byte compares only; no forward passes. Writes only to a temp folder (--tmp).
"""
import argparse, ctypes, hashlib, json, os, re, struct, subprocess, sys, tempfile, time
from pathlib import Path

import numpy as np
import torch
from safetensors import safe_open

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_edit import CONVERT, FNAME, TOOLS, apply_edit  # noqa: E402

torch.set_grad_enabled(False)
ROOT = Path(__file__).resolve().parents[1]
MODELS = TOOLS / "models"
QUANT = TOOLS / "llama.cpp" / "b11804" / "llama-quantize.exe"
SIZE_OF = {"Qwen3.5-0.8B": "0.8B", "Qwen3.5-2B": "2B"}


def say(*a):
    print(*a, flush=True)


class RawFile:
    """Reads that bypass the Windows file cache, so a bad cached page cannot fool the check (plain reads elsewhere)."""
    SECTOR = 4096

    def __init__(self, path):
        self.path, self.h = str(path), None
        if os.name == "nt":
            from ctypes import wintypes as W
            self.k = ctypes.WinDLL("kernel32", use_last_error=True)
            self.k.CreateFileW.restype = W.HANDLE
            self.k.VirtualAlloc.restype = ctypes.c_void_p
            # GENERIC_READ, FILE_SHARE_READ, OPEN_EXISTING, FILE_FLAG_NO_BUFFERING
            self.h = self.k.CreateFileW(self.path, 0x80000000, 1, None, 3, 0x20000000, None)
            if self.h in (None, W.HANDLE(-1).value):
                raise OSError(ctypes.get_last_error(), "CreateFileW", self.path)
            self.cap = 1 << 24
            self.buf = self.k.VirtualAlloc(None, self.cap, 0x3000, 4)  # page-aligned, as NO_BUFFERING needs

    def read(self, off, n):
        if self.h is None:
            with open(self.path, "rb") as f:
                f.seek(off)
                return f.read(n)
        from ctypes import wintypes as W
        out = bytearray()
        while n > 0:
            a = off // self.SECTOR * self.SECTOR
            size = min(self.cap, (off - a + n + self.SECTOR - 1) // self.SECTOR * self.SECTOR)
            hi = ctypes.c_long(a >> 32)
            self.k.SetFilePointer(self.h, a & 0xFFFFFFFF, ctypes.byref(hi), 0)
            got = W.DWORD()
            if not self.k.ReadFile(self.h, ctypes.c_void_p(self.buf), size, ctypes.byref(got), None):
                raise OSError(ctypes.get_last_error(), "ReadFile", self.path)
            take = min(n, got.value - (off - a))
            if take <= 0:
                break
            out += ctypes.string_at(self.buf + off - a, take)
            off, n = off + take, n - take
        return bytes(out)

    def close(self):
        if self.h is not None:
            self.k.VirtualFree(ctypes.c_void_p(self.buf), 0, 0x8000)
            self.k.CloseHandle(self.h)


def sha256(p):
    """SHA-256 of the bytes on disk (cache-bypassing on Windows)."""
    h, f, off, size = hashlib.sha256(), RawFile(p), 0, os.path.getsize(p)
    while off < size:
        b = f.read(off, min(1 << 24, size - off))
        h.update(b)
        off += len(b)
    f.close()
    return h.hexdigest()


def st_offsets(path):
    """safetensors header: {tensor name: absolute byte offset of its data}."""
    with open(path, "rb") as f:
        hl = struct.unpack("<Q", f.read(8))[0]
        hdr = json.loads(f.read(hl))
    return {k: 8 + hl + v["data_offsets"][0] for k, v in hdr.items() if k != "__metadata__"}


def raw_elems(path, key, idx, esz):
    """Cache-bypassing bytes of the flat elements idx of tensor key."""
    off = st_offsets(path)[key]
    f = RawFile(path)
    out = [f.read(off + int(i) * esz, esz) for i in idx]
    f.close()
    return out


def hf_sha(model_dir):
    """The LFS SHA-256 huggingface_hub recorded for the weight file (2nd line of its .metadata)."""
    m = model_dir / ".cache" / "huggingface" / "download" / (FNAME + ".metadata")
    return m.read_text().split("\n")[1].strip() if m.exists() else None


def bitdiff(a, b, cols=None):
    """Compare two same-shape tensors bitwise (a = the file as read, b = the rebuild). None if equal, else a dict:
    n elements differing, how many by a single bit, bit positions, a few examples, and the raw bytes of up to 64."""
    esz = a.element_size()
    ab = a.contiguous().view(torch.uint8).numpy().reshape(-1)
    bb = b.contiguous().view(torch.uint8).numpy().reshape(-1)
    x = np.bitwise_xor(ab, bb)
    nz = np.flatnonzero(x)
    if nz.size == 0:
        return None
    el = np.unique(nz // esz)
    bits, single = {}, 0
    for e in el[:100000]:
        word = int.from_bytes(x[e * esz:(e + 1) * esz].tobytes(), "little")
        single += word & (word - 1) == 0
        for i in range(esz * 8):
            if word >> i & 1:
                bits[i] = bits.get(i, 0) + 1
    fa, fb = a.reshape(-1).float(), b.reshape(-1).float()
    where = [(tuple(int(i) for i in np.unravel_index(int(e), tuple(a.shape))), fa[e].item(), fb[e].item())
             for e in el[:4]]
    out = dict(n=int(el.size), single=int(single), bits=dict(sorted(bits.items())), where=where, el=el[:64], esz=esz,
               want=[bb[e * esz:(e + 1) * esz].tobytes() for e in el[:64]])
    if cols is not None and a.dim() == 2:
        out["outside"] = int((~np.isin(el % a.shape[1], np.asarray(cols))).sum())
    return out


def fmt(d):
    w = "; ".join(f"{i} file {x:+.6g} vs rebuild {y:+.6g}" for i, x, y in d["where"])
    s = f"{d['n']} elements differ ({d['single']} by a single bit; bit positions {d['bits']}): {w}"
    if "outside" in d:
        s += f"; {d['outside']} outside the edited columns"
    return s + f". Verdict: {d['verdict']}"


def stage_a():
    say("\n== A. originals vs Hugging Face's SHA-256 (disk bytes)")
    bad = 0
    for m in ("Qwen3.5-0.8B", "Qwen3.5-0.8B-Base", "Qwen3.5-2B", "Qwen3.5-2B-Base"):
        d = MODELS / m
        want, got = hf_sha(d), sha256(d / FNAME)
        ok = want is not None and want == got
        bad += not ok
        say(f"  {m:20s} {'MATCH' if ok else 'MISMATCH'}  {got[:16]}" + ("" if ok else f" (want {want})"))
    return bad


def stage_b(only):
    say("\n== B. edits: disk vs build-time SHA-256, and the file vs a fresh rebuild from its start model")
    recs = [json.load(open(p)) for p in sorted((ROOT / "edited").glob("*/EDIT.json"))]
    recs.sort(key=lambda r: r["time"])  # starts are older than what is stacked on them
    bad = 0
    for r in recs:
        if only and r["name"] not in only:
            continue
        model = r.get("model", "Qwen3.5-0.8B")
        logdir = "logs" if model == "Qwen3.5-0.8B" else "logs/" + SIZE_OF[model]
        path = ROOT / "edited" / r["name"] / FNAME
        sha_ok = sha256(path) == r["sha256"]
        start = r.get("start", "original")
        sdir = MODELS / model if start == "original" else ROOT / "edited" / start
        dirs = torch.load(ROOT / r.get("dirfile", logdir + "/a04_directions.pt"))
        d = dirs[r["dir"]].float()
        d = d / d.norm()
        src = safe_open(str(sdir / FNAME), "pt")
        tensors = {k: src.get_tensor(k) for k in src.keys()}
        base = safe_open(str(MODELS / (model + "-Base") / FNAME), "pt") if r["kind"] == "revert" else None
        per_layer, _ = apply_edit(tensors, d, r["layers"], r["k"], r["scale"], base)
        cols_ok = [p["columns"] for p in per_layer] == [p["columns"] for p in r["per_layer"]]
        edited = {f"model.language_model.layers.{p['layer']}.mlp.down_proj.weight": p["columns"] for p in per_layer}
        disk = safe_open(str(path), "pt")
        diffs, ondisk = {}, 0
        if set(disk.keys()) != set(tensors):
            diffs["<keys>"] = str(sorted(set(disk.keys()) ^ set(tensors))[:5])
            ondisk += 1
        for k in sorted(set(disk.keys()) & set(tensors)):
            t = disk.get_tensor(k)
            if t.shape != tensors[k].shape or t.dtype != tensors[k].dtype:
                diffs[k] = f"shape/dtype {tuple(t.shape)} {t.dtype} vs {tuple(tensors[k].shape)} {tensors[k].dtype}"
                ondisk += 1
                continue
            c = edited.get(k)
            dd = bitdiff(t, tensors[k], c if isinstance(c, list) else None)
            if not dd:
                continue
            # Judge on disk bytes. For a tensor the edit leaves alone, the start file's disk bytes are the truth;
            # for the edited tensor, the rebuild is (it may itself be hit, so a flagged one is worth a rerun).
            raw = raw_elems(path, k, dd["el"], dd["esz"])
            ref = raw_elems(sdir / FNAME, k, dd["el"], dd["esz"]) if k not in edited else dd["want"]
            n_bad = sum(x != y for x, y in zip(raw, ref))
            dd["verdict"] = (f"ON DISK, {n_bad} of {len(raw)} checked elements" if n_bad else
                             f"this check, not the file ({len(raw)} checked elements are right on disk)")
            ondisk += n_bad > 0
            diffs[k] = dd
        ok = sha_ok and cols_ok and not ondisk
        bad += not ok
        say(f"  {r['name']:12s} ({SIZE_OF[model]}, start {start}): disk sha {'= build' if sha_ok else 'CHANGED since build'}"
            f", columns {'same' if cols_ok else 'DIFFERENT'}, rebuild {'identical' if not diffs else 'differs'}"
            f"{'' if ok else '  << FLAGGED'}")
        for k, v in diffs.items():
            say(f"      {k}: {v if isinstance(v, str) else fmt(v)}")
        del tensors
    return bad


def gguf_tensors(p):
    from gguf import GGUFReader
    return {t.name: t for t in GGUFReader(str(p)).tensors}


def q8_blocks(a, b):
    """Differing Q8_0 blocks (34 bytes: f16 scale + 32 int8) between two raw byte arrays; max |weight change|."""
    a, b = a.reshape(-1, 34), b.reshape(-1, 34)
    blk = np.flatnonzero((a != b).any(1))
    dq = lambda r: r[:, :2].copy().view(np.float16).astype(np.float32) * r[:, 2:].view(np.int8).astype(np.float32)
    dw = np.abs(dq(a[blk]) - dq(b[blk])) if blk.size else np.zeros(1)
    return blk, float(dw.max()), int((dw > 0).sum())


def rebuild_gguf(src, f16, q8):
    subprocess.run([sys.executable, CONVERT, str(src), "--outtype", "f16", "--outfile", str(f16)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([str(QUANT), str(f16), str(q8), "Q8_0"], check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    return sha256(q8)


def raw_copy(src, dst):
    """Copy a model folder's top-level files into dst, the weight file through cache-bypassing reads, so the converter
    never sees Windows' cached copy of the source (a bad cached page there would make every rebuild agree with
    itself and blame the evaluated GGUF). The copy is rehashed from disk against the source; None if they match."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    for d in dst.parent.iterdir():  # only one copy at a time in the temp folder (they are 1.5-4.5 GB each)
        for old in d.iterdir():
            old.unlink()
        d.rmdir()
    dst.mkdir()
    for p in src.iterdir():
        if not p.is_file():
            continue
        if p.name != FNAME:
            (dst / p.name).write_bytes(p.read_bytes())
            continue
        f, off, size = RawFile(p), 0, os.path.getsize(p)
        with open(dst / p.name, "wb") as out:
            while off < size:
                b = f.read(off, min(1 << 24, size - off))
                out.write(b)
                off += len(b)
        f.close()
    a, b = sha256(src / FNAME), sha256(dst / FNAME)
    return None if a == b else f"copy {b[:12]} != source {a[:12]}"


def stage_c(only, tmp):
    say("\n== C. GGUFs: evaluated Q8_0 vs a fresh f16 conversion + Q8_0 quantization of its safetensors (disk bytes)")
    tmp.mkdir(parents=True, exist_ok=True)
    f16, q8 = tmp / "rebuild-f16.gguf", tmp / "rebuild-q8_0.gguf"  # overwritten each time
    bad = 0
    for g in sorted((ROOT / "gguf").glob("*-q8_0.gguf")):
        name = g.name[: -len("-q8_0.gguf")]
        if only and name not in only:
            continue
        src = (MODELS / "Qwen3.5-0.8B" if name == "original" else MODELS / "Qwen3.5-2B" if name == "2B_original"
               else ROOT / "edited" / name)
        t0 = time.time()
        want = sha256(g)
        copy = tmp / "src" / src.name  # the converter writes the folder name into the GGUF's metadata
        err = raw_copy(src, copy)
        if err:  # the copy was hit on its way to disk; one retry, then report
            err = raw_copy(src, copy)
        if err:
            say(f"  {name:12s} could not make a clean copy of the source ({err}); skipped")
            bad += 1
            continue
        first = rebuild_gguf(copy, f16, q8)
        note = ""
        if first != want:  # the rebuild ran on the same RAM; a second one decides
            second = rebuild_gguf(copy, f16, q8)
            note = (" (first rebuild differed, second matches: the fault was in the rebuild)" if second == want else
                    " (two rebuilds agree with each other)" if second == first else " (the two rebuilds disagree too)")
            same = second == want
        else:
            same = True
        say(f"  {name:12s} Q8_0 {'identical' if same else 'DIFFERS'}{note}  ({time.time() - t0:.0f}s)")
        if same:
            continue
        bad += 1
        A, B = gguf_tensors(g), gguf_tensors(q8)
        n_t = 0
        for k in sorted(set(A) | set(B)):
            if k not in A or k not in B:
                say(f"      {k}: only in {'evaluated' if k in A else 'rebuild'}")
                continue
            a = np.asarray(A[k].data).view(np.uint8).reshape(-1)
            b = np.asarray(B[k].data).view(np.uint8).reshape(-1)
            if a.shape != b.shape:
                say(f"      {k}: sizes differ")
            elif (a != b).any():
                n_t += 1
                if A[k].tensor_type.name == "Q8_0":
                    blk, dmax, nw = q8_blocks(a, b)
                    say(f"      {k}: {blk.size} Q8_0 blocks differ, {nw} weights, max |change| {dmax:.4g}")
                else:
                    say(f"      {k}: {A[k].tensor_type.name}, {int((a != b).sum())} bytes differ")
        if not n_t:
            say("      every tensor identical: the difference is in the metadata")
    return bad


def stage_d():
    say("\n== D. evals: errors in server/console logs, finish reasons")
    benign = re.compile(r"failed to fit params to free device memory")
    pat = re.compile(r"error|fail|abort|assert|segfault|exception|traceback|out of memory|nan\b", re.I)
    bad = 0
    for rd in sorted(ROOT.glob("runs/*/math500/*")):
        if not (rd / "results.jsonl").exists():
            continue
        hits = []
        for log in ("server.log", "console.log"):
            p = rd / log
            if p.exists():
                for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                    if pat.search(line) and not benign.search(line):
                        hits.append(f"{log}: {line.strip()[:160]}")
        fin = {}
        for line in open(rd / "results.jsonl", encoding="utf-8"):
            f = json.loads(line).get("finish")
            fin[f] = fin.get(f, 0) + 1
        odd = {k: v for k, v in fin.items() if k not in ("stop", "length")}
        if hits or odd:
            bad += 1
            say(f"  {rd.relative_to(ROOT).as_posix()}: finish {fin}")
            for h in hits[:5]:
                say(f"      {h}")
            if len(hits) > 5:
                say(f"      ... {len(hits) - 5} more")
    say(f"  {bad} runs with log errors or unusual finish reasons" if bad else "  every run clean")
    return bad


def stage_e(gb, passes):
    say(f"\n== E. RAM screen: {gb} GB, {passes} pass(es), 5 patterns (user space; MemTest86 is the real test)")
    n = int(gb * (1 << 30)) // 8
    try:
        arr = np.empty(n, dtype=np.uint64)
    except MemoryError:
        say("  could not allocate; try a smaller --ram-gb")
        return 1
    C = 1 << 24
    golden = np.uint64(0x9E3779B97F4A7C15)
    pats = [("0x5555", np.uint64(0x5555555555555555)), ("0xAAAA", np.uint64(0xAAAAAAAAAAAAAAAA)),
            ("zeros", np.uint64(0)), ("ones", np.uint64(0xFFFFFFFFFFFFFFFF)), ("address", None)]
    errs = 0
    for p in range(passes):
        for label, v in pats:
            t0 = time.time()
            for i in range(0, n, C):
                j = min(n, i + C)
                arr[i:j] = v if v is not None else np.arange(i, j, dtype=np.uint64) * golden
            found, cnt = [], 0
            for i in range(0, n, C):
                j = min(n, i + C)
                want = v if v is not None else np.arange(i, j, dtype=np.uint64) * golden
                badi = np.flatnonzero(arr[i:j] != want)
                for b in badi[:8]:
                    w = int(want) if v is not None else int(want[b])
                    found.append((i + int(b), int(arr[i + b]) ^ w))
                cnt += badi.size
            errs += cnt
            say(f"  pass {p + 1} {label:8s} {time.time() - t0:5.1f}s  " +
                (f"{cnt} bad words: " + ", ".join(f"word {a} xor {x:#x}" for a, x in found[:6]) if cnt else "ok"))
    del arr
    return int(errs > 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gguf", action="store_true", help="also rebuild and compare every Q8_0 GGUF (slow)")
    ap.add_argument("--ram-gb", type=float, default=0)
    ap.add_argument("--passes", type=int, default=1)
    ap.add_argument("--only", default="", help="comma list of edit/GGUF names for B and C")
    ap.add_argument("--skip", default="", help="stages to skip, e.g. AD")
    ap.add_argument("--tmp", default=str(Path(tempfile.gettempdir()) / "wsp_verify"))
    a = ap.parse_args()
    only = set(filter(None, a.only.split(",")))
    say(f"verify_artifacts {time.strftime('%Y-%m-%d %H:%M')}")
    bad = {}
    if "A" not in a.skip:
        bad["A"] = stage_a()
    if "B" not in a.skip:
        bad["B"] = stage_b(only)
    if a.gguf and "C" not in a.skip:
        bad["C"] = stage_c(only, Path(a.tmp))
    if "D" not in a.skip:
        bad["D"] = stage_d()
    if a.ram_gb:
        bad["E"] = stage_e(a.ram_gb, a.passes)
    say("\nsummary: " + ", ".join(f"{k} {'clean' if v == 0 else f'{v} flagged'}" for k, v in bad.items()))


if __name__ == "__main__":
    main()
