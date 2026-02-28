---
title: iOS SDK | Spotify for Developers
url: https://developer.spotify.com/documentation/ios
source: crawler
fetched_at: 2026-02-27T23:38:09.463813-03:00
rendered_js: true
word_count: 323
summary: This document introduces the Spotify iOS SDK, outlining its core capabilities such as playback control, authentication, and offline support for iOS applications. It provides high-level information on system requirements, installation, and where to find detailed technical documentation.
tags:
    - spotify-sdk
    - ios-development
    - mobile-audio
    - user-authentication
    - playback-control
    - sdk-documentation
category: guide
---

This SDK lets you offload complexity to the main Spotify application such as: playback, authentication, networking, and offline caching. This means that you can focus on making your own user experience delightful.

## Getting started

We have a friendly [Getting Started](https://developer.spotify.com/documentation/ios/getting-started) guide which walks you through configuring your Xcode project, as well as authenticating users, connecting to the Spotify main application, and subscribing to player state changes.

To use the Spotify iOS SDK, your application will need to get the user's permission to control playback remotely first. We provide built-in support for this (as seen in the [User Authentication section of the Getting Started](https://developer.spotify.com/documentation/ios/getting-started#set-up-user-authentication)), and [additional scopes can be requested](https://developer.spotify.com/documentation/web-api/concepts/scopes) for making calls to the Spotify Web API.

In the [iOS SDK GitHub](https://github.com/spotify/ios-sdk), you will find a **Demo Projects** folder containing numerous demo applications with full source provided to help you build your first application with the iOS SDK.

### Key features

- Lightweight SDK
- Authentication
- Always-in-sync Playback (via the Spotify main application)
- Offline support *
- Built-in networking, track relinking, and caching support

\*Excludes calls to the Web API. User must initially authenticate your application, which requires an internet connection.

## Download

The latest stable version of the iOS SDK can be downloaded from [GitHub](https://github.com/spotify/ios-sdk/releases).

### Requirements

The framework requires a deployment target of iOS 12 or higher. The following architectures are supported in the SDK:

- device: arm64
- simulator: arm64 x86\_64

A physical iOS device is needed to install the Spotify app. [Learn more about building to devices](https://help.apple.com/xcode/mac/current/#/dev60b6fbbc7).

## Documentation

The documentation is organized as follows:

- Concepts that clarify key topics
- Tutorials, which serve as an introduction to important topics when using iOS SDK
- Reference, the API specification

## API documentation

The download packages include comprehensive documentation of all API classes in the `/docs` folder. You can also read the documentation [online](https://spotify.github.io/ios-sdk/html).

## Support

Please report problems with this SDK through the [public issue tracker](https://github.com/spotify/ios-sdk/issues) on GitHub.

## Legal

Note that by using Spotify iOS SDK, you accept our [Developer Terms of Service](https://developer.spotify.com/terms).