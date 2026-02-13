---
title: Backspace (BS) - Control
url: https://ghostty.org/docs/vt/control/bs
source: crawler
fetched_at: 2026-02-11T01:43:20.529572-03:00
rendered_js: true
word_count: 31
summary: This document defines the Backspace (BS) control sequence, which moves the terminal cursor backward by one position, equivalent to the CUB command.
tags:
    - terminal-emulation
    - control-sequences
    - cursor-movement
    - backspace
    - ghostty
category: reference
---

Move the cursor backward one position.

1. 0x08
   
   BS

This sequence performs [cursor backward (CUB)](https://ghostty.org/docs/vt/csi/cub) with `Pn = 1`. There is no additional or different behavior for using `BS`.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/control/bs.mdx)