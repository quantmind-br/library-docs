---
title: Upload images · Cloudflare Images docs
url: https://developers.cloudflare.com/images/upload-images/index.md
source: llms
fetched_at: 2026-01-24T15:15:52.867510049-03:00
rendered_js: false
word_count: 140
summary: This document outlines the supported image formats and technical limitations for uploading files to Cloudflare Images, including dimension and file size constraints.
tags:
    - cloudflare-images
    - image-upload
    - file-formats
    - upload-limits
    - image-specifications
category: reference
---

Cloudflare Images allows developers to upload images using different methods, for a wide range of use cases.

## Supported image formats

You can upload the following image formats to Cloudflare Images:

* PNG
* GIF (including animations)
* JPEG
* WebP (Cloudflare Images also supports uploading animated WebP files)
* SVG
* HEIC

Note

Cloudflare can ingest HEIC images for decoding, but they must be served in web-safe formats such as AVIF, WebP, JPG, or PNG.

## Dimensions and sizes

These are the maximum allowed sizes and dimensions when uploading to Images:

* Maximum image dimension is 12,000 pixels.
* Maximum image area is limited to 100 megapixels (for example, 10,000×10,000 pixels).
* Image metadata is limited to 1024 bytes (when uploaded and stored in Cloudflare).
* Images have a 10 megabyte (MB) size limit (when uploaded and stored in Cloudflare).
* Animated GIFs/WebP, including all frames, are limited to 50 megapixels (MP).