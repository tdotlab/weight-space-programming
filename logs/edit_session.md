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
