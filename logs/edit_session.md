# Edit session log

Editor: Claude (Opus). Rule: no forward passes through Qwen during analysis. Weight math only.

## Declared deviations from MIT setup

- I can see baseline eval transcripts (model outputs) produced before the edit phase. MIT's Astra reportedly got only weights plus a natural-language spec ("improve math", docs warn of loops). Seeing loop transcripts tells me which tokens loop; I'll note where that informs a choice.
- I know from press coverage that Astra's edit was "one direction written by the MLPs of layers 15 and 19, subtracted from 64 output columns in each". That's a strong prior Astra didn't have. I'll first search without restricting to those layers, then compare.

## Architecture facts (from config + tensor shapes)

- 24 layers, hidden 1024, MLP intermediate 3584 (SwiGLU), tied embeddings (vocab 248320).
- Full attention at layers 3,7,11,15,19,23; Gated DeltaNet linear attention elsewhere.
- MLP neuron j in layer L writes `down_proj[:, j]` (1024-d) into the residual stream.
- 64 columns x 1024 x 2 layers = 131,072 weights: matches the larger press figure.

## Steps

### a01: logit lens on every MLP neuron (src/analysis/a01_logit_lens.py, logs/a01_logit_lens.json)
Scored each down_proj column by z(restart tokens: Wait/Hmm/Actually) - z(</think>) through the tied unembedding with the (1+g) final norm.
Result: strongest neurons are late (L16, L17, L18, L20, L22: literal verb "wait/waiting/等待/delay") and end-of-text writers (L22, L23: <|im_end|>, </...).
Layers 15 and 19 do not stand out. The "wait" neurons are lexical, not the discourse "Wait," that starts a doubt spiral.

### a02: two-hop path trace (src/analysis/a02_two_hop.py, logs/a02_two_hop.json)
Upstream neurons scored by how their write vectors excite the gate rows of late doubt-writers and inhibit late closers.
Ignores attention mixing and nonlinearity. Result: noise-like (|z|>3 counts ~ Gaussian tail in every layer). Top-256 feeder
write matrix has a flat spectrum (0.62, 0.50, 0.47, ...): no dominant shared direction. Leading direction is the generic
"end-of-text / close bracket" direction, owned by layers 12-14. Dead end as a blind locator.

### Deviation 3: base-vs-instruct weight diff
Downloading Qwen/Qwen3.5-0.8B-Base and diffing weights. Pure weight math, but Astra had only one model. Rationale: the
thinking-mode doubt spiral is a post-training behavior, so the post-training delta should contain it in low rank.

