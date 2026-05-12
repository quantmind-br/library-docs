---
title: hypridle
url: https://wiki.hypr.land/Hypr-Ecosystem/hypridle/
source: sitemap
fetched_at: 2026-04-26T09:47:51.01951336-03:00
rendered_js: false
word_count: 323
summary: This document provides configuration instructions and parameter definitions for hypridle, the idle management daemon for the Hyprland compositor.
tags:
    - hyprland
    - idle-daemon
    - linux-desktop
    - configuration
    - system-management
    - wayland
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

hypridle is Hyprland's idle management daemon.

## Configuration

Config file: `~/.config/hypr/hypridle.conf`. A config file is required — hypridle won't start without one.

To start at boot, add `exec-once = hypridle` to `hyprland.conf`. With [uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start), use `systemctl --user enable --now hypridle.service`.

### General

| Variable | Description | Type | Default |
|---|---|---|---|
| `lock_cmd` | Command on dbus lock event (e.g. `loginctl lock-session`) | string | empty |
| `unlock_cmd` | Command on dbus unlock event | string | empty |
| `on_lock_cmd` | Command when session gets locked by a lock screen app | string | empty |
| `on_unlock_cmd` | Command when session gets unlocked | string | empty |
| `before_sleep_cmd` | Command on dbus prepare_sleep event | string | empty |
| `after_sleep_cmd` | Command on dbus post prepare_sleep event | string | empty |
| `ignore_dbus_inhibit` | Ignore dbus-sent idle inhibit events (e.g. Firefox) | bool | `false` |
| `ignore_systemd_inhibit` | Ignore `systemd-inhibit --what=idle` inhibitors | bool | `false` |
| `ignore_wayland_inhibit` | Ignore Wayland protocol idle inhibitors | bool | `false` |
| `inhibit_sleep` | Sleep inhibition mode | int | `2` |

`inhibit_sleep` options:
- `0` — disable sleep inhibition
- `1` — wait until `general:before_sleep_cmd` completes
- `2` (auto) — select `3` or `1` based on whether hyprlock is detected before sleep
- `3` — wait until the session lock app locks (works with all wayland session-lock apps)

> [!note]
> `general:inhibit_sleep` ensures hypridle runs `before_sleep_cmd` before the system sleeps.

### Listeners

Listeners define actions on idleness. Each listener has a `timeout` (seconds). When timeout fires, `on-timeout` runs. When activity resumes, `on-resume` runs.

```ini
listener {
    timeout = 500                            # in seconds.
    on-timeout = notify-send "You are idle!" # command to run when timeout has passed.
    on-resume = notify-send "Welcome back!"  # command to run when activity is detected after timeout has fired.
}
```

| Variable | Description | Type | Default |
|---|---|---|---|
| `timeout` | Idle time in seconds | int | required |
| `on-timeout` | Command when timeout fires | string | empty |
| `on-resume` | Command when activity resumes | string | empty |
| `ignore_inhibit` | Ignore all idle inhibitors for this rule | bool | `false` |

### Examples

Full hypridle example with hyprlock:

```ini
general {
    lock_cmd = pidof hyprlock || hyprlock       # avoid starting multiple hyprlock instances.
    before_sleep_cmd = loginctl lock-session    # lock before suspend.
    after_sleep_cmd = hyprctl dispatch dpms on  # to avoid having to press a key twice to turn on the display.
}
listener {
    timeout = 150                                # 2.5min.
    on-timeout = brightnessctl -s set 10         # set monitor backlight to minimum, avoid 0 on OLED monitor.
    on-resume = brightnessctl -r                 # monitor backlight restore.
}
# turn off keyboard backlight, comment out this section if you dont have a keyboard backlight.
listener { 
    timeout = 150                                          # 2.5min.
    on-timeout = brightnessctl -sd rgb:kbd_backlight set 0 # turn off keyboard backlight.
    on-resume = brightnessctl -rd rgb:kbd_backlight        # turn on keyboard backlight.
}
listener {
    timeout = 300                                 # 5min
    on-timeout = loginctl lock-session            # lock screen when timeout has passed
}
listener {
    timeout = 330                                                     # 5.5min
    on-timeout = hyprctl dispatch dpms off                            # screen off when timeout has passed
    on-resume = hyprctl dispatch dpms on && brightnessctl -r          # screen on when activity is detected after timeout has fired.
}
listener {
    timeout = 1800                                # 30min
    on-timeout = systemctl suspend                # suspend pc
}
```

[[054-hypr-ecosystem-hyprlauncher|hyprlauncher]] [[007-hypr-ecosystem-hyprlock|hyprlock]]

Last updated on April 20, 2026