---
title: FAQ | Walker
url: https://benz.gitbook.io/walker/faq
source: sitemap
fetched_at: 2026-02-01T13:48:40.754473188-03:00
rendered_js: false
word_count: 111
summary: This document explains common performance issues with the Walker GTK4 application and provides troubleshooting steps including background service configuration and environment variable adjustments for NVIDIA GPUs.
tags:
    - walker
    - gtk4
    - performance
    - troubleshooting
    - nvidia
    - gpu
    - service
category: guide
---

## Why is my Walker opening so slow?

Walker is a GTK4 Application with a lot of customizability. Every time you open it, there's a lot of upfront processing that has to happen. To mitigate this, you can run a background service. Read the according section.

To debug: run `walker` in a terminal and check it's output.

### Service is running and Walker is still slow to open

If you have an Nvidia GPU, try setting `GSK_RENDERER=cairo` environment variable. GTK4 uses Vulkan by default, which might cause issues with Nvidia.

### NO NVIDIA. SERVICE IS UP.

I have no idea. Open an issue with as much information as possible.

Last updated 3 months ago