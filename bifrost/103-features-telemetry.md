---
title: Telemetry
url: https://docs.getbifrost.ai/features/telemetry.md
source: llms
fetched_at: 2026-01-21T19:43:50.166894512-03:00
rendered_js: false
word_count: 817
summary: This document details the Prometheus-based telemetry system for Bifrost Gateway, covering HTTP transport metrics, AI provider performance tracking, and cost monitoring.
tags:
    - prometheus
    - monitoring
    - telemetry
    - ai-gateway
    - metrics
    - observability
    - cost-tracking
category: reference
---

# Telemetry

> Comprehensive Prometheus-based monitoring for Bifrost Gateway with custom metrics and labels.

## Overview

Bifrost provides built-in telemetry and monitoring capabilities through Prometheus metrics collection. The telemetry system tracks both HTTP-level performance metrics and upstream provider interactions, giving you complete visibility into your AI gateway's performance and usage patterns.

**Key Features:**

* **Prometheus Integration** - Native metrics collection at `/metrics` endpoint
* **Comprehensive Tracking** - Success/error rates, token usage, costs, and cache performance
* **Custom Labels** - Configurable dimensions for detailed analysis
* **Dynamic Headers** - Runtime label injection via `x-bf-prom-*` headers
* **Cost Monitoring** - Real-time tracking of AI provider costs in USD
* **Cache Analytics** - Direct and semantic cache hit tracking
* **Async Collection** - Zero-latency impact on request processing
* **Multi-Level Tracking** - HTTP transport + upstream provider metrics

The telemetry plugin operates asynchronously to ensure metrics collection doesn't impact request latency or connection performance.

***

## Default Metrics

### HTTP Transport Metrics

These metrics track all incoming HTTP requests to Bifrost:

| Metric                          | Type      | Description                     |
| ------------------------------- | --------- | ------------------------------- |
| `http_requests_total`           | Counter   | Total number of HTTP requests   |
| `http_request_duration_seconds` | Histogram | Duration of HTTP requests       |
| `http_request_size_bytes`       | Histogram | Size of incoming HTTP requests  |
| `http_response_size_bytes`      | Histogram | Size of outgoing HTTP responses |

Labels:

* `path`: HTTP endpoint path
* `method`: HTTP verb (e.g., `GET`, `POST`, `PUT`, `DELETE`)
* `status`: HTTP status code
* custom labels: Custom labels configured in the Bifrost configuration

### Upstream Provider Metrics

These metrics track requests forwarded to AI providers:

| Metric                             | Type      | Description                                          | Labels                                   |
| ---------------------------------- | --------- | ---------------------------------------------------- | ---------------------------------------- |
| `bifrost_upstream_requests_total`  | Counter   | Total requests forwarded to upstream providers       | Base Labels, custom labels               |
| `bifrost_success_requests_total`   | Counter   | Total successful requests to upstream providers      | Base Labels, custom labels               |
| `bifrost_error_requests_total`     | Counter   | Total failed requests to upstream providers          | Base Labels, `reason`, custom labels     |
| `bifrost_upstream_latency_seconds` | Histogram | Latency of upstream provider requests                | Base Labels, `is_success`, custom labels |
| `bifrost_input_tokens_total`       | Counter   | Total input tokens sent to upstream providers        | Base Labels, custom labels               |
| `bifrost_output_tokens_total`      | Counter   | Total output tokens received from upstream providers | Base Labels, custom labels               |
| `bifrost_cache_hits_total`         | Counter   | Total cache hits by type (direct/semantic)           | Base Labels, `cache_type`, custom labels |
| `bifrost_cost_total`               | Counter   | Total cost in USD for upstream provider requests     | Base Labels, custom labels               |

Base Labels:

* `provider`: AI provider name (e.g., `openai`, `anthropic`, `azure`)
* `model`: Model name (e.g., `gpt-4o-mini`, `claude-3-sonnet`)
* `method`: Request type (`chat`, `text`, `embedding`, `speech`, `transcription`)
* `virtual_key_id`: Virtual key ID
* `virtual_key_name`: Virtual key name
* `selected_key_id`: Selected key ID
* `selected_key_name`: Selected key name
* `number_of_retries`: Number of retries
* `fallback_index`: Fallback index (0 for first attempt, 1 for second attempt, etc.)
* custom labels: Custom labels configured in the Bifrost configuration

