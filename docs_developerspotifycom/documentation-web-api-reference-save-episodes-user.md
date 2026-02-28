---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-episodes-user
source: crawler
fetched_at: 2026-02-27T23:38:36.743467-03:00
rendered_js: true
word_count: 98
summary: This document outlines a deprecated Spotify API endpoint used to save podcast episodes to a user's library, providing migration guidance to the current replacement endpoint.
tags:
    - spotify-web-api
    - episodes
    - user-library
    - deprecated-api
    - endpoint-reference
category: api
---

Web API •References / Episodes / Save Episodes for Current User

## Save Episodes for Current User

Deprecated

Save one or more episodes to the current user's library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). Maximum: 50 IDs.
  
  Example: `ids=77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf`

supports free form additional properties

- A JSON array of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids).  
  A maximum of 50 items can be specified in one request. ***Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored.*

## Response

```
curl --request PUT \
  --url 'https://api.spotify.com/v1/me/episodes?ids=77o6BIVlYM3msb4MMIL1jH%2C0Q86acNRm6V9GYx55SXKwf' \
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