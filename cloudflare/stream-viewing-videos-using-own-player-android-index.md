---
title: Android · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/index.md
source: llms
fetched_at: 2026-01-24T15:24:09.11253709-03:00
rendered_js: false
word_count: 50
summary: This document provides instructions and code examples for streaming on-demand and live video from Cloudflare Stream to native Android applications using the ExoPlayer library.
tags:
    - cloudflare-stream
    - android
    - exoplayer
    - video-streaming
    - hls-playback
    - mobile-development
category: guide
---

You can stream both on-demand and live video to native Android apps using [ExoPlayer](https://exoplayer.dev/).

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)

## Example Apps

* [Android](https://developers.cloudflare.com/stream/examples/android/)

## Using ExoPlayer

Play a video from Cloudflare Stream using ExoPlayer:

```kotlin
implementation 'com.google.android.exoplayer:exoplayer-hls:2.X.X'


SimpleExoPlayer player = new SimpleExoPlayer.Builder(context).build();


// Set the media item to the Cloudflare Stream HLS Manifest URL:
player.setMediaItem(MediaItem.fromUri("https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8"));


player.prepare();
```