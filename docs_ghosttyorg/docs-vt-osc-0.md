---
title: Change Window Icon and Title (OSC 0) - OSC
url: https://ghostty.org/docs/vt/osc/0
source: crawler
fetched_at: 2026-03-03T08:23:41.600266-03:00
rendered_js: true
word_count: 54
summary: This document details the escape sequence 0x5C, which is treated as an alias for the Change Window Title (OSC 2) sequence because the terminal emulator does not support changing the window icon.
tags:
    - escape-sequence
    - terminal-control
    - osc
    - window-title
    - alias
category: reference
---

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x30
   
   0
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Equivalent to [Change Window Icon (OSC 1)](https://ghostty.org/docs/vt/osc/1) followed by [Change Window Title (OSC 2)](https://ghostty.org/docs/vt/osc/2) with the same argument `t`.

Since Ghostty does not support changing the window icon, this is treated as an alias of [Change Window Title (OSC 2)](https://ghostty.org/docs/vt/osc/2).