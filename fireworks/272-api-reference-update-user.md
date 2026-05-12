---
title: Update User - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/update-user
source: sitemap
fetched_at: 2026-04-27T20:13:29.627068291-03:00
rendered_js: false
word_count: 219
summary: Update an existing user's name, role, email, or permission preset via the Fireworks API.
tags:
    - user-update
    - bearer-authentication
    - path-parameters
    - response-schema
    - permission-preset
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Update User

Updates a user's name, role, email, or permission preset. Requires `user.name` in the request body.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Path Parameters

None

#### Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Updated display name. Max 64 characters. |
| role | string | Yes | One of: `admin`, `user`, `contributor`, `inference-user`, `custom`. When `custom`, permissions are governed by `permission_preset`. |
| email | string | Yes | The user's email address. |
| permission_preset | string | No | Permission preset. Only valid when `role` is `custom`. |

#### Response

| Field | Type | Read-only | Description |
|-------|------|-----------|-------------|
| role | string | Yes | User's role. |
| name | string | Yes | Display name. |
| email | string | Yes | Email address. |
| createTime | string (date-time) | Yes | Creation timestamp. |
| state | enum | Yes | One of: `STATE_UNSPECIFIED`, `CREATING`, `READY`, `UPDATING`, `DELETING`. Default: `STATE_UNSPECIFIED`. |
| status | object | Yes | Mimics [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto). |
| updateTime | string (date-time) | Yes | Last update timestamp. |
| permission_preset | string | Yes | Permission preset (only if `role` is `custom`). |

#api-reference #users
