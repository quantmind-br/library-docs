---
title: Spotify Android SDK | Spotify for Developers
url: https://developer.spotify.com/documentation/android
source: crawler
fetched_at: 2026-02-27T23:38:11.329428-03:00
rendered_js: true
word_count: 566
summary: This document provides an overview of the Spotify Android SDK, covering its core components for app authorization and playback control alongside technical requirements and setup resources.
tags:
    - spotify-android-sdk
    - app-remote
    - authorization-library
    - mobile-playback
    - android-development
category: guide
---

The Spotify Android SDK supports getting metadata for the currently playing track and context, issuing basic playback commands as well as initiating playback of tracks.

## Getting started

The SDK consists of two libraries:

- **Authorization Library**. This library is responsible for authorizing your app and fetching the access token that later can be used to send requests to the Spotify Web API.
- **App Remote Library**. The app remote module allows you to control playback in the Spotify app after user logs in with the access token.

![Spotify Android SDK](https://developer-assets.spotifycdn.com/images/documentation/android/ipc.png)

We provide a [Getting Started tutorial](https://developer.spotify.com/documentation/android/tutorials/getting-started) to help you set up your build environment and get started with the Spotify Android SDK.

The tutorial leads you through the creation of a simple app that connects to the Spotify app, plays a playlist and subscribes to PlayerState. Within the download package you will also find a demo app with full source code to help get you started.

In order to use the SDK, your application will need to get the user's permission to control playback remotely first. The [authorization](https://developer.spotify.com/documentation/android/tutorials/authorization) guide explains the two methods available to implement authorization in your Android application.

### Key features

- Lightweight library (less than 300k). No native code or processor architecture dependencies
- Playback always in sync with Spotify app
- Processing of playback and caching as well as network traffic is accounted for by the Spotify app
- Handles system integration such as audio focus, lockscreen controls and incoming calls
- Automatically handles track relinking for different regions
- Works offline and online and does not require Web API calls to get metadata for player state

## Download

The latest stable version of the Android SDK can be downloaded from [GitHub](https://github.com/spotify/android-sdk/releases).

### Requirements

- Minimum Android SDK Version 14
- Gson (version 2.6.1)

## Documentation

The documentation is organized as follows:

- Concepts that clarify key topics
- Tutorials, which serve as an introduction to important topics when using Android SDK
- Reference, the API specification

## API documentation

The download packages includes comprehensive documentation of all API classes in the `/docs` folder. You can also read the documentation online for the [authentication library](https://spotify.github.io/android-sdk/auth-lib/docs/index.html) and for the [app remote library](https://spotify.github.io/android-sdk/app-remote-lib/docs/index.html).

## Frequently asked questions

### SpotifyAppRemote connect/disconnect v0.4.0 vs v0.5.0

`1`

`// If your code looks like this for v0.4.0:`

`2`

`SpotifyAppRemote.CONNECTOR.disconnect(mSpotifyAppRemote);`

`3`

`SpotifyAppRemote.CONNECTOR.connect(this, mConnectionParams, mConnectionListener);`

`4`

`// you should change it to this as of v0.5.0:`

`5`

`SpotifyAppRemote.disconnect(mSpotifyAppRemote);`

`6`

`SpotifyAppRemote.connect(this, mConnectionParams, mConnectionListener);`

### I want the Spotify app to notify my app when Spotify is active. Is it possible?

You can register a broadcast receiver for an action "com.spotify.music.active". The broadcast is sent when a new track gets on top of the playing queue.

To listen to the broadcast add the next lines to your AndroidManifest.xml file:

`1`

`<receiver android:name="<ReceiverClassName>">`

`2`

`<intent-filter>`

`3`

`<action android:name="com.spotify.music.active"/>`

`4`

`</intent-filter>`

`5`

`</receiver>`

To get more information on BroadcastReceivers, have a look at [the docs](https://developer.android.com/reference/android/content/BroadcastReceiver.html) on the Android developer portal.

### Can I use Jackson instead of Gson?

Since version 0.2.0 of the SDK, [Gson](https://github.com/google/gson) is used by default for serializing  and deserializing the request, but the use of [Jackson](https://github.com/FasterXML/jackson) is still supported. If you want to use Jackson, you need to configure it when connecting to Spotify:

`1`

`ConnectionParams connectionParams =`

`2`

`new ConnectionParams.Builder(CLIENT_ID)`

`3`

`.setRedirectUri(REDIRECT_URI)`

`4`

`.setJsonMapper(JacksonMapper.create())`

`5`

`.build();`

`6`

`7`

`SpotifyAppRemote.connect(this, connectionParams, connectionListener);`

## Support

Please report problems with this SDK through the [public issue tracker](https://github.com/spotify/android-sdk/issues) on GitHub.

## Legal

Note that by using Spotify Android SDK, you accept our [Developer Terms of Service](https://developer.spotify.com/terms).