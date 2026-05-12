---
title: Performance
url: https://wiki.hypr.land/Configuring/Performance/
source: sitemap
fetched_at: 2026-04-26T09:49:32.632986295-03:00
rendered_js: false
word_count: 204
summary: Performance optimization techniques for Hyprland — fractional scaling, TLP on Intel laptops, power consumption, and gaming.
tags:
    - hyprland
    - performance-tuning
    - wayland
    - linux-optimization
    - battery-life
    - fractional-scaling
    - troubleshooting
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Fractional Scaling

Wayland fractional scaling has improved but remains imperfect. Some apps lack support or have experimental support. If experiencing high GPU usage or lag, try integer scaling (`1` or `2`):

```
monitor=,preferred,auto,2
```

## Intel iGPU Stutter with TLP (Laptops)

TLP defaults are aggressive. Set `INTEL_GPU_MIN_FREQ_ON_AC` and/or `INTEL_GPU_MIN_FREQ_ON_BAT` in `/etc/tlp.conf` higher (e.g. 500 instead of 300) to reduce or eliminate stutter.

## Minimum Power Draw on Laptop

- `decoration:blur:enabled = false` and `decoration:shadow:enabled = false` — disable battery-hungry effects.
- `misc:vfr = true` — reduces frames sent when nothing changes on-screen.

## Poor Game Performance (Proton)

Use `gamescope` to fix Wayland/Hyprland gaming issues.

> [!info] Last updated: April 20, 2026

[[013-configuring-example-configurations|Example configurations]]

#performance #troubleshooting #hyprland
