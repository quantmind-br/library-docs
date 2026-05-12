---
title: Network Log | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/privacy-security-and-licensing/network-log
source: sitemap
fetched_at: 2026-04-29T15:05:54.386637328-03:00
rendered_js: false
word_count: 109
summary: This document explains how to access and utilize Warp's network log to debug or monitor request and response data within a session.
tags:
    - warp-terminal
    - network-debugging
    - network-logs
    - troubleshooting
    - http-client
    - command-palette
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The network log tracks timestamped request and response objects handled by Warp's internal HTTP client, via pre-request and post-response hooks.

## How to use it

1. Select the Input in a session and open the [Command Palette](https://docs.warp.dev/terminal/command-palette), then search "Show Warp Network Log".
2. That inserts a command like `tail -f "some/path/to/warp_network.log"` into your Input editor.
3. Press Enter — requests and responses appear in the network log.

## Known issues

Traffic from crash reports and error messages is **not captured** because Warp uses the Sentry SDK, which encapsulates network logic and doesn't expose a hook for requests/responses. Disable Crash Reporting in **Settings** > **Privacy** to work around this.
