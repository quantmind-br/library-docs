---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/skip-users-playback-to-next-track
source: crawler
fetched_at: 2026-02-27T23:46:47.652572-03:00
rendered_js: false
word_count: 79
summary: This document describes the Web API endpoint used to skip to the next track in a user's Spotify playback queue.
tags:
    - spotify-api
    - player-api
    - playback-control
    - music-streaming
    - endpoint-reference
category: api
---

Web API •References / Player / Skip To Next

## Skip To Next

Skips to next track in the user’s queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

Important policy notes

Authorization scopes

## Request

- device\_idstring
  
  The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

Command sent