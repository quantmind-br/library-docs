---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/toggle-shuffle-for-users-playback
source: crawler
fetched_at: 2026-02-27T23:46:49.397286-03:00
rendered_js: false
word_count: 87
summary: This document explains how to use the Spotify Web API to enable or disable shuffle mode for a user's current playback session.
tags:
    - spotify-api
    - playback-control
    - shuffle-mode
    - player-api
    - endpoint-reference
category: api
---

Web API •References / Player / Toggle Playback Shuffle

## Toggle Playback Shuffle

Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- **true** : Shuffle user's playback.  
  **false** : Do not shuffle user's playback.
  
  Example: `state=true`
- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```

```