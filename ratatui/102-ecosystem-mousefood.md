---
title: Embedded
url: https://ratatui.rs/ecosystem/mousefood/
source: crawler
fetched_at: 2026-02-01T21:13:30.317878554-03:00
rendered_js: false
word_count: 36
summary: This document explains how Mousefood serves as a backend for the embedded-graphics crate to enable compatibility with various displays and platforms.
tags:
    - mousefood
    - embedded-graphics
    - graphics-backend
    - rust-psp
    - ratatui
    - embedded-rust
category: concept
---

Mousefood can also be used as a backend for any `embedded-graphics` draw target, which means you can use it with a variety of displays and platforms.

For example:

![rust-psp ratatui](https://github.com/orhun/rust-rocks/blob/main/assets/ratatui-psp.png?raw=true)

[Ratatui running on PSP](https://github.com/overdrivenpotato/rust-psp/tree/master/examples/ratatui) via `rust-psp`