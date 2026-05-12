---
title: Using Warp Offline | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/troubleshooting-and-support/using-warp-offline
source: sitemap
fetched_at: 2026-04-29T15:05:43.776780826-03:00
rendered_js: false
word_count: 88
summary: This document explains the initial setup requirements for the Warp terminal and describes how the application functions during offline versus online states.
tags:
    - warp-terminal
    - offline-access
    - cloud-features
    - user-authentication
    - network-requirements
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp's core terminal features work offline after initial setup, regardless of login status.

> [!info]
> The first launch requires an internet connection. On first open, Warp creates a unique user-ID to meter AI usage and attach cloud objects to accounts. Logged-out users are attached to an anonymous account.

Warp is "Offline" when disconnected from the internet or when calls to `app.warp.dev` are blocked on your network. There is no explicit Offline Mode.

## Cloud-based features require online access

Features requiring internet will not work offline:

#offline-access #cloud-features
