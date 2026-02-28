---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/add-to-queue
source: crawler
fetched_at: 2026-02-27T23:38:49.50469-03:00
rendered_js: true
word_count: 102
summary: This document describes the Spotify Web API endpoint used to add a specific track or podcast episode to the end of a user's current playback queue.
tags:
    - spotify-api
    - playback-queue
    - player-endpoints
    - audio-streaming
    - endpoint-reference
category: api
---

Web API •References / Player / Add Item to Playback Queue

## Add Item to Playback Queue

Add an item to be played next in the user's current playback queue. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

- The uri of the item to add to the queue. Must be a track or an episode uri.
  
  Example: `uri=spotify%3Atrack%3A4iV5W9uYEdYUVa79Axb7Rh`
- The id of the device this command is targeting. If not supplied, the user's currently active device is the target.
  
  Example: `device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8`

## Response

## Response sample

```
empty response
```