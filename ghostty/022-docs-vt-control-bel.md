---
title: Bell (BEL) - Control
url: https://ghostty.org/docs/vt/control/bel
source: crawler
fetched_at: 2026-02-11T01:43:21.294278-03:00
rendered_js: true
word_count: 184
summary: This document explains the purpose and implementation of the BEL control character, detailing its historical context, modern notification behaviors, and use as an OSC terminator.
tags:
    - terminal-emulation
    - control-characters
    - bel-sequence
    - osc-terminator
    - ghostty
    - user-notification
category: reference
---

Raise the attention of the user.

1. 0x07
   
   BEL

The purpose of the bell sequence is to raise the attention of the user.

Historically, this would [ring a physical bell](https://en.wikipedia.org/wiki/Bell_character). Today, many alternate behaviors are acceptable:

- An audible sound can be played through the speakers
- Background or border of a window can visually flash
- The terminal window can come into focus or be put on top
- Application icon can bounce or otherwise draw attention
- A desktop notification can be shown

Normally, the bell behavior is configurable and can be disabled.

The `BEL` character is also a valid terminating character for OSC sequences, although `ST` is preferred. If `BEL` is the terminating character for an OSC sequence, any responses should also terminate with the `BEL` character.[1](#user-content-fn-1)

This control character is implemented in Ghostty, although by default most behaviors that Ghostty implements are disabled. See the documentation for the [`bell-features`](https://ghostty.org/docs/config/reference#bell-features) configuration option for more information.

The BEL character can be used as an OSC terminator. If it is used as an OSC terminator, Ghostty will terminate any responses with the `BEL` character.

1. [https://invisible-island.net/xterm/ctlseqs/ctlseqs.html](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html) [↩](#user-content-fnref-1)

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/control/bel.mdx)