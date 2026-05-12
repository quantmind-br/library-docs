---
title: MooncakeConnector Usage Guide - vLLM
url: https://docs.vllm.ai/en/latest/features/mooncake_connector_usage/
source: sitemap
fetched_at: 2026-05-07T21:14:13.139630031-03:00
rendered_js: false
word_count: 300
summary: This document provides instructions for integrating the Mooncake connector with vLLM to enable efficient distributed KV cache transfer using high-speed multi-level caching.
tags:
    - vllm
    - mooncake
    - kv-cache
    - disaggregated-serving
    - rdma
    - inference-optimization
    - performance
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/mooncake_connector_usage.md "Edit this page")

## About Mooncake[¶](#about-mooncake "Permanent link")

Mooncake aims to enhance the inference efficiency of large language models (LLMs), especially in slow object storage environments, by constructing a multi-level caching pool on high-speed interconnected DRAM/SSD resources. Compared to traditional caching systems, Mooncake utilizes (GPUDirect) RDMA technology to transfer data directly in a zero-copy manner, while maximizing the use of multi-NIC resources on a single machine.

For more details about Mooncake, please refer to [Mooncake project](https://github.com/kvcache-ai/Mooncake) and [Mooncake documents](https://kvcache-ai.github.io/Mooncake/).

## Prerequisites[¶](#prerequisites "Permanent link")

### Installation[¶](#installation "Permanent link")

Install mooncake through pip: `uv pip install mooncake-transfer-engine`.

Refer to [Mooncake official repository](https://github.com/kvcache-ai/Mooncake) for more installation instructions

## Usage[¶](#usage "Permanent link")

### Prefiller Node (192.168.0.2)[¶](#prefiller-node-19216802 "Permanent link")

```
vllmserveQwen/Qwen2.5-7B-Instruct--port8010--kv-transfer-config'{"kv_connector":"MooncakeConnector","kv_role":"kv_producer"}'
```

### Decoder Node (192.168.0.3)[¶](#decoder-node-19216803 "Permanent link")

```
vllmserveQwen/Qwen2.5-7B-Instruct--port8020--kv-transfer-config'{"kv_connector":"MooncakeConnector","kv_role":"kv_consumer"}'
```

### Proxy[¶](#proxy "Permanent link")

```
pythonexamples/disaggregated/disaggregated_serving/mooncake_connector/mooncake_connector_proxy.py--prefillhttp://192.168.0.2:8010--decodehttp://192.168.0.3:8020
```

Now you can send requests to the proxy server through port 8000.

## Environment Variables[¶](#environment-variables "Permanent link")

- `VLLM_MOONCAKE_BOOTSTRAP_PORT`: Port for Mooncake bootstrap server
  
  - Default: 8998
  - Required only for prefiller instances
  - For headless instances, must be the same as the master instance
  - Each instance needs a unique port on its host; using the same port number across different hosts is fine
- `VLLM_MOONCAKE_ABORT_REQUEST_TIMEOUT`: Timeout (in seconds) for automatically releasing the prefiller’s KV cache for a particular request. (Optional)
  
  - Default: 480
  - If a request is aborted and the decoder has not yet notified the prefiller, the prefill instance will release its KV-cache blocks after this timeout to avoid holding them indefinitely.

## KV Transfer Config[¶](#kv-transfer-config "Permanent link")

### KV Role Options[¶](#kv-role-options "Permanent link")

- **kv\_producer**: For prefiller instances that generate KV caches
- **kv\_consumer**: For decoder instances that consume KV caches from prefiller
- **kv\_both**: Enables symmetric functionality where the connector can act as both producer and consumer. This provides flexibility for experimental setups and scenarios where the role distinction is not predetermined.

<!--THE END-->

- **num\_workers**: Size of thread pool for one prefiller worker to transfer KV caches by mooncake. (default 10)
- **mooncake\_protocol**: Mooncake connector protocol. (default "rdma")

## Example Scripts/Code[¶](#example-scriptscode "Permanent link")

Refer to these example scripts in the vLLM repository:

- [run\_mooncake\_connector.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/mooncake_connector/run_mooncake_connector.sh)
- [mooncake\_connector\_proxy.py](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/mooncake_connector/mooncake_connector_proxy.py)