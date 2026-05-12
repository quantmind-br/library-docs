---
title: "Warp for Linux"
url: https://docs.warp.dev/terminal/more-features/linux
source: sitemap
fetched_at: 2026-04-29T15:03:12-03:00
rendered_js: false
word_count: 105
summary: This document explains how to enable native Wayland support in Warp, its impact on global hotkeys, and the automated crash recovery mechanism that falls back to X11.
tags:
    - wayland
    - linux-support
    - configuration
    - window-manager
    - crash-recovery
    - x11
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Warp for Linux

## Native Wayland

Warp Wayland support can be enabled in **Settings** > **Features** > **System**. Enabling Wayland support may fix issues with blurry text if you have fractional scaling enabled in your window manager.

> [!warning]
> When native Wayland is enabled, Global Hotkey support will be disabled. The Wayland protocol does not expose the configuration necessary to support this feature.

## Wayland crash recovery

When Wayland support is enabled, Warp uses a custom crash recovery process to detect any crashes. If a crash occurs, Warp falls back to X11 so you can continue using the application.

#terminal #wayland #linux-support #crash-recovery
