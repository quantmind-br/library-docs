---
title: Change Window Icon (OSC 1) - OSC
url: https://ghostty.org/docs/vt/osc/1
source: crawler
fetched_at: 2026-02-11T01:43:36.846203-03:00
rendered_js: true
word_count: 82
summary: This document explains the OSC 1 escape sequence used to change a terminal's window icon name and details its lack of support in modern terminal emulators.
tags:
    - osc-sequences
    - terminal-emulators
    - escape-codes
    - window-management
    - terminal-compatibility
category: reference
---

Change the name of the window icon.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31
   
   1
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Change the window icon name to `t`. The exact method of locating the icon data through the icon name is platform-dependent.

Ghostty and most modern terminal emulators do not implement this sequence as its behavior is not well-defined or even possible on all platforms, which is also the conclusion reached by [Foot](https://codeberg.org/dnkl/foot/pulls/1832#issuecomment-2304415).

GhosttyKittyVTEAlacrittyFootiTerm2xtermOSC 1NoNoNoNo[1](#user-content-fn-alacritty)NoNoYes

1. Listed as "rejected". [↩](#user-content-fnref-alacritty)

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/1.mdx)