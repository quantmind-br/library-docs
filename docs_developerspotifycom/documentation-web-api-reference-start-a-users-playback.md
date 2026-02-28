---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/start-a-users-playback
source: crawler
fetched_at: 2026-02-27T23:38:00.34744-03:00
rendered_js: true
word_count: 168
summary: This document describes the Spotify Web API endpoint for starting or resuming playback, detailing required parameters like device ID and playback context.
tags:
    - spotify-api
    - playback-control
    - web-api
    - player-endpoints
    - music-streaming
    - device-management
category: reference
---

Web API •References / Player / Start/Resume Playback

## Start/Resume Playback

Start a new context or resume current playback on the user's active device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

supports free form additional properties

- Optional. Spotify URI of the context to play. Valid contexts are albums, artists & playlists. `{context_uri:"spotify:album:1Je1IMUlBXcx1Fz0WE7oPT"}`
- Optional. A JSON array of the Spotify track URIs to play. For example: `{"uris": ["spotify:track:4iV5W9uYEdYUVa79Axb7Rh", "spotify:track:1301WleyT98MSxVHPZCA6M"]}`
- Optional. Indicates from where in the context playback should start. Only available when context\_uri corresponds to an album or playlist object "position" is zero based and can’t be negative. Example: `"offset": {"position": 5}` "uri" is a string representing the uri of the item to start at. Example: `"offset": {"uri": "spotify:track:1301WleyT98MSxVHPZCA6M"}`
  
  supports free form additional properties

## Response

## Response sample

```
empty response
```