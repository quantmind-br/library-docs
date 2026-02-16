---
title: Animations | SketchyBar
url: https://felixkratz.github.io/SketchyBar/config/animations
source: github_pages
fetched_at: 2026-02-15T21:17:06.071167-03:00
rendered_js: false
word_count: 234
summary: This document explains how to implement animations for SketchyBar properties, covering syntax, duration calculation, and techniques for chaining multiple animations.
tags:
    - sketchybar
    - animation-syntax
    - macos-customization
    - command-line-interface
    - property-transitions
category: guide
---

All transitions between `<argb_hex>`, `<integer>` and `<positive_integer>` values can be animated, by prepending the animation command in front of any regular `--set` or `--bar` command:

```
sketchybar --animate <curve><duration>\
           --bar <property>=<value>... <property>=<value>\
           --set <name><property>=<value>... <property>=<value>
```

The `<duration>` is a positive integer quantifying the number of animation steps (the duration is the frame count on a 60Hz display, such that the temporal duration of the animation in seconds is given by `<duration>` / 60).

The animation system *always* animates between all *current* values and the values specified in a configuration command (i.e. `--bar` or `--set` commands).

If you want to chain two or more animations together, you can do so by simply changing the property multiple times in a single call, e.g.

will animate the bar to the first offset and after that to the second offset. You can chain together as main animations as you like and you can change the animation function in between. This is a nice way to create custom animations with key-frames. You can also make other properties wait with their animation till another animation is finished, by simply setting the property that should wait to its current value in the first animation.

A new non-animated `--set` command targeting a currently animated property will cancel the animation queue and immediately set the value.

A new animated `--set` command targeting a currently animated property will cancel the animation queue and immediately begin with the new animation, beginning at the current state.