---
title: Zellij 0.35.1 Stacked Panes and Swap Layouts
url: https://zellij.dev/news/stacked-panes-swap-layouts/
source: sitemap
fetched_at: 2026-01-24T15:52:45.437116743-03:00
rendered_js: false
word_count: 449
summary: This document introduces the new features of Zellij version 0.35.1, focusing on stacked panes, automatic swap layouts, and the inclusion of floating panes in layout files.
tags:
    - zellij
    - release-notes
    - terminal-multiplexer
    - stacked-panes
    - swap-layouts
    - window-management
category: guide
---

2023-03-07

We just released [Zellij 0.35.1](https://github.com/zellij-org/zellij/releases/tag/v0.35.1), including an exciting array of new features and bug fixes. Let’s dive in to some of them!

### Stacked Panes

![Stacked Panes preview](https://zellij.dev/img/stacked-panes-animated.gif)

Stacked panes are a new and unique way to arrange panes in your workspace. You can now arrange panes in a stack, showing only the title line of all but one of them - with the last one expanded just like any other pane.

You can page through them up/down as you would normally move through panes (eg. with `Alt` + `<arrow-keys>`, or `Alt` + `hjkl`), move them around with `Ctrl` + `h` + `<arrows>`/`hjkl` and even select through them with a mouse click.

#### To get stacked panes

1. Start Zellij
2. Open 3 panes with `Alt` + `n`
3. Press `Alt` + `[` to change the layout to `STACKED` (see “Auto and Swap Layouts” below for more details).
4. If you like, you can open more panes in the stack with `Alt` + `n` or move through them with `Alt` + `<arrow-keys>/hjkl`

Stacked panes can also be included [in your layouts](https://zellij.dev/documentation/creating-a-layout.html#stacked)

### Auto and Swap Layouts

![Auto and Swap Layouts preview](https://zellij.dev/img/swap-layouts-preview.gif)

Another major feature of this release is “Auto Layouts”. Previously, when opening new panes without specifying a split direction (eg. with `Alt` + `n`), Zellij would do its best to place them in the largest free area on screen. While great as a stop-gap solution, we decided we could do this more intelligently.

Starting this version, Zellij will lay these panes automatically according to a predefined set of layouts. These `swap_layouts` come built-in, and can also be [configured and adjusted to your liking](https://zellij.dev/documentation/swap-layouts.html)

As their name implies, you can also switch between these layouts whenever you want (by default with `Alt` + `[]`), if you’d like to rearrange the panes currently on screen.

These `swap_layouts` are distinct for tiled panes (the “regular” panes on screen) and floating panes.

To try these for tiled panes:

1. Start Zellij
2. Open one or more panes with `Alt` + `n`
3. Press `Alt` + `[]` to cycle through the swap layouts until you find one you like

To try these for floating panes:

1. Start Zellij
2. Open a new floating pane with `Ctrl p` + `w`
3. Add more floating panes with `Alt` + `n` or `Ctrl p` + `n`
4. Press `Alt` + `[]` to cycle through the floating swap layouts until you find one you like

Don’t like this feature? It can be disabled by adding `auto_layout false` to your [config](https://zellij.dev/documentation/options.html#auto_layout)

### Floating Panes in Layouts

This version also adds the ability to add floating panes to [layouts](https://zellij.dev/tutorials/layouts/). So now we can do:

```
layout {
    pane edit="src/main.rs"
    floating_panes {
        pane command="cargo" {
            args "check"
            y "55%"
            width "45%"
            height "45%"
        }
        pane command="cargo" {
            args "run"
            x "1%"
            y "1%"
            width "45%"
            height "45%"
        }
        pane command="cargo" {
            args "test"
            x "50%"
            y "1%"
            width "45%"
            height "45%"
        }
    }
}
```

And get:

![floating_panes in layouts](https://zellij.dev/img/floating_panes_layouts.png)

### Do you like Zellij?

Please consider helping sustain its development by [sponsoring the developer](https://github.com/sponsors/imsnif).