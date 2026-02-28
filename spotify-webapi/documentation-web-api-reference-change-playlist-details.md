---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/change-playlist-details
source: crawler
fetched_at: 2026-02-27T23:45:32.461596-03:00
rendered_js: true
word_count: 139
summary: This document explains how to update an existing Spotify playlist's name, public status, collaborative state, and description using the Web API.
tags:
    - spotify-api
    - playlist-management
    - web-api
    - endpoint-reference
    - user-playlists
category: api
---

Web API •References / Playlists / Change Playlist Details

## Change Playlist Details

Change a playlist's name and public/private state. (The user must, of course, own the playlist.)

## Request

- Example: `3cEYpjA9oz9GiPac4AsH4n`

supports free form additional properties

- The new name for the playlist, for example `"My New Playlist Title"`
- The playlist's public/private status (if it should be added to the user's profile or not): `true` the playlist will be public, `false` the playlist will be private, `null` the playlist status is not relevant. For more about public/private status, see [Working with Playlists](https://developer.spotify.com/documentation/web-api/concepts/playlists)
- If `true`, the playlist will become collaborative and other users will be able to modify the playlist in their Spotify client.  
  ***Note**: You can only set `collaborative` to `true` on non-public playlists.*
- Value for playlist description as displayed in Spotify Clients and in the Web API.

## Response

## Response sample

```
empty response
```