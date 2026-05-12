---
title: Get Evaluator - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-evaluator
source: sitemap
fetched_at: 2026-04-27T20:19:11.178536855-03:00
rendered_js: false
word_count: 166
summary: Returns the full evaluator object schema including name, state, criteria, and status.
tags:
    - data-model
    - object-structure
    - json-schema
    - api-payload
    - metadata-definition
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Evaluator

Returns the full evaluator object.

```json
{
  "name": "<string>",
  "displayName": "<string>",
  "description": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "createdBy": "<string>",
  "updateTime": "2023-11-07T05:31:56Z",
  "state": "STATE_UNSPECIFIED",
  "criteria": [
    {
      "type": "TYPE_UNSPECIFIED",
      "name": "<string>",
      "description": "<string>",
      "codeSnippets": {
        "language": "<string>",
        "fileContents": {},
        "entryFile": "<string>",
        "entryFunc": "<string>"
      }
    }
  ],
  "requirements": "<string>",
  "entryPoint": "<string>",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "commitHash": "<string>",
  "source": {
    "type": "TYPE_UNSPECIFIED",
    "githubRepositoryName": "<string>"
  },
  "defaultDataset": "<string>"
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Evaluator name. |
| `displayName` | string | Display name. |
| `description` | string | Description. |
| `createTime` | string | ISO 8601 creation timestamp. |
| `createdBy` | string | Creator identifier. |
| `updateTime` | string | ISO 8601 last update timestamp. |
| `state` | string | Evaluator state (e.g., `STATE_UNSPECIFIED`). |
| `criteria` | array | Evaluation criteria definitions. |
| `requirements` | string | Requirements for the evaluator. |
| `entryPoint` | string | Entry point for execution. |
| `status` | object | Status with `code` and `message`. |
| `commitHash` | string | Git commit hash. |
| `source` | object | Source configuration with `type` and `githubRepositoryName`. |
| `defaultDataset` | string | Default dataset for evaluation. |

> [!info]
> Schema for evaluator objects returned by the Fireworks API. #data-model #object-structure #json-schema