# AGENTS.md

See README.md for purpose and protocol. docs/STATUS.md is the running plan, progress and results; update it when a run finishes or the plan changes. logs/edit_session.md is the narrative of the weight analysis.

Rules:
- Never write to `~\tools\models\Qwen3.5-0.8B`. It is read-only; copy into `edited/` first.
- During the edit phase, no forward passes through the model (no transformers generate, no llama.cpp). Weight-tensor math only. Log every analysis step to `logs/`.
- Evals go in `runs/` with the exact sampling settings recorded.
