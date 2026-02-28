---
title: Web API Reference | Spotify for Developers
url: https://developer.spotify.com/documentation/web-api/reference/transfer-a-users-playback
source: crawler
fetched_at: 2026-02-27T23:46:45.84125-03:00
rendered_js: false
word_count: 114
summary: This document describes the Spotify Web API endpoint for transferring audio playback to a specific device for users with a Premium subscription.
tags:
    - spotify-api
    - player-api
    - playback-transfer
    - device-management
    - web-api
category: api
---

Web API •References / Player / Transfer Playback

## Transfer Playback

Transfer playback to a new device and optionally begin playback. This API only works for users who have Spotify Premium. The order of execution is not guaranteed when you use this API with other Player API endpoints.

## Request

supports free form additional properties

- device\_idsarray of strings
  
  A JSON array containing the ID of the device on which playback should be started/transferred.  
  For example:`{device_ids:["74ASZWbe4lXaubB36ztrGX"]}`  
  ***Note**: Although an array is accepted, only a single device\_id is currently supported. Supplying more than one will return `400 Bad Request`*
- **true**: ensure playback happens on new device.  
  **false** or not provided: keep the current playback state.

## Response

## Response sample

```

```