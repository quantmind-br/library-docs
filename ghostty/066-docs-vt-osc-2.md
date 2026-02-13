---
title: Change Window Title (OSC 2) - OSC
url: https://ghostty.org/docs/vt/osc/2
source: crawler
fetched_at: 2026-02-11T01:43:37.585748-03:00
rendered_js: true
word_count: 67
summary: This document explains the OSC 2 escape sequence used to change a terminal's window title and notes Ghostty's specific requirement for UTF-8 encoding.
tags:
    - terminal-escapes
    - window-title
    - osc-2
    - ghostty
    - control-sequences
category: reference
---

Change the name of the window title.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x32
   
   2
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Change the window title to `t`.

While xterm defaults to interpreting `t` as a ISO-8859-1-encoded string, which can be changed via Set Title Mode (XTSMTITLE) to either accept a hexadecimal-escaped or bare UTF-8 string, Ghostty always unconditionally expects `t` to be directly UTF-8-encoded.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/2.mdx)