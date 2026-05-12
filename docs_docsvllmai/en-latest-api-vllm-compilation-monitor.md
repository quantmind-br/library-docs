---
title: monitor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/monitor/
source: sitemap
fetched_at: 2026-05-07T21:16:17.907084449-03:00
rendered_js: false
word_count: 30
summary: This document defines a context manager designed to measure the duration of a profiling run and verify that no backend compilation occurs during that process.
tags:
    - profiling
    - context-manager
    - vllm
    - compilation-monitoring
    - performance-tracing
category: api
---

Context manager that times the initial profiling run.

Asserts that no backend compilation occurs during the profiling run (all compilation should have completed before this point).

Source code in `vllm/compilation/monitor.py`

```
@contextlib.contextmanager
defmonitor_profiling_run() -> Generator[None, None, None]:
"""Context manager that times the initial profiling run.

    Asserts that no backend compilation occurs during the profiling run
    (all compilation should have completed before this point).
    """
    fromvllm.compilation.counterimport compilation_counter

    backend_compilations_before = compilation_counter.num_backend_compilations
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    assert (
        compilation_counter.num_backend_compilations == backend_compilations_before
    ), (
        "backend compilation occurred during the initial profiling run; "
        "all compilation should be complete before the profiling run starts."
    )
    logger.info_once(
        "Initial profiling/warmup run took %.2f s",
        elapsed,
    )
```