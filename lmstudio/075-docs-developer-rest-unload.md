---
title: Unload a model
url: https://lmstudio.ai/docs/developer/rest/unload
source: sitemap
fetched_at: 2026-04-07T21:30:26.795395472-03:00
rendered_js: false
word_count: 47
summary: This documentation details the API endpoint used to programmatically unload a loaded model instance from memory.
tags:
    - api
    - model-management
    - rest-api
    - unload
    - lms-studio
category: reference
---

LM Studio REST API

Unload a loaded model from memory

`POST /api/v1/models/unload`

**Request body**

instance\_id : string

Unique identifier of the model instance to unload.

Example Request

```
curl http://localhost:1234/api/v1/models/unload \
  -H "Authorization: Bearer $LM_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "instance_id": "openai/gpt-oss-20b"
  }'
```

* * *

**Response fields**

instance\_id : string

Unique identifier for the unloaded model instance.

Response

```
{
  "instance_id": "openai/gpt-oss-20b"
}
```

This page's source is available on [GitHub](https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/unload.md)