### Streaming Metrics

These metrics capture latency characteristics specific to streaming responses:

| Metric                                       | Type      | Description                                     | Labels      |
| -------------------------------------------- | --------- | ----------------------------------------------- | ----------- |
| `bifrost_stream_first_token_latency_seconds` | Histogram | Time from request start to first streamed token | Base Labels |
| `bifrost_stream_inter_token_latency_seconds` | Histogram | Latency between subsequent streamed tokens      | Base Labels |

***

## Monitoring Examples

### Success Rate Monitoring

Track the success rate of requests to different providers:

```promql  theme={null}
# Success rate by provider
rate(bifrost_success_requests_total[5m]) / 
rate(bifrost_upstream_requests_total[5m]) * 100
```

### Token Usage Analysis

Monitor token consumption across different models:

```promql  theme={null}
# Input tokens per minute by model
increase(bifrost_input_tokens_total[1m])

# Output tokens per minute by model  
increase(bifrost_output_tokens_total[1m])

# Token efficiency (output/input ratio)
rate(bifrost_output_tokens_total[5m]) / 
rate(bifrost_input_tokens_total[5m])
```

### Cost Tracking

Monitor spending across providers and models:

```promql  theme={null}
# Cost per second by provider
sum by (provider) (rate(bifrost_cost_total[1m]))

# Daily cost estimate
sum by (provider) (increase(bifrost_cost_total[1d]))

# Cost per request by provider and model
sum by (provider, model) (rate(bifrost_cost_total[5m])) / 
sum by (provider, model) (rate(bifrost_upstream_requests_total[5m]))
```

### Cache Performance

Track cache effectiveness:

```promql  theme={null}
# Cache hit rate by type
rate(bifrost_cache_hits_total[5m]) / 
rate(bifrost_upstream_requests_total[5m]) * 100

# Direct vs semantic cache hits
sum by (cache_type) (rate(bifrost_cache_hits_total[5m]))
```

### Error Rate Analysis

Monitor error patterns:

```promql  theme={null}
# Error rate by provider
rate(bifrost_error_requests_total[5m]) / 
rate(bifrost_upstream_requests_total[5m]) * 100

# Errors by model
sum by (model) (rate(bifrost_error_requests_total[5m]))
```

***

## Configuration

Configure custom Prometheus labels to add dimensions for filtering and analysis:

<Tabs group="config-method">
  <Tab title="Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=716407bf4db1dc6b3520c491755ea999" alt="Prometheus Labels" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-prometheus-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=a30499807f09379ca3b8565bd9ce4b96 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=4904a25fe4fd9d8c37dca6aa26ad1cdf 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=b0b9ae596ff11266edbc0d0d631704e1 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=9a7caae1ecf621f5e8e3beb22f7166c7 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=536a4d15903d0e233f488fec91d05ba5 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-prometheus-labels.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=dbc964dbd67aab014c65d59a771c42de 2500w" />

    1. **Navigate to Configuration**
       * Open Bifrost UI at `http://localhost:8080`
       * Go to **Config** tab

    2. **Prometheus Labels**
       ```
       Custom Labels: team, environment, organization, project
       ```
  </Tab>

  <Tab title="API">
    ```bash  theme={null}
    # Update prometheus labels via API
    curl -X PATCH http://localhost:8080/config \
      -H "Content-Type: application/json" \
      -d '{
        "client": {
          "prometheus_labels": ["team", "environment", "organization", "project"]
        }
      }'
    ```
  </Tab>

  <Tab title="config.json">
    ```json  theme={null}
    {
      "client": {
        "prometheus_labels": ["team", "environment", "organization", "project"],
        "drop_excess_requests": false,
        "initial_pool_size": 300
      }
    }
    ```
  </Tab>
</Tabs>

### Dynamic Label Injection

Add custom label values at runtime using `x-bf-prom-*` headers:

