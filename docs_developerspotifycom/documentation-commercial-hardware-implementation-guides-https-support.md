---
title: HTTPs Support | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/https-support
source: crawler
fetched_at: 2026-02-27T23:41:25.444132-03:00
rendered_js: true
word_count: 113
summary: This document outlines the requirements for HTTPS support in the Spotify eSDK and provides guidance on implementing the TLS stack using provided abstractions and libraries.
tags:
    - spotify-esdk
    - https-support
    - tls-implementation
    - mbedtls
    - openssl
    - cmake-configuration
category: guide
---

HTTPS support is required in order to provide:

- Playback of podcasts hosted outside Spotify
- Playback of lossless audio
- User privacy
- Future use of modern protocols for eSDK to Spotify backend communication.

Note: eSDK has a software abstraction for the TLS stack that the integration must use to implement the full HTTPS stack.  
Please refer to `spotify_embedded_tls.h` for more detail on the APIs to implement.

There are also example implementations using MbedTLS and OpenSSL under examples/tls.

If you are building with cmake we include a minimal FindMbedTLS under examples (as there is no official one provided), which can be used as `find_package(MbedTLS)`.  
For OpenSSL, `find_package(OpenSSL)` is enough provided you have the development package installed.