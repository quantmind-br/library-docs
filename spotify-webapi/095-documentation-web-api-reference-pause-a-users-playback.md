---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/pause-a-users-playback
source: crawler
fetched_at: 2026-02-27T23:46:46.369764-03:00
rendered_js: false
word_count: 75
summary: This document describes the Spotify Web API endpoint used to pause playback on a user's account, outlining its requirements and parameters.
tags:
    - spotify-api
    - web-api
    - playback-control
    - player-api
    - pause-playback
category: api
---

Web API •References / Player / Pause Playback

## Pause Playback

Pause playback on the user's account. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

Important policy notes

Authorization scopes

## Request

- device\_idstring
  
  The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

Playback paused