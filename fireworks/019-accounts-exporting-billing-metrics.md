---
title: Exporting Billing Metrics - Fireworks AI Docs
url: https://docs.fireworks.ai/accounts/exporting-billing-metrics
source: sitemap
fetched_at: 2026-04-27T20:19:23.981768344-03:00
rendered_js: false
word_count: 185
summary: This document details the Fireworks CLI tool, providing instructions on how to export comprehensive billing metrics for various usage types such as serverless inference, deployments, and fine-tuning jobs into a detailed CSV file.
tags:
    - cli-tool
    - billing-metrics
    - usage-export
    - csv-format
    - firectl
    - cost-analysis
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!tip]
> Fireworks provides a CLI tool to export comprehensive billing metrics for all usage types — serverless inference, on-demand deployments, and fine-tuning jobs.

## Quick start

```bash
# Authenticate (once)
firectl login

# Export billing metrics to CSV
firectl billing export-metrics
```

## Examples

```bash
# Export all metrics
firectl billing export-metrics

# Export for specific date range
firectl billing export-metrics \
  --start-time "2025-01-01" \
  --end-time "2025-01-31" \
  --filename january_metrics.csv
```

## Output format

The CSV includes:

| Column | Description |
|--------|-------------|
| `email` | Account email |
| `start_time` | Request start timestamp |
| `end_time` | Request end timestamp |
| `usage_type` | Type (e.g., `TEXT_COMPLETION_INFERENCE_USAGE`) |
| `accelerator_type` | GPU/hardware type |
| `accelerator_seconds` | Compute time in seconds |
| `base_model_name` | Model used |
| `model_bucket` | Model category |
| `parameter_count` | Model size |
| `prompt_tokens` | Input tokens |
| `completion_tokens` | Output tokens |

### Sample row

```csv
email,start_time,end_time,usage_type,accelerator_type,accelerator_seconds,base_model_name,model_bucket,parameter_count,prompt_tokens,completion_tokens
user@example.com,2025-10-20 17:16:48 UTC,2025-10-20 17:16:48 UTC,TEXT_COMPLETION_INFERENCE_USAGE,,,accounts/fireworks/models/llama4-maverick-instruct-basic,Llama 4 Maverick Basic,401583781376,803,109
```

## Automation

```bash
# Daily export with dated filename
firectl billing export-metrics \
  --start-time "$(date -v-1d '+%Y-%m-%d')" \
  --end-time "$(date '+%Y-%m-%d')" \
  --filename "billing_$(date '+%Y%m%d').csv"
```

## Coverage

- **Serverless inference** — all serverless API usage
- **On-demand deployments** — deployment usage (see also [[029-deployments-exporting-metrics|Exporting deployment metrics]] for real-time Prometheus metrics)
- **Fine-tuning jobs** — fine-tuning compute usage
- **Other services** — all billable Fireworks services

## See also

- [[092-tools-sdks-firectl-firectl|firectl CLI overview]]
- [[029-deployments-exporting-metrics|Exporting deployment metrics]] — real-time Prometheus metrics
- [[077-guides-quotas-usage-rate-limits|Rate Limits & Quotas]] — understanding spend limits

#cli-tool #billing-metrics #cost-analysis
