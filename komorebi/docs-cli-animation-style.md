---
title: Animation style
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/animation-style.md
source: git
fetched_at: 2026-02-20T08:46:48.764249-03:00
rendered_js: false
word_count: 82
summary: This document describes the command-line usage and available options for setting the easing function of movement and transparency animations in komorebi.
tags:
    - komorebi
    - animation-style
    - cli-command
    - easing-functions
    - window-manager-configuration
category: reference
---

# animation-style

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
