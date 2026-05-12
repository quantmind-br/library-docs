---
title: Delete Supervised Fine-tuning Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-supervised-fine-tuning-job
source: sitemap
fetched_at: 2026-04-27T20:14:37.651542435-03:00
rendered_js: false
word_count: 85
summary: This document provides API reference details for managing supervised fine-tuning jobs within the Fireworks platform. It specifically details the DELETE endpoint used to remove an existing fine-tuning job.
tags:
    - api-reference
    - fireworks-ai
    - supervised-fine-tuning
    - delete-job
    - rest-api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Supervised Fine-tuning Job

Permanently delete a supervised fine-tuning job from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/supervisedFineTuningJobs/{supervised_fine_tuning_job_id}
```

## Authorizations

| Type | Location | Description |
|------|----------|-------------|
| Bearer | `Authorization` header | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `supervised_fine_tuning_job_id` | string | The Supervised Fine-tuning Job ID |

## Response

Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/supervisedFineTuningJobs/{supervised_fine_tuning_job_id} \
  --header 'Authorization: Bearer <token>'
```

## Related Operations

- [[263-api-reference-create-supervised-fine-tuning-job|Create Job]]
- [[222-api-reference-list-supervised-fine-tuning-jobs|List Jobs]]
- [[248-api-reference-get-supervised-fine-tuning-job|Get Job]]
- [[301-api-reference-resume-supervised-fine-tuning-job|Resume Job]]

#supervised-fine-tuning #rest-api
