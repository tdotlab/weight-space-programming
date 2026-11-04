#!/bin/bash
# Round 2 (2026-11-03): weaken the 'Final' brake (L23) on both models, plus a 'Therefore'-brake control on the 2B.
# Builds six edits (each checked to have edited exactly the intended column), then runs six evals.
# Predictions: logs/edit_session.md, "Round 2". Output: runs/_queue/round2.log.
# Stop everything: taskkill //F //T //PID $(cat runs/_queue/round2.pid)
cd "$(dirname "$0")/../.."
cat /proc/$$/winpid > runs/_queue/round2.pid
export PYTHONIOENCODING=utf-8
Q=~/tools/llama.cpp/b11804/llama-quantize.exe
PY=.venv/Scripts/python.exe

build() {  # NAME SIZE START DIRKEY LAYER COL SCALE   (START "" = the original model)
  local name=$1 size=$2 start=$3 key=$4 L=$5 col=$6 s=$7 logdir=logs
  [ "$size" = 2B ] && logdir=logs/2B
  echo "=== $(date '+%H:%M:%S') build $name ($size, start ${start:-original}, L$L col $col, scale $s)"
  WSP_MODEL=Qwen3.5-$size $PY src/make_edit.py --name "$name" --kind project ${start:+--start "$start"} \
    --dirfile $logdir/a12_directions.pt --dir "$key" --layers "$L" --k 1 --scale "$s" > "$logdir/build_${name#2B_}.log" 2>&1 \
    && "$Q" "gguf/$name-f16.gguf" "gguf/$name-q8_0.gguf" Q8_0 > /dev/null 2>&1 || { echo "build $name failed"; exit 1; }
  $PY -c "import json,sys; c=json.load(open('edited/$name/EDIT.json'))['per_layer'][0]['columns']; print('    edited L$L columns', c); sys.exit(c != [$col])" \
    || { echo "build $name edited the wrong column"; exit 1; }
}

build 2B_A64x3Fh 2B 2B_A64x3 brake_Final 23 6022 0.5
build 2B_A64x3F0 2B 2B_A64x3 brake_Final 23 6022 1.0
build 2B_Fh 2B "" brake_Final 23 6022 0.5
build A64x3Fh 0.8B A64x3 brake_Final 23 1238 0.5
build A64x3F0 0.8B A64x3 brake_Final 23 1238 1.0
build 2B_A64x3T0 2B 2B_A64x3 brake_Therefore 22 3895 1.0

while curl -s -m 2 http://127.0.0.1:8091/health > /dev/null; do sleep 10; done
WSP_MODEL=Qwen3.5-2B MAXTOK=8192 PAR=40 bash src/run_queue.sh A64x3Fh_8k_q8:gguf/2B_A64x3Fh-q8_0.gguf:qwen \
  A64x3F0_8k_q8:gguf/2B_A64x3F0-q8_0.gguf:qwen Fh_8k_q8:gguf/2B_Fh-q8_0.gguf:qwen
FIRST=40 MAXTOK=16384 PAR=40 bash src/run_queue.sh A64x3Fh_q8:gguf/A64x3Fh-q8_0.gguf:qwen A64x3F0_q8:gguf/A64x3F0-q8_0.gguf:qwen
WSP_MODEL=Qwen3.5-2B MAXTOK=8192 PAR=40 bash src/run_queue.sh A64x3T0_8k_q8:gguf/2B_A64x3T0-q8_0.gguf:qwen
echo "=== $(date '+%H:%M:%S') round 2 done"
