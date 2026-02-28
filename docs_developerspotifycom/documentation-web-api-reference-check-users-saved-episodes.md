---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-episodes
source: crawler
fetched_at: 2026-02-27T23:38:37.885216-03:00
rendered_js: true
word_count: 70
summary: This document describes a deprecated Spotify Web API endpoint used to verify if specific podcast episodes are currently saved in a user's library.
tags:
    - spotify-api
    - episodes
    - user-library
    - deprecated-api
    - endpoint-reference
category: api
---

Web API •References / Episodes / Check User's Saved Episodes

## Check User's Saved Episodes

Deprecated

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the episodes. Maximum: 50 IDs.
  
  Example: `ids=77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/episodes/contains?ids=77o6BIVlYM3msb4MMIL1jH%2C0Q86acNRm6V9GYx55SXKwf' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```