### a03: base vs instruct diff (src/analysis/a03_base_diff.py, logs/a03_base_diff.json)
Post-training deltas are not low-rank anywhere (top singular direction holds ~0.4-0.7% of a layer's delta energy).
But the #1 singular direction of L22's down_proj delta is a "Wait" writer: z(restart) +10.5. L23's sv2/sv3 suppress "wait" (counterweight?).
Layers 15/19 show nothing special under this lens either.

### a04: candidate direction u (src/analysis/a04_candidate.py, logs/a04_candidate.json, logs/a04_directions.pt)
u = top left singular vector of dW_down at L22, sign-fixed to promote 'Wait'.
z-scores: 'Wait' +23.3, ' Wait' +22.3, 'Actually' +6.5, 'Hmm' +4.8, '</think>' +1.3, 'Therefore' -0.9. Random control r: all |z| < 2.
L22 energy along u: instruct 0.00084, base 0.00090, random expectation 0.00098. So post-training changed *which* columns write u,
not how much. Writing along u is spread: top-64 columns hold 22.5%, top-1024 hold 82%.

### Edits built (src/make_edit.py, edited/*/EDIT.json, logs/edits.jsonl)
- D_full: revert post-training's u-component in all L22 down_proj columns (rank-1). 2.05M weights changed (rest lost to bf16 rounding), rel change 0.63%.
- P64: project u out of the 64 L22 columns with largest |u.W_j| (MIT-style budget). 64.6k weights, rel change 1.37%.
- R64: control, same as P64 with random direction r (seed 0). 64.1k weights, rel change 1.18%.
Original checksum verified unchanged after building all three.

### Eval speed change
F16 on the GTX 1070 (Pascal, crippled FP16) ran 7.8 tok/s/stream at long context. Q8_0 benchmarked 1.7x faster (723 vs 429 tok/s @ 32 streams, 2k ctx).
Aborted the F16 baseline (kept as runs/aborted_f16_*), quantized original + 3 edits to Q8_0, all evals now Q8_0, 40 streams, 16k budget, Qwen thinking sampling.

### a05: feeders of the L22 Wait writers (src/analysis/a05_feeders.py, logs/a05_feeders.json)
Targets: 64 L22 neurons post-training pushed toward writing +u. v_in = top singular direction of their (norm-scaled, weighted) gate rows.
Spectrum flat (0.009, 0.007, 0.007...): weak shared input. 81% of targets have positive drive along v_in.
v_in logit lens: 'equ', 'equal', 'equivalence' (verification-flavored, weak). Post-training delta energy along v_in by layer:
~1.0x random for L0-14, rising to 1.13 (L15), 1.1 (L16), 1.08 (L17), 1.14 (L18), 1.25 (L19), 1.24 (L20), 1.29 (L21).
Consistent with MIT's L15/L19 being in the feeding region; does not single them out.

## Results and iteration

### P64 backfired (eval, first 40 problems = baseline's first wave)
P64: 0/40 correct, 40/40 truncated. 'Wait' went from 3.2 to 107.8 per 1000 reasoning chars; 'No,' and 'Actually,' fell.
Transcripts start normally, then collapse into "Wait, wait, wait. Wait, wait..." for thousands of tokens.
So u is causal for 'Wait' (a 1.4% change to 64 columns moves it 33x), but those 64 columns were a net brake on it in
reasoning contexts: removing their u-component released 'Wait'. Run stopped at 40/100 (runs/P64_q8.jsonl); the remaining
60 would not change the verdict.

### Deviation 4: iterating on eval feedback
MIT's Astra edited blind. From here on, I use the observed effect of earlier edits to pick the next one. Later edits are
therefore not blind one-shot edits, and any win among them carries a selection effect (judged on the same 40 problems).

### a06: can weights alone tell promoters from brakes? (src/analysis/a06_signs.py, logs/a06_signs.json)
Proxy: sign(cos(gate_j, up_j)) * u.W_down[:, j]. In L22, gate and up rows are nearly orthogonal (mean |cos| 0.106 overall,
0.062 on P64's columns), so the proxy is noise. P64's columns split 29/35 on raw coefficient sign. Weight math cannot
say which neurons fire with which sign; P64's eval says the 64 together were a net brake.

### A64, A64h: amplify instead of remove
Same 64 columns as P64, u-component doubled (A64, scale -1, rel change 1.37%) or increased 1.5x (A64h, scale -0.5,
rel change 0.69%). Prediction if the response is roughly monotone: fewer 'Wait's than baseline. Risk: suppressing
self-checking entirely could trade loops for confident wrong answers.

### R64 control (first 40)
4/40 correct, 36 truncated, the same 4 problems finished as in the baseline; Wait 3.16/kchar (baseline 3.22), 'No,' 2.29 (2.25).
A same-budget projection along a random direction changes nothing measurable, so P64's 33x 'Wait' blowup is specific to u.

### A64 screen (first 40)
11/40 correct, 29 truncated, 11/11 finished answers correct (baseline 4/40, 36 truncated). Against the baseline: 8 gained,
1 lost (test/algebra/1265), sign test p about 0.04. R64's texts diverge from the baseline's within a few hundred chars yet it
got the same 4 problems right, so per-problem noise at this budget looks low.
'Wait' 3.22 -> 0.25 per kchar; 'No,' 2.25 -> 2.29, 'Let me re' and 'Actually,' about the same. In the last 4000 chars of the
29 truncated runs, sentences opening with 'Wait' fell 313 -> 16 and nothing took their place; 'No' (284 vs 284), 'Let', 'If',
'Is' are unchanged. The truncated transcripts still go around in circles ("Is this the correct form? ... No, let's look at the
elements again."). Reading: 'Wait' is one entry point into the doubt loop. Removing it is enough on easier problems (the
gains span levels 1-5) but the loop itself runs on other connectives. Reasoning openers are unchanged (half start
"Here's a thinking process..." in both), so no register switch.
Next weight-space question: is there a direction behind 'No,' the way u is behind 'Wait' (a07)?

### a07: is there a 'No,' direction? (src/analysis/a07_no_direction.py, logs/a07_no_direction.json)
Scanned the top-16 left singular vectors of the post-training delta of down_proj in L14-L23 (160 directions) by logit-lens
z for 'No'. Best: L22 sv15 z 4.5, L21 sv12 4.45, L23 sv12 4.3, each with under 0.5% of its layer's delta energy and mixed
side effects. For comparison u writes 'Wait' at z 23 and holds the top singular slot. u itself is neutral on 'No' (z 1.0).
Reading: post-training built a dedicated 'Wait' writer but not a 'No' writer. 'No,' is either a base-model habit or spread
thin, so the part of the loop A64 left behind has no single weight-space handle at the output end.

### A64VP, A64VA: the MIT-layer edit stacked on A64
make_edit.py gained --dirfile and --start (stack on an existing edit). Direction v_in (a05: the input direction that
switches on the L22 neurons post-training taught to write 'Wait'). Top-64 columns by |v_in . W_j| in L15 and L19 down_proj:
A64VP projects v_in out (scale 1), A64VA doubles it (scale -1). Rel change 1.25% (L15), 1.37% (L19) each.
Weights cannot tell which sign damps the doubt state (a06), so both are screened. Verified the stacks carry A64's L22
tensor bit-for-bit and change only L15/L19. Question they answer: does the MIT-layer edit add anything beyond A64?

### A64h screen (first 40): dose response
u-component x1.5 in the same 64 columns: 9/40 correct, 31 truncated, 9/9 finished answers correct, 'Wait' 0.96/kchar,
'No,' 2.26. Against the baseline 5 gained, none lost. Against A64: 7 shared, A64h alone gets algebra/1265 (the one A64 lost)
and geometry/967; A64 alone gets 4. Accuracy and 'Wait' both move monotonically with edit strength
(base 4/40 at 3.22, A64h 9/40 at 0.96, A64 11/40 at 0.25). Three ordered points are suggestive, not proof; together with the paired gains (5-0, 8-1) the effect looks real.

### A64x3: one more point on the dose curve
Same 64 L22 columns, u-component tripled (make_edit scale -2.0). 65079 weights changed, rel change 2.75% of L22 down_proj
(A64 was about 1.4%). sha ca063c6a... Question: does the curve keep rising, flatten, or tip over into a new failure
(the model never doubting, or a different degenerate string) the way P64 tipped into "Wait, wait"? If it keeps rising,
the full 100 goes to A64x3 instead of A64. Original model file re-hashed after the build: unchanged (04b1c301...).

### D_full screen (first 40): reverting post-training's u-component everywhere in L22
5/40 correct, 35 truncated, 5/5 finished correct, 'Wait' 2.51/kchar (base 3.22), 'No,' 2.23. Against the baseline
2 gained (counting_and_probability/190, /23957), 1 lost (counting_and_probability/389): noise. Truncated tails read like
the baseline ("Wait! Let me check the denominators again"). Reading: post-training's u-writing summed over all 3584
columns is roughly neutral; the whole-matrix revert takes out brake and promoter columns alike. A64's effect comes from
amplifying the specific 64 columns with the largest u-loadings, not from post-training's u-component in general.
(Interpretation, not separately tested.)

### A64x3 screen (first 40): the curve keeps rising
13/40 correct, 27 truncated, 13/13 finished correct, 'Wait' 0.04/kchar (base 3.22), 'Actually' 0.05 (base 0.19), 'No,' 2.40.
Against the baseline 9 gained, none lost. Against A64 4 gained (algebra/1265, algebra/170, geometry/967,
intermediate_algebra/834), 2 lost (algebra/276, algebra/907). Dose curve on the first 40: 4 (x1), 9 (x1.5), 11 (x2), 13 (x3).
A64x3 vs A64 alone is not significant (+4/-2); the trend across four points is the evidence. Early finishes read clean
("Ready to write.", "Solution is 76 degrees."), no sign of overconfident wrong answers: every finished answer is right.
The truncated runs still circle without 'Wait': re-reading the problem statement ("Maybe the term 'n' is actually...?"),
arguing over definitions ("factor" vs "prime factor"), "my derivation is **wrong**?". 'Wait' is gone, so further dose can
only act through whatever else the 64 columns carry.

### A64x5: looking for the top of the curve
u-component x5 in the same 64 columns (scale -4.0): 65305 weights changed, rel change 5.5% of L22 down_proj,
sha 1bb8b6b7... Original model re-hashed after the build: unchanged. Queue changed so the full 100 goes to A64x3 before
A64 (the waiter kills the A64 rest run the moment it starts and runs A64x5 screen, A64x3 rest, A64 rest).

### A64VP screen (first 40): MIT's layers add nothing on top of A64
11/40 correct, 29 truncated, 11/11 finished correct, 'Wait' 0.28, 'No,' 2.44. Same score as A64. Against A64: gains
algebra/1265, counting_and_probability/803, prealgebra/1686; loses algebra/1339, algebra/2391, algebra/276. A 3-for-3 swap
is the noise floor (R64 vs baseline showed sampling alone reshuffles text without moving the score). Projecting v_in out of
L15/L19 does not reach the leftover 'No,' loop, and does not disturb A64's gain either.

### A64VA screen (first 40): the other sign does nothing either
11/40 correct, 29 truncated, 11/11 finished correct, 'Wait' 0.29, 'No,' 2.34. Against A64 gains algebra/1265, algebra/824,
prealgebra/1686; loses algebra/276, algebra/907, geometry/347. Both signs of v_in at L15/L19 give A64's exact score with a
3-for-3 swap. Conclusion: the L15/L19 v_in columns are inert for this loop once the L22 brake is amplified. The upstream
handle a05 found was weak (logit lens 'equ'/'equivalence'), and the eval agrees.
Queue swap at 01:47:22 went clean: the A64 rest run was killed 3 s after start, runs/A64_q8.jsonl still has its 40 rows,
its overwritten console log was restored from git.

### A64x5 screen (first 40): the curve flattens
13/40 correct, 27 truncated, 13/13 finished correct, 'Wait' 0.01, 'Actually' 0.01, 'No,' 2.09. Same score as A64x3;
against it gains algebra/694, algebra/824, algebra/907, loses algebra/1339, geometry/347, geometry/967 (noise-level swap).
Finished answers are no shorter (median 8.9k tokens vs 8.5k), and the truncated tails are ordinary doubt loops
("Let's check if I made a calculation error", "If I pick (A,B) = (5,-2) for a different reason? No"), not degenerate strings.
Dose curve on the first 40: x1 4, x1.5 9, x2 11, x3 13, x5 13. Reading: the u edit has done all it can once 'Wait' is gone.
The 27 problems still at the cap loop through other phrasing, and amplifying the brake further neither helps nor hurts
at 5.5% relative change to L22 down_proj. A64x3 stays the pick for the full 100 (smaller edit, same score).

### A64x3 on all 100: 5 -> 30
30/100 correct, 70 truncated, 30/30 finished correct, 'Wait' 0.03/kchar (base 3.09). Against the baseline 25 gained, none
lost (two-sided sign test p about 6e-8). Split: the 40 screen problems 4 -> 13 (+9/-0), the 60 held-out problems 1 -> 17
(+16/-0, p about 3e-5). The held-out split is the cleaner number since every edit choice after P64 was made on the first 40;
it lands at 28%, close to the screen's 33%, so the selection effect is small. By level (A64x3 vs base): L1 3/5 vs 1,
L2 11/18 vs 2, L3 9/21 vs 1, L4 4/29 vs 1, L5 3/27 vs 0. The edit unlocks easy and mid problems; hard ones still loop.
Comparison with MIT (7.9 -> 48.1): same model, same kind of intervention (rank-1 weight edit, no gradients, no forward
passes during the edit). We reach 30 with an edit at layer 22, not 15/19, and with the sign chosen from an eval (Deviation 4).
Accuracy is now bounded by the 70 runs that never finish, not by wrong answers.

## 03:19 incident: 32k queue started early

The waiter for the 32k reruns keyed on `grep -q "done A64_q8" runs/queue2.log`, which was already true from the 23:12 A64 screen, so A64x3_32k_q8 started at 03:19 while A64's remaining 60 were running. Its own llama-server was still loading (port 8091 already taken by A64's), and `start_server` accepted A64's server's health check as its own, so the client may have queued requests on A64's server. Stopped at 03:21 via queue.pid with 0 rows written; A64's run was untouched (server healthy, 40 slots busy, 49/100 rows). Its files are kept as `runs/aborted_*A64x3_32k_q8*`. Results cannot be contaminated: each jsonl row is the answer to that client's own request. Fixes: the waiter now matches `^=== HH:MM:SS done A64_q8:` and waits for a second such line; `eval_math.py` now refuses to start if the port already answers.

## A64 on all 100: 5 -> 24

A64 (u x2 in the 64 columns) on the full 100: 24/100, 75 truncated, 24 of 25 finished answers correct, 'Wait' 0.28 per kchar. Against the baseline: +21/-2 (sign test p 7e-5). On the held-out last 60: 13/60 vs 1/60, +13/-1 (p 0.002). A64x3 vs A64 on the same 100: +11/-5 (p 0.21; held-out +7/-3, p 0.34). So x3 over x2 is a consistent trend on both the screen and the full set, but 100 problems cannot separate them. Both edits clear the baseline by a wide margin on problems that played no part in choosing them.

## A64x3 at a 32k token cap: 41/100

Same edit, same 100 problems and sampling, max tokens 32768, 20 slots (the 8 GB card cannot hold 40 slots at 33k context). 41/100 correct, 53 truncated at 32k, 41 of 47 finished answers right. Against A64x3 at 16k: +13/-2 (p 0.007); held-out 21/60 vs 17/60 (+5/-1). Against the 16k baseline: +36/-0. 15 runs finished past 16k tokens, 10 of them right; the other gains are problems that finished under 16k this time but not in the 16k run, because same-seed outputs are not reproducible across slot counts (20 vs 40 changes the batch numerics). The first 6 wrong finished answers for this edit appeared (one is (-inf,2]U[3,inf) for an open-interval answer). 'No,' per kchar is unchanged (2.38). Reading: token budget explains part of the gap to MIT's 48.1%, and the rest is loops that run past 32k. MIT's token budget is not known here. The baseline at 32k (running) gives the budget effect without the edit.

## Baseline at a 32k cap: 15/100

The unedited model at max tokens 32768 (20 slots): 15/100, 88 truncated, all 12 finished answers right; 7 finished past 16k, all 7 right. Against the baseline at 16k: +11/-1 (p 0.006); held-out 8/60 vs 1/60. 'Wait' per kchar unchanged (3.35). Four-way summary on the same 100: baseline 5 (16k) / 15 (32k); A64x3 30 (16k) / 41 (32k). Doubling the budget adds about 10 to either model, and the edit adds about 25 at either budget: the two effects are close to additive. At equal budget A64x3 vs baseline is +25/-0 at 16k and +26/-0 at 32k (p 3e-8; held-out +13/-0). MIT's 7.9% baseline sits between our 16k and 32k baselines, so their budget is probably in that range, and our matched-budget edited score (30 to 41) is below their 48.1%.

# Qwen3.5-2B (from 2026-11-03)

Same protocol, `WSP_MODEL=Qwen3.5-2B`, logs in `logs/2B/`, runs in `runs/2B/`. The 2B shares the 0.8B's tokenizer (every
id in `common.TOK` decodes identically), layer count (24), layer types (full attention at 3, 7, 11, 15, 19, 23) and tensor
names; hidden 2048, MLP 6144, tied embeddings.

