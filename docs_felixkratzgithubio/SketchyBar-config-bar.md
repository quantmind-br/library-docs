---
title: Bar Properties | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/bar
source: github_pages
fetched_at: 2026-02-15T21:17:16.216588-03:00
rendered_js: false
word_count: 127
summary: This document provides instructions on setting up and managing the SketchyBar configuration file and using the command line for real-time adjustments and debugging.
tags:
    - sketchybar
    - configuration
    - macos
    - shell-script
    - dotfiles
    - command-line-interface
category: configuration
---

For an example configuration see the supplied default *sketchybarrc*. The configuration file resides in `~/.config/sketchybar/sketchybarrc` and is a regular script that gets executed when *SketchyBar* launches, everything persistent should be set up in this script.

It is possible to play with properties in the commandline and change them on the fly while the bar is running, once you find a fitting value you can include it in the `sketchybarrc` file, such that the configuration is restored on restart. When configuring *SketchyBar* it can be helpful to stop the brew service and run `sketchybar` from the commandline directly to see all relevant error messages and warnings directly.

```
sketchybar --bar <setting>=<value>... <setting>=<value>
```

You can find the nomenclature for all the types [here](https://felixkratz.github.io/SketchyBar/config/types). If you are looking for colors, check out the [color picker](https://felixkratz.github.io/SketchyBar/config/tricks#color-picker).