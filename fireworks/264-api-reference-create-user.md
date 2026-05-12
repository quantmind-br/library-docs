---
title: Create User
url: https://docs.fireworks.ai/api-reference/create-user
source: sitemap
fetched_at: 2026-04-27T20:14:39.365613391-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - bearer-authentication
    - user-creation
    - request-parameters
    - api-body
    - response-fields
category: reference
word_count: 214
---
Creates a user via the Fireworks API.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Query Parameters

| Field | Type | Description |
|-------|------|-------------|
| `userId` | string | User ID to use in the user name (e.g., `my-user`). If not specified, a default ID is generated from `user.email`. |

#### Body

| Field | Type | Description |
|-------|------|-------------|
| `role` | string | User role: `admin`, `user`, `contributor`, `inference-user`, or `custom`. When `custom`, permissions are governed by `permission_preset`. |
| `displayName` | string | Human-readable display name. Must be fewer than 64 characters. |
| `email` | string | The user's email address. |
| `permissionPreset` | string | Permission preset for custom roles only. |

#### Response

| Field | Type | Description |
|-------|------|-------------|
| `role` | string | User role |
| `displayName` | string | Display name |
| `createTime` | string (date-time) | Creation time (read-only) |
| `email` | string | Email address |
| `state` | enum | State (read-only): `STATE_UNSPECIFIED`, `CREATING`, `READY`, `UPDATING`, `DELETING` |
| `status` | object | User status per [google.rpc.status](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only) |
| `updateTime` | string (date-time) | Last update time (read-only) |
| `permissionPreset` | string | Permission preset for custom roles |
