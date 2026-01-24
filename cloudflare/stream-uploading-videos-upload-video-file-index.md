---
title: Basic video uploads · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/index.md
source: llms
fetched_at: 2026-01-24T15:24:03.037295954-03:00
rendered_js: false
word_count: 113
summary: This document explains how to upload videos smaller than 200 MB to Cloudflare Stream using either the dashboard interface or the Stream API.
tags:
    - cloudflare-stream
    - video-upload
    - multipart-form-data
    - stream-api
    - dashboard-upload
category: tutorial
---

## Basic Uploads

For files smaller than 200 MB, you can use simple form-based uploads.

## Upload through the Cloudflare dashboard

1. In the Cloudflare dashboard, go to the **Stream** page.

   [Go to **Videos**](https://dash.cloudflare.com/?to=/:account/stream/videos)

2. Drag and drop your video into the **Quick upload** area. You can also click to browse for the file on your machine.

After the video finishes uploading, the video appears in the list.

## Upload with the Stream API

Make a `POST` request with the `content-type` header set to `multipart/form-data` and include the media as an input with the name set to `file`.

```bash
curl --request POST \
--header "Authorization: Bearer <API_TOKEN>" \
--form file=@/Users/user_name/Desktop/my-video.mp4 \
https://api.cloudflare.com/client/v4/accounts/{account_id}/stream
```

Note

Note that cURL's `--form` flag automatically configures the `content-type` header and maps `my-video.mp4` to a form input called `file`.