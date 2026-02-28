---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-shows
source: crawler
fetched_at: 2026-02-27T23:39:07.590916-03:00
rendered_js: true
word_count: 68
summary: This document describes a deprecated Spotify Web API endpoint used to determine if specific shows are currently saved in a user's library and directs users to a replacement endpoint.
tags:
    - spotify-api
    - web-api
    - shows
    - library-management
    - deprecated-endpoint
category: api
---

Web API •References / Shows / Check User's Saved Shows

## Check User's Saved Shows

Deprecated

Check if one or more shows is already saved in the current Spotify user's library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the shows. Maximum: 50 IDs.
  
  Example: `ids=5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/shows/contains?ids=5CfCWKI5pZ28U0uOzXkDHe%2C5as3aKmN2k11yfDDDSrvaZ' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```