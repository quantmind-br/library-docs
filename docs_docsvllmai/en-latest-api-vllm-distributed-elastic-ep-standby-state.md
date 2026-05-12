---
title: standby_state - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/elastic_ep/standby_state/
source: sitemap
fetched_at: 2026-05-07T21:17:53.060057373-03:00
rendered_js: false
word_count: 13
summary: This function retrieves all currently stored standby group configurations and resets the internal standby state to null values.
tags:
    - distributed-computing
    - vllm
    - elastic-execution-parallelism
    - state-management
    - python-api
category: api
---

Return all standby groups and clear the standby state.

Source code in `vllm/distributed/elastic_ep/standby_state.py`

```
defpop_standby_groups() -> dict:
"""Return all standby groups and clear the standby state."""
    global \
        _STANDBY_WORLD, \
        _STANDBY_WORLD_NODE_COUNT, \
        _STANDBY_DP, \
        _STANDBY_EP, \
        _STANDBY_EPLB

    result = dict(
        world=_STANDBY_WORLD,
        dp=_STANDBY_DP,
        ep=_STANDBY_EP,
        eplb=_STANDBY_EPLB,
        node_count=_STANDBY_WORLD_NODE_COUNT,
    )
    _STANDBY_WORLD = None
    _STANDBY_WORLD_NODE_COUNT = None
    _STANDBY_DP = None
    _STANDBY_EP = None
    _STANDBY_EPLB = None
    return result
```