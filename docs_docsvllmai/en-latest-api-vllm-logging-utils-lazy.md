---
title: lazy - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/lazy/
source: sitemap
fetched_at: 2026-05-07T21:22:24.950145271-03:00
rendered_js: false
word_count: 13
summary: This module provides a utility class that defers the execution of a callable until the moment it is required for log string representation.
tags:
    - python-logging
    - lazy-evaluation
    - utility-class
    - performance-optimization
    - deferred-execution
category: reference
---

Wrap a zero-argument callable evaluated only during log formatting.

Source code in `vllm/logging_utils/lazy.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20

classlazy:
"""Wrap a zero-argument callable evaluated only during log formatting."""

    __slots__ = ("_factory",)

    def__init__(self, factory: Callable[[], Any]) -> None:
        self._factory = factory

    def__str__(self) -> str:
        return str(self._factory())

    def__repr__(self) -> str:
        return str(self)
```