---
title: Backspace (BS) - Control
url: https://ghostty.org/docs/vt/control/bs
source: crawler
fetched_at: 2026-03-10T06:35:24.791487-03:00
rendered_js: true
word_count: 31
summary: This document explains the function of the Backspace (BS) control character, which moves the cursor backward by one position in a terminal interface.
tags:
    - control-character
    - cursor-movement
    - backspace
    - terminal
    - vt
category: reference
---

Move the cursor backward one position.

1. 0x08
   
   BS

This sequence performs [cursor backward (CUB)](https://ghostty.org/docs/vt/csi/cub) with `Pn = 1`. There is no additional or different behavior for using `BS`.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/control/bs.mdx)