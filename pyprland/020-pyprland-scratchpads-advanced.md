---
title: Fine tuning scratchpads | Pyprland web
url: https://hyprland-community.github.io/pyprland/scratchpads/advanced
source: github_pages
fetched_at: 2026-01-31T16:00:58.604771582-03:00
rendered_js: true
word_count: 559
summary: This document provides comprehensive configuration options for a scratchpad feature, detailing various settings that control positioning, behavior, and advanced functionality of scratchpad windows.
tags:
    - scratchpad
    - configuration
    - window-management
    - hyprland
    - positioning
    - behavior
category: reference
---

Positioning (1)

OptionDescription[`[scratchpad].offset`i](#config-offset "More details below")str

=`"100%"`

Hide animation distance

Behavior (12)

OptionDescription[`[scratchpad].pinned`i](#config-pinned "More details below")bool

=`true`

Sticky to monitor[`[scratchpad].unfocus`i](#config-unfocus "More details below")strAction on unfocus ('hide' or empty)[`[scratchpad].hysteresis`i](#config-hysteresis "More details below")float

=`0.4`

Delay before unfocus hide[`[scratchpad].excludes`i](#config-excludes "More details below")listScratches to hide when shown[`[scratchpad].restore_excluded`i](#config-restore-excluded "More details below")bool

=`false`

Restore excluded on hide[`[scratchpad].preserve_aspect`i](#config-preserve-aspect "More details below")bool

=`false`

Keep size/position across shows[`[scratchpad].hide_delay`i](#config-hide-delay "More details below")float

=`0`

Delay before hide animation[`[scratchpad].force_monitor`i](#config-force-monitor "More details below")strAlways show on specific monitor[`[scratchpad].alt_toggle`i](#config-alt-toggle "More details below")bool

=`false`

Alternative toggle for multi-monitor[`[scratchpad].allow_special_workspaces`i](#config-allow-special-workspaces "More details below")bool

=`true`

Allow over special workspaces[`[scratchpad].smart_focus`i](#config-smart-focus "More details below")bool

=`true`

Restore focus on hide[`[scratchpad].close_on_hide`i](#config-close-on-hide "More details below")bool

=`false`

Close instead of hide

Advanced (1)

OptionDescription[`[scratchpad].use`i](#config-use "More details below")strInherit from another scratchpad definition

Overrides (1)

OptionDescription[`[scratchpad].monitor`i](#config-monitor "More details below")dictPer-monitor config overrides

### `use` str [​](#config-use)

### `pinned` bool=`true` [​](#config-pinned)

Makes the scratchpad "sticky" to the monitor, following any workspace change.

### `excludes` list [​](#config-excludes)

List of scratchpads to hide when this one is displayed, eg: `excludes = ["term", "volume"]`. If you want to hide every displayed scratch you can set this to the string `"*"` instead of a list: `excludes = "*"`.

### `restore_excluded` bool=`false` [​](#config-restore-excluded)

When enabled, will remember the scratchpads which have been closed due to `excludes` rules, so when the scratchpad is hidden, those previously hidden scratchpads will be shown again.

### `unfocus` str [​](#config-unfocus)

When set to `"hide"`, allow to hide the window when the focus is lost.

Use `hysteresis` to change the reactivity

### `hysteresis` float=`0.4` [​](#config-hysteresis)

Controls how fast a scratchpad hiding on unfocus will react. Check `unfocus` option. Set to `0` to disable.

IMPORTANT

Only relevant when `unfocus="hide"` is used.

### `preserve_aspect` bool=`false` [​](#config-preserve-aspect)

When set to `true`, will preserve the size and position of the scratchpad when called repeatedly from the same monitor and workspace even though an `animation` , `position` or `size` is used (those will be used for the initial setting only).

Forces the `lazy` option.

### `offset` str=`"100%"` [​](#config-offset)

Number of pixels for the **hide** sliding animation (how far the window will go).

TIP

- It is also possible to set a string to express percentages of the client window
- `margin` is automatically added to the offset

### `hide_delay` float=`0` [​](#config-hide-delay)

### `force_monitor` str [​](#config-force-monitor)

If set to some monitor name (eg: `"DP-1"`), it will always use this monitor to show the scratchpad.

### `alt_toggle` bool=`false` [​](#config-alt-toggle)

When enabled, use an alternative `toggle` command logic for multi-screen setups. It applies when the `toggle` command is triggered and the toggled scratchpad is visible on a screen which is not the focused one.

Instead of moving the scratchpad to the focused screen, it will hide the scratchpad.

### `allow_special_workspaces` bool=`true` [​](#config-allow-special-workspaces)

When enabled, you can toggle a scratchpad over a special workspace. It will always use the "normal" workspace otherwise.

NOTE

Can't be disabled when using *Hyprland* &lt; 0.39 where this behavior can't be controlled.

### `smart_focus` bool=`true` [​](#config-smart-focus)

When enabled, the focus will be restored in a best effort way as an attempt to improve the user experience. If you face issues such as spontaneous workspace changes, you can disable this feature.

### `close_on_hide` bool=`false` [​](#config-close-on-hide)

When enabled, the window in the scratchpad is closed instead of hidden when `pypr hide <name>` is run. This option implies `lazy = true`. This can be useful on laptops where background apps may increase battery power draw.

Note: Currently this option changes the hide animation to use hyprland's close window animation.

### `monitor` dict [​](#config-monitor)