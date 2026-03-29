---
title: Export images · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/export-images/index.md
source: llms
fetched_at: 2026-01-24T15:15:25.968662258-03:00
rendered_js: false
word_count: 110
summary: This document explains how to export original images from Cloudflare Images using both the dashboard interface and the API.
tags:
    - cloudflare-images
    - image-export
    - api-request
    - dashboard-navigation
    - image-retrieval
category: guide
---

Cloudflare Images supports image exports via the Cloudflare dashboard and API which allows you to get the original version of your image.

## Export images via the Cloudflare dashboard

1. In the Cloudflare dashboard, go to the **Transformations** page.

   [Go to **Transformations**](https://dash.cloudflare.com/?to=/:account/images/transformations)

2. Find the image or images you want to export.

3. To export a single image, select **Export** from its menu. To export several images, select the checkbox next to each image and then select **Export selected**.

Your images are downloaded to your machine.

## Export images via the API

Make a `GET` request as shown in the example below. `<IMAGE_ID>` must be fully URL encoded in the API call URL.

`GET accounts/<ACCOUNT_ID>/images/v1/<IMAGE_ID>/blob`