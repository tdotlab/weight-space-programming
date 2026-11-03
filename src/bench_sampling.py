"""Throughput and correctness check for llama-server CPU vs GPU (backend) sampling.

Throughput: N parallel MATH-500 prompts, thinking on, qwen preset, short max_tokens; reports aggregate tok/s.
Penalty check: with presence_penalty=100 a token can appear at most about once, so a prompt that asks for
one word 30 times shows whether the penalty is applied at all.
Usage: python src/bench_sampling.py --gguf gguf/original-q8_0.gguf [--cpu-sampling]
"""
import argparse, json, time
from concurrent.futures import ThreadPoolExecutor

import requests

from eval_math import PRESETS, PROMPT_SUFFIX, ROOT, load_problems, start_server


def chat(port, content, max_tokens, think, **sampling):
    body = {"messages": [{"role": "user", "content": content}], "max_tokens": max_tokens, "seed": 0,
            "chat_template_kwargs": {"enable_thinking": think}, **sampling}
    return requests.post(f"http://127.0.0.1:{port}/v1/chat/completions", json=body, timeout=3600).json()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gguf", required=True)
    ap.add_argument("--parallel", type=int, default=40)
    ap.add_argument("--max-tokens", type=int, default=768)
    ap.add_argument("--cpu-sampling", action="store_true")
    ap.add_argument("--port", type=int, default=8092)
    a = ap.parse_args()
    mode = "cpu" if a.cpu_sampling else "gpu"
    srv = start_server(ROOT / a.gguf, a.port, a.parallel, 17408, f"bench_{mode}", backend_sampling=not a.cpu_sampling)
    try:
        probs = load_problems(a.parallel, 123)
        t0 = time.time()
        with ThreadPoolExecutor(a.parallel) as ex:
            rs = list(ex.map(lambda r: chat(a.port, r["problem"] + PROMPT_SUFFIX, a.max_tokens, True, **PRESETS["qwen"]), probs))
        dt = time.time() - t0
        toks = sum(r["usage"]["completion_tokens"] for r in rs)
        word = "banana"
        pen = {}
        for pp in (0.0, 100.0):
            r = chat(a.port, f"Write the word {word} 30 times, separated by spaces. Output nothing else.", 120, False,
                     temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=pp)
            txt = r["choices"][0]["message"].get("content") or ""
            pen[pp] = dict(count=txt.lower().count(word), text=txt[:200])
        out = dict(mode=mode, parallel=a.parallel, max_tokens=a.max_tokens, tokens=toks, secs=round(dt, 1),
                   tok_per_s=round(toks / dt, 1), sample_reasoning=(rs[0]["choices"][0]["message"].get("reasoning_content") or "")[:400],
                   penalty_check=pen)
        print(json.dumps(out, indent=1, ensure_ascii=False))
        with open(ROOT / "logs" / "bench_sampling.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
    finally:
        srv.kill()


if __name__ == "__main__":
    main()
