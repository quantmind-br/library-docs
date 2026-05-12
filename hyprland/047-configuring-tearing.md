---
title: Tearing
url: https://wiki.hypr.land/Configuring/Tearing/
source: sitemap
fetched_at: 2026-04-26T09:48:50.64325088-03:00
rendered_js: false
word_count: 199
summary: This document provides instructions on how to enable screen tearing in Hyprland to reduce input latency in games, including configuration requirements and troubleshooting common issues.
tags:
    - hyprland
    - screen-tearing
    - window-rules
    - gpu-configuration
    - latency-reduction
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# Tearing

Screen tearing reduces latency and/or jitter in games.

## Enabling tearing

1. Set `general:allow_tearing` to `true` — this is the master toggle.
2. Add an `immediate` windowrule for the game:

```env
general {
    allow_tearing = true
}
windowrule = match:class cs2, immediate yes
```

> [!warning]
> Tearing only applies when the game is in fullscreen and the only visible thing on screen.

> [!warning]
> Tearing support is experimental. If you experience graphical issues, see the culprits below.

## Common Issues

### No tearing at all

- Verify window rules match and the master toggle is enabled.
- Ensure nothing else is visible on the monitor: no notifications, overlays, lockscreens, bars, other windows. (Different monitor is fine.)

### Apps that should tear, freeze

- Your GPU driver does not support tearing.
- Do **not** report issues for this.

### Graphical artifacts (random colorful pixels)

- Likely a graphics driver issue.
- Do **not** report issues for this — most likely your GPU driver's fault.

#screen-tearing #window-rules #gpu-configuration