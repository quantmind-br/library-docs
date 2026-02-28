---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/follow-playlist
source: crawler
fetched_at: 2026-02-27T23:47:03.106092-03:00
rendered_js: false
word_count: 75
summary: This document describes a deprecated Spotify Web API endpoint used to add the current user as a follower of a playlist and points to its current replacement.
tags:
    - spotify-api
    - playlist-management
    - deprecated-endpoint
    - user-following
    - web-api
category: reference
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

## Response sample

```
empty response
```