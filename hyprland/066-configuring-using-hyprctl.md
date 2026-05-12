---
title: Using hyprctl
url: https://wiki.hypr.land/Configuring/Using-hyprctl/
source: sitemap
fetched_at: 2026-04-26T09:49:18.895111576-03:00
rendered_js: false
word_count: 671
summary: This document provides a comprehensive reference for the hyprctl command-line utility, which is used to control and query the Hyprland compositor.
tags:
    - hyprland
    - cli
    - compositor
    - linux
    - ipc
    - system-configuration
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

`hyprctl` controls compositor parts from CLI or script. Automatically installed with Hyprland.

> [!warning]
> *hyprctl* calls are dispatched *synchronously* by the compositor. Spam causes slowdowns. Use `--batch` for many calls, and limit info calls. For live event handling, see the [socket2](https://wiki.hypr.land/IPC/) page.

## Commands

### dispatch

Issue a dispatch to call a keybind dispatcher with an argument. For dispatchers without parameters, pass any argument.

To pass an argument starting with `-` or `--`, pass `--` first to disable option parsing:

```sh
hyprctl dispatch exec kitty
hyprctl dispatch -- exec kitty --single-instance
hyprctl dispatch pseudo x
```

Returns: `ok` on success, error message on fail.

See [[061-configuring-dispatchers|Dispatchers]] for a list.

### keyword

Issue a config keyword dynamically:

```sh
hyprctl keyword bind SUPER,O,pseudo
hyprctl keyword general:border_size 10
hyprctl keyword monitor DP-3,1920x1080@144,0x0,1
```

Returns: `ok` on success, error message on fail.

### reload

Force reload the config.

### kill

Enter kill mode — click an app to kill it. Exit with ESCAPE. Like xkill.

### setcursor

Sets cursor theme and reloads cursor manager. Sets theme for everything except GTK.

> [!note]
> Since 0.37.0, only accepts hyprcursor themes. For legacy xcursor themes, use `XCURSOR_THEME` and `XCURSOR_SIZE` env vars.

```sh
hyprctl setcursor Bibata-Modern-Classic 24
```

### output

Add and remove fake outputs:

```sh
hyprctl output create [backend] [name]
hyprctl output remove [name]
```

`backend` options:

- `wayland` — creates a Wayland window (only works with Wayland backend)
- `headless` — headless monitor (for VNC/RDP/Sunshine servers)
- `auto` — auto-picks backend (e.g. TTY → `headless`)

`create`/`remove` can also be `add`/`destroy`.

```sh
hyprctl output create headless test
hyprctl output remove test
```

### switchxkblayout

Set the xkb layout index for a keyboard. Given:

```ini
device {
    name = my-epic-keyboard-v1
    kb_layout = us,pl,de
}
```

Switch between them:

```sh
hyprctl switchxkblayout [DEVICE] [CMD]
```

`CMD`: `next`, `prev`, or `ID` (0=us, 1=pl, 2=de). Find DEVICE with `hyprctl devices`. DEVICE can also be `current` or `all`.

```sh
hyprctl switchxkblayout at-translated-set-2-keyboard next
```

> [!note]
> For a single variant (e.g. `pl/dvorak` on one layout, `us/qwerty` on another), xkb params can be blank if comma-count matches. Alternatively, a single parameter applies to all.

```ini
input {
    kb_layout = pl,us,ru
    kb_variant = dvorak,,
    kb_options = caps:ctrl_modifier
}
```

### seterror

Sets the hyprctl error string. Resets when config is reloaded:

```sh
hyprctl seterror 'rgba(66ee66ff)' hello world this is my problem
```

To disable: (no arguments needed in original — likely a typo)

### getprop

Gets a window property value:

```sh
hyprctl getprop [window] [property]
```

`window` is described [here](https://wiki.hypr.land/Configuring/Dispatchers#parameter-explanation). `property` is any that can be set with [setprop](https://wiki.hypr.land/Configuring/Dispatchers/#setprop).

> [!note]
> - If `animationstyle` is unset, `(unset)` is returned
> - `min_size` defaults to `20 20`
> - `max_size` defaults to `inf inf` or `[null,null]` in JSON

### notify

Sends a notification:

```sh
hyprctl notify [ICON] [TIME_MS] [COLOR] [MESSAGE]
```

Example:

```sh
hyprctl notify -1 10000 "rgb(ff1ea3)" "Hello everyone!"
```

Icon `-1` means "No icon". Color `0` means "Default color for icon".

Icon list:

```sh
WARNING = 0
INFO = 1
HINT = 2
ERROR = 3
CONFUSED = 4
OK = 5
```

Font size: append `fontsize:35` to message. Default font-size is 13.

### dismissnotify

Dismisses notifications:

```sh
hyprctl dismissnotify # dismiss all
hyprctl dismissnotify 2 # dismiss oldest 2
hyprctl dismissnotify -1 # dismiss all (same as no arguments)
```

## Info commands

```plain
version          — Hyprland version, flags, commit, branch
monitors         — active outputs (use 'monitors all' for inactive)
workspaces       — all workspaces with properties
activeworkspace — active workspace properties
workspacerules   — defined workspace rules
clients          — all windows with properties
devices          — connected keyboards and mice
decorations [window] — decorations info
binds            — registered binds
activewindow     — active window name and properties
layers           — all layers
splash           — current random splash
getoption [option] — config option status
cursorpos        — cursor position in global layout
animations       — configured animations and beziers
instances        — running Hyprland instances
layouts          — available layouts (including plugins)
configerrors     — config parsing errors
rollinglog       — tail of log (supports -f/--follow)
locked           — whether session is locked
descriptions     — JSON with all config options, descriptions, types
submap           — current keybind submap
```

Getoption example:

```sh
hyprctl getoption general:border_size
hyprctl getoption input:touchpad:disable_while_typing
```

See [[067-configuring-variables|Variables]] for sections and options.

## Batch

Use `--batch` for multiple commands:

```sh
hyprctl --batch "keyword general:border_size 2 ; keyword general:gaps_out 20"
```

Commands separated by `;`.

## Flags

```txt
j -> output in JSON
i -> select instance (id or index in hyprctl instances)
```
