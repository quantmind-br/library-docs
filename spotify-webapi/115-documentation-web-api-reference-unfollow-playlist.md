---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/unfollow-playlist
source: crawler
fetched_at: 2026-02-27T23:47:02.744638-03:00
rendered_js: false
word_count: 48
summary: This document provides details for a deprecated API endpoint that allows a user to stop following a specific Spotify playlist.
tags:
    - spotify-api
    - playlist-management
    - deprecated-endpoint
    - user-library
    - endpoint-reference
category: reference
---

Web API •References / Users / Unfollow Playlist

## Unfollow Playlist

Deprecated

Remove the current user as a follower of a playlist.

**Note:** This endpoint is deprecated. Use [Remove Items from Library](https://developer.spotify.com/documentation/web-api/reference/remove-library-items) instead.

Authorization scopes

## Request

- playlist\_idstring
  
  Required
  
  The [Spotify ID](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids) of the playlist.
  
  Example: `3cEYpjA9oz9GiPac4AsH4n`

## Response

Playlist unfollowed