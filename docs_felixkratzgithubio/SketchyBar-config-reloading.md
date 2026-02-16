---
title: Reloading the configuration | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/reloading
source: github_pages
fetched_at: 2026-02-15T21:17:26.656037-03:00
rendered_js: false
word_count: 121
summary: This document explains how to manually reload SketchyBar configurations and how to enable the automatic hotload feature for real-time updates.
tags:
    - sketchybar
    - configuration-reloading
    - hotload
    - macos-customization
    - command-line
category: configuration
---

If you wish to reload the configuration file of the bar without resorting to manually restarting the process you can use the following command:

which, has the same effect as restarting the process, but is a bit more convenient. Additionally, an optional `<path>` argument to a new `sketchybarrc` file can be given to load a different configuration. If the optional argument is left out, the current configuration is reloaded.

If you wish that the bar automatically reloads the configuration file once you edit it, you can use the hotload functionality included in SketchyBar. It will monitor the directory of the current configuration for changes and reload the configuration should it detect file changes. To control the hotload feature you can use:

```
sketchybar --hotload <boolean>
```