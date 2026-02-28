---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/pause-a-users-playback
source: crawler
fetched_at: 2026-02-27T23:38:47.316949-03:00
rendered_js: true
word_count: 69
summary: This document describes the Spotify Web API endpoint used to pause audio playback on a user's active or specified device.
tags:
    - spotify-api
    - playback-control
    - pause-playback
    - player-api
    - media-streaming
category: api
---

Web API •References / Player / Pause Playback

## Pause Playback

Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```
empty response
```