---
title: Web Playback SDK | Spotify for Developers
url: https://developer.spotify.com/documentation/web-playback-sdk
source: crawler
fetched_at: 2026-02-27T23:38:09.405013-03:00
rendered_js: true
word_count: 334
summary: This document introduces the Web Playback SDK, a client-side JavaScript library that enables Spotify audio streaming and playback control directly within web browsers.
tags:
    - spotify-web-playback-sdk
    - javascript-library
    - audio-streaming
    - spotify-connect
    - web-development
category: guide
---

The Web Playback SDK is a client-side only JavaScript library designed to create a local [Spotify Connect](https://developer.spotify.com/documentation/web-playback-sdk/concepts/spotify-connect) device in your browser, stream and control audio tracks from Spotify inside your website and get metadata about the current playback.

## Getting started

The Web Playback SDK is supported by most web browsers (Chrome, Firefox, Safari and Microsoft Edge) in both mobile (Android and iOS) and Desktop (macOS, Windows and Linux).

We provide a [getting started tutorial](https://developer.spotify.com/documentation/web-playback-sdk/tutorials/getting-started) to help you get started with the Web Playback SDK.

## Documentation

The documentation is organized as follows:

- Concepts that clarify key topics
- How-Tos, step-by-step guides that cover practical tasks or use cases
- Reference, the API specification

## Examples

We've provided a complete [step-by-step how-to](https://developer.spotify.com/documentation/web-playback-sdk/howtos/web-app-player) to lead you through the creation of a simple web app that makes a Spotify Player instance that can be controlled through Spotify Connect.

## Troubleshooting

- iOS support has some limitations:
  
  - The playback does not start automatically after transfering playback. The user must interact with the SDK events to play audio.
- The Web Playback SDK require iframes to allow encrypted-media and autoplay in cases of cross origin iframes. This currently affects Chrome browsers since they introduced Feature Policy which disallows features within iframes by default.
- Some users have reported issues when loading the SDK using certain browser extensions, specifically the ones related to privacy or 3rd party blockers. If you experience a similar behavior, try to temporarily disable those extensions.

## Support

If you have any questions or run into any issues while using the Spotify Web Playback SDK, you can find help in the [Spotify Developer Community](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). Here, you can connect and get help from other developers.

## Legal

This SDK must not be used in commercial projects without Spotify's prior written approval. By using Spotify developer tools, you accept our [Developer Terms of Use](https://developer.spotify.com/terms). They contain important information about what you can and can't do with our developer tools. We highly suggest getting familiar with our [Developer Policy](https://developer.spotify.com/policy) and [Complying with Spotify's developer policy](https://developer.spotify.com/compliance-tips). Please read them carefully.