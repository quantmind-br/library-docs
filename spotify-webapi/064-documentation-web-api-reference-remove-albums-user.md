---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-albums-user
source: crawler
fetched_at: 2026-02-27T23:45:57.329382-03:00
rendered_js: true
word_count: 112
summary: This document describes a deprecated Spotify Web API endpoint for removing specific albums from a user's library and directs developers to the updated replacement endpoint.
tags:
    - spotify-api
    - web-api
    - albums
    - user-library
    - deprecated-api
category: api
---

Web API •References / Albums / Remove Users' Saved Albums

## Remove Users' Saved Albums

Deprecated

Remove one or more albums from the current user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the albums. Maximum: 20 IDs.
  
  Example: `ids=382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc`

supports free form additional properties

- A JSON array of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `["4iV5W9uYEdYUVa79Axb7Rh", "1301WleyT98MSxVHPZCA6M"]`  
  A maximum of 50 items can be specified in one request. ***Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored.*

## Response

Album(s) have been removed from the library

```
curl --request DELETE \
  --url 'https://api.spotify.com/v1/me/albums?ids=382ObEPsp2rxGrnsizN5TX%2C1A2GTWGtFfWp7KSQTwWOyo%2C2noRn2Aes5aoNVsU6iWThc' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "ids": [
        "string"
    ]
}'
```

* * *

## Response sample

```
empty response
```