---
title: aquamarine
url: https://wiki.hypr.land/Hypr-Ecosystem/aquamarine/
source: sitemap
fetched_at: 2026-04-26T09:49:46.524023655-03:00
rendered_js: false
word_count: 105
summary: This document provides an overview of the Aquamarine library, a lightweight rendering backend for Linux, including instructions for configuring it via environment variables.
tags:
    - linux
    - rendering-backend
    - wayland
    - drm
    - kms
    - environment-variables
    - hyprland
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# aquamarine

[aquamarine](https://github.com/hyprwm/aquamarine) is a lightweight Linux rendering backend library. It is not a replacement or competitor to wlroots or libweston — it implements only low-level KMS/DRM rendering backends.

Configuration is passed via environment variables prefixed with `AQ_` to an app using aquamarine (e.g. Hyprland).

## Variables

| Variable | Description |
|----------|-------------|
| `AQ_TRACE` | Enables trace (very verbose) logging. |
| `AQ_DRM_DEVICES` | Colon-separated list of DRM devices (GPUs). First is primary. Example: `/dev/dri/card1:/dev/dri/card0`. |
| `AQ_NO_MODIFIERS` | Disables modifiers for DRM buffers. |
| `AQ_MGPU_NO_EXPLICIT` | Disables passing of explicit fences for multi-gpu scanouts. |
| `AQ_NO_ATOMIC` | **(HEAVILY NOT RECOMMENDED)** Disables atomic modesetting. |

#rendering-backend #wayland #drm