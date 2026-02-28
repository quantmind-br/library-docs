---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/follow-playlist
source: crawler
fetched_at: 2026-02-27T23:39:16.9843-03:00
rendered_js: true
word_count: 75
summary: This document describes the deprecated Spotify Web API endpoint used to add the current user as a follower of a specific playlist. It includes request parameters and provides a link to the current recommended method for saving items to a user's library.
tags:
    - spotify-api
    - playlists
    - user-following
    - deprecated
    - web-api
category: api
---

Web API •References / Users / Follow Playlist

## Follow Playlist

Deprecated

Add the current user as a follower of a playlist.

**Note:** This endpoint is deprecated. Use [Save Items to Library](https://developer.spotify.com/documentation/web-api/reference/save-library-items) instead.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

supports free form additional properties

- Defaults to `true`. If `true` the playlist will be included in user's public playlists (added to profile), if `false` it will remain private. For more about public/private status, see [Working with Playlists](https://developer.spotify.com/documentation/web-api/concepts/playlists)

## Response

```
curl --request PUT \
  --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/followers \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z' \
  --header 'Content-Type: application/json' \
  --data '{
    "public": false
}'
```

* * *

## Response sample

```
empty response
```