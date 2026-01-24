---
title: Set Audio Configurations · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/index.md
source: llms
fetched_at: 2026-01-24T15:36:24.368297783-03:00
rendered_js: false
word_count: 190
summary: This document explains how to configure audio recording settings, including codec and channel selection, and describes the process for downloading recorded audio files.
tags:
    - audio-recording
    - codec-configuration
    - audio-channels
    - media-settings
    - api-parameters
category: configuration
---

Recording audio requires configuring the **codec** and **channel** parameters to guarantee optimal quality and compatibility with your application's demands. The codec determines the encoding format for the audio, and the channel specifies the number of audio channels for the recording. You can modify the following `audio_config` used for recording the audio:

## Codec

Codec determines the audio encoding format for recording, with MP3 and AAC being the supported formats.

* AAC (default)
* MP3

Note

If [VP8](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/) is selected for `video_config`, changing `audio_config` is not allowed. In this case, the codec in the `audio_config` is automatically set to `vorbis`.

## Channel

Audio signal pathway within an audio file that carries a specific sound source. The following channels are supported:

* stereo (default)
* mono

You can modify the configs by specifying it in the `audio_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:

```json
{
  "audio_config": {
    "codec": "AAC"
    "channel": "stereo"
  }
}
```

## Download Audio Files

The audio file for your recording is generated only if you passed the `audio_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `audio_download_url` provided in the response body of the [Fetch details of a recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/) to download and export the audio file.