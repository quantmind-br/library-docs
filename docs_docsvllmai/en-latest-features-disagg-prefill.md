---
title: Disaggregated Prefilling (experimental) - vLLM
url: https://docs.vllm.ai/en/latest/features/disagg_prefill/
source: sitemap
fetched_at: 2026-05-07T21:14:09.208511151-03:00
rendered_js: false
word_count: 770
summary: This document explains the disaggregated prefilling feature in vLLM, which separates prefill and decoding phases into distinct instances to optimize latency control and performance tuning.
tags:
    - vllm
    - llm-inference
    - disaggregated-prefilling
    - kv-cache
    - distributed-computing
    - latency-optimization
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/disagg_prefill.md "Edit this page")

This page introduces you to the disaggregated prefilling feature in vLLM.

Note

This feature is experimental and subject to change.

## Why disaggregated prefilling?[¶](#why-disaggregated-prefilling "Permanent link")

Two main reasons:

- **Tuning time-to-first-token (TTFT) and inter-token-latency (ITL) separately**. Disaggregated prefilling put prefill and decode phase of LLM inference inside different vLLM instances. This gives you the flexibility to assign different parallel strategies (e.g. `tp` and `pp`) to tune TTFT without affecting ITL, or to tune ITL without affecting TTFT.
- **Controlling tail ITL**. Without disaggregated prefilling, vLLM may insert some prefill jobs during the decoding of one request. This results in higher tail latency. Disaggregated prefilling helps you solve this issue and control tail ITL. Chunked prefill with a proper chunk size also can achieve the same goal, but in practice it's hard to figure out the correct chunk size value. So disaggregated prefilling is a much more reliable way to control tail ITL.

Note

Disaggregated prefill DOES NOT improve throughput.

## Usage example[¶](#usage-example "Permanent link")

Please refer to [examples/disaggregated/disaggregated\_prefill.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/disaggregated_prefill.sh) for the example usage of disaggregated prefilling.

Now supports 6 types of connectors:

