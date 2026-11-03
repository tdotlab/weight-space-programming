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
