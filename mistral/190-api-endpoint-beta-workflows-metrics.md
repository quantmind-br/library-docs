---
title: Beta Workflows Metrics
url: https://docs.mistral.ai/api/endpoint/beta/workflows/metrics
source: sitemap
fetched_at: 2026-04-26T04:01:55.66524765-03:00
rendered_js: false
word_count: 83
summary: API endpoint for retrieving performance and execution metrics for a specified workflow, including success rates, latency, and retry statistics.
tags:
    - api-endpoint
    - workflow-metrics
    - performance-monitoring
    - data-retrieval
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows Metrics

`GET /v1/workflows/{workflow_name}/metrics`

Get comprehensive metrics for a specific workflow.

### Query Parameters

| Param | Type | Description |
|-------|------|-------------|
| `workflow_name` | string | Name of workflow type |
| `start_time` | string (ISO 8601) | Optional start time filter |
| `end_time` | string (ISO 8601) | Optional end time filter |

### Response Metrics

| Metric | Type | Description |
|-------|------|-------------|
| `execution_count` | integer | Total executions |
| `success_count` | integer | Successful executions |
| `error_count` | integer | Failed/terminated executions |
| `average_latency_ms` | number | Average duration in milliseconds |
| `retry_rate` | number | Proportion of workflows with retries |
| `latency_over_time` | array | Time-series execution durations |

### Examples

```
GET /v1/workflows/MyWorkflow/metrics
GET /v1/workflows/MyWorkflow/metrics?start_time=2025-01-01T00:00&end_time=2025-12-31T23:59
```

#workflow-metrics #performance-monitoring
