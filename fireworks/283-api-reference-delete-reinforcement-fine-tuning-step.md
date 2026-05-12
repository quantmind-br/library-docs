---
title: Delete Reinforcement Fine-tuning Step - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-reinforcement-fine-tuning-step
source: sitemap
fetched_at: 2026-04-27T20:14:37.735377419-03:00
rendered_js: false
word_count: 109
summary: This document serves as a comprehensive overview of the Fireworks AI documentation, detailing resources for getting started and providing specific API reference endpoints, particularly for Reinforcement Fine-tuning operations.
tags:
    - api-reference
    - reinforcement-fine-tuning
    - sdk
    - cli
    - deployment
    - getting-started
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Reinforcement Fine-tuning Step

Permanently delete a reinforcement fine-tuning step (RLOR trainer job) from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id}
```

## Authorizations

| Type | Location | Required | Description |
|------|----------|----------|-------------|
| Bearer | `Authorization` header | Yes | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | The Account ID |
| `rlor_trainer_job_id` | string | The RLOR Trainer Job ID |

## Response

`200 application/json` — Successful response. Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id} \
  --header 'Authorization: Bearer <token>'
```

## Related Operations

- [[261-api-reference-create-reinforcement-fine-tuning-step|Create Step]]
- [[219-api-reference-list-reinforcement-fine-tuning-steps|List Steps]]
- [[101-api-reference-get-reinforcement-fine-tuning-step|Get Step]]
- [[300-api-reference-resume-reinforcement-fine-tuning-step|Resume Step]]
- [[291-api-reference-execute-reinforcement-fine-tuning-step|Execute Step]]

#reinforcement-fine-tuning #rest-api
