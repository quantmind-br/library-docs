---
title: Update Quota
url: https://docs.fireworks.ai/api-reference/update-quota
source: sitemap
fetched_at: 2026-04-27T20:17:08.852368988-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - api-patch
    - quota-update
    - accounts
    - fireworks-ai
    - bearer-authentication
category: reference
word_count: 147
---
Updates a quota via `PATCH /v1/accounts/{account_id}/quotas/{quota_id}`.

```bash
curl --request PATCH \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/quotas/{quota_id} \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "value": "<string>",
  "maxValue": "<string>"
}'
```

**Response**

```json
{
  "name": "<string>",
  "value": "<string>",
  "maxValue": "<string>",
  "usage": 123,
  "updateTime": "2023-11-07T05:31:56Z"
}
```

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Query Parameters

| Field | Type | Description |
|-------|------|-------------|
| `createIfNotExists` | boolean | If `true` and the quota does not exist, it will be created. |

#### Body

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | **Required.** Quota name. |
| `value` | string | Enforced quota value. May be lower than `max_value` if manually lowered. |
| `maxValue` | string | Maximum approved value. |

#### Response

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Quota name |
| `value` | string | Enforced value |
| `maxValue` | string | Maximum approved value |
| `usage` | integer | Current usage |
| `updateTime` | string (date-time) | Last update time (read-only) |
