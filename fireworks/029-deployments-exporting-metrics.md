---
title: Exporting Metrics - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/exporting-metrics
source: sitemap
fetched_at: 2026-04-27T20:18:59.127513026-03:00
rendered_js: false
word_count: 308
summary: This document details the metrics endpoint provided by Fireworks in Prometheus format, explaining how to access it via a specific URL and API key. It provides guidance on setting up integration with various observability tools like Prometheus, OpenTelemetry, Datadog, and Grafana, alongside listing all available rate, latency, token distribution, and resource utilization metrics.
tags:
    - prometheus-metrics
    - observability-integration
    - fireworks-api
    - metrics-endpoint
    - otel-collector
    - rate-limits
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks provides a metrics endpoint in Prometheus format for integration with Prometheus, OpenTelemetry (OTel) Collector, Datadog Agent, and Vector.

## Endpoint

```
https://api.fireworks.ai/v1/accounts/<account-id>/metrics
```

### Authentication

```json
{ "Authorization": "Bearer YOUR_API_KEY" }
```

### Scrape interval

Use a **1-minute scrape interval** — metrics are updated every 30s.

### Rate limits

- Maximum 6 requests/minute per account
- Exceeding this returns HTTP 429

## Integration options

### OpenTelemetry Collector

Configure a Prometheus receiver that scrapes the endpoint. See the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/) for exporter options.

### Direct Prometheus

```yaml
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'fireworks'
    metrics_path: 'v1/accounts/<account-id>/metrics'
    authorization:
      type: "Bearer"
      credentials: "YOUR_API_KEY"
    static_configs:
      - targets: ['api.fireworks.ai']
    scheme: https
```

See [Prometheus configuration docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Supported platforms

- Prometheus
- Datadog
- Grafana
- New Relic

## Available metrics

### Common labels

All metrics include:

- `base_model` — base model identifier (e.g., `accounts/fireworks/models/deepseek-v3`)
- `deployment` — full deployment path
- `deployment_account` — account name
- `deployment_id` — deployment identifier

### Rate metrics (per second)

| Metric | Description |
|---|---|
| `request_counter_total:sum_by_deployment` | Request rate per deployment |
| `requests_error_total:sum_by_deployment` | Error rate per deployment (by `http_code`) |
| `tokens_cached_prompt_total:sum_by_deployment` | Rate of cached prompt tokens |
| `tokens_prompt_total:sum_by_deployment` | Rate of total prompt tokens |

### Latency histogram metrics

| Metric | Description |
|---|---|
| `latency_generation_per_token_ms_bucket:sum_by_deployment` | Per-token generation time |
| `latency_generation_queue_ms_bucket:sum_by_deployment` | Time in generation queue |
| `latency_overall_ms_bucket:sum_by_deployment` | End-to-end request latency |
| `latency_to_first_token_ms_bucket:sum_by_deployment` | Time to first token |
| `latency_prefill_ms_bucket:sum_by_deployment` | Prefill processing time |
| `latency_prefill_queue_ms_bucket:sum_by_deployment` | Time in prefill queue |

### Token distribution metrics

| Metric | Description |
|---|---|
| `tokens_generated_per_request_bucket:sum_by_deployment` | Generated tokens per request |
| `tokens_prompt_per_request_bucket:sum_by_deployment` | Prompt tokens per request |

### Resource utilization metrics (gauges)

| Metric | Description |
|---|---|
| `generator_kv_blocks_fraction:avg_by_deployment` | KV cache blocks in use |
| `generator_kv_slots_fraction:avg_by_deployment` | KV cache slots in use |
| `generator_model_forward_time:avg_by_deployment` | Time in model forward pass |
| `requests_coordinator_concurrent_count:avg_by_deployment` | Average concurrent requests |
| `prefiller_prompt_cache_ttl:avg_by_deployment` | Prompt cache time-to-live |

#prometheus-metrics #observability-integration #metrics-endpoint
