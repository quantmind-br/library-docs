---
title: animation - Komorebi
url: https://lgug2z.github.io/komorebi/cli/animation.html
source: github_pages
fetched_at: 2026-02-20T08:45:31.991917-03:00
rendered_js: true
word_count: 9
summary: This command reference explains how to enable or disable window movement and transparency animations in the komorebi window manager using the CLI.
tags:
    - komorebi
    - cli
    - animation
    - window-management
    - transparency
    - configuration
category: reference
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/cli/animation.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/cli/animation.md "View source of this page")

```
Enable or disable movement animations

Usage: komorebic.exe animation [OPTIONS] <BOOLEAN_STATE>

Arguments:
  <BOOLEAN_STATE>
          [possible values: enable, disable]

Options:
  -a, --animation-type <ANIMATION_TYPE>
          Animation type to apply the state to. If not specified, sets global state

          [possible values: movement, transparency]

  -h, --help
          Print help
```