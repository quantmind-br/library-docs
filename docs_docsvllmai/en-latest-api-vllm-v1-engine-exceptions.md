---
title: exceptions - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/engine/exceptions/
source: sitemap
fetched_at: 2026-05-07T21:40:36.713314921-03:00
rendered_js: false
word_count: 12
summary: This document defines the EngineDeadError exception, which indicates an unrecoverable failure within the vLLM EngineCore.
tags:
    - exception-handling
    - engine-core
    - error-reporting
    - vllm-framework
category: reference
---

Bases: `Exception`

Raised when the EngineCore dies. Unrecoverable.

Source code in `vllm/v1/engine/exceptions.py`

```
classEngineDeadError(Exception):
"""Raised when the EngineCore dies. Unrecoverable."""

    def__init__(self, *args, suppress_context: bool = False, **kwargs):
        ENGINE_DEAD_MESSAGE = "EngineCore encountered an issue. See stack trace (above) for the root cause."  # noqa: E501

        super().__init__(ENGINE_DEAD_MESSAGE, *args, **kwargs)
        # Make stack trace clearer when using with LLMEngine by
        # silencing irrelevant ZMQError.
        self.__suppress_context__ = suppress_context
```