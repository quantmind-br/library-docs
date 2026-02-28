---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/createUploadUrl
source: crawler
fetched_at: 2026-02-27T23:39:54.524695-03:00
rendered_js: true
word_count: 71
summary: This document provides technical details for the API endpoint used to retrieve a signed Google Cloud Storage (GCS) URL for uploading audience user list files.
tags:
    - ads-api
    - audiences
    - gcs-upload
    - user-list
    - signed-url
category: api
---

Ads API •References / audiences / Get Signed GCS upload URL to upload a user list file

## Get Signed GCS upload URL to upload a user list file

Get Signed GCS upload URL.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

## Response

A signed GCS upload URL.

- A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- Signed GCS upload URL to upload a user list file.

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/audiences/upload_url \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
{"id": "ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a","upload_url": "string"}
```