---
title: Cancel Reinforcement Fine-tuning Job - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/cancel-reinforcement-fine-tuning-job
source: sitemap
fetched_at: 2026-04-27T20:15:06.243369105-03:00
rendered_js: false
word_count: 74
summary: This document provides the details for canceling a specific reinforcement fine-tuning job using an API call. It outlines the HTTP method, endpoint structure, required headers, and request/response body formats.
tags:
    - api
    - reinforcement-fine-tuning
    - cancel
    - job
    - endpoint
    - fireworks-ai
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Cancel Reinforcement Fine-tuning Job

Cancel an in-progress reinforcement fine-tuning job.

## Endpoint

```
POST /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel
```

## Authorizations

| Type | Location | Description |
|------|----------|-------------|
| Bearer | `Authorization` header | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `reinforcement_fine_tuning_job_id` | string | The Reinforcement Fine-tuning Job ID |

## Body

`object` — Empty body `{}`.

## Response

Returns an `object`.

## Example

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{}'
```

#reinforcement-fine-tuning #rest-api
