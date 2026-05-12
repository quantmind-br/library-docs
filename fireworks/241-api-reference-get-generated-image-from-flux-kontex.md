---
title: Get generated image from FLUX.1 Kontext - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-generated-image-from-flux-kontex
source: sitemap
fetched_at: 2026-04-27T20:14:05.03113895-03:00
rendered_js: false
word_count: 169
summary: Retrieve FLUX.1 Kontext image generation results via POST request.
tags:
    - api-reference
    - http-post
    - inference
    - fireworks-ai
    - model-retrieval
    - workflow
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Generated Image from FLUX.1 Kontext

Retrieve results for FLUX.1 Kontext image generation requests.

## Endpoint

```
POST https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result
```

## Supported Models

- **FLUX.1 Kontext Pro**: use `flux-kontext-pro` as the model name
- **FLUX.1 Kontext Max**: use `flux-kontext-max` as the model name

## Request

```python
import requests

url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer $API_KEY",
}
data = {
    "id": "request_id"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
```

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Model to use: `flux-kontext-pro` or `flux-kontext-max`. |

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Request ID generated from the create/edit image request. |

## Response

```json
{
  "id": "<string>",
  "status": {},
  "result": "<any>",
  "progress": {},
  "details": {}
}
```

## Status Values

| Value | Description |
|-------|-------------|
| `Task not found` | Request ID not found. |
| `Pending` | Task is processing. |
| `Request Moderated` | Content is under moderation. |
| `Content Moderated` | Content was moderated. |
| `Ready` | Result is ready for retrieval. |
| `Error` | Task encountered an error. |

> [!tip]
> Poll this endpoint until status is `Ready` or an error occurs. #api-reference #inference #workflow