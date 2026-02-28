---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-library-contains
source: crawler
fetched_at: 2026-02-27T23:46:44.56878-03:00
rendered_js: false
word_count: 75
summary: This document describes the Spotify Web API endpoint used to check if specific items such as tracks, albums, or episodes are already saved in the current user's library.
tags:
    - spotify-api
    - user-library
    - saved-items
    - spotify-uris
    - boolean-response
category: api
---

Web API •References / Library / Check User's Saved Items

## Check User's Saved Items

Check if one or more items are already saved in the current user's library. Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, artists, users, and playlists.

## Request

- A comma-separated list of [Spotify URIs](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). Maximum: 40 URIs.
  
  Supported URI types:
  
  - `spotify:track:{id}`
  - `spotify:album:{id}`
  - `spotify:episode:{id}`
  - `spotify:show:{id}`
  - `spotify:audiobook:{id}`
  - `spotify:artist:{id}`
  - `spotify:user:{id}`
  - `spotify:playlist:{id}`
  
  Example: `uris=spotify%3Atrack%3A7a3LWj5xSFhFRYmztS8wgK,spotify%3Aalbum%3A4aawyAB9vmqN3uQ7FjRGTy,spotify%3Aartist%3A2takcwOaAZWiXQijPHIx7B`

## Response

Array of booleans

An array of:

Example: `[false,true]`

## Response sample

```
[false, true]
```