---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-audiobooks-user
source: crawler
fetched_at: 2026-02-27T23:46:16.323079-03:00
rendered_js: true
word_count: 64
summary: This document provides technical details for a deprecated Spotify Web API endpoint used to save specific audiobooks to a user's library.
tags:
    - spotify-api
    - audiobooks
    - user-library
    - deprecated-endpoint
    - http-put
category: api
---

Web API •References / Audiobooks / Save Audiobooks for Current User

## Save Audiobooks for Current User

Deprecated

Save one or more audiobooks to the current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ`. Maximum: 50 IDs.
  
  Example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe`

## Response

Audiobook(s) are saved to the library

```
curl --request PUT \
  --url 'https://api.spotify.com/v1/me/audiobooks?ids=18yVqkdbdRvS24c0Ilj2ci%2C1HGw3J3NxZO1TP1BTtVhpZ%2C7iHfbu1YPACw6oZPAFJtqe' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```