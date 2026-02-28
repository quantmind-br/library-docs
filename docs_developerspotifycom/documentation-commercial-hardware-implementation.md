---
title: Implementation | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation
source: crawler
fetched_at: 2026-02-27T23:40:48.438097-03:00
rendered_js: true
word_count: 207
summary: This document introduces the Spotify eSDK for hardware devices and outlines the essential steps for developers to integrate Spotify playback and control into their firmware.
tags:
    - spotify-esdk
    - hardware-integration
    - spotify-connect
    - embedded-sdk
    - device-playback
category: guide
---

The SDK provides a compact binary; by integrating the Spotify eSDK with the firmware of a device, you make it possible to discover and control playback on that device directly from the Spotify iOS, Android, desktop or web player app. Playback can also be controlled from your hardware companion app.

In this documentation we will cover how to get started, how to initialize the library, how to create the application and, most importantly, what to look out for.

The binary takes care of all negotiation with backend Spotify services, including digital rights management. In addition, it delivers audio as a compressed stream ready for decoding by your device. The binary runs single-threaded to keep the integration simple.

1. Download an eSDK build from Certomato under the [*Builds*](https://certomato.spotify.com/builds/) section.
2. Create an App to get a valid Client ID. You can learn how to create an App following the [App Guide](https://developer.spotify.com/documentation/web-api/concepts/apps). Please be aware that you are only allowed **ONE** Client ID per brand, and should use the existing client ID for new products.
3. Read through Implementation Guides.
4. Read through eSDK API Reference documentation.
5. Debug during development. To get fast feedback on your integration, please use our self-testing certification tool [Certomato](https://certomato.spotify.com/) during your implementation.
6. Read the [Frequently Asked Questions](https://developer.spotify.com/documentation/commercial-hardware/implementation/faqs) page.