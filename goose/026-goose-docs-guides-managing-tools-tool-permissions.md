---
title: Managing Tool Permissions | goose
url: https://block.github.io/goose/docs/guides/managing-tools/tool-permissions
source: github_pages
fetched_at: 2026-01-22T22:14:07.365215885-03:00
rendered_js: true
word_count: 48
summary: This document explains how to configure and manage fine-grained tool permissions in goose to override default behaviors for specific extension tools.
tags:
    - goose
    - tool-permissions
    - access-control
    - configuration
    - extension-management
category: guide
---

Tool permissions provide fine-grained control over how goose uses different tools within extensions. This guide will help you understand and configure these permissions effectively.

Tool permissions work alongside [goose permission modes](https://block.github.io/goose/docs/guides/goose-permissions). The mode sets the default behavior, while tool permissions let you override the behavior of specific tools.

```
Development Task:
✓ File reading → Always Allow
✓ Code editing → Ask Before
✓ Test running → Always Allow
✗ System commands → Ask Before

Documentation Task:
✓ File reading → Always Allow
✓ Markdown editing → Always Allow
✗ Code editing → Never Allow
✗ System commands → Never Allow
```