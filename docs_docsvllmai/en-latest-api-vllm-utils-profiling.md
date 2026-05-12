---
title: profiling - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/profiling/
source: sitemap
fetched_at: 2026-05-07T21:38:54.75191404-03:00
rendered_js: false
word_count: 51
summary: This document provides a decorator utility for profiling Python methods using cProfile, noting its upcoming deprecation in favor of standard library usage.
tags:
    - python
    - profiling
    - cprofile
    - decorator
    - code-utility
    - deprecated
category: reference
---

Decorator to profile a Python method using cProfile.

Parameters:

Name Type Description Default `save_file` `str | None`

Path to save the profile result. If "1", None, or "", results will be printed to stdout.

`None` `enabled` `bool`

Set to false to turn this into a no-op

`True`

Source code in `vllm/utils/profiling.py`

```
@deprecated(
    "vllm.utils.profiling.cprofile() is deprecated and will be removed in "
    "v0.21. Use Python's cProfile module directly instead."
)
defcprofile(save_file: str | None = None, enabled: bool = True):
"""Decorator to profile a Python method using cProfile.

    Args:
        save_file: Path to save the profile result.
            If "1", None, or "", results will be printed to stdout.
        enabled: Set to false to turn this into a no-op
    """

    defdecorator(func: Callable):
        @wraps(func)
        defwrapper(*args: Any, **kwargs: Any):
            if not enabled:
                # If profiling is disabled, just call the function directly.
                return func(*args, **kwargs)

            with cprofile_context(save_file):
                return func(*args, **kwargs)

        return wrapper

    return decorator
```