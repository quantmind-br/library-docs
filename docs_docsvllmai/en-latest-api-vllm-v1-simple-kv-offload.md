---
title: simple_kv_offload - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/simple_kv_offload/
source: sitemap
fetched_at: 2026-05-07T21:41:38.333050923-03:00
rendered_js: false
word_count: 35
summary: This document lists and defines the core modules associated with the SimpleCPUOffloadConnector, including memory management, DMA transfers, and worker-scheduler coordination.
tags:
    - dma-copy
    - cuda-hip
    - memory-management
    - gpu-offload
    - system-architecture
category: reference
---

Modules:

Name Description `copy_backend`

DMA copy backend for GPU&lt;-&gt;CPU block transfers.

`cuda_mem_ops`

Low-level CUDA/HIP memory helpers: pinning and batch DMA transfers.

`manager`

Scheduler-side manager for SimpleCPUOffloadConnector.

`metadata`

Metadata for SimpleCPUOffloadConnector.

`worker`

Worker-side handler for SimpleCPUOffloadConnector.