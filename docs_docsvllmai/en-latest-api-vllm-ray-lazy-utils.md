---
title: lazy_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/ray/lazy_utils/
source: sitemap
fetched_at: 2026-05-07T21:34:50.07697442-03:00
rendered_js: false
word_count: 0
summary: This document provides a utility function to programmatically determine if the current execution context is running within a Ray actor.
tags:
    - ray
    - python
    - actor-model
    - runtime-context
    - distributed-computing
category: api
---

```
17
18
19
20
21
22
23
24
25
26
27
28
29
30

defis_in_ray_actor():
"""Check if we are in a Ray actor."""

    try:
        importray

        return (
            ray.is_initialized()
            and ray.get_runtime_context().get_actor_id() is not None
        )
    except ImportError:
        return False
    except AttributeError:
        return False
```