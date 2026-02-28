---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/upload-logo
source: crawler
fetched_at: 2026-02-27T23:42:08.77099-03:00
rendered_js: true
word_count: 101
summary: This document provides the API specifications and image requirements for uploading a partner logo within the Spotify Open Access platform.
tags:
    - spotify-open-access
    - partner-logo
    - api-endpoint
    - image-requirements
    - logo-upload
category: api
---

Open Access •References / Set partner logo

## Set partner logo

**Required scope:** `soa-manage-partner`

Image guidelines:

- Neither height nor width should be greater than 8000 pixels.
- At least one side should be 1000 pixels or greater.
- It is advised to use a square image.
- The file size should not exceed 10 Mb.
- Supported file formats are PNG, JPG, and TIFF.
- Make sure that the partner logo respects the logos and naming restrictions according to Spotify’s design guidelines.

## Request

- The Partner ID issued by Spotify at creation.

## Response

A successful response will have HTTP status code 200 and an empty payload.

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/upload-logo/string \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: image/*' \
  --data string
```

* * *

## Response sample

```
empty response
```