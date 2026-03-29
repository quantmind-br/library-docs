---
title: Cloudflare Polish · Cloudflare Images docs
url: https://developers.cloudflare.com/images/polish/index.md
source: llms
fetched_at: 2026-01-24T15:15:33.36735803-03:00
rendered_js: false
word_count: 194
summary: Cloudflare Polish is an automated image optimization tool that improves website performance by stripping metadata and compressing images directly in the Cloudflare cache.
tags:
    - cloudflare-polish
    - image-optimization
    - performance
    - compression
    - cache
    - image-processing
category: guide
---

Cloudflare Polish is a one-click image optimization product that automatically optimizes images in your site. Polish strips metadata from images and reduces image size through lossy or lossless compression to accelerate the speed of image downloads.

When an image is fetched from your origin, our systems automatically optimize it in Cloudflare's cache. Subsequent requests for the same image will get the smaller, faster, optimized version of the image, improving the speed of your website.

![Example of Polish compression's quality.](https://developers.cloudflare.com/_astro/polish.DBlbPZoO_GT9cH.webp)

## Comparison

* **Polish** automatically optimizes all images served from your origin server. It keeps the same image URLs, and does not require changing markup of your pages.
* **Cloudflare Images** API allows you to create new images with resizing, cropping, watermarks, and other processing applied. These images get their own new URLs, and you need to embed them on your pages to take advantage of this service. Images created this way are already optimized, and there is no need to apply Polish to them.

## Availability

| | Free | Pro | Business | Enterprise |
| - | - | - | - | - |
| Availability | No | Yes | Yes | Yes |