### a03 on 2B: the same direction in the same slot (logs/2B/a03_base_diff.txt)

L22 sv0 is again the post-training delta's strongest 'Wait' writer, and stronger than on the 0.8B: doubt +12.11
(zR +14.08, zEnd +1.97; 0.8B +9.22). Its singular energy share is 0.0032, against about 0.0022 elsewhere. L23 again has a
promoter/suppressor pair: sv3 writes 'Wait' (+8.69) and sv2 un-writes it (-7.82, + side code/LaTeX openers). The weaker
writers are L21 sv7 (+5.77), L19 sv6 (+4.94) and L15 sv0 (+4.21). Nothing about the 2B called for looking anywhere else.

### a04 on 2B: u (logs/2B/a04_candidate.txt, a04_directions.pt)

u = L22 sv0. Unembedding z-scores: 'Wait' +31.65 (0.8B +23.3), 'Actually' +8.14, 'Hmm' +5.22, '</think>' +1.97,
'Therefore' +0.12. Random control r: every |z| < 2.7. u's writing is more spread over columns than on the 0.8B: the
top-64 columns hold 17.1% of it (0.8B 22.5%), and the top 2048 hold 85.8%. 64 columns are 1.04% of 6144. The same
fraction as 64 of the 0.8B's 3584 would be 110.

