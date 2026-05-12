---
title: Delete Reinforcement Fine-tuning Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-reinforcement-fine-tuning-job
source: sitemap
fetched_at: 2026-04-27T20:14:31.779217309-03:00
rendered_js: false
word_count: 70
summary: This document details the HTTP DELETE method used to remove a specific Reinforcement Fine-tuning Job from an account via the Fireworks AI API.
tags:
    - delete
    - reinforcement-fine-tuning
    - api-endpoint
    - job-deletion
    - fireworks-ai
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Reinforcement Fine-tuning Job

Permanently delete a reinforcement fine-tuning job from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}
```

## Authorizations

| Type | Location | Description |
|------|----------|-------------|
| Bearer | `Authorization` header | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `reinforcement_fine_tuning_job_id` | string | The Reinforcement Fine-tuning Job ID |

## Response

Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id} \
  --header 'Authorization: Bearer <token>'
```

#reinforcement-fine-tuning #rest-api
