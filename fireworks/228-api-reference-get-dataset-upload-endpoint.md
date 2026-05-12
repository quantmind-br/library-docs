---
title: Get Dataset Upload Endpoint - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-dataset-upload-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:31.544210155-03:00
rendered_js: false
word_count: 121
summary: This document details how to retrieve the upload endpoint for a specific dataset via a POST request to the Fireworks AI API. It shows the required parameters and describes the structure of both the request body and the response.
tags:
    - api-endpoint
    - dataset-upload
    - post-request
    - fireworks-ai
    - signed-urls
    - rest-api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Dataset Upload Endpoint

Retrieve signed URLs for uploading dataset files.

## Endpoint

`POST /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint`

## Request

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "filenameToSize": {},
  "readMask": "<string>"
}
'
```

## Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Path Parameters

| Param | Type | Description |
|---|---|---|
| `account_id` | string | Fireworks account identifier. |
| `dataset_id` | string | Dataset identifier. |

## Body

| Field | Type | Description |
|---|---|---|
| `filenameToSize` | object | Mapping from filename to its size in bytes. |
| `readMask` | string | Fields to return; empty or `*` returns all. |

## Response

| Field | Type | Description |
|---|---|---|
| `filenameToSignedUrls` | object | Mapping of filenames to signed upload URLs. |

#api-reference #datasets
