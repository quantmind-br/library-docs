---
title: Overview · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/index.md
source: llms
fetched_at: 2026-01-24T15:35:46.958379073-03:00
rendered_js: false
word_count: 296
summary: RealtimeKit is a suite of SDKs and backend infrastructure designed to integrate live video and voice calling into applications using WebRTC technology. It offers tools ranging from pre-built UI components to low-level media routing via Cloudflare's global network.
tags:
    - webrtc
    - real-time-communications
    - video-sdk
    - voice-calling
    - cloudflare-network
    - sfu-architecture
category: concept
---

Add live video and voice to your web or mobile apps in minutes — customizable SDKs, Integrate in just a few lines of code.

With RealtimeKit, you can expect:

* **Fast, simple integration:** Add live video and voice calling to any platform using our SDKs in minutes.
* **Customizable:** Tailor the experience to your needs.
* **Powered by WebRTC:** Built on top of modern, battle-tested WebRTC technology. RealtimeKit sits on top of [Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) handling media track management, peer management, and other complicated tasks for you.

Experience the product:

[Try A Demo Meeting](https://demo.realtime.cloudflare.com)

[Build using Examples](https://github.com/cloudflare/realtimekit-web-examples)

[RealtimeKit Dashboard](https://dash.cloudflare.com/?to=/:account/realtime/kit)

## Build with RealtimeKit

RealtimeKit powers a wide range of usecases — here are the most common ones

#### Group Calls

Experience team meetings, virtual classrooms with interactive plugins, and seamless private or group video chats — all within your platform.

#### Webinars

Host large, interactive one-to-many events with virtual stage management, and engagement tools like plugins, chat, and polls — ideal for product demos, company all-hands, and live workshops

#### Audio Only Calls

Host audio-only calls — perfect for team discussions, support lines, and community hangouts— low bandwidth usage and features like mute controls, hand-raise, and role management.

## Product Suite

* [**UI Kit**](https://developers.cloudflare.com/realtime/realtimekit/ui-kit) UI library of pre-built, customizable components for rapid development — sits on top of the Core SDK.

* [**Core SDK**](https://developers.cloudflare.com/realtime/realtimekit/core) Client SDK built on top of Realtime SFU that provides a full set of APIs for managing video calls, from joining and leaving sessions to muting, unmuting, and toggling audio and video.

* [**Realtime SFU**](https://developers.cloudflare.com/realtime/sfu) efficiently routes media with low latency—all running on Cloudflare’s global network for reliability and scale.

The **Backend Infrastructure** Powering the SDKs is a robust layer that includes REST APIs for managing meetings, participants, recordings and more, along with webhooks for server-side events. A dedicated signalling server coordinates real-time updates.