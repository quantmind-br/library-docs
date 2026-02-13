---
title: Show Desktop Notification (OSC 9) - OSC
url: https://ghostty.org/docs/vt/osc/9
source: crawler
fetched_at: 2026-02-11T01:43:38.212782-03:00
rendered_js: true
word_count: 95
summary: This document explains how to use the OSC 9 escape sequence to trigger desktop notifications within supported terminal emulators like Ghostty and iTerm.
tags:
    - terminal-emulator
    - escape-sequences
    - osc-9
    - desktop-notifications
    - ghostty
    - iterm2
category: reference
---

Show a desktop notification.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x39
   
   9
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Show a desktop notification with title `t`.

To avoid conflicting with the [ConEmu extensions](https://ghostty.org/docs/vt/osc/conemu), which also use OSC 9 due to historical happenstance, the title should not begin with a number and then a semicolon (`;`). In practice a collision of this kind should be rare. Ghostty's parser will silently convert any invalid ConEmu sequence to a OSC 9 sequence, though this behavior should not be relied upon.

Originated from iTerm since before 2010.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/9.mdx)