---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/check-if-user-follows-playlist
source: crawler
fetched_at: 2026-02-27T23:47:04.710183-03:00
rendered_js: false
word_count: 82
summary: This deprecated API documentation describes the endpoint used to verify if the current user follows a specific Spotify playlist. It outlines the required parameters and response format while recommending the use of a newer replacement endpoint.
tags:
    - spotify-web-api
    - playlist-management
    - user-follows
    - deprecated-api
    - endpoint-reference
category: api
---

Web API •References / Users / Check if Current User Follows Playlist

## Check if Current User Follows Playlist

Deprecated

Check to see if the current user is following a specified playlist.

**Note:** This endpoint is deprecated. Use [Check User's Saved Items](https://developer.spotify.com/documentation/web-api/reference/check-library-contains) instead.

## Request

- playlist\_idstring
  
  Required
  
  The [Spotify ID](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of the playlist.
  
  Example: `3cEYpjA9oz9GiPac4AsH4n`
- idsstring
  
  **Deprecated** A single item list containing current user's [Spotify Username](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids). Maximum: 1 id.
  
  Example: `ids=jmperezperez`

## Response

Array of boolean, containing a single boolean

An array of:

Example: `[true]`