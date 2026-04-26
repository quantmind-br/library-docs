---
title: Batch
url: https://docs.mistral.ai/api/endpoint/batch
source: sitemap
fetched_at: 2026-04-26T04:01:23.759822648-03:00
rendered_js: false
word_count: 273
summary: Technical documentation for Mistral API batch inference endpoints, covering job creation, retrieval, listing, and cancellation.
tags:
    - api-reference
    - batch-inference
    - mistral-api
    - rest-api
    - asynchronous-tasks
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Batch Jobs

Asynchronous batch inference API.

---

## List Batch Jobs

`GET /v1/batch/jobs`

Get batch jobs for your organization.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `object` | string | `"list"` | Response object type |

### Code Example

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.batch.jobs.list({});
  console.log(result);
}
run();
```

```python
from mistralai import Mistral
import os

with Mistral(api_key=os.getenv("MISTRAL_API_KEY","")) as mistral:
    res = mistral.batch.jobs.list(page=0, page_size=100, created_by_me=False)
    print(res)
```

```bash
curl https://api.mistral.ai/v1/batch/jobs \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

---

## Create Batch Job

`POST /v1/batch/jobs`

Create and queue a new batch job.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `endpoint` | string | - | Target endpoint: `/v1/chat/completions`, `/v1/embeddings`, `/v1/fim/completions`, `/v1/moderations`, `/v1/chat/moderations`, `/v1/ocr`, `/v1/classifications`, `/v1/chat/classifications`, `/v1/conversations`, `/v1/audio/transcriptions` |
| `input_files` | array\<string\>\|null | - | Input JSONL files containing request bodies |
| `metadata` | map | - | Job metadata |
| `model` | string | - | Model to use |
| `requests` | array\<BatchRequest\>\|null | - | Inline batch requests |
| `timeout_hours` | integer | `24` | Job timeout |

> [!info]
> Input files should be JSONL with `{"custom_id": "0", "body": {"max_tokens": 100, "messages": [...]}}` format.

### Response

| Field | Type | Description |
|-------|------|-------------|
| `completed_requests` | integer | Completed requests |
| `input_files` | array\<string\> | Input files |
| `object` | string | `"batch"` |
| `outputs` | array\<map\>\|null | Results |
| `status` | string | `"QUEUED"\|"RUNNING"\|"SUCCESS"\|"FAILED"\|"TIMEOUT_EXCEEDED"\|"CANCELLATION_REQUESTED"\|"CANCELLED"` |
| `succeeded_requests` | integer | Successful requests |

### Code Example

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.batch.jobs.create({
    inputFiles: ["fe3343a2-3b8d-404b-ba32-a78dede2614a"],
    endpoint: "/v1/classifications",
  });
  console.log(result);
}
run();
```

---

## Get Batch Job

`GET /v1/batch/jobs/{job_id}`

Get batch job details by UUID.

---

## Cancel Batch Job

`POST /v1/batch/jobs/{job_id}/cancel`

Request cancellation of a batch job.

#batch-inference #async-tasks #rest-api
