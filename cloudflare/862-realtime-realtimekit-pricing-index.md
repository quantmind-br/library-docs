---
title: Pricing · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:35:47.449695149-03:00
rendered_js: false
word_count: 125
summary: This document outlines the pricing structure for Cloudflare RealtimeKit, detailing per-minute costs for audio/video participants, media exports, and real-time transcription services.
tags:
    - cloudflare
    - realtimekit
    - pricing
    - billing
    - streaming
    - beta
category: reference
---

Cloudflare RealtimeKit is currently in Beta and is available at no cost during this period.

When RealtimeKit reaches general availability (GA), usage will be charged according to the pricing model below:

| Feature | Price |
| - | - |
| Audio/Video Participant | $0.002 / minute |
| Audio-Only Participant | $0.0005 / minute |
| Export (recording, RTMP or HLS streaming) | $0.010 / minute |
| Export (recording, RTMP or HLS streaming, audio only) | $0.003 / minute |
| Export (Raw RTP) into R2 | $0.0005 / minute |
| Transcription (Real-time) | Standard model pricing via Workers AI |

Whether a participant is an audio-only participant or an audio/video participant is determined by the `Meeting Type` of their [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).