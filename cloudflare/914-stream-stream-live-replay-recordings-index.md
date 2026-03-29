---
title: Record and replay live streams · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/stream-live/replay-recordings/index.md
source: llms
fetched_at: 2026-01-24T15:23:48.517300239-03:00
rendered_js: false
word_count: 40
summary: This document explains how to retrieve a list of video recordings for a specific live input using the Cloudflare Stream API.
tags:
    - cloudflare-stream
    - live-inputs
    - video-recordings
    - rest-api
    - video-management
category: api
---

Live streams are automatically recorded, and available instantly once a live stream ends. To get a list of recordings for a given input ID, make a [`GET` request to `/live_inputs/<UID>/videos`](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/get/) and filter for videos where `state` is set to `ready`:

```bash
curl -X GET \
-H "Authorization: Bearer <API_TOKEN>" \
https://dash.cloudflare.com/api/v4/accounts/<ACCOUNT_ID>/stream/live_inputs/<LIVE_INPUT_UID>/videos
```

```json
{
  "result": [
...
    {
      "uid": "6b9e68b07dfee8cc2d116e4c51d6a957",
      "thumbnail": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg",
      "thumbnailTimestampPct": 0,
      "readyToStream": true,
      "status": {
        "state": "ready",
        "pctComplete": "100.000000",
        "errorReasonCode": "",
        "errorReasonText": ""
      },
      "meta": {
        "name": "Stream Live Test 22 Sep 21 22:12 UTC"
      },
      "created": "2021-09-22T22:12:53.587306Z",
      "modified": "2021-09-23T00:14:05.591333Z",
      "size": 0,
      "preview": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch",
      "allowedOrigins": [],
      "requireSignedURLs": false,
      "uploaded": "2021-09-22T22:12:53.587288Z",
      "uploadExpiry": null,
      "maxSizeBytes": null,
      "maxDurationSeconds": null,
      "duration": 7272,
      "input": {
        "width": 640,
        "height": 360
      },
      "playback": {
        "hls": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8",
        "dash": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd"
      },
      "watermark": null,
      "liveInput": "34036a0695ab5237ce757ac53fd158a2"
    }
  ],
  "success": true,
  "errors": [],
  "messages": []
}
```