---
title: op - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fla/ops/op/
source: sitemap
fetched_at: 2026-05-07T21:24:25.47876049-03:00
rendered_js: false
word_count: 27
summary: This document defines a placeholder fallback implementation for the gather operation in Triton to ensure compatibility when the native tl.gather function is unsupported.
tags:
    - triton
    - gather-operation
    - fallback-mechanism
    - compiler-compatibility
    - vllm-ops
category: api
---

Gather operation that works when tl.gather is not supported. This is a fallback implementation that returns None. Just to make triton compiler happy.

Source code in `vllm/model_executor/layers/fla/ops/op.py`

```
@triton.jit
defgather(src, index, axis, _builder=None):
"""
    Gather operation that works when tl.gather is not supported.
    This is a fallback implementation that returns None.
    Just to make triton compiler happy.
    """
    return None
```