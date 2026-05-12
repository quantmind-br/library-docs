---
title: Disaggregated Prefill - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/disaggregated_prefill/
source: sitemap
fetched_at: 2026-05-07T21:12:39.159334396-03:00
rendered_js: false
word_count: 6
summary: This document provides a script and instructions for implementing disaggregated prefilling in vLLM by splitting prefill and decode workloads across separate instances using KV cache transfer.
tags:
    - vllm
    - disaggregated-prefill
    - kv-cache
    - distributed-inference
    - nccl
    - model-serving
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/disaggregated_prefill.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/disaggregated\_prefill.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/disaggregated_prefill.sh).

```
#!/bin/bash
# This file demonstrates the example usage of disaggregated prefilling
# We will launch 2 vllm instances (1 for prefill and 1 for decode),
# and then transfer the KV cache between them.

set-xe

echo"🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧"
sleep1

# meta-llama/Meta-Llama-3.1-8B-Instruct or deepseek-ai/DeepSeek-V2-Lite
MODEL_NAME=${HF_MODEL_NAME:-meta-llama/Meta-Llama-3.1-8B-Instruct}

# Trap the SIGINT signal (triggered by Ctrl+C)
trap'cleanup'INT

# Cleanup function
cleanup(){
echo"Caught Ctrl+C, cleaning up..."
# Cleanup commands
pgreppython|xargskill-9
pkill-fpython
echo"Cleanup complete. Exiting."
exit0
}


if[[-z"${VLLM_HOST_IP:-}"]];then
exportVLLM_HOST_IP=127.0.0.1
echo"Using default VLLM_HOST_IP=127.0.0.1 (override by exporting VLLM_HOST_IP before running this script)"
else
echo"Using provided VLLM_HOST_IP=${VLLM_HOST_IP}"
fi


# install quart first -- required for disagg prefill proxy serve
ifpython3-c"import quart"&>/dev/null;then
echo"Quart is already installed."
else
echo"Quart is not installed. Installing..."
python3-mpipinstallquart
fi

# a function that waits vLLM server to start
wait_for_server(){
localport=$1
timeout1200bash-c"
    until curl -i localhost:${port}/v1/models > /dev/null; do
      sleep 1
    done"&&return0||return1
}


# You can also adjust --kv-ip and --kv-port for distributed inference.

# prefilling instance, which is the KV producer
CUDA_VISIBLE_DEVICES=0vllmserve"$MODEL_NAME"\
--host0.0.0.0\
--port8100\
--max-model-len100\
--gpu-memory-utilization0.8\
--trust-remote-code\
--kv-transfer-config\
'{"kv_connector":"P2pNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_buffer_size":"1e9","kv_port":"14579","kv_connector_extra_config":{"proxy_ip":"'"$VLLM_HOST_IP"'","proxy_port":"30001","http_ip":"'"$VLLM_HOST_IP"'","http_port":"8100","send_type":"PUT_ASYNC"}}'&

# decoding instance, which is the KV consumer  
CUDA_VISIBLE_DEVICES=1vllmserve"$MODEL_NAME"\
--host0.0.0.0\
--port8200\
--max-model-len100\
--gpu-memory-utilization0.8\
--trust-remote-code\
--kv-transfer-config\
'{"kv_connector":"P2pNcclConnector","kv_role":"kv_consumer","kv_rank":1,"kv_parallel_size":2,"kv_buffer_size":"1e10","kv_port":"14580","kv_connector_extra_config":{"proxy_ip":"'"$VLLM_HOST_IP"'","proxy_port":"30001","http_ip":"'"$VLLM_HOST_IP"'","http_port":"8200","send_type":"PUT_ASYNC"}}'&

# wait until prefill and decode instances are ready
wait_for_server8100
wait_for_server8200

# launch a proxy server that opens the service at port 8000
# the workflow of this proxy:
# - send the request to prefill vLLM instance (port 8100), change max_tokens 
#   to 1
# - after the prefill vLLM finishes prefill, send the request to decode vLLM 
#   instance
# NOTE: the usage of this API is subject to change --- in the future we will 
# introduce "vllm connect" to connect between prefill and decode instances
python3../../benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py&
sleep1

# serve two example requests
output1=$(curl-XPOST-shttp://localhost:8000/v1/completions\
-H"Content-Type: application/json"\
-d'{
"model": "'"$MODEL_NAME"'",
"prompt": "San Francisco is a",
"max_tokens": 10,
"temperature": 0
}')

output2=$(curl-XPOST-shttp://localhost:8000/v1/completions\
-H"Content-Type: application/json"\
-d'{
"model": "'"$MODEL_NAME"'",
"prompt": "Santa Clara is a",
"max_tokens": 10,
"temperature": 0
}')


# Cleanup commands
pgreppython|xargskill-9
pkill-fpython

echo""

sleep1

# Print the outputs of the curl requests
echo""
echo"Output of first request: $output1"
echo"Output of second request: $output2"

echo"🎉🎉 Successfully finished 2 test requests! 🎉🎉"
echo""
```