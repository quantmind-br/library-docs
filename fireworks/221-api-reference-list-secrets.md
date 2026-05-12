---
title: List Secrets - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-secrets
source: sitemap
fetched_at: 2026-04-27T20:19:05.624204222-03:00
rendered_js: false
word_count: 154
summary: This document describes a GET endpoint for retrieving secret information associated with a specific account ID via the Fireworks AI API. It details the required authentication method, expected response structure, and available fields.
tags:
    - api-endpoint
    - get-request
    - account-secrets
    - bearer-auth
    - response-schema
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# List Secrets

Returns a paginated list of secrets for an account.

## Endpoint

`GET /v1/accounts/{account_id}/secrets`

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/secrets \
  --header 'Authorization: Bearer <token>'
```

## Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Response

| Field | Type | Description |
|---|---|---|
| `secrets` | array | List of secret objects. |
| `secrets[].name` | string | Secret name. |
| `secrets[].keyName` | string | Key name. |
| `secrets[].value` | string | Secret value (e.g., `sk-...`). |
| `nextPageToken` | string | Pagination token for next page. |
| `totalSize` | integer | Total number of secrets. |

## Query Parameters

| Param | Type | Default | Description |
|---|---|---|---|
| `pageToken` | string | — | Pagination token (required for ListRequest). |
| `pageSize` | integer | — | Page size (required for ListRequest). |
| `readMask` | string | `*` | Fields to return; empty or `*` returns all. |

#api-reference #list-request
