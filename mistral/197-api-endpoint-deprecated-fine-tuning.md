---
title: Deprecated Fine Tuning
url: https://docs.mistral.ai/api/endpoint/deprecated/fine-tuning
source: sitemap
fetched_at: 2026-04-26T04:02:09.806802711-03:00
rendered_js: false
word_count: 302
summary: API specification for managing fine-tuning jobs, including endpoints for creating, listing, retrieving, and canceling jobs.
tags:
    - fine-tuning
    - machine-learning
    - api-documentation
    - model-training
    - mistral-ai
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Deprecated Fine Tuning Endpoints

> [!warning]
> These endpoints are deprecated. Use the new Fine Tuning API.

Fine-tuning job management API.

---

## List Jobs

`GET /v1/fine_tuning/jobs`

Get fine-tuning jobs for your organization.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `object` | string | `"list"` | Response object type |

### Code Example

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.fineTuning.jobs.list({});
  console.log(result);
}
run();
```

---

## Create Job

`POST /v1/fine_tuning/jobs`

Create and queue a new fine-tuning job.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `auto_start` | boolean | - | If `true`, returns metadata without spawning job |
| `classifier_targets` | array\|null | - | Classification targets |
| `integrations` | array | - | Integrations (e.g., Wandb) |
| `invalid_sample_skip_percentage` | number | `0` | Percentage of invalid samples to skip |
| `job_type` | "completion"\|"classifier" | - | Job type |
| `model` | string | - | Base model name |
| `repositories` | array\|null | - | GitHub repositories |
| `suffix` | string | - | Suffix added to model name |
| `training_files` | array | - | Training file IDs |
| `validation_files` | array\|null | - | Validation file IDs |

### Response Types

- `CompletionJobOut`
- `ClassifierJobOut`
- `LegacyJobMetadataOut`

### Code Example

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.fineTuning.jobs.create({
    model: "Camaro",
    hyperparameters: { learningRate: 0.0001 },
  });
  console.log(result);
}
run();
```

---

## Get Job

`GET /v1/fine_tuning/jobs/{job_id}`

Get fine-tuned job details by UUID.

### Response Types

- `CompletionDetailedJobOut`
- `ClassifierDetailedJobOut`

---

## Cancel Job

`POST /v1/fine_tuning/jobs/{job_id}/cancel`

Request job cancellation.

---

## Start Job

`POST /v1/fine_tuning/jobs/{job_id}/start`

Start a validated job.

#fine-tuning #model-training #deprecated