### a08: a weight-only sign proxy that works (src/analysis/a08_self_gain.py; logs/a08_self_gain.txt, logs/2B/)

a06's gate/up cosine proxy was noise on the 0.8B, so the edit sign there came from an eval (Deviation 4). a08 asks a
narrower question that the weights can answer. Put the input to L22's MLP along +u (x = alpha * u through the RMSNorm
gain) and read each neuron's write back along u: c_j = silu(alpha g_j.u~) (alpha up_j.u~) (u.W_down[:, j]). This is a
bilinear readout at a chosen input, not a forward pass. A set of columns with sum c < 0 brakes 'Wait' once it is coming.
Scaling those columns' u-component by (1 + s) changes the brake by s times.

On the 0.8B, two bits are known from evals. The top-64 columns were a strong brake (P64 removed it, 'Wait' x33; A64
doubled it, 'Wait' /13). Post-training's u-delta was a weak promoter (D_full reverted it, 'Wait' 3.22 -> 2.51). a08 gets
both: top-64 sum -0.89 (alpha = 0.25 sqrt(H)), random 64-column sets 95% in [-0.006, +0.002], and post-training's delta
+0.015. A coin gets both 25% of the time, so this is weak calibration, but the 2B reads the same way at every alpha
tried (0.1 to 1.0 sqrt(H)): top-64 -4.59, random [-0.014, +0.003], post-training delta +0.106, r control ~0.
Prediction from weights alone: on the 2B, amplifying (A64) cuts 'Wait' and removing (P64) feeds it, as on the 0.8B.

