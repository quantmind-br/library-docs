---
title: log_time - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/log_time/
source: sitemap
fetched_at: 2026-05-07T21:22:25.816633202-03:00
rendered_js: false
word_count: 27
summary: The logtime decorator provides a mechanism for measuring and logging the execution time of Python functions within the vLLM library.
tags:
    - python-decorator
    - execution-time
    - logging-utility
    - performance-monitoring
    - vllm-framework
category: reference
---

## vllm.logging\_utils.log\_time [¶](#vllm.logging_utils.log_time "Permanent link")

Provides a timeslice logging decorator

## logtime [¶](#vllm.logging_utils.log_time.logtime "Permanent link")

```
logtime(logger, msg=None)
```

Logs the execution time of the decorated function. Always place it beneath other decorators.

Source code in `vllm/logging_utils/log_time.py`

```
deflogtime(logger, msg=None):
"""
    Logs the execution time of the decorated function.
    Always place it beneath other decorators.
    """

    def_inner(func):
        @functools.wraps(func)
        def_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start

            prefix = (
                f"Function '{func.__module__}.{func.__qualname__}'"
                if msg is None
                else msg
            )
            logger.debug("%s: Elapsed time %.7f secs", prefix, elapsed)
            return result

        return _wrapper

    return _inner
```