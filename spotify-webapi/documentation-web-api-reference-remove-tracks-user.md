---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-tracks-user
source: crawler
fetched_at: 2026-02-27T23:46:58.720557-03:00
rendered_js: false
word_count: 105
summary: This document outlines the deprecated Spotify Web API endpoint for removing one or more tracks from a user's 'Your Music' library using Spotify IDs.
tags:
    - spotify-api
    - tracks
    - user-library
    - deprecated-endpoint
    - endpoint-reference
category: api
---

Web API •References / Tracks / Remove User's Saved Tracks

## Remove User's Saved Tracks

Deprecated

Remove one or more tracks from the current user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `ids=4iV5W9uYEdYUVa79Axb7Rh,1301WleyT98MSxVHPZCA6M`. Maximum: 50 IDs.
  
  Example: `ids=7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B`

supports free form additional properties

- A JSON array of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). For example: `["4iV5W9uYEdYUVa79Axb7Rh", "1301WleyT98MSxVHPZCA6M"]`  
  A maximum of 50 items can be specified in one request. ***Note**: if the `ids` parameter is present in the query string, any IDs listed here in the body will be ignored.*

## Response

## Response sample

```
empty response
```