---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/remove-library-items
source: crawler
fetched_at: 2026-02-27T23:38:41.381543-03:00
rendered_js: true
word_count: 65
summary: This document specifies the Web API endpoint and parameters required to remove tracks, albums, and other media items from a user's library using Spotify URIs.
tags:
    - spotify-api
    - library-management
    - delete-items
    - web-api
    - uris
    - media-library
category: api
---

Web API •References / Library / Remove Items from Library

## Remove Items from Library

Remove one or more items from the current user's library. Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, users, and playlists.

## Request

- A comma-separated list of [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). Maximum: 40 URIs.
  
  Supported URI types:
  
  - `spotify:track:{id}`
  - `spotify:album:{id}`
  - `spotify:episode:{id}`
  - `spotify:show:{id}`
  - `spotify:audiobook:{id}`
  - `spotify:user:{id}`
  - `spotify:playlist:{id}`
  
  Example: `uris=spotify%3Atrack%3A7a3LWj5xSFhFRYmztS8wgK,spotify%3Aalbum%3A4aawyAB9vmqN3uQ7FjRGTy`

## Response

Items removed from library

## Response sample

```
empty response
```