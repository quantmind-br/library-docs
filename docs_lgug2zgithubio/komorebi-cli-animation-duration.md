---
title: animation-duration - Komorebi
url: https://lgug2z.github.io/komorebi/cli/animation-duration.html
source: github_pages
fetched_at: 2026-02-20T08:45:25.72237-03:00
rendered_js: true
word_count: 9
summary: This document describes the usage and arguments for the komorebic CLI command to set durations for movement and transparency animations.
tags:
    - komorebi
    - cli-reference
    - window-management
    - animation-settings
    - configuration
category: reference
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/cli/animation-duration.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/cli/animation-duration.md "View source of this page")

```
Set the duration for movement animations in ms

Usage: komorebic.exe animation-duration [OPTIONS] <DURATION>

Arguments:
  <DURATION>
          Desired animation durations in ms

Options:
  -a, --animation-type <ANIMATION_TYPE>
          Animation type to apply the duration to. If not specified, sets global duration

          [possible values: movement, transparency]

  -h, --help
          Print help
```