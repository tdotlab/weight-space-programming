#!/bin/bash
# Run evals one after another (single GPU). Usage: bash src/run_queue.sh NAME:GGUF:PRESET [...]
cd "$(dirname "$0")/.."
# Windows: killing the launching shell leaves this script alive. Stop with: taskkill //F //T //PID $(cat runs/queue.pid)
echo $$ > runs/queue.pid
for spec in "$@"; do
  IFS=: read name gguf preset <<< "$spec"
  echo "=== $(date '+%H:%M:%S') start $name"
  .venv/Scripts/python.exe src/eval_math.py --gguf "$gguf" --name "$name" --n 100 --preset "$preset" --max-tokens 16384 --parallel ${PAR:-40} > "runs/$name.console.log" 2>&1
  echo "=== $(date '+%H:%M:%S') done $name: $(grep -E '"acc"|"truncated"' runs/$name.summary.json | tr -d '\n ')"
done
