---
title: Beta Workflows Runs
url: https://docs.mistral.ai/api/endpoint/beta/workflows/runs
source: sitemap
fetched_at: 2026-04-26T04:01:56.925672169-03:00
rendered_js: false
word_count: 131
summary: API reference for retrieving and inspecting execution history and status details of individual workflow runs.
tags:
    - api-reference
    - workflow-management
    - execution-tracking
    - mistral-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Workflows Runs

List and inspect individual workflow runs.

---

## List Runs

`GET /v1/workflows/runs`

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `executions` | array | List of workflow executions |
| `next_page_token` | string\|null | Token for next page (null if last page) |

### Code Example

```bash
curl https://api.mistral.ai/v1/workflows/runs \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

### Response

```json
{
  "executions": [{
    "end_time": null,
    "execution_id": "ipsum eiusmod",
    "root_execution_id": "consequat do",
    "start_time": "2025-10-07T20:56:01.974Z",
    "status": "RUNNING",
    "workflow_name": "reprehenderit ut dolore"
  }]
}
```

---

## Get Run

`GET /v1/workflows/runs/{run_id}`

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `end_time` | string\|null | End time |
| `execution_id` | string | Execution ID |
| `parent_execution_id` | string\|null | Parent execution ID |
| `result` | object\|null | Execution result |
| `root_execution_id` | string | Root execution ID |
| `start_time` | string | Start time |
| `status` | string | `"RUNNING"\|"COMPLETED"\|"FAILED"\|"CANCELED"\|"TERMINATED"\|"CONTINUED_AS_NEW"\|"TIMED_OUT"\|"RETRYING_AFTER_ERROR"` |
| `total_duration_ms` | integer\|null | Total duration in milliseconds |

---

## Get Run History

`GET /v1/workflows/runs/{run_id}/history`

#workflow-management #execution-tracking
