---
title: Get Evaluator Upload Endpoint - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-evaluator-upload-endpoint
source: sitemap
fetched_at: 2026-04-27T20:19:17.247918532-03:00
rendered_js: false
word_count: 74
summary: Retrieve the upload endpoint for an evaluator within a given account via POST.
tags:
    - api-endpoint
    - evaluator-upload
    - fireworks-ai
    - post-request
    - get-endpoint
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Evaluator Upload Endpoint

POST `https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id}:getUploadEndpoint`

## Request

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/evaluators/{evaluator_id}:getUploadEndpoint \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "filenameToSize": {},
  "readMask": "<string>"
}
'
```

## Authorization

Bearer authentication using your Fireworks API key.

## Body Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filenameToSize` | object | Mapping of filename to size in bytes. |
| `readMask` | string | Fields to return. If empty or `"*"`, all fields are returned. |

## Response

```json
{
  "filenameToSignedUrls": {}
}
```

> [!note]
> Returns signed URLs for uploading evaluator files. #api-endpoint #evaluator-upload #post-request