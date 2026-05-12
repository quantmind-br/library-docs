---
title: List API Keys - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-api-keys
source: sitemap
fetched_at: 2026-04-27T20:13:58.775243562-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - api-response
    - api-keys
    - data-structure
    - pagination-token
    - key-management
category: reference
word_count: 64
---
# List API Keys

`GET /api_keys` — Returns a paginated list of API keys for the account.

## Response Schema

```json
{
  "apiKeys": [
    {
      "keyId": "<string>",
      "displayName": "<string>",
      "key": "<string>",
      "createTime": "2023-11-07T05:31:56Z",
      "secure": true,
      "email": "<string>",
      "prefix": "<string>",
      "expireTime": "2023-11-07T05:31:56Z",
      "annotations": {},
      "lastUsed": "2023-11-07T05:31:56Z"
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `apiKeys` | array | List of API key objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of API keys. |