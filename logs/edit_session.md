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
