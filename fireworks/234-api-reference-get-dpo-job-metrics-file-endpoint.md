---
title: Get DPO Job Metrics File Endpoint - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-dpo-job-metrics-file-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:16.245661193-03:00
rendered_js: false
word_count: 55
summary: Retrieves a short-lived signed URL for downloading the metrics file of a DPO fine-tuning job.
tags:
    - api-reference
    - fine-tuning
    - dpo
    - metrics
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint`

Retrieves a signed URL for downloading the metrics file of a DPO fine-tuning job.

**Authorizations:** Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

### Request

No body required.

### Response

| Field | Type | Description |
|---|---|---|
| `signedUrl` | string | Short-lived signed URL for the metrics file |

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint \
  --header 'Authorization: Bearer <token>'
```

```json
{
  "signedUrl": "<string>"
}
```