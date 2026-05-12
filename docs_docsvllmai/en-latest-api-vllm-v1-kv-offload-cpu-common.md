---
title: common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/cpu/common/
source: sitemap
fetched_at: 2026-05-07T21:40:56.228855318-03:00
rendered_js: false
word_count: 15
summary: This document defines the CPULoadStoreSpec class, which specifies the interface for loading and storing KV blocks within CPU memory.
tags:
    - kv-cache
    - cpu-offload
    - data-storage
    - memory-management
    - python-class
category: reference
---

Bases: `BlockIDsLoadStoreSpec`

Spec for loading/storing a KV block to CPU memory.

Source code in `vllm/v1/kv_offload/cpu/common.py`

```
classCPULoadStoreSpec(BlockIDsLoadStoreSpec):
"""
    Spec for loading/storing a KV block to CPU memory.
    """

    @staticmethod
    defmedium() -> str:
        return "CPU"
```