---
title: Download live stream videos · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/stream-live/download-stream-live-videos/index.md
source: llms
fetched_at: 2026-01-24T15:23:46.153539001-03:00
rendered_js: false
word_count: 127
summary: This document provides step-by-step instructions for enabling and downloading MP4 versions of live stream recordings through the Cloudflare dashboard.
tags:
    - cloudflare-stream
    - video-downloads
    - live-input
    - mp4
    - video-management
category: guide
---

You can enable downloads for live stream videos from the Cloudflare dashboard. Videos are available for download after they enter the **Ready** state.

Note

Downloadable MP4s are only available for live recordings under four hours. Live recordings exceeding four hours can be played at a later time but cannot be downloaded as an MP4.

1. In the Cloudflare dashboard, go to the **Live inputs** page.

   [Go to **Live inputs**](https://dash.cloudflare.com/?to=/:account/stream/inputs)

2. Select a live input from the list.

3. Under **Videos created by live input**, select your video.

4. Under **Settings**, select **Enable MP4 Downloads**.

5. Select **Save**. You will see a progress bar as the video generates a download link.

6. When the download link is ready, under **Download URL**, copy the URL and enter it in a browser to download the video.