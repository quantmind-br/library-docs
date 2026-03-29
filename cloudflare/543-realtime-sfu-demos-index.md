---
title: Demos · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/demos/index.md
source: llms
fetched_at: 2026-01-24T15:37:05.216213354-03:00
rendered_js: false
word_count: 135
summary: A collection of demo applications and interactive visualizations designed to showcase the capabilities and implementation of Cloudflare Realtime in WebRTC and SFU environments.
tags:
    - cloudflare-realtime
    - webrtc
    - sfu-architecture
    - demo-applications
    - whip-whep
    - datachannels
category: guide
---

Learn how you can use Realtime within your existing architecture.

## Demos

Explore the following demo applications for Realtime.

* [Realtime Echo Demo:](https://github.com/cloudflare/calls-examples/tree/main/echo) Demonstrates a local stream alongside a remote echo stream.
* [Orange Meets:](https://github.com/cloudflare/orange) Orange Meets is a demo WebRTC application built using Cloudflare Realtime.
* [WHIP-WHEP Server:](https://github.com/cloudflare/calls-examples/tree/main/whip-whep-server) WHIP and WHEP server implemented on top of Realtime API.
* [Realtime DataChannel Test:](https://github.com/cloudflare/calls-examples/tree/main/echo-datachannels) This example establishes two datachannels, one publishes data and the other one subscribes, the test measures how fast a message travels to and from the server.

## Interactive Demos

### Global SFU Network Visualization

An interactive visualization showing how Realtime uses Cloudflare's global network as a distributed SFU. Click anywhere on the map to add participants and watch them connect to their nearest datacenter via anycast routing, with media tracks flowing along Cloudflare's private backbone.

[View Global SFU Visualization](https://realtime-sfu.dev-demos.workers.dev)