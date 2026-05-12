---
title: Warp URI scheme | Warp
url: https://docs.warp.dev/terminal/more-features/uri-scheme
source: sitemap
fetched_at: 2026-04-29T15:03:11.900952197-03:00
rendered_js: false
word_count: 56
summary: This document describes the structure and usage of Warp's URI scheme to trigger specific actions like opening tabs, windows, or launch configurations.
tags:
    - warp-terminal
    - uri-scheme
    - automation
    - integration
    - command-line
    - deep-linking
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## Overview

Use Warp URIs to trigger actions externally.

| Action | URI Format |
|--------|------------|
| New window | `warp://action/new_window?path=<folder_path>` |
| New tab | `warp://action/new_tab?path=<folder_path>` |
| Launch config | `warp://launch/<launch_configuration_path>` |

> [!info]
> [Warp Preview](https://docs.warp.dev/support-and-community/community/warp-preview-and-alpha-program) URI uses `warppreview://`

## Example

See [Warp + Raycast Extension](https://github.com/raycast/extensions/blob/74521b70b62355004b0958393a64f9417b1ff3a6/extensions/warp/src/uri.ts) for URIs in action.

#warp-terminal #uri-scheme #automation
