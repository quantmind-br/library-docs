---
title: eplb_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/eplb_utils/
source: sitemap
fetched_at: 2026-05-07T21:42:24.026151122-03:00
rendered_js: false
word_count: 13
summary: This document defines a Python decorator utility used to trigger an EPLB step automatically after the successful execution of model runner methods.
tags:
    - eplb
    - model-runner
    - python-decorator
    - task-automation
    - execution-hooks
category: api
---

Step EPLB after a model runner method completes successfully.

Source code in `vllm/v1/worker/gpu/eplb_utils.py`

```
defstep_eplb_after(*, is_dummy: bool = False) -> Callable:
"""Step EPLB after a model runner method completes successfully."""

    defdecorator(fn: Callable) -> Callable:
        @wraps(fn)
        defwrapper(self: Any, *args, **kwargs) -> Any:
            result = fn(self, *args, **kwargs)
            if kwargs.get("skip_eplb", False):
                return result

            is_profile = kwargs.get("is_profile", False) if is_dummy else False
            self.eplb.step(is_dummy=is_dummy, is_profile=is_profile)
            return result

        return wrapper

    return decorator
```