- **ExampleConnector**: refer to [examples/disaggregated/example\_connector/run.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/example_connector/run.sh) for the example usage of ExampleConnector disaggregated prefilling.
- **LMCacheConnectorV1**: refer to [examples/disaggregated/lmcache/disagg\_prefill\_lmcache\_v1/disagg\_example\_nixl.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/lmcache/disagg_prefill_lmcache_v1/disagg_example_nixl.sh) for the example usage of LMCacheConnectorV1 disaggregated prefilling which uses NIXL as the underlying KV transmission.
- **NixlConnector**: refer to [tests/v1/kv\_connector/nixl\_integration/run\_accuracy\_test.sh](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh) for the example usage of NixlConnector disaggregated prefilling which support fully async send/recv. For detailed usage guide, see [NixlConnector Usage Guide](https://docs.vllm.ai/en/latest/features/nixl_connector_usage/). For feature compatibility details, see [NixlConnector Compatibility Matrix](https://docs.vllm.ai/en/latest/features/nixl_connector_compatibility/).
- **P2pNcclConnector**: refer to [examples/disaggregated/p2p\_nccl\_xpyd/disagg\_example\_p2p\_nccl\_xpyd.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/p2p_nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh) for the example usage of P2pNcclConnector disaggregated prefilling.
- **MooncakeConnector**: refer to [examples/disaggregated/mooncake\_connector/run\_mooncake\_connector.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/mooncake_connector/run_mooncake_connector.sh) for the example usage of MooncakeConnector disaggregated prefilling. For detailed usage guide, see [MooncakeConnector Usage Guide](https://docs.vllm.ai/en/latest/features/mooncake_connector_usage/).
- **MultiConnector**: take advantage of the kv\_connector\_extra\_config: dict\[str, Any] already present in KVTransferConfig to stash all the connectors we want in an ordered list of kwargs.such as:

```
--kv-transfer-config'{"kv_connector":"MultiConnector","kv_role":"kv_both","kv_connector_extra_config":{"connectors":[{"kv_connector":"NixlConnector","kv_role":"kv_both"},{"kv_connector":"ExampleConnector","kv_role":"kv_both","kv_connector_extra_config":{"shared_storage_path":"local_storage"}}]}}'
```

For NixlConnector, you may also specify one or multiple NIXL\_Backend. Such as:

```
--kv-transfer-config'{"kv_connector":"NixlConnector","kv_role":"kv_both", "kv_buffer_device":"cuda", "kv_connector_extra_config":{"backends":["UCX", "GDS"]}}'
```

- **OffloadingConnector**: enable offloading of KV data to CPU memory, customizing the CPU block size (in tokens) and total CPU memory bytes to allocate:

```
--kv-transfer-config'{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"block_size": 64, "cpu_bytes_to_use": 1000000000}}'
```

- **FlexKVConnectorV1**: refer to [examples/disaggregated/flexkv\_connector/prefix\_caching\_flexkv.py](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated/flexkv_connector/prefix_caching_flexkv.py) for the example usage of FlexKVConnectorV1. FlexKV is a distributed KV Store and multi-level cache management system for ultra-large-scale LLM inference.

```
--kv-transfer-config'{"kv_connector":"FlexKVConnectorV1","kv_role":"kv_both"}'
```

## Benchmarks[¶](#benchmarks "Permanent link")

Please refer to [benchmarks/disagg\_benchmarks](https://github.com/vllm-project/vllm/tree/main/benchmarks/disagg_benchmarks) for disaggregated prefilling benchmarks.

## Development[¶](#development "Permanent link")

We implement disaggregated prefilling by running 2 vLLM instances. One for prefill (we call it prefill instance) and one for decode (we call it decode instance), and then use a connector to transfer the prefill KV caches and results from prefill instance to decode instance.

All disaggregated prefilling implementation is under `vllm/distributed/kv_transfer`.

Key abstractions for disaggregated prefilling:

- **Connector**: Connector allows **kv consumer** to retrieve the KV caches of a batch of request from **kv producer**.
- **LookupBuffer**: LookupBuffer provides two API: `insert` KV cache and `drop_select` KV cache. The semantics of `insert` and `drop_select` are similar to SQL, where `insert` inserts a KV cache into the buffer, and `drop_select` returns the KV cache that matches the given condition and drop it from the buffer.
- **Pipe**: A single-direction FIFO pipe for tensor transmission. It supports `send_tensor` and `recv_tensor`.

Note

`insert` is non-blocking operation but `drop_select` is blocking operation.

Here is a figure illustrating how the above 3 abstractions are organized:

[![Disaggregated prefilling abstractions](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/abstraction.jpg)](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/abstraction.jpg)

The workflow of disaggregated prefilling is as follows:

[![Disaggregated prefilling workflow](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/overview.jpg)](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/overview.jpg)

The `buffer` corresponds to `insert` API in LookupBuffer, and the `drop_select` corresponds to `drop_select` API in LookupBuffer.

Now every process in vLLM will have a corresponding connector. Specifically, we have:

- Scheduler connector: the connector that locates in the same process as the scheduler process. It schedules the KV cache transfer ops.
- Worker connectors: the connectors that locate in the worker processes. They execute KV cache transfer ops.

Here is a figure illustrating how the above 2 connectors are organized:

[![Disaggregated prefilling high level design](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/high_level_design.png)](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/high_level_design.png)

The figure below shows how the worker connector works with the attention module to achieve layer-by-layer KV cache store and load:

[![Disaggregated prefilling workflow](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/workflow.png)](https://docs.vllm.ai/en/latest/assets/features/disagg_prefill/workflow.png)

## Third-party contributions[¶](#third-party-contributions "Permanent link")

Disaggregated prefilling is highly related to infrastructure, so vLLM relies on third-party connectors for production-level disaggregated prefilling (and vLLM team will actively review and merge new PRs for third-party connectors).

We recommend three ways of implementations:

- **Fully-customized connector**: Implement your own `Connector`, and call third-party libraries to send and receive KV caches, and many many more (like editing vLLM's model input to perform customized prefilling, etc.). This approach gives you the most control, but at the risk of being incompatible with future vLLM versions.
- **Database-like connector**: Implement your own `LookupBuffer` and support the `insert` and `drop_select` APIs just like SQL.
- **Distributed P2P connector**: Implement your own `Pipe` and support the `send_tensor` and `recv_tensor` APIs, just like `torch.distributed`.