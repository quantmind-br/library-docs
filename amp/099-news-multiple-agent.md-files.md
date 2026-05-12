---
title: Multiple AGENT.md Files
url: https://ampcode.com/news/multiple-AGENT.md-files
source: crawler
fetched_at: 2026-02-06T02:08:45.58828575-03:00
rendered_js: false
word_count: 67
summary: This document explains how the Amp editor utilizes AGENTS.md files across various directory levels to provide localized context and configuration. It details the file search hierarchy and the ability to include additional file references within these documents.
tags:
    - amp-editor
    - agents-md
    - configuration-files
    - hierarchical-config
    - context-management
category: configuration
---

*Update: Amp now looks in files named `AGENTS.md` (with an `S`).*

Amp now looks for `AGENT.md` files in subtrees, parent directories, and `~/.config/AGENT.md`.

This lets you keep your top-level `AGENT.md` general and create more specific `AGENT.md` files in subtrees. They'll be included only when Amp works in that subtree.

You can also @-mention files in `AGENT.md` to include additional context.

[Manual »](https://ampcode.com/manual#AGENTS.md)

![Multiple AGENT.md files in use](https://static.ampcode.com/news/multiple-agent-md-files-2.png)