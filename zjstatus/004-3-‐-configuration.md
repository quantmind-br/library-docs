---
title: !!binary MyDvv72AkCBDb25maWd1cmF0aW9u
url: https://github.com/dj95/zjstatus/wiki/3-‐-Configuration
source: wiki
fetched_at: 2026-04-30T12:58:27.573857874-03:00
rendered_js: false
word_count: 1366
summary: This document provides a comprehensive guide for configuring the zjstatus plugin for Zellij, covering layout integration, widget customization, border management, and styling directives.
tags:
    - zellij
    - zjstatus
    - terminal-emulator
    - plugin-configuration
    - theming
    - bar-layout
category: configuration
---

Configuration can be performed in the layout file, when importing the plugin. Here's a short example.

```javascript
layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="https://github.com/dj95/zjstatus/releases/latest/download/zjstatus.wasm" {
                format_left   "{mode} #[fg=#89B4FA,bold]{session}"
                format_center "{tabs}"
                format_right  "{command_git_branch} {datetime}"
                format_space  ""

                border_enabled  "false"
                border_char     "─"
                border_format   "#[fg=#6C7086]{char}"
                border_position "top"

                hide_frame_for_single_pane "true"

                mode_normal  "#[bg=blue] "
                mode_tmux    "#[bg=#ffc387] "

                tab_normal   "#[fg=#6C7086] {name} "
                tab_active   "#[fg=#9399B2,bold,italic] {name} "

                command_git_branch_command     "git rev-parse --abbrev-ref HEAD"
                command_git_branch_format      "#[fg=blue] {stdout} "
                command_git_branch_interval    "10"
                command_git_branch_rendermode  "static"

                datetime        "#[fg=#6C7086,bold] {format} "
                datetime_format "%A, %d %b %Y %H:%M"
                datetime_timezone "Europe/Berlin"
            }
        }
    }
}
```

In order to start using zjstatus you need to specify the widgets you'd like to use under the `format_left` and/or `format_center` and/or `format_right`
configuration. Formatting can be done with `#[..]`, while widgets and properties are surrounded by `{..}`.
The blank space between the left and the right part can be colored with `format_space`.

## General configuration

This section describes some general configuration for zjstatus.

> [!CAUTION]
> Please disable pane_frames in your global zellij configs as zjstatus will activate them in certain scenarios. Otherwise weird behavior might occur as zellij will reset the frames on each event cycle and causes conflicts.

### Hide pane frames for tabs single panes

The option `hide_frame_for_single_pane` will toggle the pane frames depending on how many panes (not plugin panes) are shown.
This will effectively hide the frame border, when only one pane, like an editor, is shown. Pane frames are toggled as soon
as there is another pane created.

### Hide pane frames except for search

The option `hide_frame_except_for_search ` will toggle the pane frames only on, when search mode is enabled. Otherwise it will toggle the pane frames off.

### Hide pane frames except for fullscreen

The option `hide_frame_except_for_fullscreen` will toggle the pane frames only to on, when the current active pane is in fullscreen mode. Otherwise the frames are off.

### Hide pane frames except for scroll

The option `hide_frame_except_for_scroll` will toggle the pane frames only to on, when the scroll mode is active.

### Border for the bar

When hiding the pane frames, zjstatus might blend in too well with the background and opened panes since zellij won't draw
the border for non-selectable plugins. Therefore zjstatus provides its own border, that can be activated and customized.
Most important, the pane height for the plugin **must be set to 2**. Otherwise zjstatus won't be able to draw it. For top
bar configurations the position of the border is also implemented.

```javascript
border_enabled  "true"           // "true" | "false" for activating the bar
border_char     "─"              // character used for drawing the bar
border_format   "#[fg=#6C7086]"  // format specifier for theming
border_position "top"            // "top" | "bottom" for the border position relative to the bar
```

### Hiding format parts on over length

With zjstatus 0.15.0 there is an option to hide parts (left, center, right) when the parts are so long that they flow into each other. The feature consists of two configuration option. One toggle to enable the behaviour and a configuration for the precedence, which part should stay in place and which one is the least important one and can be hidden.

```javascript
format_hide_on_overlength "false"
format_precedence         "lrc"
```

The precedence should contain all three letters `l` (left part), `c` (center part) and `r` (right part). The first letter represents the most important part, which is always visible. The last letter is the least important and hidden first in case there are overlapping parts. With this example, the right part is hidden, when center and right part collide. Also the center part is hidden, in case the center and left part collide.

## Formatting and theming

Text and modules can be themed with directives in `#[]`. These directives tell zjstatus to print the following
text in the specified format. It will reset the format on any new directives or after rendering a widget.
Options can be combined with a `,`, when they occur in the same bracket.

