---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-audiobooks-user
source: crawler
fetched_at: 2026-02-27T23:38:33.045799-03:00
rendered_js: true
word_count: 62
summary: This document describes a deprecated Spotify Web API endpoint used to remove one or more audiobooks from a user's saved library.
tags:
    - spotify-api
    - audiobooks
    - user-library
    - deprecated-endpoint
    - delete-method
category: api
---

Web API •References / Audiobooks / Remove User's Saved Audiobooks

## Remove User's Saved Audiobooks

Deprecated

Remove one or more audiobooks from the Spotify user's library.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ`. Maximum: 50 IDs.
  
  Example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe`

## Response

Audiobook(s) have been removed from the library

```
curl --request DELETE \
  --url 'https://api.spotify.com/v1/me/audiobooks?ids=18yVqkdbdRvS24c0Ilj2ci%2C1HGw3J3NxZO1TP1BTtVhpZ%2C7iHfbu1YPACw6oZPAFJtqe' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```