---
title: Multiple bar instances
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/multiple-bar-instances.md
source: git
fetched_at: 2026-02-20T08:51:19.605844-03:00
rendered_js: false
word_count: 88
summary: This document explains how to run multiple instances of komorebi-bar by specifying individual configuration file paths for different monitors.
tags:
    - komorebi-bar
    - multi-monitor
    - configuration-files
    - monitor-targeting
category: configuration
---

# Multiple Bar Instances

If you would like to run multiple instances of `komorebi-bar` to target different monitors, it is possible to do so
by maintaining multiple `komorebi.bar.json` configuration files and specifying their paths in the `bar_configurations`
array in your `komorebi.json` configuration file.

```json
{
  "bar_configurations": [
    "C:/Users/LGUG2Z/komorebi.bar.monitor1.json",
    "C:/Users/LGUG2Z/komorebi.bar.monitor2.json"
  ]
}
```

You may also use `$Env:USERPROFILE` or `$Env:KOMOREBI_CONFIG_HOME` when specifying the paths.

The main difference between different `komorebi.bar.json` files will be the value of `monitor.index` which is used to
target the monitor for each instance of `komorebi-bar`.