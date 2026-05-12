---
title: async_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/async_utils/
source: sitemap
fetched_at: 2026-05-07T21:42:17.237807181-03:00
rendered_js: false
word_count: 16
summary: This document defines a lightweight Python context manager designed to switch CUDA streams while bypassing the overhead of standard current stream and device lookups.
tags:
    - cuda-streams
    - python-context-manager
    - gpu-optimization
    - vllm-library
    - performance-tuning
category: api
---

Lightweight version of torch.cuda.stream() context manager which avoids current\_stream and device lookups.

Source code in `vllm/v1/worker/gpu/async_utils.py`

```
@contextlib.contextmanager
defstream(to_stream: torch.cuda.Stream, from_stream: torch.cuda.Stream):
"""Lightweight version of torch.cuda.stream() context manager which
    avoids current_stream and device lookups.
    """
    try:
        torch.cuda.set_stream(to_stream)
        yield
    finally:
        torch.cuda.set_stream(from_stream)
```