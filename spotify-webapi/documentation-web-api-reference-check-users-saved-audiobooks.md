---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-audiobooks
source: crawler
fetched_at: 2026-02-27T23:46:19.510565-03:00
rendered_js: true
word_count: 68
summary: This document describes the deprecated Spotify Web API endpoint used to verify if specific audiobooks are present in a user's saved library.
tags:
    - spotify-api
    - audiobooks
    - user-library
    - deprecated-endpoint
    - api-reference
category: reference
---

Web API •References / Audiobooks / Check User's Saved Audiobooks

## Check User's Saved Audiobooks

Deprecated

Check if one or more audiobooks are already saved in the current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ`. Maximum: 50 IDs.
  
  Example: `ids=18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/audiobooks/contains?ids=18yVqkdbdRvS24c0Ilj2ci%2C1HGw3J3NxZO1TP1BTtVhpZ%2C7iHfbu1YPACw6oZPAFJtqe' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```