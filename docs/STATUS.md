# Status

Last updated 2026-11-03 09:45 EST.

## Where it stands

Headline: A64x3 (u-component tripled in 64 columns of layer 22's MLP output, 65k weights, found by weight math) takes MATH-500 (100-problem sample) from 5/100 to 30/100: 25 gained, none lost, sign test p about 6e-8. On the 60 problems no edit was ever judged on, 1/60 to 17/60 (p about 3e-5). Every answer it finishes is correct; the other 70 still hit the 16k cap. With a 32k cap A64x3 scores 41/100 (+13/-2 vs 16k, p 0.007; held-out 21/60), 53 still truncated: budget explains part of the gap to MIT's 48.1%, and the rest is loops that do not end even at 32k. The baseline at 32k scores 15/100 (88 truncated), so at equal budget the edit is +26/-0 (p 3e-8; held-out 8/60 to 21/60, +13/-0). Budget and edit add roughly independently: doubling the cap is worth about +10 to either model, the edit about +25 at either cap. MIT reports 7.9% to 48.1% with edits at layers 15 and 19; MIT's layers do nothing here (A64VP/A64VA). By level: L1 3/5, L2 11/18, L3 9/21, L4 4/29, L5 3/27 (baseline 1, 2, 1, 1, 0).

Baseline done: 5/100 correct, 94 truncated at the 16k cap in "Wait... No..." self-checking spirals. That is in line with MIT's 7.9%, and accuracy is almost entirely capped by looping.

The MIT-shaped edit P64 backfired. On the first 40 problems it scored 0/40 with every answer truncated, and "Wait" rose from 3.2 to 108 per 1000 reasoning chars. Reasoning starts normally and collapses into "Wait, wait, wait..." strings. So the direction u does control "Wait", but the 64 columns it touched were a net brake on it. P64 was stopped at 40/100 since the rest could not change the verdict.

The random-direction control R64 matches the baseline exactly (4/40, 36 truncated, Wait 3.16 vs 3.22), so P64's effect is specific to u.

A64, the opposite of P64 (u-component in the same 64 L22 columns doubled), is the first edit that helps: 11/40 correct vs 4/40, every finished answer right, 8 problems gained and 1 lost against the baseline (sign test p about 0.04). 'Wait' fell 13x (3.22 to 0.25 per kchar). The half-strength version A64h lands in between (9/40, Wait 0.96, 5 gained and none lost), so the response is graded with dose. But 29/40 still hit the 16k cap: the spiral keeps going on 'No, ...', 'Is this the correct form?', 'Let's re-verify'. 'Wait' was one leg of the loop, not the loop. There is no post-training direction behind 'No,' to grab (a07: best of 160 candidates z 4.5, vs u's z 23 for 'Wait'), so the rest of the loop is not one surgical target. D_full, which reverts post-training's whole u-component in L22, does next to nothing (5/40, Wait 3.22 to 2.51), so the lever is those 64 columns specifically, not post-training's u-writing in general. A64x3 (u-component tripled) keeps the curve rising: 13/40, 9 gained and none lost, 'Wait' practically gone (0.04). A64VP (A64 plus v_in projected out of the top-64 columns of MIT's layers 15 and 19) scores exactly A64's 11/40 with a 3-for-3 swap of problems: the MIT-layer edit adds nothing on top. A64VA (the opposite sign) also lands on exactly 11/40, so neither sign of v_in at MIT's layers matters once A64 is in. A64x5 (u x5) also scores 13/40 with a 3-for-3 swap, so the dose curve flattens at x3 (4, 9, 11, 13, 13): once 'Wait' is gone, more of the same edit buys nothing, and it does not break the model either. A64 on all 100: 24/100 (+21/-2, held-out 13/60). A64x3 at a 32k cap: 41/100; the baseline at a 32k cap: 15/100. Queue empty; GPU idle. From here on edits use eval feedback, which MIT's blind setup did not (Deviation 4 in `logs/edit_session.md`).

## Plan

1. Done: baseline on 100 MATH-500 problems (seed 0), qwen preset, thinking on, 16k max tokens.
2. Screens on the first 40: R64 (is P64's effect specific to u?), A64/A64h/A64x3 (does amplifying the brake cut loops, and where does the dose curve top out?), D_full (revert post-training's u-component across L22).
3. Done: A64x3 on all 100 (30/100), A64 on all 100 (24/100). At a 32k cap: A64x3 41/100, baseline 15/100.
4. Done: a07 found no post-training 'No,' direction. Next lever is upstream: v_in at L15+L19 stacked on A64, both signs (A64VP, A64VA), since weights cannot fix the sign.
5. Then: the winner gets the full 100, a greedy baseline, and later a slightly bigger Qwen.

## Results

First-40 numbers compare against the baseline's same 40 problems: 4/40 correct, 36/40 truncated, Wait 3.2/kchar.

| run | problems | acc | truncated | acc when finished | waits/kchar | notes |
|---|---|---|---|---|---|---|
| smoke (F16, 8k) | 8 | 1/8 | 7/8 | | 1.8 (finished) vs 1.8 to 5.4 (truncated) | loops are "Wait... No..." spirals, not verbatim repeats |
| base_q8 | 100 | 5/100 | 94/100 | 5/6 | 3.41 (trunc 3.44, fin 2.02) | mean 15.9k tokens; right answers spread over levels 1-4 |
| P64_q8 | first 40 | 0/40 | 40/40 | | median 113 | degenerates into "Wait, wait, wait" strings; stopped at 40 |
| R64_q8 | first 40 | 4/40 | 36/40 | 4/4 | 3.16 (base 3.22) | random-direction control matches baseline: P64's effect is specific to u |
| A64_q8 | first 40 | 11/40 | 29/40 | 11/11 | 0.25 | u doubled in P64's columns. +8/-1 vs baseline. 'No,' unchanged (2.29); truncated runs still spiral without 'Wait' |
| A64h_q8 | first 40 | 9/40 | 31/40 | 9/9 | 0.96 | u x1.5. +5/-0 vs baseline; 7 of its 9 also right under A64. Graded between base and A64 |
| Dfull_q8 | first 40 | 5/40 | 35/40 | 5/5 | 2.51 | post-training's u-component reverted across all of L22. +2/-1 vs baseline: noise. Loops unchanged |
| A64x3_q8 | first 40 | 13/40 | 27/40 | 13/13 | 0.04 | u x3. +9/-0 vs baseline, +4/-2 vs A64. 'Wait' gone; truncated runs still spiral on 'No,' and re-reading the problem |
| A64x3_q8 | 100 | 30/100 | 70/100 | 30/30 | 0.03 (base 3.09) | +25/-0 vs baseline, p 6e-8. Held-out last 60: 17/60 vs 1/60 |
| A64_q8 | 100 | 24/100 | 75/100 | 24/25 | 0.28 | u x2. +21/-2 vs baseline (p 7e-5); held-out 13/60 vs 1/60 (p 0.002). A64x3 vs A64: +11/-5 (p 0.21), a trend, not proven |
| A64x3_32k_q8 | 100 | 41/100 | 53/100 | 41/47 | 0.03 | 32k cap, 20 slots. +13/-2 vs A64x3 at 16k (p 0.007), +36/-0 vs baseline 16k. Held-out 21/60. 15 finished past 16k, 10 of them right. 6 finished wrong (first wrong answers for this edit). By level 4/5, 13/18, 13/21, 8/29, 3/27 |
| base_32k_q8 | 100 | 15/100 | 88/100 | 12/12 | 3.35 | baseline at a 32k cap, 20 slots. +11/-1 vs baseline at 16k. Held-out 8/60. 7 finished past 16k, all right. By level 2/5, 8/18, 2/21, 2/29, 1/27. A64x3_32k vs this: +26/-0, p 3e-8 |
| A64x5_q8 | first 40 | 13/40 | 27/40 | 13/13 | 0.01 | u x5. Same score as A64x3 (+3/-3 swap): the curve plateaus at x3. No degeneracy at 5.5% rel change |
| A64VP_q8 | first 40 | 11/40 | 29/40 | 11/11 | 0.28 | A64 + v_in projected out of top-64 cols at L15, L19. Same score as A64, +3/-3 swap: adds nothing |
| A64VA_q8 | first 40 | 11/40 | 29/40 | 11/11 | 0.29 | A64 + v_in doubled in those columns. Same as A64 again (+3/-3 swap). MIT's layers do nothing here in either sign |

Weight-analysis findings are in `logs/edit_session.md`. In short, post-training's top change to L22's MLP output is a direction u that writes "Wait" (z +23). The neurons feeding it get extra post-training change in L15 to L21, consistent with MIT's 15/19 without singling them out. Weight math alone cannot tell which L22 neurons push u up or down when they fire (gate and up rows are nearly orthogonal, a06), so P64's sign had to be learned from the eval.

## Throughput (GTX 1070, i5-8400)

- F16 is about 1.7x slower than Q8_0 on Pascal, so evals use Q8_0.
- With CPU sampling, llama-server samples all slots on one CPU core, so throughput tops out near 365 tok/s at 40 slots with the GPU around 30% busy. More slots don't help.
- GPU backend sampling (`-bs`, the default in `eval_math.py`) does 715 tok/s on the same test. Same-seed outputs are identical to CPU sampling, and presence_penalty is applied. See `src/bench_sampling.py` and `logs/bench_sampling.jsonl`.
- At long context per-slot speed falls to about 11-12 t/s, so a wave of 40 that runs to the 16k cap takes about 24 min, and a full 100-problem run of a looping model takes about 60 min.

## Gotchas

- Stopping the queue: `taskkill //F //T //PID $(cat runs/queue.pid)`. queue.pid holds the Windows PID (from `/proc/$$/winpid`); Git Bash's `$$` is not a Windows PID. Stopping the launching shell does not stop the queue.
- Queue waiters that grep `runs/queue2.log` must match the exact `^=== HH:MM:SS done NAME:` line and count occurrences: a name screened earlier already has a done line (the 03:19 early start). `eval_math.py` now exits if its port is already serving.
- `eval_math.py` resumes from `runs/<name>.jsonl`. Move a stale or aborted file aside before rerunning under different settings (prefix `aborted_`), and never delete runs.
- math-verify needs `parsing_timeout=None` and `timeout_seconds=None` on Windows, and Python output needs `PYTHONIOENCODING=utf-8`.
- Write scripts with a file editor, not bash heredocs, which mangle backslashes.
