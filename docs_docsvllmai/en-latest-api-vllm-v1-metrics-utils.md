---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/metrics/utils/
source: sitemap
fetched_at: 2026-05-07T21:41:16.309142154-03:00
rendered_js: false
word_count: 13
summary: This document defines a utility function that generates individual labeled Prometheus metric instances for specific engine indices.
tags:
    - python
    - metrics
    - prometheus
    - vllm
    - engine-utils
category: api
---

Create a labeled metric child for each engine index.

Source code in `vllm/v1/metrics/utils.py`

```
defcreate_metric_per_engine(
    metric: PromMetric,
    per_engine_labelvalues: dict[int, list[object]],
) -> dict[int, PromMetric]:
"""Create a labeled metric child for each engine index."""
    return {
        idx: metric.labels(*labelvalues)
        for idx, labelvalues in per_engine_labelvalues.items()
    }
```