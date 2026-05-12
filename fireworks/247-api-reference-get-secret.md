---
title: Get Secret - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-secret
source: sitemap
fetched_at: 2026-04-27T20:19:08.071110877-03:00
rendered_js: false
word_count: 153
summary: Retrieve a specific secret associated with an account via GET request.
tags:
    - api-endpoint
    - get-request
    - account-secrets
    - bearer-auth
    - fireworks-api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Secret

GET `https://api.fireworks.ai/v1/accounts/{account_id}/secrets/{secret_id}`

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/secrets/{secret_id} \
  --header 'Authorization: Bearer <token>'
```

## Authorization

Bearer authentication using your Fireworks API key.

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | Account identifier. |
| `secret_id` | string | Secret identifier. |

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `readMask` | string | Fields to return. If empty or `"*"`, all fields are returned. |

## Response

```json
{
  "name": "<string>",
  "keyName": "<string>",
  "value": "sk-1234567890abcdef"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Secret name. |
| `keyName` | string | Key name. |
| `value` | string | Secret value. **INPUT_ONLY** — not returned in GET/LIST responses for security. Only accepted when creating or updating secrets. |

> [!warning]
> The `value` field is `INPUT_ONLY` and will not be returned in GET or LIST responses for security reasons. Only provide it when creating or updating secrets. #api-endpoint #get-request #account-secrets