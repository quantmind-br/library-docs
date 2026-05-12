---
title: Delete Evaluation Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-evaluation-job
source: sitemap
fetched_at: 2026-04-27T20:14:45.751964583-03:00
rendered_js: false
word_count: 71
summary: Delete a specific evaluation job associated with an account using the Fireworks API.
tags:
    - api-delete
    - fireworks-ai
    - evaluation-jobs
    - bearer-authentication
    - http-request
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Evaluation Job

Deletes a specific evaluation job for an account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| evaluation_job_id | string | Yes | The Evaluation Job Id. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #evaluators
