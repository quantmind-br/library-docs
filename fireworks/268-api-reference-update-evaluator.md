---
title: Update Evaluator - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/update-evaluator
source: sitemap
fetched_at: 2026-04-27T20:19:06.821278066-03:00
rendered_js: false
word_count: 433
summary: This document provides a reference detailing how to update an existing evaluator within a specific account on the Fireworks AI API using a PATCH request via curl, outlining the required parameters and response structure.
tags:
    - api-reference
    - evaluator-update
    - patch-request
    - fireworks-ai
    - rest-api
    - account-management
category: api
optimized: true
optimized_at: 2026-04-27T23:04:00Z
---
# Update Evaluator

PATCH `/v1/accounts/{account_id}/evaluators/{evaluator_id}`

Updates an existing evaluator within a specific account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Request

### Path Parameters

| Param | Type | Description |
|---|---|---|
| `account_id` | `string` | Account ID |
| `evaluator_id` | `string` | Evaluator ID |

### Query Parameters

| Param | Type | Description |
|---|---|---|
| `prepare_build` | `boolean` | If `true`, prepare a new code upload/build attempt by transitioning the evaluator to `BUILDING` state. Can be used without `update_mask`. |

### Body

| Field | Type | Description |
|---|---|---|
| `displayName` | `string` | Display name |
| `description` | `string` | Description |
| `criteria` | `object[]` | Criteria for the evaluator — each produces a score for a named metric. Used for eval3 with UI upload path. |
| `criteria[].type` | `string` | Criterion type |
| `criteria[].name` | `string` | Criterion name |
| `criteria[].description` | `string` | Criterion description |
| `criteria[].codeSnippets` | `object` | Source code for the criterion |
| `criteria[].codeSnippets.language` | `string` | Language |
| `criteria[].codeSnippets.fileContents` | `object` | File contents |
| `criteria[].codeSnippets.entryFile` | `string` | Entry file |
| `criteria[].codeSnippets.entryFunc` | `string` | Entry function |
| `requirements` | `string` | Python requirements |
| `entryPoint` | `string` | Entry point |
| `commitHash` | `string` | Commit hash |
| `source` | `object` | Source information for the evaluator codebase |
| `source.type` | `string` | Source type |
| `source.githubRepositoryName` | `string` | GitHub repository name |
| `defaultDataset` | `string` | Default dataset |

```bash
curl --request PATCH \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id} \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
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
}
'
```

## Response

| Field | Type | Description |
|---|---|---|
| `name` | `string` | Evaluator name |
| `displayName` | `string` | Display name |
| `description` | `string` | Description |
| `createTime` | `string (date-time)` | Creation timestamp (read-only) |
| `createdBy` | `string` | Creator ID (read-only) |
| `updateTime` | `string (date-time)` | Last update timestamp (read-only) |
| `state` | `enum` | Evaluator state (read-only). Options: `STATE_UNSPECIFIED`, `ACTIVE`, `BUILDING`, `BUILD_FAILED` |
| `criteria` | `object[]` | Criteria for the evaluator (read-only) |
| `requirements` | `string` | Python requirements |
| `entryPoint` | `string` | Entry point |
| `status` | `object` | Build status exposed to the user (read-only) |
| `status.code` | `string` | Status code (e.g., `OK`) |
| `status.message` | `string` | Status message |
| `commitHash` | `string` | Commit hash |
| `source` | `object` | Source information for the evaluator codebase (read-only) |
| `defaultDataset` | `string` | Default dataset |
