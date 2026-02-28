---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/save-library-items
source: crawler
fetched_at: 2026-02-27T23:46:41.488402-03:00
rendered_js: true
word_count: 61
summary: This document provides technical details for the Spotify Web API endpoint used to add tracks, albums, and other content to a user's library using specific URIs.
tags:
    - spotify-api
    - user-library
    - item-management
    - spotify-uris
    - endpoint-reference
category: api
---

Web API •References / Library / Save Items to Library

## Save Items to Library

Add one or more items to the current user's library. Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, users, and playlists.

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

## Response sample

```
empty response
```