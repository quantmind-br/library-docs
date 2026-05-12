---
title: Get Dataset Download Endpoint - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-dataset-download-endpoint
source: sitemap
fetched_at: 2026-04-27T20:14:27.148379159-03:00
rendered_js: false
word_count: 137
summary: This document details the endpoint used to retrieve the download endpoints for a specific dataset within an account on the Fireworks AI API.
tags:
    - dataset-download
    - api-endpoint
    - fireworks-ai
    - get-endpoint
    - signed-urls
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Dataset Download Endpoint

Retrieve signed URLs for downloading dataset files.

## Endpoint

`GET /v1/accounts/{account_id}/datasets/{dataset_id}:getDownloadEndpoint`

## Request

```bash
curl --request GET \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/datasets/{dataset_id}:getDownloadEndpoint \
  --header 'Authorization: Bearer <token>'
```

## Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Path Parameters

| Param | Type | Description |
|---|---|---|
| `account_id` | string | Fireworks account identifier. |
| `dataset_id` | string | Dataset identifier. |

## Query Parameters

| Param | Type | Default | Description |
|---|---|---|---|
| `readMask` | string | `*` | Fields to return; empty or `*` returns all. |
| `includeLineage` | boolean | — | If `true`, downloads entire lineage chain (all related datasets). Filenames prefixed with dataset IDs to avoid collisions. |

## Response

| Field | Type | Description |
|---|---|---|
| `filenameToSignedUrls` | object | Mapping of filenames to signed download URLs. |

#api-reference #datasets
