---
title: Upload videos · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/uploading-videos/index.md
source: llms
fetched_at: 2026-01-24T15:23:57.824222444-03:00
rendered_js: false
word_count: 188
summary: This document outlines the various methods for uploading videos to Cloudflare Stream and provides technical specifications regarding supported file formats and encoding recommendations.
tags:
    - cloudflare-stream
    - video-upload
    - file-formats
    - encoding-recommendations
    - upload-methods
category: reference
---

Before you upload your video, review the options for uploading a video, supported formats, and recommendations.

## Upload options

| Upload method | When to use |
| - | - |
| [Stream Dashboard](https://dash.cloudflare.com/?to=/:account/stream) | Upload videos from the Stream Dashboard without writing any code. |
| [Upload with a link](https://developers.cloudflare.com/stream/uploading-videos/upload-via-link/) | Upload videos using a link, such as an S3 bucket or content management system. |
| [Upload video file](https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/) | Upload videos stored on a computer. |
| [Direct creator uploads](https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/) | Allows end users of your website or app to upload videos directly to Cloudflare Stream. |

## Supported video formats

Note

Files must be less than 30 GB, and content should be encoded and uploaded in the same frame rate it was recorded.

* MP4
* MKV
* MOV
* AVI
* FLV
* MPEG-2 TS
* MPEG-2 PS
* MXF
* LXF
* GXF
* 3GP
* WebM
* MPG
* Quicktime

## Recommendations for on-demand videos

* Optional but ideal settings:

  * MP4 containers
  * AAC audio codec
  * H264 video codec
  * 60 or fewer frames per second

* Closed GOP (*Only required for live streaming.*)

* Mono or Stereo audio. Stream will mix audio tracks with more than two channels down to stereo.