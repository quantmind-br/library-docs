---
title: Beta Observability Judges
url: https://docs.mistral.ai/api/endpoint/beta/observability/judges
source: sitemap
fetched_at: 2026-04-26T04:01:45.203423744-03:00
rendered_js: false
word_count: 82
summary: API reference for Mistral Observability Judges endpoints, for creating, managing, and executing judges for evaluating chat completions.
tags:
    - api
    - observability
    - judges
    - evaluation
    - chat-completions
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Observability Judges

Create, update, and manage judges for evaluating chat completions.

---

## List Judges

`GET /v1/observability/judges`

Get judges with optional filtering.

### Code Example

```bash
curl https://api.mistral.ai/v1/observability/judges \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

### Response

```json
{"judges": {"count": 87}}
```

---

## Create Judge

`POST /v1/observability/judges`

| Param | Type | Description |
|-------|------|-------------|
| `name` | string | Judge name |
| `description` | string | Description |
| `instructions` | string | Judge instructions |
| `model_name` | string | Model to use |
| `output` | object | Output options with `options` array |
| `tools` | array | Tool list |

### Code Example

```bash
curl https://api.mistral.ai/v1/observability/judges \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"description": "ipsum eiusmod", "instructions": "consequat do", "model_name": "reprehenderit ut dolore", "name": "occaecat dolor sit", "output": {"options": [{"description": "nostrud", "value": "aute aliqua aute commodo"}]}, "tools": ["irure"]}'
```

---

## Get Judge

`GET /v1/observability/judges/{judge_id}`

---

## Update Judge

`PUT /v1/observability/judges/{judge_id}`

---

## Delete Judge

`DELETE /v1/observability/judges/{judge_id}`

---

## Run Live Judging

`POST /v1/observability/judges/{judge_id}/live-judging`

Run a saved judge on a conversation.

#judges #evaluation #chat-completions
