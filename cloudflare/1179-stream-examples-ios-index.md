---
title: iOS (AVPlayer)
url: https://developers.cloudflare.com/stream/examples/ios/index.md
source: llms
fetched_at: 2026-01-24T15:23:31.073275421-03:00
rendered_js: false
word_count: 124
summary: This document provides a code example and instructions for playing Cloudflare Stream videos on iOS using the native AVPlayer and AVKit frameworks.
tags:
    - ios
    - avplayer
    - cloudflare-stream
    - video-playback
    - swiftui
    - hls
    - mobile-development
category: tutorial
---

---
title: iOS (AVPlayer) · Cloudflare Stream docs
description: Example of video playback on iOS using AVPlayer
lastUpdated: 2025-08-20T20:59:04.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/ios/
  md: https://developers.cloudflare.com/stream/examples/ios/index.md
---

Note

Before you can play videos, you must first [upload a video to Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/) or be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live)

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

### Download and run an example app

1. Download [this example app](https://developer.apple.com/documentation/avfoundation/offline_playback_and_storage/using_avfoundation_to_play_and_persist_http_live_streams) from Apple's developer docs
2. Open and run the app using [Xcode](https://developer.apple.com/xcode/).
3. Search in Xcode for `m3u8`, and open the `Streams` file
4. Replace the value of `playlist_url` with the HLS manifest URL for your video.

![Screenshot of a video with Cloudflare watermark at top right](https://developers.cloudflare.com/_astro/ios-example-screenshot-edit-hls-url.CK2bGBBG_Z1npgqh.webp)

1. Click the Play button in Xcode to run the app, and play your video.

For more, see [read the docs](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/).