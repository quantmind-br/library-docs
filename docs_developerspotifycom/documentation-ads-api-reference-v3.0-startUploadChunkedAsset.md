---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/startUploadChunkedAsset
source: crawler
fetched_at: 2026-02-27T23:40:39.061929-03:00
rendered_js: true
word_count: 129
summary: This document describes the API endpoint used to initiate a chunked asset upload process for media files such as images, audio, and video. it explains how to retrieve a unique upload session ID and determine the maximum chunk size required for data transfer.
tags:
    - ads-api
    - asset-management
    - chunked-upload
    - media-upload
    - api-endpoint
category: api
---

Ads API •References / assets / Start Upload Chunked Asset

## Start Upload Chunked Asset

Start a chunked asset upload process and retrieve upload session id. Asset type can be image, audio, or video. Client is expected to use max\_chunk\_size\_mb in the response to dynamically determine how big each file chunk should be.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

Contains a unique upload session ID to be used in subsequent transfer requests. Also, the maximum file chunk size in megabytes.

- upload\_session\_idstring \[uuid]
  
  A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- max\_chunk\_size\_mbinteger \[int32]
  
  Maximum file chunk size in megabytes. Client must use this value to dynamically determine how to split the file.
  
  Example: `10`

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/assets/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/chunked_upload/start \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"upload_session_id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","max_chunk_size_mb": 10}
```