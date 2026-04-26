---
title: Beta Workflows Executions
url: https://docs.mistral.ai/api/endpoint/beta/workflows/executions
source: sitemap
fetched_at: 2026-04-26T04:01:53.404664407-03:00
rendered_js: false
word_count: 67
summary: API endpoints for managing and retrieving workflow execution life cycles and tracing.
tags:
    - workflow-management
    - rest-api
    - execution-history
    - trace-data
    - api-endpoints
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows Executions

Workflow execution lifecycle and tracing API.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/v1/workflows/executions/{execution_id}` | Get execution |
| `GET` | `/v1/workflows/executions/{execution_id}/history` | Get history |
| `POST` | `/v1/workflows/executions/{execution_id}/signals` | Signal execution |
| `POST` | `/v1/workflows/executions/{execution_id}/queries` | Query execution |
| `POST` | `/v1/workflows/executions/{execution_id}/terminate` | Terminate execution |
| `POST` | `/v1/workflows/executions/terminate` | Batch terminate |
| `POST` | `/v1/workflows/executions/{execution_id}/cancel` | Cancel execution |
| `POST` | `/v1/workflows/executions/cancel` | Batch cancel |
| `POST` | `/v1/workflows/executions/{execution_id}/reset` | Reset execution |
| `POST` | `/v1/workflows/executions/{execution_id}/updates` | Update execution |
| `GET` | `/v1/workflows/executions/{execution_id}/trace/otel` | Get OTEL trace |
| `GET` | `/v1/workflows/executions/{execution_id}/trace/summary` | Get trace summary |
| `GET` | `/v1/workflows/executions/{execution_id}/trace/events` | Get trace events |
| `GET` | `/v1/workflows/executions/{execution_id}/stream` | Stream execution |

#workflow-management #execution-history #trace-data
