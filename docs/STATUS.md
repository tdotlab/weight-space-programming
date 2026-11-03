# Status

Last updated 2026-11-02 22:20 EST.

## Where it stands

Baseline done: 5/100 correct, 94 truncated at the 16k cap in "Wait... No..." self-checking spirals. That is in line with MIT's 7.9%, and accuracy is almost entirely capped by looping.

The MIT-shaped edit P64 backfired. On the first 40 problems it scored 0/40 with every answer truncated, and "Wait" rose from 3.2 to 108 per 1000 reasoning chars. Reasoning starts normally and collapses into "Wait, wait, wait..." strings. So the direction u does control "Wait", but the 64 columns it touched were a net brake on it. P64 was stopped at 40/100 since the rest could not change the verdict.

Now screening on the first 40 problems (`FIRST=40`, the same problems as a full run's first wave, about 25 min each): R64 (random-direction control), then A64 and A64h (the opposite of P64: u-component in the same 64 columns doubled, or 1.5x), then D_full. Queue log: `runs/queue2.log`. From here on edits use eval feedback, which MIT's blind setup did not (Deviation 4 in `logs/edit_session.md`).

## Plan

1. Done: baseline on 100 MATH-500 problems (seed 0), qwen preset, thinking on, 16k max tokens.
2. Screens on the first 40: R64 (is P64's effect specific to u?), A64/A64h (does amplifying the brake cut loops?), D_full (revert post-training's u-component across L22).
3. Any edit that beats the baseline's first 40 (4/40 correct, 36 truncated) gets the full 100, and R64 too if it hasn't.
4. Then: an L15+L19 edit along v_in (`logs/a05_vin.pt`), a greedy baseline, and later a slightly bigger Qwen.

## Results

First-40 numbers compare against the baseline's same 40 problems: 4/40 correct, 36/40 truncated, Wait 3.2/kchar.

| run | problems | acc | truncated | acc when finished | waits/kchar | notes |
|---|---|---|---|---|---|---|
| smoke (F16, 8k) | 8 | 1/8 | 7/8 | | 1.8 (finished) vs 1.8 to 5.4 (truncated) | loops are "Wait... No..." spirals, not verbatim repeats |
| base_q8 | 100 | 5/100 | 94/100 | 5/6 | 3.41 (trunc 3.44, fin 2.02) | mean 15.9k tokens; right answers spread over levels 1-4 |
| P64_q8 | first 40 | 0/40 | 40/40 | | median 113 | degenerates into "Wait, wait, wait" strings; stopped at 40 |
| R64_q8 | first 40 | running | | | | |
| A64_q8 | first 40 | queued | | | | |
| A64h_q8 | first 40 | queued | | | | |
| Dfull_q8 | first 40 | queued | | | | |

Weight-analysis findings are in `logs/edit_session.md`. In short, post-training's top change to L22's MLP output is a direction u that writes "Wait" (z +23). The neurons feeding it get extra post-training change in L15 to L21, consistent with MIT's 15/19 without singling them out. Weight math alone cannot tell which L22 neurons push u up or down when they fire (gate and up rows are nearly orthogonal, a06), so P64's sign had to be learned from the eval.

## Throughput (GTX 1070, i5-8400)

- F16 is about 1.7x slower than Q8_0 on Pascal, so evals use Q8_0.
- With CPU sampling, llama-server samples all slots on one CPU core, so throughput tops out near 365 tok/s at 40 slots with the GPU around 30% busy. More slots don't help.
- GPU backend sampling (`-bs`, the default in `eval_math.py`) does 715 tok/s on the same test. Same-seed outputs are identical to CPU sampling, and presence_penalty is applied. See `src/bench_sampling.py` and `logs/bench_sampling.jsonl`.
- At long context per-slot speed falls to about 11-12 t/s, so a wave of 40 that runs to the 16k cap takes about 24 min, and a full 100-problem run of a looping model takes about 60 min.

## Gotchas

- Stopping the queue: `taskkill //F //T //PID $(cat runs/queue.pid)`. queue.pid holds the Windows PID (from `/proc/$$/winpid`); Git Bash's `$$` is not a Windows PID. Stopping the launching shell does not stop the queue.
- `eval_math.py` resumes from `runs/<name>.jsonl`. Move a stale or aborted file aside before rerunning under different settings (prefix `aborted_`), and never delete runs.
- math-verify needs `parsing_timeout=None` and `timeout_seconds=None` on Windows, and Python output needs `PYTHONIOENCODING=utf-8`.
- Write scripts with a file editor, not bash heredocs, which mangle backslashes.
