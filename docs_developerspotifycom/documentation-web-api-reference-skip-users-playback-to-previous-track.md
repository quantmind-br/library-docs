---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/skip-users-playback-to-previous-track
source: crawler
fetched_at: 2026-02-27T23:38:47.197447-03:00
rendered_js: true
word_count: 73
summary: This document describes the Skip To Previous API endpoint, which allows Spotify Premium users to skip to the previous track in their playback queue.
tags:
    - spotify-api
    - playback-control
    - player-endpoint
    - premium-feature
    - device-management
category: reference
---

Web API •References / Player / Skip To Previous

## Skip To Previous

Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```
empty response
```