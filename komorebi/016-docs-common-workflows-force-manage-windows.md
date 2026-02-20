---
title: Force manage windows
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/force-manage-windows.md
source: git
fetched_at: 2026-02-20T08:51:09.846759-03:00
rendered_js: false
word_count: 67
summary: This document explains how to manually configure komorebi to manage windows that are not automatically detected by defining management rules in the configuration file.
tags:
    - komorebi
    - window-management
    - configuration
    - manage-rules
    - tiling-window-manager
category: configuration
---

# Force Manage Windows

❗️**NOTE**: A significant number of force-manage window rules for the most
common applications are [already generated for
you](https://github.com/LGUG2Z/komorebi-application-specific-configuration)

In some rare cases, a window may not automatically be registered to be managed
by `komorebi`. You can add rules to enforce this behaviour in the
`komorebi.json` configuration file.

```json
{
  "manage_rules": [
    {
      "kind": "Title",
      "id": "Media Player",
      "matching_strategy": "Equals"
    }
  ]
}
```
