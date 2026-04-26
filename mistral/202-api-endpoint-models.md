---
title: Models
url: https://docs.mistral.ai/api/endpoint/models
source: sitemap
fetched_at: 2026-04-26T04:02:19.289435809-03:00
rendered_js: false
word_count: 182
summary: API reference for managing Mistral models, including endpoints to list, retrieve, update, and delete models.
tags:
    - model-management
    - api-reference
    - mistral-api
    - fine-tuning
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Models Endpoints

Model management API.

---

## List Models

`GET /v1/models`

List all models available to the user.

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `data` | array | Array of BaseModelCard or FTModelCard |
| `object` | string | `"list"` |

### Code Example

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.models.list();
  console.log(result);
}
run();
```

---

## Get Model

`GET /v1/models/{model_id}`

Retrieve model information by ID.

---

## Delete Model

`DELETE /v1/models/{model_id}`

Delete a fine-tuned model.

### Response Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `deleted` | boolean | `true` | Deletion status |
| `id` | string | - | Deleted model ID |
| `object` | string | `"model"` | Object type |

---

## Update Model

`PATCH /v1/fine_tuning/models/{model_id}`

Update model name or description.

### Response Types

- `CompletionFTModelOut`
- `ClassifierFTModelOut`

---

## Archive Model

`POST /v1/fine_tuning/models/{model_id}/archive`

Archive a fine-tuned model.

---

## Unarchive Model

`DELETE /v1/fine_tuning/models/{model_id}/archive`

Un-archive a fine-tuned model.

#model-management #fine-tuning #mistral-api
