---
title: PD Disaggregation — SGLang
url: https://docs.sglang.io/advanced_features/pd_disaggregation.html
source: crawler
fetched_at: 2026-02-04T08:46:53.665020415-03:00
rendered_js: false
word_count: 519
summary: This document explains the concept and implementation of Prefill and Decoding (PD) disaggregation in SGLang to improve LLM inference efficiency. It provides configuration details, deployment examples for Mooncake and NIXL backends, and instructions for routing and profiling.
tags:
    - sglang
    - pd-disaggregation
    - llm-inference
    - distributed-computing
    - kv-cache
    - mooncake
    - nixl
category: guide
---

## Contents

## PD Disaggregation[#](#pd-disaggregation "Link to this heading")

## Why and What is PD Disaggregation?[#](#why-and-what-is-pd-disaggregation "Link to this heading")

Large Language Model (LLM) inference comprises two distinct phases: **Prefill** and **Decode**. The Prefill phase is computation-intensive, processing the entire input sequence, while the Decode phase is memory-intensive, managing the Key-Value (KV) cache for token generation. Traditionally, these phases are handled within a unified engine, where combined scheduling of prefill and decode batches introduces inefficiencies. To address these challenges, we introduce **Prefill and Decoding (PD) Disaggregation** in SGLang.

### Issues with Unified Scheduling[#](#issues-with-unified-scheduling "Link to this heading")

The conventional unified engine, which processes prefill and decode batches together, results in two significant problems:

1. **Prefill Interruption**: Incoming prefill batches frequently interrupt ongoing decode batches, causing substantial delays in token generation.
2. **DP Attention Imbalance**: In data-parallel (DP) attention, one DP worker may process a prefill batch while another handles a decode batch simultaneously, leading to increased decode latency.

PD Disaggregation resolves these by separating the two stages, enabling tailored optimizations for each.

