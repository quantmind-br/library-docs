---
title: Restore Cursor (DECRC) - ESC
url: https://ghostty.org/docs/vt/esc/decrc
source: crawler
fetched_at: 2026-03-03T08:23:30.395285-03:00
rendered_js: true
word_count: 41
summary: This document describes the ANSI escape sequence used to restore the cursor-related state that was previously saved using the Save Cursor (DECSC) sequence.
tags:
    - vt100
    - escape-sequence
    - cursor-restoration
    - decrc
    - terminal-control
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