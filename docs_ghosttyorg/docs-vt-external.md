---
title: External Protocols - Terminal API (VT)
url: https://ghostty.org/docs/vt/external
source: crawler
fetched_at: 2026-03-03T08:23:27.25934-03:00
rendered_js: true
word_count: 110
summary: This document lists and details the external terminal emulator protocols that the Ghostty application supports, acknowledging specifications inherited from other tools.
tags:
    - external-protocols
    - terminal-emulators
    - osc-8
    - osc-21
    - specification-support
category: reference
---

A list of external protocols that Ghostty supports.

Ghostty inherits the rich tradition of innovation from other terminal emulators, and many modern, well-written specifications do not need to be reinvented here. If Ghostty's behavior deviates from these specifications, we treat them as bugs which will be fixed according to spec.

Note that we may still provide specifications here if upstream behavior is not well-specified (such is the case for most xterm and [ConEmu](https://ghostty.org/docs/vt/osc/conemu) extensions), or Ghostty intentionally deviates from it for good reason.

Below is a list of protocols that Ghostty supports, which originate from other terminal emulators:

ProtocolSpecificationOSC 8 (Hyperlinks)[VTE and iTerm2](https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda)OSC 21 (Kitty Color Protocol)[Kitty](https://sw.kovidgoyal.net/kitty/color-stack/)

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/external.mdx)