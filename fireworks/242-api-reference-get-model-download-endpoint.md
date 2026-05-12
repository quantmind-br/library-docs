---
title: Get Model Download Endpoint - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-model-download-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:25.944105393-03:00
rendered_js: false
word_count: 108
summary: Retrieve the download endpoint URL for a specific model via GET request.
tags:
    - api-endpoint
    - download-url
    - model-access
    - bearer-auth
    - fireworks-ai
    - get-request
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Model Download Endpoint

GET `https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint`

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint \
  --header 'Authorization: Bearer <token>'
```

## Authorization

Bearer authentication using your Fireworks API key.

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | Account identifier. |
| `model_id` | string | Model identifier. |

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `readMask` | string | Fields to return. If empty or `"*"`, all fields are returned. |

## Response

```json
{
  "filenameToSignedUrls": {}
}
```

| Field | Type | Description |
|-------|------|-------------|
| `filenameToSignedUrls` | object | Signed URLs for downloading model files. |

> [!note]
> Returns signed URLs for downloading model files. #api-endpoint #download-url #model-access