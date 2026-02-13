---
title: Restore Cursor (DECRC) - ESC
url: https://ghostty.org/docs/vt/esc/decrc
source: crawler
fetched_at: 2026-02-11T01:43:23.631644-03:00
rendered_js: true
word_count: 41
summary: This document describes the DECRC escape sequence used to restore the cursor-related state in a terminal emulator. It also explains the default behavior if no cursor state was previously saved.
tags:
    - terminal-emulation
    - vt-sequences
    - cursor-control
    - decrc
    - escape-codes
category: reference
---

Restore the cursor-related state saved via Save Cursor (DECSC).

1. 0x1B
   
   ESC
2. 0x38
   
   8

If a cursor was never previously saved, this sets all the typically saved values to their default values.

Validation is shared with [Save Cursor (DECSC)](https://ghostty.org/docs/vt/esc/decsc).

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/esc/decrc.mdx)