---
title: NixlConnector Usage Guide - vLLM
url: https://docs.vllm.ai/en/latest/features/nixl_connector_usage/
source: sitemap
fetched_at: 2026-05-07T21:14:15.814287379-03:00
rendered_js: false
word_count: 825
summary: This document provides instructions on how to configure and use the NixlConnector in vLLM to enable high-performance, asynchronous cross-process KV cache transfer for disaggregated prefilling architectures.
tags:
    - vllm
    - kv-cache
    - disaggregated-prefilling
    - nixl
    - ucx
    - distributed-inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/nixl_connector_usage.md "Edit this page")

NixlConnector is a high-performance KV cache transfer connector for vLLM's disaggregated prefilling feature. It provides fully asynchronous send/receive operations using the NIXL library for efficient cross-process KV cache transfer.

For feature compatibility details (supported model architectures, TP configurations, and feature interactions), see the [NixlConnector Compatibility Matrix](https://docs.vllm.ai/en/latest/features/nixl_connector_compatibility/).

## Prerequisites[¶](#prerequisites "Permanent link")

### Installation[¶](#installation "Permanent link")

Install the NIXL library: `uv pip install nixl`, as a quick start on Nvidia platform.

- Refer to [NIXL official repository](https://github.com/ai-dynamo/nixl) for more installation instructions
- The specified required NIXL version can be found in [requirements/kv\_connectors.txt](https://github.com/vllm-project/vllm/blob/main/requirements/kv_connectors.txt) and other relevant config files

For ROCm platform, the [base ROCm docker file](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base) includes RIXL and ucx already.

- Refer to [RIXL official repository](https://github.com/rocm/rixl) for more information
- The supportive libraries for RIXL can be found in [requirements/kv\_connectors\_rocm.txt](https://github.com/vllm-project/vllm/blob/main/requirements/kv_connectors_rocm.txt)
- In the future we may remove RIXL from docker image file and users will be able to install from pre-compiled binary packages

For non-cuda platform, please install nixl with ucx build from source, instructed as below.

```
pythontools/install_nixl_from_source_ubuntu.py
```

### Transport Configuration[¶](#transport-configuration "Permanent link")

NixlConnector uses NIXL library for underlying communication, which supports multiple transport backends. UCX (Unified Communication X) is the primary default transport library used by NIXL. Configure transport environment variables:

```
# Example UCX configuration, adjust according to your environment
exportUCX_TLS=all# or specify specific transports like "rc,ud,sm,^cuda_ipc" ..etc
exportUCX_NET_DEVICES=all# or specify network devices like "mlx5_0:1,mlx5_1:1"
```

Tip

When using UCX as the transport backend, NCCL environment variables (like `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`) are not applicable to NixlConnector, so configure UCX-specific environment variables instead of NCCL variables.

#### Selecting a NIXL transport backend (plugin)[¶](#selecting-a-nixl-transport-backend-plugin "Permanent link")

NixlConnector can use different NIXL transport backends (plugins). By default, NixlConnector uses UCX as the transport backend.

To select a different backend, set `kv_connector_extra_config.backends` in `--kv-transfer-config`.

### Example: using LIBFABRIC backend[¶](#example-using-libfabric-backend "Permanent link")

```
vllmserve<MODEL>\
--kv-transfer-config'{
    "kv_connector":"NixlConnector",
    "kv_role":"kv_both",
    "kv_connector_extra_config":{"backends":["LIBFABRIC"]}
  }'
```

You can also pass JSON keys individually using dotted arguments, and you can append list elements using `+`:

```
vllmserve<MODEL>\
--kv-transfer-config.kv_connectorNixlConnector\
--kv-transfer-config.kv_rolekv_both\
--kv-transfer-config.kv_connector_extra_config.backends+LIBFABRIC
```

Note

Backend availability depends on how NIXL was built and what plugins are present in your environment. Refer to the [NIXL repository](https://github.com/ai-dynamo/nixl) for available backends and build instructions.

## Basic Usage (on the same host)[¶](#basic-usage-on-the-same-host "Permanent link")

### Producer (Prefiller) Configuration[¶](#producer-prefiller-configuration "Permanent link")

Start a prefiller instance that produces KV caches

```
# 1st GPU as prefiller
CUDA_VISIBLE_DEVICES=0\
UCX_NET_DEVICES=all\
VLLM_NIXL_SIDE_CHANNEL_PORT=5600\
vllmserveQwen/Qwen3-0.6B\
--port8100\
--enforce-eager\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_load_failure_policy":"fail"}'
```

### Consumer (Decoder) Configuration[¶](#consumer-decoder-configuration "Permanent link")

Start a decoder instance that consumes KV caches:

```
# 2nd GPU as decoder
CUDA_VISIBLE_DEVICES=1\
UCX_NET_DEVICES=all\
VLLM_NIXL_SIDE_CHANNEL_PORT=5601\
vllmserveQwen/Qwen3-0.6B\
--port8200\
--enforce-eager\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_load_failure_policy":"fail"}'
```

### Proxy Server[¶](#proxy-server "Permanent link")

Use a proxy server to route requests between prefiller and decoder:

```
pythontests/v1/kv_connector/nixl_integration/toy_proxy_server.py\
--port8192\
--prefiller-hostslocalhost\
--prefiller-ports8100\
--decoder-hostslocalhost\
--decoder-ports8200
```

## Environment Variables[¶](#environment-variables "Permanent link")

- `VLLM_NIXL_SIDE_CHANNEL_PORT`: Port for NIXL handshake communication
  
  - Default: 5600
  - **Required for both prefiller and decoder instances**
  - Each vLLM worker needs a unique port on its host; using the same port number across different hosts is fine
  - For TP/DP deployments, each worker's port on a node is computed as: base\_port + dp\_rank (e.g., with `--data-parallel-size=2` and base\_port=5600, dp\_rank 0..1 use port 5600, 5601 on that node).
  - Used for the initial NIXL handshake between the prefiller and the decoder
- `VLLM_NIXL_SIDE_CHANNEL_HOST`: Host for side channel communication
  
  - Default: "localhost"
  - Set when prefiller and decoder are on different machines
  - Connection info is passed via KVTransferParams from prefiller to decoder for handshake
- `VLLM_NIXL_ABORT_REQUEST_TIMEOUT`: Timeout (in seconds) for automatically releasing the prefiller’s KV cache for a particular request. (Optional)
  
  - Default: 480
  - If a request is aborted and the decoder has not yet read the KV-cache blocks through the nixl channel, the prefill instance will release its KV-cache blocks after this timeout to avoid holding them indefinitely.

## Multi-Instance Setup[¶](#multi-instance-setup "Permanent link")

### Multiple Prefiller Instances on Different Machines[¶](#multiple-prefiller-instances-on-different-machines "Permanent link")

```
# Prefiller 1 on Machine A (example IP: ${IP1})
VLLM_NIXL_SIDE_CHANNEL_HOST=${IP1}\
VLLM_NIXL_SIDE_CHANNEL_PORT=5600\
UCX_NET_DEVICES=all\
vllmserveQwen/Qwen3-0.6B--port8000\
--tensor-parallel-size8\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_producer","kv_load_failure_policy":"fail"}'

# Prefiller 2 on Machine B (example IP: ${IP2})
VLLM_NIXL_SIDE_CHANNEL_HOST=${IP2}\
VLLM_NIXL_SIDE_CHANNEL_PORT=5600\
UCX_NET_DEVICES=all\
vllmserveQwen/Qwen3-0.6B--port8000\
--tensor-parallel-size8\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_producer","kv_load_failure_policy":"fail"}'
```

### Multiple Decoder Instances on Different Machines[¶](#multiple-decoder-instances-on-different-machines "Permanent link")

```
# Decoder 1 on Machine C (example IP: ${IP3})
VLLM_NIXL_SIDE_CHANNEL_HOST=${IP3}\
VLLM_NIXL_SIDE_CHANNEL_PORT=5600\
UCX_NET_DEVICES=all\
vllmserveQwen/Qwen3-0.6B--port8000\
--tensor-parallel-size8\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_consumer","kv_load_failure_policy":"fail"}'

# Decoder 2 on Machine D (example IP: ${IP4})
VLLM_NIXL_SIDE_CHANNEL_HOST=${IP4}\
VLLM_NIXL_SIDE_CHANNEL_PORT=5600\
UCX_NET_DEVICES=all\
vllmserveQwen/Qwen3-0.6B--port8000\
--tensor-parallel-size8\
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_consumer","kv_load_failure_policy":"fail"}'
```

### Proxy for Multiple Instances[¶](#proxy-for-multiple-instances "Permanent link")

```
pythontests/v1/kv_connector/nixl_integration/toy_proxy_server.py\
--port8192\
--prefiller-hosts${IP1}${IP2}\
--prefiller-ports80008000\
--decoder-hosts${IP3}${IP4}\
--decoder-ports80008000
```

For multi-host DP deployment, only need to provide the host/port of the head instances.

### KV Role Options[¶](#kv-role-options "Permanent link")

- **kv\_producer**: For prefiller instances that generate KV caches
- **kv\_consumer**: For decoder instances that consume KV caches from prefiller
- **kv\_both**: Enables symmetric functionality where the connector can act as both producer and consumer. This provides flexibility for experimental setups and scenarios where the role distinction is not predetermined.

Tip

NixlConnector currently does not distinguish `kv_role`; the actual prefiller/decoder roles are determined by the upper-level proxy (e.g., `toy_proxy_server.py` using `--prefiller-hosts` and `--decoder-hosts`). Therefore, `kv_role` in `--kv-transfer-config` is effectively a placeholder and does not affect NixlConnector's behavior.

### KV Load Failure Policy[¶](#kv-load-failure-policy "Permanent link")

The `kv_load_failure_policy` setting controls how the system handles failures when the decoder instance loads KV cache blocks from the prefiller instance:

- **fail** (default): Immediately fail the request with an error when KV load fails. This prevents performance degradation by avoiding recomputation of prefill work on the decode instance.
- **recompute**: Recompute failed blocks locally on the decode instance. This may cause performance *jitter* on decode instances as the scheduled prefill will delay and interfere with other decodes. Furthermore, decode instances are typically configured with low-latency optimizations.

Warning

Using `kv_load_failure_policy="recompute"` can lead to performance degradation in production deployments. When KV loads fail, the decode instance will execute prefill work with decode-optimized configurations, which is inefficient and defeats the purpose of disaggregated prefilling. This also increases tail latency for other ongoing decode requests.

## Experimental Feature[¶](#experimental-feature "Permanent link")

### Heterogeneous KV Layout support[¶](#heterogeneous-kv-layout-support "Permanent link")

Support use case: Prefill with 'HND' and decode with 'NHD' with experimental configuration

```
--kv-transfer-config'{..., "enable_permute_local_kv":"True"}'
```

### Cross layers blocks[¶](#cross-layers-blocks "Permanent link")

By default, this feature is disabled. On attention backends that support this feature, each logical block is contiguous in physical memory. This reduces the number of buffers that need to be transferred. To enable this feature:

```
--kv-transfer-config'{..., "kv_connector_extra_config": {"enable_cross_layers_blocks": "True"}}'
```

## Example Scripts/Code[¶](#example-scriptscode "Permanent link")

Refer to these example scripts in the vLLM repository:

- [run\_accuracy\_test.sh](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh)
- [toy\_proxy\_server.py](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/toy_proxy_server.py)
- [test\_accuracy.py](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/test_accuracy.py)