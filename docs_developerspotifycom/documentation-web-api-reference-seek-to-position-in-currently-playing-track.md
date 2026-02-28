---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/seek-to-position-in-currently-playing-track
source: crawler
fetched_at: 2026-02-27T23:37:58.246488-03:00
rendered_js: true
word_count: 113
summary: This document describes the Spotify Web API endpoint for seeking to a specific millisecond within the currently playing track for Premium users.
tags:
    - spotify-api
    - playback-control
    - player-api
    - seek-to-position
category: reference
---

Web API •References / Player / Seek To Position

## Seek To Position

Seeks to the given position in the user’s currently playing track. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The position in milliseconds to seek to. Must be a positive number. Passing in a position that is greater than the length of the track will cause the player to start playing the next song.
  
  Example: `position_ms=25000`
- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```
empty response
```