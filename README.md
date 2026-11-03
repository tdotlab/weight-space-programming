# WeightSpaceProgramming

Home replication attempt of MIT CSAIL's "Weight-Space Programming" (Nov 2, 2026): a frontier LLM edits Qwen3.5-0.8B's weights to stop its math reasoning loops, with no gradients and no forward passes. Here the editor is Claude instead of GPT-6 Astra.

## Setup

- Model (original, read-only): `~\tools\models\Qwen3.5-0.8B`
  sha256 `04b1c301231dd422b8860db31311ab2721511346a32cb1e079c4c4e5f1fe4696`
- Python env: `uv sync` (uv at `~\tools\uv\0.12.19\uv.exe`). Torch here is CPU-only and is used for weight math only.
- Inference/eval: llama.cpp at `~\tools\llama.cpp\b11804` (GTX 1070), via GGUF conversions.

## Protocol

1. Baseline: MATH-500 subset, record accuracy and loop rate (hit token limit). Run both greedy and Qwen's recommended sampling (presence_penalty 1.5).
2. Blind edit: analyze weights with numpy/torch, no forward passes. Every analysis step logged in `logs/`. Edits are written only to copies in `edited/`.
3. Re-test edited model plus a same-size random-direction control.

## Layout

`src/` scripts, `runs/` eval outputs (each run also exported as readable per-problem transcripts in `runs/<name>/`), `edited/` modified weight copies (gitignored), `logs/` edit-session log, `docs/` notes.

Current state, plan and results: [docs/STATUS.md](docs/STATUS.md).
