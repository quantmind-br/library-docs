---
title: Ignore windows
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/ignore-windows.md
source: git
fetched_at: 2026-02-20T08:51:10.115498-03:00
rendered_js: false
word_count: 66
summary: This document explains how to configure komorebi to exclude specific applications from tiling by defining ignore rules in the configuration file. It outlines how to target windows using various identifiers like titles and matching strategies.
tags:
    - komorebi
    - window-management
    - configuration
    - ignore-rules
    - tiling-manager
    - json-configuration
category: configuration
---

# Ignore Windows

❗️**NOTE**: A significant number of ignored window rules for the most common
applications are [already generated for
you](https://github.com/LGUG2Z/komorebi-application-specific-configuration)

Sometimes you will want a specific application to never be tiled, and instead
be completely ignored. You can add rules to enforce this behaviour in the
`komorebi.json` configuration file.

```json
{
  "ignore_rules": [
    {
      "kind": "Title",
      "id": "Media Player",
      "matching_strategy": "Equals"
    }
  ]
}
```
