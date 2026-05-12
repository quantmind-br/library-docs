---
title: ray_wrappers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/metrics/ray_wrappers/
source: sitemap
fetched_at: 2026-05-07T21:41:13.41690969-03:00
rendered_js: false
word_count: 42
summary: This document describes a utility function used to sanitize metric names for compatibility between Ray and OpenTelemetry by replacing disallowed characters with underscores.
tags:
    - metric-sanitization
    - opentelemetry
    - ray-framework
    - data-normalization
    - instrumentation
category: api
---

For compatibility with Ray + OpenTelemetry, the metric name must be sanitized. In particular, this replaces disallowed character (e.g., ':') with '\_' in the metric name. Allowed characters: a-z, A-Z, 0-9, _

#### ruff: noqa: E501[¶](#vllm.v1.metrics.ray_wrappers.RayPrometheusMetric._get_sanitized_opentelemetry_name--ruff-noqa-e501 "Permanent link")

Ref: https://github.com/open-telemetry/opentelemetry-cpp/blob/main/sdk/src/metrics/instrument\_metadata\_validator.cc#L22-L23 Ref: https://github.com/ray-project/ray/blob/master/src/ray/stats/metric.cc#L107

Source code in `vllm/v1/metrics/ray_wrappers.py`

```
@staticmethod
def_get_sanitized_opentelemetry_name(name: str) -> str:
"""
    For compatibility with Ray + OpenTelemetry, the metric name must be
    sanitized. In particular, this replaces disallowed character (e.g., ':')
    with '_' in the metric name.
    Allowed characters: a-z, A-Z, 0-9, _

    # ruff: noqa: E501
    Ref: https://github.com/open-telemetry/opentelemetry-cpp/blob/main/sdk/src/metrics/instrument_metadata_validator.cc#L22-L23
    Ref: https://github.com/ray-project/ray/blob/master/src/ray/stats/metric.cc#L107
    """

    return re.sub(r"[^a-zA-Z0-9_]", "_", name)
```