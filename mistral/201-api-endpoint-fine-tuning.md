---
title: Fine Tuning
url: https://docs.mistral.ai/api/endpoint/fine-tuning
source: sitemap
fetched_at: 2026-04-26T04:02:18.01474593-03:00
rendered_js: false
word_count: 300
summary: API reference for managing fine-tuning jobs, including endpoints to create, list, retrieve, and cancel model fine-tuning processes.
tags:
    - fine-tuning
    - api-reference
    - mistral-ai
    - machine-learning
    - model-training
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Fine Tuning Endpoints

Fine-tuning job management API.

---

## List Jobs

`GET /v1/fine_tuning/jobs`

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

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `auto_start` | boolean | - | If `true`, returns metadata without spawning job |
| `classifier_targets` | array\|null | - | Classification targets |
| `integrations` | array\|null | - | Integrations (e.g., Wandb) |
| `invalid_sample_skip_percentage` | number | `0` | Invalid sample skip percentage |
| `job_type` | "completion"\|"classifier" | - | Job type |
| `model` | string | - | Base model name |
| `repositories` | array\|null | - | GitHub repositories |
| `suffix` | string | - | Suffix for model name (e.g., `ft:open-mistral-7b:my-great-model:xxx...`) |
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

Request fine-tuning job cancellation.

---

## Start Job

`POST /v1/fine_tuning/jobs/{job_id}/start`

Start a validated fine-tuning job.

#fine-tuning #model-training #machine-learning