The top-64 sum is 94-97% of the whole layer's self-gain on both models. Almost all of it is one neuron:

| | column | rank by abs(u.W) | share of layer self-gain | cos(gate, u) | cos(up, u) | cos(down, u) |
|---|---|---|---|---|---|---|
| 0.8B | 573 | 0 | 94% | +0.647 | -0.494 | +0.547 |
| 2B | 5041 | 0 | 96% | +0.646 | -0.590 | +0.562 |

The typical |cos(gate, u)| is 0.02 (p99 0.09 on the 0.8B, 0.06 on the 2B). The next-largest carrier holds under 1%.
The two models carry the same neuron at the same geometry: the gate fires on +u, up is negative on +u, so the activation
is negative and the down column (+u) writes -u. It is a one-sided negative-feedback loop on 'Wait'.

### a09: the brake is a pretraining feature (src/analysis/a09_brake_neuron.py)

The same column in the base model has the same geometry (0.8B base cosines +0.640 / -0.486 / +0.539; 2B +0.638 / -0.579
/ +0.562), the same u-write (0.8B 0.1436 base vs 0.1432 instruct; 2B 0.1903 vs 0.1883) and the same self-gain within 1%.
Post-training changed it no more than a typical column (down 0.100 vs median 0.085 on the 0.8B; 0.099 vs 0.080 on
the 2B). It also holds about none of post-training's u-delta: 0.0% of sigma_0^2, rank 2796 of 3584 on the 0.8B and
1707 of 6144 on the 2B. So u was not built from this neuron. Post-training wrote its 'Wait' direction across many
columns, and that direction lines up (cos 0.55) with a brake the base model already had. The whole-layer brake got
slightly weaker in post-training (0.8B -0.959 -> -0.946, 2B -4.81 -> -4.77), too little to be the story by itself.

