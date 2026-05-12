---
title: List Quotas - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-quotas
source: sitemap
fetched_at: 2026-04-27T20:17:05.663301007-03:00
rendered_js: false
word_count: 211
summary: GET request to retrieve account quotas from the Fireworks AI API.
tags:
    - api-quotas
    - fireworks-ai
    - get-request
    - account-details
    - pagination
    - bearer-token
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!info]
> **Endpoint:** `GET /v1/accounts/{account_id}/quotas`  
> **Auth:** Bearer token — format: `Bearer <API_KEY>`

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/quotas \
  --header 'Authorization: Bearer <token>'
```

## Query Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page_size` | integer | 50 | Maximum quotas to return. Max: 200. |
| `page_token` | string | — | Page token from a previous `ListQuotas` call. |
| `order_by` | string | — | Comma-separated fields to order by. Append ` desc` for descending. Subfields use `.` (e.g., `foo.bar`). |
| `fields` | string | `"*"` | Fields to return. Use `*` or empty for all. |

## Response Schema

```json
{
  "quotas": [
    {
      "name": "<string>",
      "value": "<string>",
      "maxValue": "<string>",
      "usage": 123,
      "updateTime": "2023-11-07T05:31:56Z"
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `quotas` | array | List of quota objects. |
| `nextPageToken` | string | Token for the next page. Omitted when no more pages. |
| `totalSize` | integer | Total number of quotas matching the query. |

### Quota Object Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Quota name identifier. |
| `value` | string | Current quota value. |
| `maxValue` | string | Maximum allowed quota value. |
| `usage` | integer | Current usage count. |
| `updateTime` | string (RFC 3339) | Last update timestamp. |
