---
title: Get Deployed Model - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-deployed-model
source: sitemap
fetched_at: 2026-04-27T20:14:19.734411632-03:00
rendered_js: false
word_count: 131
summary: Response schema for the GET /accounts/{account_id}/deployedModels/{deployed_model_id} endpoint.
tags:
    - api-reference
    - deployed-models
    - response-schema
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/deployedModels/{deployed_model_id}`

## Response

| Field | Type | Description |
|---|---|---|
| `name` | string | Resource name |
| `displayName` | string | Display name |
| `description` | string | Description |
| `createTime` | string (RFC3339) | Creation timestamp |
| `model` | string | Associated model |
| `deployment` | string | Associated deployment |
| `default` | boolean | Whether this is the default deployed model |
| `state` | string | Model state (e.g. `STATE_UNSPECIFIED`) |
| `serverless` | boolean | Whether serverless mode is enabled |
| `status.code` | string | Status code (e.g. `OK`) |
| `status.message` | string | Status message |
| `public` | boolean | Whether publicly accessible |
| `updateTime` | string (RFC3339) | Last update timestamp |

```json
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
```