Rereading the 0.8B results in this light: A64 doubled a pretraining brake on the post-training 'Wait' direction, and P64
removed its u-write, which is why P64 ran away ('Wait' x33). This is a hypothesis about what the edit does. The test is an
edit that touches only that column.

### Edits built for the 2B round (logs/build_A1x3.log, logs/2B/build_edits.log)

- `2B_A64x3`: L22, top-64 columns by |u.W|, u-component x3 (scale -2). This is the 0.8B winner moved over blind, with the
  same k and scale. The 2B gets no proportional-k tweak and no sign check by eval first.
- `2B_A1x3`: L22, the top-1 column (5041, the brake), u-component x3. Relative change to L22 down_proj is tiny.
- `A1x3` (0.8B): column 573 only, x3. It calibrates the single-neuron claim on the model where A64x3 is known.

### Predictions, written before any 2B edit was evaluated

Eval plan: the 2B edits run all 100 at 8k with the same sampling, slots and seed as `runs/2B/math500/base_8k_q8`.
`A1x3` (0.8B) runs the first 40 at 16k like every 0.8B screen. On the 2B no edit choice used an eval, so all 100
problems count as held-out.

1. `2B_A64x3` vs 2B baseline: 'Wait' per kchar falls at least 5x, truncations fall, and more problems are gained than
   lost, with sign-test p < 0.05.
2. If the brake neuron carries the effect, `A1x3` on the 0.8B gets 'Wait' per kchar under 1.0 (base 3.47 on these 40,
   A64x3 0.11) and at least 8/40 correct (base 4, A64x3 13). If it stays near base ('Wait' above 2.5, 6/40 or fewer),
   the one-neuron story is wrong and A64 works through the other 63 columns' direct writes, which the weights can't sign.
3. `2B_A1x3` lands between the 2B baseline and `2B_A64x3` on both 'Wait' and accuracy, and closer to `2B_A64x3`.

### a10: a bank of token brakes in L22-L23 (src/analysis/a10_self_loops.py; logs/a10_self_loops.txt, logs/2B/)

The brake is one of a class. A SwiGLU neuron with down column d forms a self-loop when its gate and up rows (times the
RMSNorm gain) line up with d. Fed from the side that opens its gate, it writes against its input iff up.d < 0 (a brake)
and with it iff up.d > 0 (an amplifier), whatever the gate's sign. Strength = |cos(gate, d)| |cos(up, d)|. Over all
86k neurons of the 0.8B the median strength is 0.040 and the 99.9th percentile is 0.44. Among the 20 strongest, 19 are
brakes; they sit mostly at column indices under 300 and read as multilingual junk through the unembedding.

