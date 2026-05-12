---
title: Create Evaluator - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/create-evaluator
source: sitemap
fetched_at: 2026-04-27T20:19:17.507943048-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - evaluator
    - api-post
    - fireworks-ai
    - rest-api
    - json-body
    - resource-management
category: reference
word_count: 287
---
Creates an evaluator via `POST /v1/accounts/{account_id}/evaluatorsV2`.

## Request

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluatorsV2 \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "evaluator": {
    "displayName": "<string>",
    "description": "<string>",
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
    "commitHash": "<string>",
    "source": {
      "type": "TYPE_UNSPECIFIED",
      "githubRepositoryName": "<string>"
    },
    "defaultDataset": "<string>"
  },
  "evaluatorId": "<string>"
}'
```

### Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

### Body Parameters

| Field | Type | Description |
|-------|------|-------------|
| `evaluator` | object | Evaluator configuration |
| `evaluator.displayName` | string | Display name |
| `evaluator.description` | string | Description |
| `evaluator.criteria` | array | Criteria for the evaluator; produces a score for the metric |
| `evaluator.criteria[].type` | string | Criteria type |
| `evaluator.criteria[].name` | string | Metric name |
| `evaluator.criteria[].description` | string | Description |
| `evaluator.criteria[].codeSnippets` | object | Code snippets for evaluation |
| `evaluator.requirements` | string | Python requirements |
| `evaluator.entryPoint` | string | Entry point |
| `evaluator.commitHash` | string | Commit hash |
| `evaluator.source` | object | Source information |
| `evaluator.defaultDataset` | string | Default dataset |
| `evaluatorId` | string | Evaluator ID (optional) |

## Response

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

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Evaluator name |
| `displayName` | string | Display name |
| `description` | string | Description |
| `createTime` | string (date-time) | Creation time (read-only) |
| `createdBy` | string | Creator (read-only) |
| `updateTime` | string (date-time) | Last update time (read-only) |
| `state` | enum | State (read-only): `STATE_UNSPECIFIED`, `ACTIVE`, `BUILDING`, `BUILD_FAILED` |
| `criteria` | array | Evaluation criteria |
| `requirements` | string | Python requirements |
| `entryPoint` | string | Entry point |
| `status` | object | Build status (read-only) |
| `commitHash` | string | Commit hash |
| `source` | object | Source repository info |
| `defaultDataset` | string | Default dataset |
