---
title: Get Quota - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-quota
source: sitemap
fetched_at: 2026-04-27T20:17:08.646711639-03:00
rendered_js: false
word_count: 80
summary: Returns the quota object schema with name, value, maxValue, usage, and updateTime fields.
tags:
    - data-schema
    - object-structure
    - json-format
    - metadata-template
    - field-definition
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Quota

Returns the quota object.

```json
{
  "name": "<string>",
  "value": "<string>",
  "maxValue": "<string>",
  "usage": 123,
  "updateTime": "2023-11-07T05:31:56Z"
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Quota name. |
| `value` | string | Current quota value. |
| `maxValue` | string | Maximum allowed quota value. |
| `usage` | integer | Current usage count. |
| `updateTime` | string | ISO 8601 timestamp of last update. |

> [!info]
> Schema for quota objects tracking resource limits and usage. #data-schema #object-structure #json-format