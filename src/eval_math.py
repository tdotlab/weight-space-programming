"""MATH-500 eval through llama-server. Records accuracy and loop behavior.

Usage: uv run python src/eval_math.py --gguf gguf/original-f16.gguf --name base_qwen --n 100
"""
import argparse, json, os, random, re, subprocess, sys, time, zlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from math_verify import parse, verify

from runs import model_size, run_dir

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(os.environ.get("WSP_TOOLS", Path.home() / "tools"))  # models, llama.cpp, sources
SERVER = str(TOOLS / "llama.cpp" / "b11804" / "llama-server.exe")
PROMPT_SUFFIX = "\n\nPlease reason step by step, and put your final answer within \\boxed{}."

PRESETS = {
    # Qwen's recommended thinking-mode text settings
    "qwen": dict(temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5),
    # Greedy, no penalty: worst case for loops
    "greedy": dict(temperature=0.0, top_p=1.0, top_k=1, min_p=0.0, presence_penalty=0.0),
}


WAIT_RE = re.compile(r"(?<![A-Za-z])(?:Wait|wait|Hmm|Hold on|Let me re-?(?:check|verify|examine|read|consider)|Actually,)")


def loop_metrics(text):
    """Self-doubt spiral markers. Verbatim loops are rare here; 'Wait... No...' restarts are the failure."""
    waits = len(WAIT_RE.findall(text))
    tail = text[-4000:].encode("utf-8", "ignore")
    zr = len(zlib.compress(tail, 9)) / len(tail) if len(tail) >= 1000 else 1.0
    return waits, round(1000 * waits / max(len(text), 1), 3), round(zr, 4)


def load_problems(n, seed):
    rows = [json.loads(l) for l in open(ROOT / "docs" / "math500.jsonl", encoding="utf-8")]
    if n >= len(rows):
        return rows
    return random.Random(seed).sample(rows, n)


def start_server(gguf, port, parallel, ctx_per_slot, log_path, backend_sampling=True):
    # CPU sampling is single-threaded over the 248k vocab: ~365 tok/s at 40 slots, GPU ~30% busy.
    # GPU backend sampling (-bs): ~715 tok/s, and same-seed outputs are identical to CPU (logs/bench_sampling.jsonl).
    args = [SERVER, "-m", str(gguf), "--port", str(port), "-ngl", "99",
            "-np", str(parallel), "-c", str(parallel * ctx_per_slot),
            "--jinja", "--no-webui", "-fa", "on", "-ctk", "q8_0", "-ctv", "q8_0"]
    if backend_sampling:
        args.append("-bs")
    # A server already on this port would pass the health check below and silently serve another model.
    try:
        requests.get(f"http://127.0.0.1:{port}/health", timeout=2)
        sys.exit(f"port {port} is already serving; another eval is running")
    except requests.RequestException:
        pass
    log = open(log_path, "w")
    p = subprocess.Popen(args, stdout=log, stderr=subprocess.STDOUT)
    for _ in range(240):
        try:
            if requests.get(f"http://127.0.0.1:{port}/health", timeout=2).status_code == 200:
                return p
        except requests.RequestException:
            pass
        if p.poll() is not None:
            sys.exit(f"server died, see {log_path}")
        time.sleep(1)
    p.kill()
    sys.exit("server did not come up")


def ask(port, row, sampling, max_tokens, think, seed):
    body = {
        "messages": [{"role": "user", "content": row["problem"] + PROMPT_SUFFIX}],
        "max_tokens": max_tokens,
        "seed": seed,
        "chat_template_kwargs": {"enable_thinking": think},
        **sampling,
    }
    t0 = time.time()
    r = requests.post(f"http://127.0.0.1:{port}/v1/chat/completions", json=body, timeout=7200).json()
    ch = r["choices"][0]
    msg = ch["message"]
    reasoning = msg.get("reasoning_content") or ""
    content = msg.get("content") or ""
    full = reasoning + "\n" + content
    gold = parse("$" + row["answer"] + "$", parsing_timeout=None)
    pred = parse(content, parsing_timeout=None) if content.strip() else []
    try:
        correct = bool(pred) and verify(gold, pred, timeout_seconds=None)
    except Exception:
        correct = False
    waits, waits_per_k, zr = loop_metrics(full)
    return {
        "id": row["unique_id"], "level": row["level"], "subject": row["subject"],
        "answer": row["answer"], "pred": str(pred[-1]) if pred else None, "correct": correct,
        "finish": ch.get("finish_reason"), "tokens": r["usage"]["completion_tokens"],
        "waits": waits, "waits_per_kchar": waits_per_k, "tail_zlib": zr, "secs": round(time.time() - t0, 1),
        "reasoning": reasoning, "content": content,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gguf", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--preset", default="qwen", choices=PRESETS)
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=16384)
    ap.add_argument("--parallel", type=int, default=32)
    ap.add_argument("--no-think", action="store_true")
    ap.add_argument("--port", type=int, default=8091)
    ap.add_argument("--cpu-sampling", action="store_true", help="sample on CPU instead of GPU (about 2x slower)")
    ap.add_argument("--first", type=int, default=0, help="only run the first K problems of the --n sample (screening)")
    a = ap.parse_args()

    rd = run_dir(a.name)  # runs/<model>/math500/<name>/, model from $WSP_MODEL
    rd.mkdir(parents=True, exist_ok=True)
    out = rd / "results.jsonl"
    done = {}
    if out.exists():
        for l in open(out, encoding="utf-8"):
            d = json.loads(l); done[d["id"]] = d
    pool = load_problems(a.n, a.seed)
    if a.first:
        pool = pool[:a.first]  # screen on the first K of the same sample (= the first wave of a full run)
    probs = [r for r in pool if r["unique_id"] not in done]
    print(f"{a.name}: {len(done)} cached, {len(probs)} to run", flush=True)

    sampling = PRESETS[a.preset]
    srv = start_server(ROOT / a.gguf, a.port, a.parallel, a.max_tokens + 1024, rd / "server.log",
                       backend_sampling=not a.cpu_sampling) if probs else None
    try:
        with open(out, "a", encoding="utf-8") as f, ThreadPoolExecutor(a.parallel) as ex:
            futs = {ex.submit(ask, a.port, r, sampling, a.max_tokens, not a.no_think, a.seed): r for r in probs}
            for i, fu in enumerate(as_completed(futs), 1):
                d = fu.result(); done[d["id"]] = d
                f.write(json.dumps(d) + "\n"); f.flush()
                if i % 10 == 0:
                    print(f"  {i}/{len(probs)}", flush=True)
    finally:
        if srv:
            srv.kill()

    rs = list(done.values())
    n = len(rs)
    acc = sum(r["correct"] for r in rs) / n
    trunc = sum(r["finish"] == "length" for r in rs) / n
    toks = sum(r["tokens"] for r in rs) / n
    fin = [r for r in rs if r["finish"] != "length"]
    acc_fin = sum(r["correct"] for r in fin) / len(fin) if fin else 0.0
    wpk = sum(r["waits_per_kchar"] for r in rs) / n
    meta = dict(name=a.name, model=model_size(), task="math500", gguf=a.gguf, preset=a.preset, sampling=sampling, n=n,
                max_tokens=a.max_tokens, think=not a.no_think, seed=a.seed, first=a.first,
                backend_sampling=not a.cpu_sampling,
                acc=round(acc, 4), truncated=round(trunc, 4), acc_when_finished=round(acc_fin, 4),
                n_finished=len(fin), mean_tokens=round(toks), mean_waits_per_kchar=round(wpk, 3))
    json.dump(meta, open(rd / "summary.json", "w"), indent=2)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
