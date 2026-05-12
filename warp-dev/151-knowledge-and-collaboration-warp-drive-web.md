---
title: Warp Drive on the web | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/web
source: sitemap
fetched_at: 2026-04-29T15:03:34.112724913-03:00
rendered_js: false
word_count: 306
summary: This document explains how to access, view, and manage Warp Drive objects and shared sessions directly within a web browser, including configuration options for switching between web and desktop interfaces.
tags:
    - warp-drive
    - web-interface
    - session-sharing
    - browser-compatibility
    - workflow-management
    - link-redirection
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp Drive on the Web lets you view and edit Warp Drive objects and shared sessions directly in the browser, on any device.

> [!info]
> You can edit and view objects and sessions normally on the web. The exception is executing a command from a workflow or notebook — there is no shell session running on the web.

## Access Warp on the web

> [!warning]
> The desktop option is only presented if Warp's web service detects the desktop app installed locally (opens localhost port 9277). If Warp is not installed, you will be prompted to download it on first link follow.

## Manage view preferences (web vs desktop)

Configure whether Warp links open in the desktop app or browser:

1. **First link follow:** If Warp is not installed, a popup prompts you to download or dismiss to stay on the web.
2. **Settings:** On the web version, go to **Settings** → **Features** → **General** → **Open links in desktop app**.
3. **Per-object switch:**
   - Web → Desktop: open the *overflow menu → Open link on Desktop*
   - Desktop → Web: click *View on the web* on the redirect screen

## Supported browsers

**Desktop:** Chrome, Firefox, Safari

**Mobile:**
- iOS Safari 15+
- Android Chrome 58+
- Samsung Internet 7.2+

> [!info]
> Mobile minimums are required for WebGL 2.0 support. Most up-to-date devices meet these requirements.

## Touch screen and mobile support

Touch input works on both the web and desktop app.

| Gesture | Action |
|---|---|
| Touch and scroll | Vertical and horizontal scrolling |
| Double tap | Select text or elements |
| Long press | Open context menu (equivalent to right-click) |

## Related features

- [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) — workflows, prompts, and environment variables
- [Session Sharing](https://docs.warp.dev/knowledge-and-collaboration/session-sharing) — real-time terminal collaboration

#warp-drive #web-interface #session-sharing #browser-compatibility #workflow-management #link-redirection
