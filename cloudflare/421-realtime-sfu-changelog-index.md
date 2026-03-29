---
title: Changelog · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/changelog/index.md
source: llms
fetched_at: 2026-01-24T15:37:02.988123086-03:00
rendered_js: false
word_count: 210
summary: A chronological record of updates and feature releases for Cloudflare Realtime, focusing on SFU capabilities, WebRTC adapters, and TURN service milestones.
tags:
    - cloudflare-realtime
    - sfu
    - webrtc
    - websocket-adapter
    - changelog
    - product-updates
category: reference
---

[Subscribe to RSS](https://developers.cloudflare.com/realtime/sfu/changelog/index.xml)

## 2025-11-21

**WebSocket adapter video (JPEG) support**

Updated Media Transport Adapters (WebSocket adapter) to support video egress as JPEG frames in addition to audio.

* Stream audio and video between WebRTC tracks and WebSocket endpoints
* Video egress-only as JPEG at approximately 1 FPS for snapshots, thumbnails, and computer vision pipelines
* Clarified media formats for PCM audio and JPEG video over Protocol Buffers
* Updated docs: [Adapters](https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/), [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/websocket-adapter/)

## 2025-08-29

**Media Transport Adapters (WebSocket) open beta**

Open beta for Media Transport Adapters (WebSocket adapter) to bridge audio between WebRTC and WebSocket.

* Ingest (WebSocket → WebRTC) and Stream (WebRTC → WebSocket)
* Opus for WebRTC tracks; PCM over WebSocket via Protocol Buffers

Docs: [Adapters](https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/), [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/media-transport-adapters/websocket-adapter/)

## 2024-09-25

**TURN service is generally available (GA)**

Cloudflare Realtime TURN service is generally available and helps address common challenges with real-time communication. For more information, refer to the [blog post](https://blog.cloudflare.com/webrtc-turn-using-anycast/) or [TURN documentation](https://developers.cloudflare.com/realtime/turn/).

## 2024-04-04

**Orange Meets availability**

Orange Meets, Cloudflare's internal video conferencing app, is open source and available for use from [Github](https://github.com/cloudflare/orange?cf_target_id=40DF7321015C5928F9359DD01303E8C2).

## 2024-04-04

**Cloudflare Realtime open beta**

Cloudflare Realtime is in open beta and available from the Cloudflare Dashboard.

## 2022-09-27

**Cloudflare Realtime closed beta**

Cloudflare Realtime is available as a closed beta for users who request an invitation. Refer to the [blog post](https://blog.cloudflare.com/announcing-cloudflare-calls/) for more information.