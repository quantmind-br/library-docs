---
title: Delete Batch Inference Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-batch-inference-job
source: sitemap
fetched_at: 2026-04-27T20:14:48.491629367-03:00
rendered_js: false
word_count: 74
summary: Delete a specific batch inference job associated with an account using the Fireworks API.
tags:
    - api-reference
    - batch-inference
    - delete-job
    - fireworks-ai
    - rest-api
    - curl
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Batch Inference Job

Deletes a specific batch inference job for an account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| batch_inference_job_id | string | Yes | The Batch Inference Job Id. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #batch-inference
