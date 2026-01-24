---
title: Example architecture · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/example-architecture/index.md
source: llms
fetched_at: 2026-01-24T15:37:07.351137563-03:00
rendered_js: false
word_count: 78
summary: This document outlines the architectural flow and integration steps for building a video calling application using the Cloudflare Realtime API and WebRTC.
tags:
    - cloudflare-realtime-api
    - webrtc
    - video-calling
    - architecture
    - real-time-communication
category: concept
---

![Example Architecture](https://developers.cloudflare.com/_astro/video-calling-application.CIYa-lzM_e7Gu.webp)

1. Clients connect to the backend service
2. Backend service manages the relationship between the clients and the tracks they should subscribe to
3. Backend service contacts the Cloudflare Realtime API to pass the SDP from the clients to establish the WebRTC connection.
4. Realtime API relays back the Realtime API SDP reply and renegotiation messages.
5. If desired, headless clients can be used to record the content from other clients or publish content.
6. Admin manages the rooms and room members.