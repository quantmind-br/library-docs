---
title: Ec Both Encoder - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/ec_both_encoder/
source: sitemap
fetched_at: 2026-05-07T21:12:40.920926399-03:00
rendered_js: false
word_count: 9
summary: This document provides a bash script for configuring and benchmarking vLLM with a disaggregated encoder setup using an EC (Encoder-Cache) connector.
tags:
    - vllm
    - disaggregated-serving
    - encoder-cache
    - benchmarking
    - model-serving
    - automation-script
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/ec_both_encoder.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/ec\_both\_encoder](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/ec_both_encoder).

## Ec Both Encoder[¶](#ec-both-encoder_1 "Permanent link")

```
#!/bin/bash
set-euopipefail

MODEL="${MODEL:-Qwen/Qwen2.5-VL-3B-Instruct}"
PORT="${PORT:-8000}"
GPU="${GPU:-0}"
NUM_PROMPTS="${NUM_PROMPTS:-200}"
EC_SHARED_STORAGE_PATH="${EC_SHARED_STORAGE_PATH:-/tmp/ec_cache}"
TIMEOUT="${TIMEOUT:-600}"

SERVER_PID=""

cleanup(){
echo"Stopping server..."
if[[-n"$SERVER_PID"]]&&kill-0"$SERVER_PID"2>/dev/null;then
kill"$SERVER_PID"2>/dev/null||true
wait"$SERVER_PID"2>/dev/null||true
fi
echo"Done."
}
trapcleanupEXITINTTERM

wait_for_server(){
localdeadline=$((SECONDS+TIMEOUT))
echo"Waiting for server on port $PORT..."
while((SECONDS<deadline));do
ifcurl-sf"http://localhost:${PORT}/v1/models">/dev/null2>&1;then
echo"Server ready."
return0
fi
sleep2
done
echo"ERROR: Server did not start within ${TIMEOUT}s"
return1
}

rm-rf"$EC_SHARED_STORAGE_PATH"
mkdir-p"$EC_SHARED_STORAGE_PATH"

###############################################################################
# Start server with ec_both
###############################################################################
CUDA_VISIBLE_DEVICES="$GPU"\
vllmserve"$MODEL"\
--port"$PORT"\
--enforce-eager\
--ec-transfer-config'{
        "ec_connector": "ECExampleConnector",
        "ec_role": "ec_both",
        "ec_connector_extra_config": {
            "shared_storage_path": "'"$EC_SHARED_STORAGE_PATH"'"
        }
    }'\
"$@"&

SERVER_PID=$!
wait_for_server

###############################################################################
# Benchmark -- dataset contains duplicate images, exercises cache hits
###############################################################################
echo"Running benchmark ($NUM_PROMPTS prompts)..."
vllmbenchserve\
--model"$MODEL"\
--backendopenai-chat\
--endpoint/v1/chat/completions\
--dataset-namehf\
--dataset-pathlmarena-ai/VisionArena-Chat\
--seed0\
--num-prompts"$NUM_PROMPTS"\
--port"$PORT"

echo"Benchmark complete."
```