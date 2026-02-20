---
title: border-colour - Komorebi
url: https://lgug2z.github.io/komorebi/cli/border-colour.html
source: github_pages
fetched_at: 2026-02-20T08:45:38.025189-03:00
rendered_js: true
word_count: 9
summary: This document provides the command-line interface specification for setting RGB color values for different window border types in the komorebi window manager.
tags:
    - komorebi
    - cli-command
    - window-management
    - border-color
    - rgb-configuration
category: reference
---

[](https://github.com/LGUG2Z/komorebi/edit/master/docs/cli/border-colour.md "Edit this page")[](https://github.com/LGUG2Z/komorebi/raw/master/docs/cli/border-colour.md "View source of this page")

```
Set the colour for a window border kind

Usage: komorebic.exe border-colour [OPTIONS] <R> <G> <B>

Arguments:
  <R>
          Red

  <G>
          Green

  <B>
          Blue

Options:
  -w, --window-kind <WINDOW_KIND>
          [default: single]
          [possible values: single, stack, monocle, unfocused, unfocused-locked, floating]

  -h, --help
          Print help
```