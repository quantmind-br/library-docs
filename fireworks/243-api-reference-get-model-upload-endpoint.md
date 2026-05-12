---
title: Get Model Upload Endpoint - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-model-upload-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:11.475717534-03:00
rendered_js: false
word_count: 163
summary: Retrieve the upload endpoint for a specific model via POST request.
tags:
    - api-endpoint
    - model-upload
    - post-request
    - fireworks-ai
    - authentication
    - url-generation
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Model Upload Endpoint

POST `https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint`

## Request

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "filenameToSize": {},
  "enableResumableUpload": true,
  "readMask": "<string>"
}
'
```

## Authorization

Bearer authentication using your Fireworks API key.

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | Account identifier. |
| `model_id` | string | Model identifier. |

## Body Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `filenameToSize` | object | required | Mapping from filename to size in bytes. |
| `enableResumableUpload` | boolean | false | Enable resumable upload instead of PUT. |
| `readMask` | string | - | Fields to return. If empty or `"*"`, all fields returned. |

## Response

```json
{
  "filenameToSignedUrls": {},
  "filenameToUnsignedUris": {}
}
```

| Field | Type | Description |
|-------|------|-------------|
| `filenameToSignedUrls` | object | Signed URLs for uploading model files. |
| `filenameToUnsignedUris` | object | Unsigned URIs (e.g., `s3://bucket/key`, `gs://bucket/key`) for uploading. Returned when the caller has permission. |

> [!note]
> Use `enableResumableUpload: true` for large files that may need to resume. #api-endpoint #model-upload #post-request