---
title: Media Acquisition Approaches · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/media-acquisition-approaches/index.md
source: llms
fetched_at: 2026-01-24T15:36:13.688158825-03:00
rendered_js: false
word_count: 54
summary: This guide explains the different methods for acquiring and managing participant audio and video tracks within the RealtimeKit SDK, covering both automatic and manual approaches.
tags:
    - realtimekit
    - media-acquisition
    - audio-tracks
    - video-tracks
    - sdk-initialization
category: guide
---

Note

This guide assumes that you are already familiar with [initializing the RealtimeKit SDK](https://developers.cloudflare.com/realtime/realtimekit/core/).

RealtimeKit provides flexible approaches for acquiring and managing participant media (audio and video tracks). By default, the SDK handles media acquisition automatically when you initialize it. However, certain use cases require accessing media tracks before or independently of SDK initialization.