---
title: Add Watermark · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/index.md
source: llms
fetched_at: 2026-01-24T15:36:23.131209684-03:00
rendered_js: false
word_count: 98
summary: This document explains how to configure and customize an image watermark for video recordings using the RealtimeKit Start Recording API.
tags:
    - realtime-kit
    - video-recording
    - watermark
    - api-configuration
    - video-settings
category: configuration
---

RealtimeKit's watermark feature enables you to include an image as a watermark in your recording. To add watermark, configure the following parameters to video\_config in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

| **Parameter** | **Description** |
| - | - |
| URL | Specify the URL of the watermark image |
| Position | Specify the placement of the watermark, you have the flexibility to choose between left top, right top, left bottom, or right bottom. The default position is set to left top. |
| Size | Specify the height and width of the watermark in pixels. |

```json
{
  "video_config": {
    "watermark": {
      "url": "https://test.io/images/client-logos-6.webp",
      "position": "left top",
      "size": {
        "height": 20,
        "width": 100
      }
    }
  }
}
```