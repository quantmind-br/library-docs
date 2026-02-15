---
title: Progresses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/progresses
source: sitemap
fetched_at: 2026-02-15T09:14:24.550926-03:00
rendered_js: false
word_count: 23
summary: This document describes the API endpoint for retrieving detailed information about a specific progress record by its ID, including authentication and response formats.
tags:
    - api-endpoint
    - progress-tracking
    - authentication
    - json-response
    - get-request
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

chevron-right

200

Getting a specific progress

application/json

get

/api/v1/progresses/{id}

```
GET /api/v1/progresses/{id} HTTP/1.1
Host:REPLACE_ME
Authorization:YOUR_API_KEY
Accept:*/*
```

200

Getting a specific progress

```
{
"progress":{
"id":2,
"account_id":67,
"canvas_user_id":null,
"completion_percent":null,
"workflow_state":"queued",
"payload":{},
"created_at":"2024/01/01 00:00:00 +0000",
"updated_at":"2024/01/01 00:00:00 +0000"
}
}
```