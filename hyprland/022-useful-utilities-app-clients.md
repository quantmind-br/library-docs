---
title: App clients
url: https://wiki.hypr.land/Useful-Utilities/App-Clients/
source: sitemap
fetched_at: 2026-04-26T09:48:12.733540684-03:00
rendered_js: false
word_count: 198
summary: This document lists recommended Wayland-compatible replacements for common communication applications that struggle with native Wayland support.
tags:
    - wayland
    - linux-desktop
    - software-alternatives
    - discord-clients
    - matrix-clients
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

# App clients

Wayland-native replacements for communication apps that typically struggle under Wayland.

## Discord

| Client | Type | Wayland Support | Screen Sharing | Notes |
|--------|------|-----------------|----------------|-------|
| [WebCord](https://github.com/SpacingBat3/WebCord) | Electron (Ozone) | Yes | PipeWire | Tries to respect Discord ToS |
| [Vesktop](https://github.com/Vencord/Vesktop) | Electron + Vencord | Yes | Built-in + audio sharing | Uses Vencord mod; violates Discord ToS |
| [dissent](https://github.com/diamondburned/dissent) | GTK4 | Yes | Via XWayland bridge | No webview; violates Discord ToS |

> [!warning]
> WebCord is the only Discord client that attempts to respect Discord's Terms of Service. Vesktop and dissent use mods that violate ToS.

## Matrix/Element

| Client | Framework | E2EE | Cross-device Verification | VoIP |
|--------|-----------|------|---------------------------|------|
| [Fractal](https://wiki.gnome.org/Apps/Fractal) | GTK4 | Yes | Yes | No |

Fractal is a GTK4 Matrix client. Unlike Electron-based Element, it has no webview dependencies. All features work except VoIP calling.

Last updated on April 20, 2026

[[078-useful-utilities-app-launchers|App launchers]] [[024-useful-utilities-color-pickers|Color pickers]]