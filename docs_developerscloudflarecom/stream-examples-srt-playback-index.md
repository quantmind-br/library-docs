---
title: SRT playback
url: https://developers.cloudflare.com/stream/examples/srt_playback/index.md
source: llms
fetched_at: 2026-01-24T15:23:34.477522571-03:00
rendered_js: false
word_count: 97
summary: This document provides instructions and a command-line example for achieving low-latency live video playback using the SRT protocol and ffplay.
tags:
    - srt-playback
    - low-latency
    - cloudflare-stream
    - live-video
    - ffplay
category: tutorial
---

---
title: SRT playback · Cloudflare Stream docs
description: Example of sub 1s latency video playback using SRT and ffplay
lastUpdated: 2025-09-09T16:21:39.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/srt_playback/
  md: https://developers.cloudflare.com/stream/examples/srt_playback/index.md
---

Note

Before you can play live video, you must first be [actively streaming to a live input](https://developers.cloudflare.com/stream/stream-live/start-stream-live).

Copy the SRT Playback URL for your live input from either:

* The **Live inputs** page of the Cloudflare dashboard.

  [Go to **Live inputs**](https://dash.cloudflare.com/?to=/:account/stream/inputs)

* The [Stream API](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#use-the-api)

Paste it into the URL below, replacing `<SRT_PLAYBACK_URL>`:

```sh
ffplay -analyzeduration 1 -fflags -nobuffer -probesize 32 -sync ext '<SRT_PLAYBACK_URL>'
```

For more, refer to [Play live video in native apps with less than one second latency](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/#play-live-video-in-native-apps-with-less-than-1-second-latency).