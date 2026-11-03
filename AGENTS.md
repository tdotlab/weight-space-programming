# AGENTS.md

See README.md for purpose and protocol. docs/STATUS.md is the running plan, progress and results; update it when a run finishes or the plan changes. logs/edit_session.md is the narrative of the weight analysis.

Rules:
- Every downloaded original under `~\tools\models\` (Qwen3.5-0.8B, 2B and their -Base models, and any later ones) is read-only and kept permanently; never edit, delete or replace them. Edits copy into `edited/` first. Disk space is not a reason to remove an original.
- During the edit phase, no forward passes through the model (no transformers generate, no llama.cpp). Weight-tensor math only. Log every analysis step to `logs/`.
- Evals go in `runs/` with the exact sampling settings recorded.
