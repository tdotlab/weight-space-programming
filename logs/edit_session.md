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
