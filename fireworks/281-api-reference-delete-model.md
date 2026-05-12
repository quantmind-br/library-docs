---
title: Delete Model - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-model
source: sitemap
fetched_at: 2026-04-27T20:14:31.522244122-03:00
rendered_js: false
word_count: 90
summary: This document details the HTTP DELETE endpoint used to completely remove a specific model associated with an account via the Fireworks AI API.
tags:
    - delete
    - model
    - api-call
    - fireworks-ai
    - endpoint
    - resource-removal
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Model

Permanently delete a model from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/models/{model_id}
```

## Authorizations

| Type | Location | Required | Description |
|------|----------|----------|-------------|
| Bearer | `Authorization` header | Yes | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | The Account ID |
| `model_id` | string | The Model ID |

## Response

`200 application/json` — Successful response. Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id} \
  --header 'Authorization: Bearer <token>'
```

## Related Operations

[[269-api-reference-update-model|Update Model]] · [[297-api-reference-prepare-model|Prepare Model]]

#model #rest-api
