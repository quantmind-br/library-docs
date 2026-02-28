---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-if-user-follows-playlist
source: crawler
fetched_at: 2026-02-27T23:39:22.385607-03:00
rendered_js: true
word_count: 74
summary: This document describes a deprecated Spotify Web API endpoint used to check if a specific user follows a playlist and provides a link to its recommended replacement.
tags:
    - spotify-web-api
    - playlists
    - user-follows
    - deprecated
    - api-reference
category: reference
---

Web API •References / Users / Check if Current User Follows Playlist

## Check if Current User Follows Playlist

Deprecated

Check to see if the current user is following a specified playlist.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`
- **Deprecated** A single item list containing current user's [Spotify Username](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). Maximum: 1 id.
  
  Example: `ids=jmperezperez`

## Response

Array of boolean, containing a single boolean

An array of:

Example: `[true]`

```
curl --request GET \
  --url https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/followers/contains \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
```

* * *