#!/bin/bash
# Run evals one after another (single GPU). Usage: [FIRST=40] bash src/run_queue.sh NAME:GGUF:PRESET [...]
# MAXTOK=N sets the token cap (default 16384; 32768 needs PAR=20 on 8 GB).
# FIRST=K screens on the first K of the 100-problem sample (the same problems as a full run's first wave).
cd "$(dirname "$0")/.."
# Windows: killing the launching shell leaves this script alive. queue.pid holds the Windows PID.
# Stop with: taskkill //F //T //PID $(cat runs/queue.pid)
cat /proc/$$/winpid > runs/queue.pid
for spec in "$@"; do
  IFS=: read name gguf preset <<< "$spec"
  echo "=== $(date '+%H:%M:%S') start $name"
  .venv/Scripts/python.exe src/eval_math.py --gguf "$gguf" --name "$name" --n 100 --first ${FIRST:-0} --preset "$preset" --max-tokens ${MAXTOK:-16384} --parallel ${PAR:-40} > "runs/$name.console.log" 2>&1
  echo "=== $(date '+%H:%M:%S') done $name: $(grep -E '"acc"|"truncated"' runs/$name.summary.json | tr -d '\n ')"
done
