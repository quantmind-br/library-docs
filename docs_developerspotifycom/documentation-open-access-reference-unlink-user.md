---
title: Open Access Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/reference/unlink-user
source: crawler
fetched_at: 2026-02-27T23:39:22.720981-03:00
rendered_js: true
word_count: 64
summary: This document describes the Spotify Open Access API endpoint used to disconnect a partner user ID from a linked Spotify account.
tags:
    - spotify-api
    - open-access
    - user-management
    - account-linking
    - authentication
category: api
---

Open Access •References / Unlink user

## Unlink user

**Required scope:** `user-soa-unlink`

Given a partner user ID, unlink that user from the Spotify user account that they are currently linked to.

## Request

This endpoint requires the payload to be [provided as a JWT](https://developer.spotify.com/documentation/open-access/concepts#jwt--jws-usage).

The payload has the following fields:

## Response

A successful response will have HTTP status code 200 and an empty payload.

```
curl --request POST \
  --url https://open-access.spotify.com/api/v1/unlink-user \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```