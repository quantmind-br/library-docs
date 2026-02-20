---
title: Floating applications
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/floating-applications.md
source: git
fetched_at: 2026-02-20T08:51:07.845061-03:00
rendered_js: false
word_count: 46
summary: This document explains how to configure specific applications to behave as floating windows by adding rules to the komorebi configuration file.
tags:
    - komorebi
    - floating-windows
    - window-management
    - configuration
    - json
category: configuration
---

# Floating Windows

Sometimes you will want a specific application to be managed as a floating window.
You can add rules to enforce this behaviour in the `komorebi.json` configuration file.

```json
{
  "floating_applications": [
    {
      "kind": "Title",
      "id": "Media Player",
      "matching_strategy": "Equals"
    }
  ]
}
```
