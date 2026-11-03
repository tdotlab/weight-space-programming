# Status

Last updated 2026-11-02 20:45 EST.

## Where it stands

The weight analysis is done and three edits are built, but no edit has been evaluated yet. The eval queue (baseline plus three edits, 100 MATH-500 problems each) started at 20:43 with GPU sampling. The estimate is about 40 min per run, so about 2.7 h total, and progress is checked every 30 minutes. An earlier launch at 20:23 was stopped to switch to GPU sampling; its partial files are kept as `runs/aborted_*`.

## Plan

1. Baseline: run the original Q8_0 on 100 MATH-500 problems (seed 0), qwen preset, thinking on, 16k max tokens.
2. Evaluate the edits on the same 100 problems:
   - P64 (MIT-shaped): project the "Wait" direction u out of the top-64 L22 down_proj columns.
   - R64 (control): the same procedure with a random direction.
   - D_full: revert post-training's u-component across all of L22.
3. Compare accuracy, truncation (loops), acc_when_finished and waits/kchar. P64 has to beat both the baseline and R64 to count.
4. Then: an MIT-shaped L15+L19 edit along v_in (logs/a05_vin.pt), overshoot scales, a greedy baseline, and later a slightly bigger Qwen.

## Results

| run | acc | truncated | acc when finished | waits/kchar | notes |
|---|---|---|---|---|---|
| smoke (F16, 8 problems, 8k) | 1/8 | 7/8 | | 1.8 (finished) vs 1.8 to 5.4 (truncated) | loops are "Wait... No..." spirals, not verbatim repeats |
| base_q8 | pending | | | | |
| P64_q8 | pending | | | | |
| R64_q8 | pending | | | | |
| Dfull_q8 | pending | | | | |

Weight-analysis findings are in `logs/edit_session.md`. In short, post-training's top change to L22's MLP output is a direction that writes "Wait" (z +23). The neurons feeding it get extra post-training change in L15 to L21. That is consistent with MIT's 15/19, though it doesn't single those two out.

## Throughput (GTX 1070, i5-8400)

- F16 is about 1.7x slower than Q8_0 on Pascal, so evals use Q8_0.
- With CPU sampling, llama-server samples all slots on one CPU core, so throughput tops out near 365 tok/s at 40 slots with the GPU around 30% busy. More slots don't help.
- GPU backend sampling (`-bs`, now the default in `eval_math.py`) does 715 tok/s on the same test. Same-seed outputs are identical to CPU sampling, and presence_penalty is applied. See `src/bench_sampling.py` and `logs/bench_sampling.jsonl`. The first `-bs` attempt read 0.38 tok/s per slot only because an orphaned second server was sharing the GPU.
- The fallback, if `-bs` ever misbehaves, is two servers with about 16 slots each, so two CPU cores sample.

## Gotchas

- Stopping the queue: stopping the shell that launched `run_queue.sh` does not kill it on Windows. Kill the tree with `taskkill //F //T //PID <pid in runs/queue.pid>`, or the queue moves on to the next run and the orphaned llama-server keeps holding VRAM.
- `eval_math.py` resumes from `runs/<name>.jsonl`. Move a stale or aborted file aside before rerunning under different settings (prefix `aborted_`), and never delete runs.
- math-verify needs `parsing_timeout=None` and `timeout_seconds=None` on Windows, and Python output needs `PYTHONIOENCODING=utf-8`.
- Write scripts with a file editor, not bash heredocs, which mangle backslashes.
