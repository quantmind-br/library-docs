---
title: ray_env_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/executor/ray_env_utils/
source: sitemap
fetched_at: 2026-05-07T21:40:47.076843265-03:00
rendered_js: false
word_count: 50
summary: This document describes a utility function that identifies and returns environment variables from the driver process to be propagated to Ray workers, while excluding specific reserved or user-defined variables.
tags:
    - environment-variables
    - ray-framework
    - distributed-computing
    - configuration-management
    - worker-nodes
category: reference
---

Return driver env vars to propagate to Ray workers.

Returns everything from `os.environ` except `worker_specific_vars` and user-configured exclusions (`RAY_NON_CARRY_OVER_ENV_VARS`).

Source code in `vllm/v1/executor/ray_env_utils.py`

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

defget_driver_env_vars(
    worker_specific_vars: set[str],
) -> dict[str, str]:
"""Return driver env vars to propagate to Ray workers.

    Returns everything from ``os.environ`` except ``worker_specific_vars``
    and user-configured exclusions (``RAY_NON_CARRY_OVER_ENV_VARS``).
    """
    exclude_vars = worker_specific_vars | RAY_NON_CARRY_OVER_ENV_VARS

    return {key: value for key, value in os.environ.items() if key not in exclude_vars}
```