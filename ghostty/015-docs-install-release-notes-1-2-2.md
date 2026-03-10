---
title: 1.2.2 - Release Notes
url: https://ghostty.org/docs/install/release-notes/1-2-2
source: crawler
fetched_at: 2026-03-10T06:35:19.174146-03:00
rendered_js: true
word_count: 104
summary: This document details the release notes for Ghostty version 1.2.2, primarily addressing a critical memory leak regression from the previous version and a minor font rendering fix on macOS.
tags:
    - release-notes
    - hotfix
    - memory-leak
    - macos
    - font-rendering
    - bug-fix
category: reference
---

## Ghostty 1.2.2

Release notes for Ghostty 1.2.2, released on October 8, 2025.

Ghostty 1.2.2 is a hotfix to fix a critical regression from 1.2.1 where we accidentally forgot to backport a memory leak fix. As a result, Ghostty 1.2.1 has a significant memory leak under certain scenarios that can cause runaway memory growth. This issue affects all platforms.

We've also included a very small fix for macOS font rendering that would cause very small (one pixel or half pixel) offsets for some glyphs that could result in blurriness.

This was released very shortly after 1.2.1, please see the [1.2.1 release notes](https://ghostty.org/docs/install/release-notes/1-2-1).

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/install/release-notes/1-2-2.mdx)