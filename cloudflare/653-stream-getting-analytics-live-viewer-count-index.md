---
title: Get live viewer counts · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/index.md
source: llms
fetched_at: 2026-01-24T15:23:24.932425353-03:00
rendered_js: false
word_count: 46
summary: This document explains how to retrieve real-time live viewer counts for Cloudflare Stream videos using a dedicated API endpoint.
tags:
    - cloudflare-stream
    - live-streaming
    - viewer-counts
    - api-endpoint
    - video-analytics
category: reference
---

The Stream player has full support for live viewer counts by default. To get the viewer count for live videos for use with third party players, make a `GET` request to the `/views` endpoint.

```bash
https://customer-<CODE>.cloudflarestream.com/<INPUT_ID>/views
```

Below is a response for a live video with several active viewers:

```json
{ "liveViewers": 113 }
```