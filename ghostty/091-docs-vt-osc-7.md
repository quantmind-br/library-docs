---
title: Change Working Directory (OSC 7) - OSC
url: https://ghostty.org/docs/vt/osc/7
source: crawler
fetched_at: 2026-03-10T06:35:42.067954-03:00
rendered_js: true
word_count: 72
summary: This document describes the control sequence used by terminal emulators to signal a change in the current working directory to an integrated shell, often using a specific Operating System Command (OSC) sequence.
tags:
    - terminal-control
    - current-working-directory
    - osc-sequence
    - shell-integration
    - uri-navigation
category: reference
---

Change the current working directory of the terminal.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x37
   
   7
4. 0x3B
   
   ;
5. \_\_\__
   
   u
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Change the current working directory to the path denoted by the URI `u`.

The URI should always have a scheme of `file://` and point to an existent folder.

Primarily used by shell integrations for the shell to inform the terminal when the current working directory has changed.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/7.mdx)