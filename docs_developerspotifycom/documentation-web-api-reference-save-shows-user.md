---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-shows-user
source: crawler
fetched_at: 2026-02-27T23:39:02.811934-03:00
rendered_js: true
word_count: 57
summary: This document describes a deprecated Spotify Web API endpoint for saving shows to a user's library and provides a link to its recommended replacement.
tags:
    - spotify-api
    - user-library
    - show-management
    - deprecated-api
    - http-put
category: api
---

Web API •References / Shows / Save Shows for Current User

## Save Shows for Current User

Deprecated

Save one or more shows to current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the shows. Maximum: 50 IDs.
  
  Example: `ids=5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ`

## Response

```
curl --request PUT \
  --url 'https://api.spotify.com/v1/me/shows?ids=5CfCWKI5pZ28U0uOzXkDHe%2C5as3aKmN2k11yfDDDSrvaZ' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```