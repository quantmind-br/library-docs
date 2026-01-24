---
title: Configure Video Settings · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/index.md
source: llms
fetched_at: 2026-01-24T15:36:24.544443731-03:00
rendered_js: false
word_count: 167
summary: This document explains how to configure video codecs and download recorded video files using the recording API.
tags:
    - video-codecs
    - h264
    - vp8
    - video-recording
    - api-configuration
    - video-download
category: configuration
---

Video codecs are software programs that compress and decompress digital video data for transmission, storage, or playback. Configuring the appropriate video codec can help reduce file size, enhance video quality, and ensure compatibility with different playback devices.

## Configure Codecs

You can modify the codec which is used for recording the videos. We currently support the following codecs:

* **H264 (default)**: Records video using the H.264 codec with 1280px × 720px resolution, and 384 kbps AAC audio in MP4 container.
* **VP8**: Records video using the VP8 codec with 1280px × 720px resolution, and Vorbis codec audio in WebM container.

You can change the codec by specifying the codec in the `video_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:

```json
{
  "video_config": {
    "codec": "H264"
  }
}
```

## Download Video Files

The video file for your recording is generated only if you passed the `video_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `downloadUrl` provided in the response body of the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/) to download and export the video file.