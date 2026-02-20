---
title: animation-style - Komorebi
url: https://lgug2z.github.io/komorebi/cli/animation-style.html
source: github_pages
fetched_at: 2026-02-20T08:45:30.760205-03:00
rendered_js: true
word_count: 9
summary: This document outlines the command-line interface for configuring animation easing styles and types within the komorebi window manager.
tags:
    - komorebi
    - cli-reference
    - animation-styles
    - easing-functions
    - window-management
category: reference
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/cli/animation-style.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/cli/animation-style.md "View source of this page")

```
Set the ease function for movement animations

Usage: komorebic.exe animation-style [OPTIONS]

Options:
  -s, --style <STYLE>
          Desired ease function for animation

          [default: linear]
          [possible values: linear, ease-in-sine, ease-out-sine, ease-in-out-sine, ease-in-quad, ease-out-quad, ease-in-out-quad, ease-in-cubic, ease-in-out-cubic, ease-in-quart, ease-out-quart, ease-in-out-quart, ease-in-quint, ease-out-quint, ease-in-out-quint, ease-in-expo,
          ease-out-expo, ease-in-out-expo, ease-in-circ, ease-out-circ, ease-in-out-circ, ease-in-back, ease-out-back, ease-in-out-back, ease-in-elastic, ease-out-elastic, ease-in-out-elastic, ease-in-bounce, ease-out-bounce, ease-in-out-bounce]

  -a, --animation-type <ANIMATION_TYPE>
          Animation type to apply the style to. If not specified, sets global style

          [possible values: movement, transparency]

  -h, --help
          Print help
```