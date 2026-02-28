---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-albums
source: crawler
fetched_at: 2026-02-27T23:38:23.7432-03:00
rendered_js: true
word_count: 70
summary: This document provides the technical specifications for a deprecated Spotify Web API endpoint used to check if specific albums are saved in a user's library. It details the required request parameters and response formats while directing users to a more current alternative.
tags:
    - spotify-web-api
    - user-library
    - album-management
    - api-deprecation
    - endpoint-reference
category: api
---

Web API •References / Albums / Check User's Saved Albums

## Check User's Saved Albums

Deprecated

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- A comma-separated list of the [Spotify IDs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) for the albums. Maximum: 20 IDs.
  
  Example: `ids=382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc`

## Response

Array of booleans

An array of:

Example: `[false,true]`

```
curl --request GET \
  --url 'https://api.spotify.com/v1/me/albums/contains?ids=382ObEPsp2rxGrnsizN5TX%2C1A2GTWGtFfWp7KSQTwWOyo%2C2noRn2Aes5aoNVsU6iWThc' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
[false, true]
```