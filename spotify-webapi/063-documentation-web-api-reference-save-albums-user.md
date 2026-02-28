---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-albums-user
source: crawler
fetched_at: 2026-02-27T23:45:53.93681-03:00
rendered_js: true
word_count: 107
summary: This document provides technical specifications and a deprecation notice for the Spotify Web API endpoint used to save albums to a user's personal library.
tags:
    - spotify-api
    - album-management
    - user-library
    - deprecated-endpoint
    - web-api
category: api
---

Web API •References / Albums / Save Albums for Current User

## Save Albums for Current User

Deprecated

Save one or more albums to the current user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the albums. Maximum: 20 IDs.
  
  Example: `ids=382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc`

supports free form additional properties

- A JSON array of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `["4iV5W9uYEdYUVa79Axb7Rh", "1301WleyT98MSxVHPZCA6M"]`  
  A maximum of 50 items can be specified in one request. ***Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored.*

## Response

```
curl --request PUT \
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