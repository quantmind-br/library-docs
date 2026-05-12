---
title: List Users - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-users
source: sitemap
fetched_at: 2026-04-27T20:13:43.333817185-03:00
rendered_js: false
word_count: 10
summary: This document defines the structure of a response object, detailing an array of user objects and pagination metadata.
tags:
    - user-data
    - response-object
    - pagination
    - service-account
    - identity
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# List Users

Response schema for listing users.

```json
{
  "users": [
    {
      "role": "<string>",
      "name": "<string>",
      "displayName": "<string>",
      "serviceAccount": true,
      "createTime": "2023-11-07T05:31:56Z",
      "email": "<string>",
      "state": "STATE_UNSPECIFIED",
      "status": {
        "code": "OK",
        "message": "<string>"
      },
      "updateTime": "2023-11-07T05:31:56Z",
      "permissionPreset": "<string>"
    }
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

#api-reference #users
