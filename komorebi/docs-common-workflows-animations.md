---
title: Animations
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/animations.md
source: git
fetched_at: 2026-02-20T08:51:01.215729-03:00
rendered_js: false
word_count: 115
summary: This document explains how to enable and customize window movement animations in the komorebi window manager using the JSON configuration file.
tags:
    - komorebi
    - window-manager
    - animations
    - json-configuration
    - performance
category: configuration
---

# Animations

If you would like to add window movement animations, ensure the following options are
defined in the `komorebi.json` configuration file.

```json
{
  "animation": {
    "enabled": true,
    "duration": 250,
    "fps": 60,
    "style": "EaseOutSine"
  }
}
```

Window movement animations only apply to actions taking place within the same monitor
workspace.

You can optionally set a custom duration in ms with `animation.duration` (default: `250`),
a custom style with `animation.style` (default: `Linear`), and a custom FPS value with
`animation.fps` (default: `60`).

It is important to note that higher `fps` and a longer `duration` settings will result
in increased CPU usage.

This feature is not considered stable, and you may encounter visual artifacts
from time to time.