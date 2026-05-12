---
title: List LoRAs - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-deployed-models
source: sitemap
fetched_at: 2026-04-27T20:14:02.089744355-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - model-deployment
    - api-response
    - deployed-models
    - json-structure
    - metadata
    - pagination
category: api
word_count: 62
---
# List LoRAs

`GET /deployed_models` — Returns a paginated list of deployed models and LoRAs.

## Response Schema

```json
{
  "deployedModels": [
    {
      "name": "<string>",
      "displayName": "<string>",
      "description": "<string>",
      "createTime": "2023-11-07T05:31:56Z",
      "model": "<string>",
      "deployment": "<string>",
      "default": true,
      "state": "STATE_UNSPECIFIED",
      "serverless": true,
      "status": {
        "code": "OK",
        "message": "<string>"
      },
      "public": true,
      "updateTime": "2023-11-07T05:31:56Z"
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `deployedModels` | array | List of deployed model objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of deployed models. |