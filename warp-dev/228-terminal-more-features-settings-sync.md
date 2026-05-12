---
title: Settings Sync (Beta) | Warp
url: https://docs.warp.dev/terminal/more-features/settings-sync
source: sitemap
fetched_at: 2026-04-29T15:03:09.959955541-03:00
rendered_js: false
word_count: 120
summary: This document explains how the Settings Sync feature synchronizes application configurations across multiple devices and outlines which specific settings are excluded from this process.
tags:
    - settings-sync
    - cloud-configuration
    - cross-device-sync
    - user-preferences
    - warp-terminal
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## How to toggle Settings Sync

Enable or disable via **Settings** > **Account**.

## How Settings Sync works

Settings Sync syncs most Warp settings to cloud servers. After logging in on another device or via [[229-terminal-more-features-session-sharing|Session Sharing]], enabled settings persist. Themes, features, privacy, and AI settings are consistent everywhere.

On first enable, settings from that device become the default for all devices. Toggling off/on reapplies the current device's settings everywhere.

### Non-synced settings

Not all settings are synced:

- Custom themes
- Device-specific settings (e.g., preferred editor, startup shell)
- Platform-specific settings are synced across devices on the same platform (e.g., Linux clipboard settings sync across all Linux devices, not macOS/Windows/Web).

Settings with a cloud strikethrough icon are not synced.