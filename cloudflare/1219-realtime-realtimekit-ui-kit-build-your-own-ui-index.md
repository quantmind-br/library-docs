---
title: Build Your Own UI · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/index.md
source: llms
fetched_at: 2026-01-24T15:36:51.005395237-03:00
rendered_js: false
word_count: 144
summary: This guide explains how to build custom real-time video user interfaces using Cloudflare RealtimeKit's UI Kit components and SDK.
tags:
    - cloudflare-realtimekit
    - video-conferencing
    - ui-customization
    - frontend-sdk
    - real-time-communication
category: guide
---

This guide explains how to use Cloudflare RealtimeKit SDKs to build fully custom real-time video UIs.

## Prerequisites

This page builds upon the [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Render Default Meeting UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/) & [UI Kit States](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/state-management/) guides. Make sure you've read those first.

The code examples on this page assume you've already imported the necessary packages and initialized the SDK. We won't repeat those setup steps here for brevity.

## Building Your Own UI, With UI Kit

If default meeting component is not enough, and you need more control over layout or behavior, use [UI Kit components](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/component-library/) to build a custom interface. The UI Kit provides pre-built components that sit on top of the Core SDK, letting you mix and match pieces while saving time compared to building from scratch.

Building a custom UI requires managing participant audio, notifications, dialogs, component layout, and screen transitions yourself.

## Example Code