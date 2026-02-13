---
title: Horizontal Position Relative (HPR) - CSI
url: https://ghostty.org/docs/vt/csi/hpr
source: crawler
fetched_at: 2026-02-11T01:43:32.058989-03:00
rendered_js: true
word_count: 134
summary: This document describes the Horizontal Position Relative (HPR) terminal escape sequence, explaining how to move the cursor to a specific column relative to its current position.
tags:
    - terminal-emulation
    - escape-sequences
    - cursor-movement
    - csi-sequences
    - ghostty
category: reference
---

Move the cursor to a specific column relative to the current position.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   x
4. 0x61
   
   a

This sequence performs [cursor position (CUP)](https://ghostty.org/docs/vt/csi/cup) with `x` set to the current cursor column plus `x` and `y` set to the current cursor row. There is no additional or different behavior for using `HPR`.

The parameter `x` must be an integer greater than or equal to 1. If `x` is less than or equal to 0, adjust `x` to be 1. If `x` is omitted, `x` defaults to 1.

Because this invokes `CUP`, the cursor row (`y`) can change if it is outside the bounds of the `CUP` operation. For example, if [origin mode](#TODO) is set and the current cursor position is outside of the scroll region, the row will be adjusted.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/hpr.mdx)