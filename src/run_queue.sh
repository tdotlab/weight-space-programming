#!/bin/bash
# Run evals one after another (single GPU). Usage: [FIRST=40] bash src/run_queue.sh NAME:GGUF:PRESET [...]
# MAXTOK=N sets the token cap (default 16384; 32768 needs PAR=20 on 8 GB).
# FIRST=K screens on the first K of the 100-problem sample (the same problems as a full run's first wave).
# WSP_MODEL picks the model folder: runs land in runs/<size>/math500/NAME/ (default size 0.8B).
# Send this script's own output to runs/_queue/<something>.log.
cd "$(dirname "$0")/.."
mkdir -p runs/_queue
# Windows: killing the launching shell leaves this script alive. queue.pid holds the Windows PID.
# Stop with: taskkill //F //T //PID $(cat runs/_queue/queue.pid)
cat /proc/$$/winpid > runs/_queue/queue.pid
model=${WSP_MODEL:-Qwen3.5-0.8B}
size=${model##*-}
for spec in "$@"; do
  IFS=: read name gguf preset <<< "$spec"
  rd="runs/$size/math500/$name"
  mkdir -p "$rd"
  echo "=== $(date '+%H:%M:%S') start $name"
  .venv/Scripts/python.exe src/eval_math.py --gguf "$gguf" --name "$name" --n 100 --first ${FIRST:-0} --preset "$preset" --max-tokens ${MAXTOK:-16384} --parallel ${PAR:-40} > "$rd/console.log" 2>&1
  echo "=== $(date '+%H:%M:%S') done $name: $(grep -E '"acc"|"truncated"' $rd/summary.json | tr -d '\n ')"
  .venv/Scripts/python.exe src/index_runs.py > /dev/null
done
