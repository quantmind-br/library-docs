---
title: Delete secret - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-secret
source: sitemap
fetched_at: 2026-04-27T20:14:37.855951613-03:00
rendered_js: false
word_count: 87
summary: This document details the DELETE endpoint within the Fireworks API, providing specific cURL examples and outlining the required components such as authorization headers, path parameters (account_id and secret_id), and expected successful response structure.
tags:
    - api-reference
    - delete-endpoint
    - fireworks-ai
    - curl-command
    - bearer-token
    - secret-deletion
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete Secret

Permanently delete a secret from an account.

## Endpoint

```
DELETE /v1/accounts/{account_id}/secrets/{secret_id}
```

## Authorizations

| Type | Location | Required | Description |
|------|----------|----------|-------------|
| Bearer | `Authorization` header | Yes | Fireworks API key. Format: `Bearer <API_KEY>` |

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | The Account ID |
| `secret_id` | string | The Secret ID |

## Response

`200 application/json` — Successful response. Returns an `object`.

## Example

```bash
curl --request DELETE \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/secrets/{secret_id} \
  --header 'Authorization: Bearer <token>'
```

## Related Operations

[[271-api-reference-update-secret|Update Secret]]

#secret-deletion #rest-api