```bash  theme={null}
# Add custom labels to specific requests
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-bf-prom-team: engineering" \
  -H "x-bf-prom-environment: production" \
  -H "x-bf-prom-organization: my-org" \
  -H "x-bf-prom-project: my-project" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

**Header Format:**

* Prefix: `x-bf-prom-`
* Label name: Any string after the prefix
* Value: String value for the label

***

## Infrastructure Setup

### Development & Testing

For local development and testing, use the provided Docker Compose setup:

```bash  theme={null}
# Navigate to telemetry plugin directory
cd plugins/telemetry

# Start Prometheus and Grafana
docker-compose up -d

# Access endpoints
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3000 (admin/admin)
# Bifrost metrics: http://localhost:8080/metrics
```

<Warning>
  **Development Only**: The provided Docker Compose setup is for testing purposes only. Do not use in production without proper security, scaling, and persistence configuration.
</Warning>

You can use the Prometheus scraping endpoint to create your own Grafana dashboards. Given below are few examples created using the Docker Compose setup.

<img src="https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=d955f6ccf0bbf7e3edcb173abbff5051" alt="Grafana Dashboard" data-og-width="1942" width="1942" data-og-height="2040" height="2040" data-path="media/ui-grafana-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=280&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=e403c848058a69917048b62412f01985 280w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=560&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=a468740b8e3cbd9f09ec442c45636168 560w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=840&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=5e686051bf08029d5e51517b9d83dc4b 840w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=1100&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=bde9c8bf97a2e6b09ed84114c3d66815 1100w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=1650&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=aa5ee091e35ae657cb4181b6d24380eb 1650w, https://mintcdn.com/bifrost/pg2nvSfno0tQR_mg/media/ui-grafana-dashboard.png?w=2500&fit=max&auto=format&n=pg2nvSfno0tQR_mg&q=85&s=af5c52153506858c275bd22e6da91912 2500w" />

### Production Deployment

For production environments:

1. **Deploy Prometheus** with proper persistence, retention, and security
2. **Configure scraping** to target your Bifrost instances at `/metrics`
3. **Set up Grafana** with authentication and dashboards
4. **Configure alerts** based on your SLA requirements

**Prometheus Scrape Configuration:**

```yaml  theme={null}
scrape_configs:
  - job_name: "bifrost-gateway"
    static_configs:
      - targets: ["bifrost-instance-1:8080", "bifrost-instance-2:8080"]
    scrape_interval: 30s
    metrics_path: /metrics
```

### Production Alerting Examples

Configure alerts for critical scenarios using the new metrics:

**High Error Rate Alert:**

```yaml  theme={null}
- alert: BifrostHighErrorRate
  expr: sum by (provider) (rate(bifrost_error_requests_total[5m])) / sum by (provider) (rate(bifrost_upstream_requests_total[5m])) > 0.05
  for: 2m
  labels:
    severity: warning
  annotations:
    summary: "High error rate detected for provider {{ $labels.provider }} ({{ $value | humanizePercentage }})"
```

**High Cost Alert:**

```yaml  theme={null}
- alert: BifrostHighCosts
  expr: sum by (provider) (increase(bifrost_cost_total[1d])) > 100  # $100/day threshold
  for: 10m
  labels:
    severity: warning
  annotations:
    summary: "Daily cost for provider {{ $labels.provider }} exceeds $100 ({{ $value | printf \"%.2f\" }})"
```

**Cache Performance Alert:**

```yaml  theme={null}
- alert: BifrostLowCacheHitRate
  expr: sum by (provider) (rate(bifrost_cache_hits_total[15m])) / sum by (provider) (rate(bifrost_upstream_requests_total[15m])) < 0.1
  for: 5m
  labels:
    severity: info
  annotations:
    summary: "Cache hit rate for provider {{ $labels.provider }} below 10% ({{ $value | humanizePercentage }})"
```

***

## Next Steps

* **[Prometheus Documentation](https://prometheus.io/docs/)** - Official Prometheus guides
* **[Grafana Setup](https://grafana.com/docs/)** - Dashboard creation and management
* **[Tracing](./observability/default)** - Request/response logging for detailed analysis


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt