---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/set-repeat-mode-on-users-playback
source: crawler
fetched_at: 2026-02-27T23:46:47.983369-03:00
rendered_js: false
word_count: 96
summary: Technical documentation for the Spotify Web API endpoint that allows users with Premium accounts to set the repeat mode for their current playback session.
tags:
    - spotify-api
    - player-api
    - playback-control
    - repeat-mode
    - endpoint-reference
category: api
---

Web API •References / Player / Set Repeat Mode

## Set Repeat Mode

Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- **track**, **context** or **off**.  
  **track** will repeat the current track.  
  **context** will repeat the current context.  
  **off** will turn repeat off.
  
  Example: `state=context`
- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```

```