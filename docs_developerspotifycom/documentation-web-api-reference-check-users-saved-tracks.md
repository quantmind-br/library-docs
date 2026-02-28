---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-tracks
source: crawler
fetched_at: 2026-02-27T23:39:11.096025-03:00
rendered_js: true
word_count: 70
summary: This document provides technical details for a deprecated Spotify Web API endpoint used to check if specific tracks are saved in a user's library.
tags:
    - spotify-api
    - web-api
    - user-library
    - tracks
    - deprecated-api
category: api
---

Web API •References / Tracks / Check User's Saved Tracks

## Check User's Saved Tracks

Deprecated

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=4iV5W9uYEdYUVa79Axb7Rh,1301WleyT98MSxVHPZCA6M`. Maximum: 50 IDs.
  
  Example: `ids=7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/tracks/contains?ids=7ouMYWpwJ422jRcDASZB7P%2C4VqPOruhp5EdPBeR92t6lQ%2C2takcwOaAZWiXQijPHIx7B' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```