Searching by token instead (score = z of the token for the neuron's concept times its strength, brakes only, all
layers) needs no u. For 'Wait' it returns L22 col 573 first on the 0.8B and L22 col 5041 first on the 2B. Those are the
neurons a08 found through u, so the search checks out. Both models carry one brake per discourse token, in the same
layers:

| token | 0.8B brake (z, strength) | 2B brake (z, strength) |
|---|---|---|
| Wait | L22 c573 (+14.9, 0.20) | L22 c5041 (+19.3, 0.20) |
| No | L23 c613 (+25.4, 0.37); L22 c1777 (+22.0, 0.10) | L23 c2014 (+35.4, 0.39); L22 c4317 (+27.5, 0.12) |
| Actually | L22 c787 (+16.1, 0.31) | L22 c4604 (+22.8, 0.31) |
| Therefore | L22 c311 (+13.3, 0.29) | L22 c3552 (+19.2, 0.29) |
| </think> | L23 c1116 (+7.7, 0.39) | L23 c2464 (+14.1, 0.39) |
| \n\n | L21 c371 / L23 c985 | L23 c3548 / L21 c3523 |

The 'No' brake is the lead for what A64x3 leaves behind. a07 found no post-training direction behind 'No,', but a
pretraining brake on it exists, and it is stronger than the Wait brake in both z and strength. Its column is the top
|d.W| column at L23 on both models, so a k=1 project edit along its own column with scale -2 triples exactly that
column. Brake directions are saved in `a10_directions.pt` (keys `brake_Wait`, `brake_No`, `brake_Actually`,
`brake_Therefore`, `brake_think`, each with a `_where` = (layer, col)). Note the opposite lever too: weakening the
`</think>` or 'Therefore' brakes should make committing easier. It is untested.

### No-brake stacks (logs/build_A64x3N3.log, logs/2B/build_A64x3N3.log)

- `A64x3N3` (0.8B): A64x3 plus L23 col 613 tripled.
- `2B_A64x3N3`: 2B_A64x3 plus L23 col 2014 tripled.

Queue (`runs/_queue/2B_round1.sh`, log `2B_round1.log`): 2B `A64x3_8k_q8`, then 0.8B `A1x3_q8` and `A64x3N3_q8` (first 40,
16k), then 2B `A1x3_8k_q8` and `A64x3N3_8k_q8`.

4. `A64x3N3` vs `A64x3` on the 0.8B's first 40 (A64x3: 13/40, 27 truncated, 'No,' 2.40 per kchar): 'No,' per kchar
   falls at least 2x. Accuracy is the open question. If the loop is a state that speaks through whatever word is free,
   it moves to other phrasing and the score stays near 13. If 'No,' is a load-bearing leg as 'Wait' was, truncations
   fall and the score rises. Either result is informative. A score well below 13 would mean the brake also cuts useful
   self-correction.
5. `2B_A64x3N3` vs `2B_A64x3`: same as 4.

## Results, 2B round 1

### Baseline: 26/100 at 8k (runs/2B/math500/base_8k_q8)
74 truncated at the 8k cap, every finished answer right. First 40 11/40, held-out 60 15/60. 'Wait' 1.55 per kchar,
'No,' 1.43 (0.8B base: 3.09 and 2.14). Same loop as the 0.8B, less Wait-heavy.

### 2B_A64x3: 26 -> 46 (runs/2B/math500/A64x3_8k_q8). Prediction 1 holds.
The 0.8B recipe moved over blind: u from the 2B's own post-training delta, top 64 |u.W| columns of L22, u-component
x3, no 2B eval used to choose anything. Gained 21, lost 1 (sign test p 1e-5). First 40 11 -> 19 (+9/-1), held-out
60 15 -> 27 (+12/-0, p 5e-4). Truncated 74 -> 55. 'Wait' 1.55 -> 0.04 per kchar (about 40x; predicted >= 5x).
'No,' unchanged (1.43 -> 1.41), as on the 0.8B, so the No-brake stack is aimed at the right leftover. Gains are
spread over levels, weighted to the hard end (level 4: 5 -> 11, level 5: 2 -> 8). I expected a smaller gain than the
0.8B's because there was less 'Wait' to remove; it was +20 points against the 0.8B's +25, so that hedge was mostly
wrong. This run is cleaner evidence than the 0.8B win: the sign and dose were fixed before any 2B eval.

