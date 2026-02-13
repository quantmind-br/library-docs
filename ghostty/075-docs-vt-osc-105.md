---
title: Reset Special Colors (OSC 105) - OSC
url: https://ghostty.org/docs/vt/osc/105
source: crawler
fetched_at: 2026-02-11T01:43:40.023287-03:00
rendered_js: true
word_count: 48
summary: This document defines the OSC 105 escape sequence used to reset specific or all special colors within a terminal emulator.
tags:
    - terminal-emulator
    - escape-sequences
    - osc-105
    - color-management
    - ghostty
    - vt-control-codes
category: reference
---

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x30 0x35
   
   105
4. 0x3B
   
   ;
5. \_\_\__
   
   n
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Reset the [special color](https://ghostty.org/docs/vt/concepts/colors#special-colors) at index `n`. `n` can be specified **zero or more** times, separated with semicolons (`;`) When `n` is not specified, all special colors are reset.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/105.mdx)