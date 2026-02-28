---
title: Spotify Connect | Spotify for Developers
url: https://developer.spotify.com/documentation/web-playback-sdk/concepts/spotify-connect
source: crawler
fetched_at: 2026-02-27T23:40:15.001985-03:00
rendered_js: true
word_count: 78
summary: This document introduces Spotify Connect and explains how the Web Playback SDK enables developers to integrate Spotify playback functionality directly into their web applications.
tags:
    - spotify-connect
    - web-playback-sdk
    - audio-streaming
    - remote-control
    - device-casting
category: concept
---

Spotify Connect is a feature on Spotify that allows users to use Spotify clients as a remote and cast content to [different devices](https://spotify-everywhere.com/), such as smart speakers, game consoles, TVs, or wearables.

All devices must be connected to the same network. Once connected they will appear under the device icon of the Spotify app:

![Spotify Connect](https://developer-assets.spotifycdn.com/images/documentation/web-playback-sdk/spotify_connect.png)

The Web Playback SDK allows to create a new player instance in Spotify Connect and play audio from Spotify inside your application.