### A1x3 (0.8B, one column): 4 -> 10 on the first 40 (runs/0.8B/math500/A1x3_q8). Prediction 2 holds.
Only L22 col 573, the Wait brake, tripled: 1 column instead of A64x3's 64, about 1k weights. 'Wait' 3.22 -> 0.02 per
kchar, as low as A64x3's 0.04, so the one neuron carries essentially all of the Wait suppression (predicted under
1.0). Gained 6, lost 0 vs baseline (p 0.03). Against A64x3 it is 10 vs 13 (+2/-5, p 0.45): no significant gap, but
the other 63 columns may add a few points through their direct writes; 40 problems can't tell. 'No,' 2.38 per kchar,
same as A64x3's 2.40, and 29 truncated against 27. One finished answer is wrong (prealgebra/1686), the first
finished-wrong answer in any 16k screen. Reading: the mechanism story from a08/a09 survives its first test. The
lever is a pretraining brake neuron, and the weights found it without an eval choosing it.

### A64x3N3 (0.8B, plus the No brake): 12/40 (runs/0.8B/math500/A64x3N3_q8). Prediction 4 holds on 'No,'; the score does not move.
A64x3 plus L23 col 613, the 'No' brake, tripled. 'No,' 2.40 -> 0.03 per kchar, 80x down (predicted at least 2x).
'Wait' stays at 0.04. But the score is 12/40 against A64x3's 13 (+3/-4, p 1), and 28 still truncate against 27. Every
finished answer is right (12/12). Vs baseline +8/-0 (p 0.008). This is the first branch of the prediction: the loop is
a state that speaks through whatever word is free. With 'Wait' and 'No' both gone, the truncated tails wander through
"Let's check", "Is it", "Is there", "Maybe", "Or maybe" and re-derivations of the same quantity, never committing. Not
well below 13, so the No brake does not visibly cut useful self-correction either. Reading: the discourse markers are
symptoms. Silencing them one at a time is done; the next lever has to act on the decision to stop, which points at the
`</think>` / 'Therefore' brakes from a10 (weaken them so committing gets easier).

### 2B_A1x3 (one column): 26 -> 42 (runs/2B/math500/A1x3_8k_q8). Prediction 3 holds on accuracy; on 'Wait' it overshoots.
Only L22 col 5041, the 2B's Wait brake, tripled. Full 100: 42 vs baseline 26 (+17/-1, p 1e-4) and 2B_A64x3's 46 (+5/-9,
p 0.42). First 40 17 (A64x3 19), held-out 60 25 (A64x3 27). Truncated 58. Every finished answer right. Accuracy lands
between the two and closer to 2B_A64x3, as predicted. 'Wait' was predicted to land between them too; it went to 0.03
per kchar, as low as 2B_A64x3's 0.04, so the miss is in the edit's favour. Same result as the 0.8B's A1x3: one pretraining
neuron, found from the weights, carries the Wait suppression, and the other 63 columns are worth a few points at most
(4 here, 3 there, neither significant). 'No,' 1.43, untouched.

### 2B_A64x3N3 (plus the No brake): 41/100 (runs/2B/math500/A64x3N3_8k_q8). Prediction 5 holds on 'No,'; accuracy flat to down.
2B_A64x3 plus L23 col 2014 tripled. 'No,' 1.41 -> 0.30 per kchar (4.7x; predicted at least 2x), a smaller cut than the
0.8B's 80x. Score 41 vs 2B_A64x3's 46 (+3/-8, p 0.23), truncated 59 vs 55, first 40 19 (same), held-out 22 vs 27. Every
finished answer right. Vs baseline +16/-1. The truncated tails read as on the 0.8B: "Let's check", "Is it", "Is there",
"Correct", recomputing without committing. Same answer as prediction 4, on the bigger model.

### Round 1 summary
Five predictions, written before the evals. 1 (the 0.8B recipe moves to the 2B blind and gains) held: 26 -> 46.
2 and 3 (one Wait-brake neuron does most of it) held on both models: 10 vs 13 on the 0.8B first 40, 42 vs 46 on the 2B
100, neither gap significant; on the 2B, 'Wait' fell all the way instead of partway, which the prediction did not
expect. 4 and 5 (the No brake cuts 'No,') held on the marker, and both answered the open question the same way: the
loop is a state that talks through whatever word is free. Accuracy did not rise on either model (12 vs 13, 41 vs 46).

What this establishes: the weights alone located the lever (a pretraining brake neuron on the post-training 'Wait'
direction), the sign and dose transferred across model sizes without a 2B eval, and the fix is one column. What it
rules out: silencing discourse markers one at a time as a route past the remaining truncations. The leftover failure
is not committing, so round 2 should act on stopping: weaken the `</think>` and 'Therefore' brakes from a10 (the
opposite sign to everything so far), on both models, with predictions written first.
