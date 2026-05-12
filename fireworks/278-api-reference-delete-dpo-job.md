---
title: Delete DPO Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-dpo-job
source: sitemap
fetched_at: 2026-04-27T20:14:48.503592096-03:00
rendered_js: false
word_count: 72
summary: Delete a specific DPO fine-tuning job associated with an account using the Fireworks API.
tags:
    - api-deletion
    - dpo-job
    - fireworks-ai
    - bearer-auth
    - http-request
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete DPO Job

Deletes a specific DPO fine-tuning job for an account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| account_id | string | Yes | The Account Id. |
| dpo_job_id | string | Yes | The DPO Job Id. |

#### Response

Returns an `object`.

#### Endpoint

```
DELETE /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}
```

#### Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/dpoJobs/{dpo_job_id} \
  --header 'Authorization: Bearer <token>'
```

#api-reference #fine-tuning
