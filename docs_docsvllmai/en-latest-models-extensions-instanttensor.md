---
title: Loading Model Weights with InstantTensor
url: https://docs.vllm.ai/en/latest/models/extensions/instanttensor/
source: sitemap
fetched_at: 2026-05-07T21:14:56.037237831-03:00
rendered_js: false
word_count: 91
summary: This document explains how to integrate the InstantTensor extension into vLLM to accelerate the loading of model weights on CUDA devices using optimized I/O techniques.
tags:
    - vllm
    - model-loading
    - cuda
    - performance-optimization
    - safetensors
    - instanttensor
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/instanttensor.md "Edit this page")

InstantTensor accelerates loading Safetensors weights on CUDA devices through distributed loading, pipelined prefetching, and direct I/O. InstantTensor also supports GDS (GPUDirect Storage) when available. For more details, see the [InstantTensor GitHub repository](https://github.com/scitix/InstantTensor).

## Installation[¶](#installation "Permanent link")

```
pipinstallinstanttensor
```

## Use InstantTensor in vLLM[¶](#use-instanttensor-in-vllm "Permanent link")

Add `--load-format instanttensor` as a command-line argument.

For example:

```
vllmserveQwen/Qwen2.5-0.5B--load-formatinstanttensor
```

## Benchmarks[¶](#benchmarks "Permanent link")

Model GPU Backend Load Time (s) Throughput (GB/s) Speedup Qwen3-30B-A3B 1\*H200 Safetensors 57.4 1.1 1x Qwen3-30B-A3B 1\*H200 InstantTensor 1.77 35 **32.4x** DeepSeek-R1 8\*H200 Safetensors 160 4.3 1x DeepSeek-R1 8\*H200 InstantTensor 15.3 45 **10.5x**

For the full benchmark results, see [https://github.com/scitix/InstantTensor/blob/main/docs/benchmark.md](https://github.com/scitix/InstantTensor/blob/main/docs/benchmark.md).