# AGENTS.md

See README.md for purpose and protocol.

Rules:
- Never write to `~\tools\models\Qwen3.5-0.8B`. It is read-only; copy into `edited/` first.
- During the edit phase, no forward passes through the model (no transformers generate, no llama.cpp). Weight-tensor math only. Log every analysis step to `logs/`.
- Evals go in `runs/` with the exact sampling settings recorded.
