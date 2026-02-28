---
title: Ads API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/ads-api/reference/v3.0/transferChunkedAsset
source: crawler
fetched_at: 2026-02-27T23:40:40.351482-03:00
rendered_js: true
word_count: 109
summary: This document describes an API endpoint for uploading individual sections of binary media data as part of a chunked asset upload process for advertisements.
tags:
    - ads-api
    - media-upload
    - chunked-transfer
    - asset-management
    - api-reference
category: api
---

Ads API •References / assets / Transfer Chunked Asset

## Transfer Chunked Asset

Continues the upload session of a chunked asset by transferring one section of binary media data. Supports uploads of file chunks up to 20MB in size. Asset type can be either image, audio, or video.

## Request

- ad\_account\_idstring \[uuid]
  
  A unique identifier for an Ad Account.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`
- A unique identifier for the entity.
  
  Example: `ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a`

<!--THE END-->

- upload\_session\_idstring \[uuid]
  
  A unique identifier for the entity.
  
  Example: `"ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a"`
- upload\_sectioninteger \[int32]
  
  Minimum value: `1`Example: `1`
- Supported content-type(s): `image/png, image/jpeg, audio/ogg, audio/mp3, audio/wav, audio/mpeg, audio/x-wav, video/mp4, video/quicktime`
- Allowed values: `"AUDIO"`, `"IMAGE"`, `"VIDEO"`Example: `"IMAGE"`

## Response

A boolean success indicator.

```
curl --request POST \
  --url https://api-partner.spotify.com/ads/v3/ad_accounts/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/assets/ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a/chunked_upload/transfer \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: multipart/form-data' \
  --form upload_session_id=ce4ff15e-f04d-48b9-9ddf-fb3c85fbd57a \
  --form media=string \
  --form asset_type=IMAGE
```

* * *

## Response sample

```
{"success": true}
```