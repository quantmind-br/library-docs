---
title: Execute one training step for keep-alive Reinforcement Fine-tuning Step - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/execute-reinforcement-fine-tuning-step
source: sitemap
fetched_at: 2026-04-27T20:14:35.607865627-03:00
rendered_js: false
word_count: 82
summary: This document details the endpoint and method required to execute a single training step for a keep-alive Reinforcement Learning Fine-tuning job via the Fireworks API.
tags:
    - api
    - reinforcement-learning
    - training-step
    - fireworks
    - rlor-trainer-jobs
    - execute
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Execute one training step for keep-alive Reinforcement Fine-tuning Step

Executes a single training step for a keep-alive RLoR (Reinforcement Learning with Reinforcement) trainer job.

## Endpoint

```
POST /v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id}:executeTrainStep
```

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `dataset` | string | Dataset to process for this iteration. |
| `outputModel` | string | Output model to materialize when training completes. |

## Response

Returns an `object`.

## Example

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id}:executeTrainStep \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "dataset": "<string>",
  "outputModel": "<string>"
}
'
```
