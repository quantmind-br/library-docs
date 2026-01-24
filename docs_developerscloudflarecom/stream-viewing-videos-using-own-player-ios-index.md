---
title: iOS · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/index.md
source: llms
fetched_at: 2026-01-24T15:24:13.088672247-03:00
rendered_js: false
word_count: 53
summary: This document provides instructions and code examples for streaming on-demand and live video from Cloudflare Stream to native iOS, tvOS, and macOS applications using the AVPlayer framework. It includes a Swift implementation for embedding a video player within a SwiftUI view.
tags:
    - cloudflare-stream
    - avplayer
    - ios-development
    - video-playback
    - swift
    - hls-streaming
category: guide
---

You can stream both on-demand and live video to native iOS, tvOS and macOS apps using [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer).

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)

## Example Apps

* [iOS](https://developers.cloudflare.com/stream/examples/ios/)

## Using AVPlayer

Play a video from Cloudflare Stream using AVPlayer:

```swift
import SwiftUI
import AVKit


struct MyView: View {
    // Change the url to the Cloudflare Stream HLS manifest URL
    private let player = AVPlayer(url: URL(string: "https://customer-9cbb9x7nxdw5hb57.cloudflarestream.com/8f92fe7d2c1c0983767649e065e691fc/manifest/video.m3u8")!)


    var body: some View {
        VideoPlayer(player: player)
            .onAppear() {
                player.play()
            }
    }
}


struct MyView_Previews: PreviewProvider {
    static var previews: some View {
        MyView()
    }
}
```