Possible formatting options are:

| name              | value                     | example                | description      |
|-------------------|---------------------------|------------------------|------------------|
| fg                | hex or ansi color or name | `#[fg=#ffffff]`        | foreground color |
| bg                | hex or ansi color or name | `#[bg=#ffffff]`        | background color |
| bold              | none                      | `#[bold]`              | bold text        |
| italic            | none                      | `#[italic]` *or* `#[italics]`     | italic text      |
| underscore        | none                      | `#[underscore]`        | underline the text (check your terminal support) |
| blink             | none                      | `#[blink]`             | blinking text (check your terminal support) |
| hidden            | none                      | `#[hidden]`            | hide the text    |
| strikethrough     | none                      | `#[strikethrough]`     | strike through text (check your terminal support)  |
| double underscore | none                      | `#[double-underscore]` | double underline (check your terminal support) |
| curly underscore  | none                      | `#[curly-underscore]`  | curly underline (check your terminal support)  |
| dotted underscore | none                      | `#[dotted-underscore]` | dotted underline (check your terminal support) |
| dashed underscore | none                      | `#[dashed-underscore]` | dashed underline (check your terminal support) |
| reverse           | none                      | `#[reverse]`           | reverse foreground and background color        |


### Colors

The easiest way to use colors is to use either the 6 character hexadecimal value (e.g. `#00ff00`) or the ANSI color code (`0`..`255`). Color ANSI names like `blue` or `bright_blue` are also supported.

```javascript
mode_normal          "#[bg=#89b4fa] "
mode_tmux            "#[bg=yellow] "
mode_default_to_mode "tmux"
```

### Color Aliases

Starting with version 0.17.0, zjstatus provides the ability to create color aliases. This feature allows to specify all colors in one place and use them throughout the configuration. On color changes, it must only be done in one place. To use color aliases, simply specify them somewhere in the config (I'd recommend the top :D):

```javascript
color_bg     "#181825"
color_fg     "#9399B2"
color_fg_dim "#6C7086"
color_blue   "#89b4fa"
color_orange "#ffc387"
```

Then the name (without the `color_`) can be used in the formats with a preceding `$`. Here's an example for the mode and date widget:

```javascript
mode_normal          "#[bg=$blue] "
mode_tmux            "#[bg=$orange] "
mode_default_to_mode "tmux"

datetime          "#[fg=$fg,bg=$bg] {format} "
datetime_format   "%A, %d %b %Y %H:%M"
datetime_timezone "Europe/Berlin"
```

## Swap Layouts

Zellij offers a feature called [swap layouts](https://zellij.dev/documentation/swap-layouts), which allow you to switch the layout of multiple panes within a session. Since zjstatus requires to override the default layout, default swap layouts will also be overridden and unavailable until you reconfigure them.

Let's use the following base layout as an example:

```javascript
layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="https://github.com/dj95/zjstatus/releases/latest/download/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}
```

In order to introduce swap layouts, add `swap_tiled_layout` or `swap_floating_layout` sections to the layout.

```diff
layout {
+   swap_tiled_layout name="vertical" {
+       tab max_panes=5 {
+           pane split_direction="vertical" {
+               pane
+               pane { children; }
+           }
+       }
+       tab max_panes=8 {
+           pane split_direction="vertical" {
+               pane { children; }
+               pane { pane; pane; pane; pane; }
+           }
+       }
+       tab max_panes=12 {
+           pane split_direction="vertical" {
+               pane { children; }
+               pane { pane; pane; pane; pane; }
+               pane { pane; pane; pane; pane; }
+           }
+       }
+   }

    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="https://github.com/dj95/zjstatus/releases/latest/download/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}
```

> [!TIP]
> You can use `zellij setup --dump-swap-layout default` to dump all default swap layouts.

Another way of using swap layouts is to define them in a separate file near the layout file.

**zjstatus.kdl**

```javascript
layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="https://github.com/dj95/zjstatus/releases/latest/download/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}
```

**zjstatus.swap.kdl**

```diff
+swap_tiled_layout name="vertical" {
+    tab max_panes=5 {
+        pane split_direction="vertical" {
+            pane
+            pane { children; }
+        }
+    }
+    tab max_panes=8 {
+        pane split_direction="vertical" {
+            pane { children; }
+            pane { pane; pane; pane; pane; }
+        }
+    }
+    tab max_panes=12 {
+        pane split_direction="vertical" {
+            pane { children; }
+            pane { pane; pane; pane; pane; }
+            pane { pane; pane; pane; pane; }
+        }
+    }
+}
```

Now swap layouts should work again. Instead of dumping the default swap layouts, you are also able to define your own ones.
