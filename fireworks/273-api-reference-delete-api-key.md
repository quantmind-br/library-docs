---
title: Delete API Key - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/delete-api-key
source: sitemap
fetched_at: 2026-04-27T20:14:43.058712502-03:00
rendered_js: false
word_count: 71
summary: Delete a specific API key for a user within an account using a POST request.
tags:
    - api-key-deletion
    - fireworks-ai
    - post-request
    - bearer-authentication
    - account-user-api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Delete API Key

Deletes a specific API key for a user within a given account.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

None

#### Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| keyId | string | Yes | The ID of the API key to delete. |

#### Response

Returns an `object`.

#### Endpoint

```
POST /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete
```

#### Example

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/users/{user_id}/apiKeys:delete \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{"keyId": "<string>"}'
```

#api-reference #api-keys
