#!/bin/bash
# 2B round 1 (2026-11-03): build the No-brake stacks, wait for the 2B baseline to finish, then run five evals.
# Output: runs/_queue/2B_round1.log. Stop: taskkill //F //T //PID $(cat runs/_queue/queue.pid)
cd "$(dirname "$0")/../.."
export PYTHONIOENCODING=utf-8
Q=~/tools/llama.cpp/b11804/llama-quantize.exe

echo "=== $(date '+%H:%M:%S') build A64x3N3 (0.8B: A64x3 + L23 No-brake column tripled)"
.venv/Scripts/python.exe src/make_edit.py --name A64x3N3 --kind project --start A64x3 \
  --dirfile logs/a10_directions.pt --dir brake_No --layers 23 --k 1 --scale -2 > logs/build_A64x3N3.log 2>&1 \
  && "$Q" gguf/A64x3N3-f16.gguf gguf/A64x3N3-q8_0.gguf Q8_0 > /dev/null 2>&1 || { echo "build A64x3N3 failed"; exit 1; }
echo "=== $(date '+%H:%M:%S') build 2B_A64x3N3"
WSP_MODEL=Qwen3.5-2B .venv/Scripts/python.exe src/make_edit.py --name 2B_A64x3N3 --kind project --start 2B_A64x3 \
  --dirfile logs/2B/a10_directions.pt --dir brake_No --layers 23 --k 1 --scale -2 > logs/2B/build_A64x3N3.log 2>&1 \
  && "$Q" gguf/2B_A64x3N3-f16.gguf gguf/2B_A64x3N3-q8_0.gguf Q8_0 > /dev/null 2>&1 || { echo "build 2B_A64x3N3 failed"; exit 1; }

echo "=== $(date '+%H:%M:%S') waiting for base_8k_q8"
until grep -qE "^=== [0-9:]+ done base_8k_q8:" runs/_queue/2B_queue.log; do sleep 30; done
while curl -s -m 2 http://127.0.0.1:8091/health > /dev/null; do sleep 10; done
sleep 20

WSP_MODEL=Qwen3.5-2B MAXTOK=8192 PAR=40 bash src/run_queue.sh A64x3_8k_q8:gguf/2B_A64x3-q8_0.gguf:qwen
FIRST=40 MAXTOK=16384 PAR=40 bash src/run_queue.sh A1x3_q8:gguf/A1x3-q8_0.gguf:qwen A64x3N3_q8:gguf/A64x3N3-q8_0.gguf:qwen
WSP_MODEL=Qwen3.5-2B MAXTOK=8192 PAR=40 bash src/run_queue.sh A1x3_8k_q8:gguf/2B_A1x3-q8_0.gguf:qwen A64x3N3_8k_q8:gguf/2B_A64x3N3-q8_0.gguf:qwen
echo "=== $(date '+%H:%M:%S') round 1 done"
