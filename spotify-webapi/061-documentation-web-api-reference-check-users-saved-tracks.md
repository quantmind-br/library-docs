---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-users-saved-tracks
source: crawler
fetched_at: 2026-02-27T23:46:58.677464-03:00
rendered_js: false
word_count: 70
summary: This document describes a deprecated Spotify Web API endpoint used to verify whether specific tracks are saved in the current user's library.
tags:
    - spotify-api
    - user-library
    - track-management
    - deprecated-api
    - web-api
category: reference
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

## Response sample

```
[false, true]
```