For the design details, please refer to [link](https://docs.google.com/document/d/1rQXJwKd5b9b1aOzLh98mnyMhBMhlxXA5ATZTHoQrwvc/edit?tab=t.0).

Currently, we support Mooncake and NIXL as the transfer engine.

## Profiling in PD Disaggregation Mode[#](#profiling-in-pd-disaggregation-mode "Link to this heading")

When you need to profile prefill or decode workers in PD disaggregation mode, please refer to the [Profile In PD Disaggregation Mode](https://docs.sglang.io/developer_guide/benchmark_and_profiling.html#profile-in-pd-disaggregation-mode) section in the Benchmark and Profiling guide. Due to torch profiler limitations, prefill and decode workers must be profiled separately using dedicated command-line options.

## Router Integration[#](#router-integration "Link to this heading")

For deploying PD disaggregation at scale with load balancing and fault tolerance, SGLang provides a router. The router can distribute requests between prefill and decode instances using various routing policies. For detailed information on setting up routing with PD disaggregation, including configuration options and deployment patterns, see the [SGLang Model Gateway (former Router)](https://docs.sglang.io/advanced_features/sgl_model_gateway.html#prefill-decode-disaggregation).

## Mooncake[#](#mooncake "Link to this heading")

### Requirements[#](#requirements "Link to this heading")

```
uvpipinstallmooncake-transfer-engine
```

### Usage[#](#usage "Link to this heading")

### Llama Single Node[#](#llama-single-node "Link to this heading")

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modeprefill\
--port30000\
--disaggregation-ib-devicemlx5_roce0
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modedecode\
--port30001\
--base-gpu-id1\
--disaggregation-ib-devicemlx5_roce0
python-msglang_router.launch_router--pd-disaggregation--prefillhttp://127.0.0.1:30000--decodehttp://127.0.0.1:30001--host0.0.0.0--port8000
```

### DeepSeek Multi-Node[#](#deepseek-multi-node "Link to this heading")

```
# prefill 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-ib-device${device_name}\
--disaggregation-modeprefill\
--host${local_ip}\
--port30000\
--trust-remote-code\
--dist-init-addr${prefill_master_ip}:5000\
--nnodes2\
--node-rank0\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8
# prefill 1
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-ib-device${device_name}\
--disaggregation-modeprefill\
--host${local_ip}\
--port30000\
--trust-remote-code\
--dist-init-addr${prefill_master_ip}:5000\
--nnodes2\
--node-rank1\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8
# decode 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-ib-device${device_name}\
--disaggregation-modedecode\
--host${local_ip}\
--port30001\
--trust-remote-code\
--dist-init-addr${decode_master_ip}:5000\
--nnodes2\
--node-rank0\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8\
--max-running-requests128
# decode 1
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-ib-device${device_name}\
--disaggregation-modedecode\
--host${local_ip}\
--port30001\
--trust-remote-code\
--dist-init-addr${decode_master_ip}:5000\
--nnodes2\
--node-rank1\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8\
--max-running-requests128
```

### Advanced Configuration[#](#advanced-configuration "Link to this heading")

PD Disaggregation with Mooncake supports the following environment variables for fine-grained control over system behavior.

#### NVLink Transport Configuration[#](#nvlink-transport-configuration "Link to this heading")

To enable NVLink transport for KV cache transfers with the mooncake backend (recommended for NVL72 deployments), set the following environment variables. Note that auxiliary data transfer will still use TCP as a temporary workaround.

```
exportSGLANG_MOONCAKE_CUSTOM_MEM_POOL=True
exportMC_FORCE_MNNVL=True
```

#### Prefill Server Configuration[#](#prefill-server-configuration "Link to this heading")

If a greater mean TTFT is acceptable, you can `export SGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600` (10 minutes) to relax the timeout condition. Please be aware that this setting will cause prefill instances to take a longer time to clean up the affected memory resources when a running decode node loses connection.

#### Decode Server Configuration[#](#decode-server-configuration "Link to this heading")

If a greater mean TTFT is acceptable, you can `export SGLANG_DISAGGREGATION_WAITING_TIMEOUT=600` (10 minutes) to relax the timeout condition.

## NIXL[#](#nixl "Link to this heading")

### Requirements[#](#id1 "Link to this heading")

Install via pip.

Or build from source - may be required if you already have UCX installed.

```
gitclonehttps://github.com/ai-dynamo/nixl.git
cdnixl
pipinstall.--config-settings=setup-args="-Ducx_path=/path/to/ucx"
```

### Usage[#](#id2 "Link to this heading")

### Llama Single Node[#](#id3 "Link to this heading")

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modeprefill\
--port30000\
--disaggregation-transfer-backendnixl
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modedecode\
--port30001\
--base-gpu-id1\
--disaggregation-transfer-backendnixl
python-msglang_router.launch_router--pd-disaggregation--prefillhttp://127.0.0.1:30000--decodehttp://127.0.0.1:30001--host0.0.0.0--port8000
```

### DeepSeek Multi-Node[#](#id4 "Link to this heading")

```
# prefill 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendnixl\
--disaggregation-modeprefill\
--host${local_ip}\
--port30000\
--trust-remote-code\
--dist-init-addr${prefill_master_ip}:5000\
--nnodes2\
--node-rank0\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8
# prefill 1
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendnixl\
--disaggregation-modeprefill\
--host${local_ip}\
--port30000\
--trust-remote-code\
--dist-init-addr${prefill_master_ip}:5000\
--nnodes2\
--node-rank1\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8
# decode 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendnixl\
--disaggregation-modedecode\
--host${local_ip}\
--port30001\
--trust-remote-code\
--dist-init-addr${decode_master_ip}:5000\
--nnodes2\
--node-rank0\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8\
--max-running-requests128
# decode 1
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendnixl\
--disaggregation-modedecode\
--host${local_ip}\
--port30001\
--trust-remote-code\
--dist-init-addr${decode_master_ip}:5000\
--nnodes2\
--node-rank1\
--tp-size16\
--dp-size8\
--enable-dp-attention\
--moe-a2a-backenddeepep\
--mem-fraction-static0.8\
--max-running-requests128
```

### Advanced Configuration[#](#id5 "Link to this heading")

#### NIXL Backend Selection[#](#nixl-backend-selection "Link to this heading")

By default, NIXL uses the **UCX** backend for KV cache transfers. You can select a different NIXL plugin backend depending on your infrastructure using the environment variable `SGLANG_DISAGGREGATION_NIXL_BACKEND`.

Example: `export SGLANG_DISAGGREGATION_NIXL_BACKEND=LIBFABRIC`

**Available backends:** UCX (default), LIBFABRIC, or any installed NIXL plugin.

Example usage:

```
exportSGLANG_DISAGGREGATION_NIXL_BACKEND=LIBFABRIC
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modeprefill\
--disaggregation-transfer-backendnixl\
--port30000
```

## ASCEND[#](#ascend "Link to this heading")

### Usage[#](#id6 "Link to this heading")

Use ascend backend with [memfabric\_hybrid](https://gitcode.com/Ascend/memfabric_hybrid) and ASCEND\_MF\_STORE\_URL being set

```
pipinstallmemfabric-hybrid==1.0.0
exportASCEND_MF_STORE_URL="tcp://xxx.xx.xxx.xxx:xxxx"
```

Use mooncake backend, more details can be found in mooncake section.

```
exportENABLE_ASCEND_TRANSFER_WITH_MOONCAKE=true
```

ASCEND\_NPU\_PHY\_ID need to be set in container env

```
exportASCEND_NPU_PHY_ID=xxx
```

### Llama Single Node[#](#id7 "Link to this heading")

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modeprefill\
--port30000\
--disaggregation-transfer-backendascend
python-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modedecode\
--port30001\
--base-gpu-id1\
--disaggregation-transfer-backendascend
python-msglang_router.launch_router--pd-disaggregation--prefillhttp://127.0.0.1:30000--decodehttp://127.0.0.1:30001--host0.0.0.0--port8000
```

### DeepSeek Multi-Node[#](#id8 "Link to this heading")

```
# prefill 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendascend\
--disaggregation-modeprefill\
--host${local_ip}\
--port30000\
--trust-remote-code\
--dist-init-addr${prefill_master_ip}:5000\
--nnodes1\
--node-rank0\
--tp-size16
# decode 0
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3-0324\
--disaggregation-transfer-backendascend\
--disaggregation-modedecode\
--host${local_ip}\
--port30001\
--trust-remote-code\
--dist-init-addr${decode_master_ip}:5000\
--nnodes1\
--node-rank0\
--tp-size16
```