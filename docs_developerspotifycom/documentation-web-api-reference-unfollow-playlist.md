---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/unfollow-playlist
source: crawler
fetched_at: 2026-02-27T23:39:14.637339-03:00
rendered_js: true
word_count: 38
summary: This document provides technical details for the deprecated Spotify Web API endpoint used to remove the current user as a follower of a specific playlist.
tags:
    - spotify-api
    - playlists
    - follower-management
    - deprecated
    - web-api
    - endpoint-reference
category: reference
---

Web API •References / Users / Unfollow Playlist

## Unfollow Playlist

Deprecated

Remove the current user as a follower of a playlist.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

## Response

```
curl --request DELETE \
  --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/followers \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *

## Response sample

```
empty response
```