---
title: Status bars
url: https://wiki.hypr.land/Useful-Utilities/Status-Bars/
source: sitemap
fetched_at: 2026-04-26T09:47:28.66730148-03:00
rendered_js: false
word_count: 871
summary: This document provides an overview and configuration guide for various status bar and widget system tools compatible with the Hyprland Wayland compositor.
tags:
    - hyprland
    - wayland
    - waybar
    - desktop-customization
    - widgets
    - linux-desktop
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Simple status bars

### Waybar

[Waybar](https://github.com/Alexays/Waybar) is a GTK status bar for wlroots compositors with native Hyprland support. Install via your distro's package manager.

Copy config files from `/etc/xdg/waybar/` to `~/.config/waybar/`.

For workspaces, replace `sway/workspaces` with `hyprland/workspaces` and `sway/mode` with `hyprland/submap`.

See [The Waybar Wiki](https://github.com/Alexays/Waybar/wiki/Module:-Hyprland) for more.

#### Launching

Add to Hyprland config:

```ini
exec-once = waybar
```

Or use the Waybar systemd service with [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start):

```ini
systemctl --user enable --now waybar.service
```

#### FAQ

**Active workspace doesn't show up**

Replace `#workspaces button.focused` with `#workspaces button.active` in `~/.config/waybar/style.css`.

**Scrolling through workspaces**

```json
"hyprland/workspaces": {
     "format": "{icon}",
     "on-scroll-up": "hyprctl dispatch workspace e+1",
     "on-scroll-down": "hyprctl dispatch workspace e-1"
}
```

**Window title is missing**

The prefix is `hyprland` not `wlr`:

```json
"modules-center": ["hyprland/window"],
```

For multiple monitors:

```json
"hyprland/window": {
    "separate-outputs": true
},
```

### ashell

[ashell](https://malpenzibo.github.io/ashell/) is a ready-to-go Wayland status bar for Hyprland.

- Ready to use out of the box with essential modules (workspaces, time, battery, network, etc.)
- Powered by iced (cross-platform Rust GUI library)
- Limited configuration — fast setup but some waybar tweaks not possible
- Calendar absent but [on the roadmap](https://github.com/MalpenZibo/ashell/issues/181)

Workaround for calendar:

```toml
[modules]
center = [ "calendar", "Clock" ]
# ...
[[CustomModule]]
name = "calendar"
icon = ""
command = "zenity --calendar --title=\"Calendar\""
```

## Widget systems

For fully customizable menus, write code. Popular options:

| Tool | Language | UI Framework |
|------|----------|--------------|
| [AGS/Astal](https://aylur.github.io/astal/) | JS(X)/TS | GTK 3/4 |
| [EWW](https://elkowar.github.io/eww/) | Yuck (Lisp) | GTK 3 |
| [Quickshell](https://quickshell.outfoxxed.me/) | QML | Qt |

### AGS/Astal

- [Astal](https://aylur.github.io/astal/) — suite for desktop shells and Wayland widgets with GTK
- [AGS](https://aylur.github.io/ags/) — scaffolding for Astal with TypeScript/JavaScript(X)

See [installation instructions](https://aylur.github.io/astal/guide/installation) and [examples](https://aylur.github.io/astal/guide/introduction#supported-languages). For AGS: [Quick start](https://aylur.github.io/ags/guide/quick-start.html).

**Advantages:**
- Language flexibility (any language with [Gobject Introspection](https://en.wikipedia.org/wiki/List_of_language_bindings_for_GTK))
- Large library set including Network (Wi-Fi/Ethernet) and Bluetooth

**Disadvantages:**
- No hot reload out of the box

### Eww

[Eww](https://github.com/elkowar/eww) (ElKowar's Wacky Widgets) is a Rust + GTK widget system for custom widgets, similar to AwesomeWM but independent of window manager.

Install via distro package manager (`eww-wayland`) or [compile manually](https://elkowar.github.io/eww).

**Advantages:**
- Simple Lisp-like config syntax
- Built-in SCSS styling

**Disadvantages:**
- Heavy reliance on external scripts (few built-in libraries)
- GTK 3 only (no GPU acceleration)
- Overhead from external scripts and unnecessary component recreations

**Configuration:** Examples in the [Readme](https://github.com/elkowar/eww) and [Configuration options](https://elkowar.github.io/eww/configuration.html).

#### Example widgets

**Workspaces widget** — displays workspaces 1-10, clickable to jump, scrollable to cycle. Different styles for current/occupied/empty workspaces. Requires: bash, awk, stdbuf, grep, seq, socat, jq, Python 3.

`~/.config/eww.yuck`:

```lisp
...
(deflisten workspaces :initial "[]" "bash ~/.config/eww/scripts/get-workspaces")
(deflisten current_workspace :initial "1" "bash ~/.config/eww/scripts/get-active-workspace")
(defwidget workspaces []
  (eventbox :onscroll "bash ~/.config/eww/scripts/change-active-workspace {} ${current_workspace}" :class "workspaces-widget"
    (box :space-evenly true
      (label :text "${workspaces}${current_workspace}" :visible false)
      (for workspace in workspaces
        (eventbox :onclick "hyprctl dispatch workspace ${workspace.id}"
          (box :class "workspace-entry ${workspace.windows > 0 ? "occupied" : "empty"}"
            (label :text "${workspace.id}" :class "workspace-entry ${workspace.id == current_workspace ? "current" : ""}" )
            )
          )
        )
      )
    )
  )
...
```

`~/.config/eww/scripts/change-active-workspace`:

```sh
#!/usr/bin/env bash
function clamp {
  min=$1
  max=$2
  val=$3
  python -c "print(max($min, min($val, $max)))"
}
direction=$1
current=$2
if test "$direction" = "down"
then
  target=$(clamp 1 10 $(($current+1)))
  echo "jumping to $target"
  hyprctl dispatch workspace $target
elif test "$direction" = "up"
then
  target=$(clamp 1 10 $(($current-1)))
  echo "jumping to $target"
  hyprctl dispatch workspace $target
fi
```

`~/.config/eww/scripts/get-active-workspace`:

```sh
#!/usr/bin/env bash
hyprctl monitors -j | jq '.[] | select(.focused) | .activeWorkspace.id'
socat -u UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock - |
  stdbuf -o0 awk -F '>>|,' -e '/^workspace>>/ {print $2}' -e '/^focusedmon>>/ {print $3}'
```

`~/.config/eww/scripts/get-workspaces`:

```sh
#!/usr/bin/env bash
spaces (){
  WORKSPACE_WINDOWS=$(hyprctl workspaces -j | jq 'map({key: .id | tostring, value: .windows}) | from_entries')
  seq 1 10 | jq --argjson windows "${WORKSPACE_WINDOWS}" --slurp -Mc 'map(tostring) | map({id: ., windows: ($windows[.]//0)})'
}
spaces
socat -u UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock - | while read -r line; do
  spaces
done
```

**Active window title widget** — displays the active window title. Requires: awk, stdbuf, socat, jq.

`~/.config/eww/eww.yuck`:

```lisp
...
(deflisten window :initial "..." "sh ~/.config/eww/scripts/get-window-title")
(defwidget window_w []
  (box
    (label :text "${window}"
    )
  )
...
```

`~/.config/eww/scripts/get-window-title`:

```sh
#!/bin/sh
hyprctl activewindow -j | jq --raw-output .title
socat -u UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock - | stdbuf -o0 awk -F '>>|,' '/^activewindow>>/{print $3}'
```

### Quickshell

[Quickshell](https://quickshell.outfoxxed.me/) is a flexible QtQuick-based desktop shell toolkit. Styles independently despite Qt theming challenges.

See [setup instructions](https://quickshell.outfoxxed.me/docs/configuration/getting-started/) and [guided hello world](https://quickshell.outfoxxed.me/docs/configuration/intro/).

**Advantages:**
- Advanced Wayland/Hyprland integrations (live window previews)
- Auto-reloads config on changes

**Disadvantages:**
- Qt positioning less intuitive than GTK
- No Wi-Fi service yet
- Alpha status — minor breaking changes expected
- Styles declared with components instead of CSS

## Tips

### Blur

Use `blur` and `ignore_alpha` [layer rules](https://wiki.hypr.land/Configuring/Window-Rules/#layer-rules). `blur` enables blur. `ignore_alpha` makes the bar ignore insufficiently opaque regions — value should be higher than shadow opacity and lower than bar/menu content opacity. For transparent popups, use `blur_popups` rule.
