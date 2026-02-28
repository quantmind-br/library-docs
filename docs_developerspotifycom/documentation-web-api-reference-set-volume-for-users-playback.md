---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/set-volume-for-users-playback
source: crawler
fetched_at: 2026-02-27T23:38:51.777368-03:00
rendered_js: true
word_count: 89
summary: This document describes the Web API endpoint used to set the playback volume for a user's active or specified Spotify device.
tags:
    - spotify-api
    - player-api
    - playback-control
    - volume-control
    - device-management
category: api
---

Web API •References / Player / Set Playback Volume

## Set Playback Volume

Set the volume for the user’s current playback device. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The volume to set. Must be a value from 0 to 100 inclusive.
  
  Example: `volume_percent=50`
- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```
empty response
```