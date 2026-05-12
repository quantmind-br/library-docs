---
title: Get Evaluation Job Log Endpoint - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-evaluation-job-log-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:20.972162619-03:00
rendered_js: false
word_count: 125
summary: Retrieves a short-lived signed URL for streaming the execution logs of an evaluation job, including tracing IDs.
tags:
    - api-reference
    - evaluation
    - logs
    - observability
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}:getExecutionLogEndpoint`

Retrieves a short-lived signed URL for streaming the execution logs of an evaluation job.

**Authorizations:** Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

### Request

No body required.

### Response

| Field | Type | Description |
|---|---|---|
| `executionLogSignedUri` | string | Short-lived signed URL for the execution log file. Empty if the log file has not been created yet (e.g. job not started or still initializing). |
| `contentType` | string | Content type for the log file (e.g. `text/plain`). Only set when `executionLogSignedUri` is present. |
| `expireTime` | string (RFC3339) | Expiration time of the signed URL. Only set when `executionLogSignedUri` is present. |

> [!info]
> Response carries the stream log URL for use with VirtualizedLogViewer.

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}:getExecutionLogEndpoint \
  --header 'Authorization: Bearer <token>'
```

```json
{
  "executionLogSignedUri": "<string>",
  "contentType": "<string>",
  "expireTime": "2023-11-07T05:31:56Z"
}
```