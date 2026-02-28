---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/toggle-shuffle-for-users-playback
source: crawler
fetched_at: 2026-02-27T23:38:48.348416-03:00
rendered_js: true
word_count: 87
summary: This document provides technical details for the Spotify Web API endpoint used to toggle the shuffle state of a user's playback. It outlines the required parameters, such as the shuffle state and device ID, and notes the necessity of a Premium subscription.
tags:
    - spotify-api
    - playback-control
    - shuffle-mode
    - web-api
    - player-endpoint
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
empty response
```