---
title: Change Window Icon and Title (OSC 0) - OSC
url: https://ghostty.org/docs/vt/osc/0
source: crawler
fetched_at: 2026-03-10T06:35:40.49838-03:00
rendered_js: true
word_count: 54
summary: This document details the byte sequences for several control characters and explains that the specific sequence 0x1B 0x5C maps to an alias for the Change Window Title operating system command (OSC 2) in the Ghostty terminal emulator.
tags:
    - control-characters
    - byte-sequence
    - osc-command
    - alias
    - terminal-emulator
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