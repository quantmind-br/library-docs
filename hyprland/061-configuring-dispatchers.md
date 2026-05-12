---
title: Dispatchers
url: https://wiki.hypr.land/Configuring/Dispatchers/
source: sitemap
fetched_at: 2026-04-26T09:48:06.691285679-03:00
rendered_js: false
word_count: 1870
summary: Reference for Hyprland dispatchers and parameter types — window management, workspace control, groups, signals, and execution rules.
tags:
    - hyprland
    - dispatchers
    - window-management
    - wayland-compositor
    - configuration-reference
category: reference
optimized: true
optimized_at: 2026-04-26T18:00:00.000Z
---

> [!info]
>Layout-specific dispatchers are listed on their layout pages (see sidebar).

## Parameter Types

| Type | Description |
|---|---|
| `window` | Window spec: class regex (default), `class:`, `initialclass:`, `title:`, `initialtitle:`, `tag:`, `pid:`, `address:`, `activewindow`, `floating`, `tiled` |
| `workspace` | See [[#workspaces]] |
| `direction` | `l`, `r`, `u`, `d` (left, right, up, down) |
| `monitor` | Direction, ID, name, `current`, or relative (`+1`, `-1`) |
| `resize` | Pixel delta vec2 (`10 -10`), % of window size (`20 25%`), or `exact` + vec2/percentage |
| `floatvalue` | Relative float delta (`-0.2`, `+0.2`) or `exact` + value |
| `zheight` | `top` or `bottom` |
| `mod` | `SUPER`, `SUPER_ALT`, etc. |
| `key` | `g`, `code:42`, `42`, or mouse clicks (`mouse:272`) |

## List of Dispatchers

| Dispatcher | Description | Params |
|---|---|---|
| `exec` | Execute shell command (supports rules) | command |
| `execd` | Execute raw shell command (no rules) | command |
| `pass` | Pass key (with mods) to a specified window | mod, key\[, window] |
| `sendshortcut` | Send keys (with mods) to a window | key, mod\[, window] |
| `sendkeystate` | Send key with specific state (down/repeat/up) | mod, key, state, window |
| `killactive` | Close (not kill) active window | none |
| `forcekillactive` | Kill active window | none |
| `closewindow` | Close specified window | window |
| `killwindow` | Kill specified window | window |
| `signal` | Send signal to active window | signal |
| `signalwindow` | Send signal to specified window | `window,signal`, e.g. `class:Alacritty,9` |
| `workspace` | Change workspace | workspace |
| `movetoworkspace` | Move focused window to workspace | `workspace` or `workspace,window` |
| `movetoworkspacesilent` | Same as above, without switching | `workspace` or `workspace,window` |
| `togglefloating` | Toggle current window's floating | `active` or current, `window` for specific |
| `setfloating` | Set floating on | `active` or current, `window` for specific |
| `settiled` | Set floating off | `active` or current, `window` for specific |
| `fullscreen` | Set fullscreen mode | `mode action` (`mode`: 0 fullscreen, 1 maximize; `action`: `toggle` default, `set`, `unset`) |
| `fullscreenstate` | Set Hyprland + client fullscreen state | `internal client action` (`-1`: current, `0`: none, `1`: maximize, `2`: fullscreen, `3`: maximize+fullscreen) |
| `dpms` | Set DPMS | `on`, `off`, `toggle` (add monitor name for specific) |
| `forceidle` | Set idle timers | floatvalue (seconds) |
| `pin` | Pin window to all workspaces | `active` or current, `window` for specific |
| `movefocus` | Move focus in direction | direction |
| `movewindow` | Move active window in direction/to monitor | direction or `mon:` + monitor + `silent` |
| `swapwindow` | Swap active window with another | direction or `window` |
| `centerwindow` | Center active window | none (or 1 for monitor center respecting reserved area) |
| `resizeactive` | Resize active window | resizeparams |
| `moveactive` | Move active window | resizeparams |
| `resizewindowpixel` | Resize selected window | `resizeparams,window` |
| `movewindowpixel` | Move selected window | `resizeparams,window` |
| `cyclenext` | Focus next window | `next`/`prev`, `tiled`, `floating`, `visible`, `visible next floating hist` |
| `swapnext` | Swap with next window on workspace | `next`/`prev` |
| `tagwindow` | Apply tag to window | `tag [window]`, e.g. `+code ^(foot)$` |
| `focuswindow` | Focus first window matching | window |
| `focusmonitor` | Focus monitor | monitor |
| `movecursortocorner` | Move cursor to corner | direction (0-3: bottom-left=0, bottom-right=1, top-right=2, top-left=3) |
| `movecursor` | Move cursor to position | `x y` |
| `renameworkspace` | Rename workspace | `id name`, e.g. `2 work` |
| `exit` | Exit compositor (use [[008-hypr-ecosystem-hyprshutdown| hyprshutdown]] instead) | none |
| `forcerendererreload` | Reload all resources and outputs | none |
| `movecurrentworkspacetomonitor` | Move active workspace to monitor | monitor |
| `focusworkspaceoncurrentmonitor` | Focus workspace on current monitor (swaps current workspace to other monitor) | workspace |
| `moveworkspacetomonitor` | Move workspace to monitor | `workspace monitor` |
| `swapactiveworkspaces` | Swap active workspaces between monitors | two monitors |
| `bringactivetotop` | *Deprecated* — use alterzorder | none |
| `alterzorder` | Modify window stack order | `zheight[,window]` |
| `togglespecialworkspace` | Toggle special workspace | none (first) or name |
| `focusurgentorlast` | Focus urgent or last window | none |
| `togglegroup` | Toggle window into group | none |
| `changegroupactive` | Switch to next window in group | `b` (back), `f` (forward), or index |
| `focuscurrentorlast` | Switch focus from current to previously focused | none |
| `lockgroups` | Lock/unlock/toggle all groups | `lock`/`unlock`/`toggle` |
| `lockactivegroup` | Lock/unlock/toggle focused group | `lock`/`unlock`/`toggle` |
| `moveintogroup` | Move window into group in direction | direction |
| `moveintoorcreategroup` | Move window into group or create group first | direction |
| `moveoutofgroup` | Move window out of group | `active` or current, `window` for specific |
| `movewindoworgroup` | `moveintogroup` if group in direction, else `moveoutofgroup` if no group, else `movewindow` | direction |
| `movegroupwindow` | Swap with next/previous in group | `b` (back) or forward |
| `denywindowfromgroup` | Prohibit window from group | `on`, `off`, `toggle` |
| `setignoregrouplock` | Toggle `binds:ignore_group_lock` | `on`, `off`, `toggle` |
| `global` | Global Shortcut via GlobalShortcuts portal | name (see [[012-configuring-binds#dbus-global-shortcuts]]) |
| `submap` | Change mapping group | `reset` or name |
| `event` | Emit custom event to socket2 | data |
| `setprop` | Set window property | `window property value` |
| `toggleswallow` | Unswallow/reattach swallowed window | none |

> [!warning]
>[uwsm](https://wiki.hypr.land/Useful-Utilities/Systemd-start) users: avoid `exit` dispatcher; use `exec, uwsm stop` or `exec, loginctl terminate-user ""` for graceful shutdown. Replace `exit` in `hyprland.conf` keybinds.

> [!warning]
>Do not set DPMS or `forceidle` directly with a keybind — causes undefined behavior. Instead:
```ini
bind = MOD, KEY, exec, sleep 1 && hyprctl dispatch dpms off
```

### Grouped (Tabbed) Windows

`togglegroup` creates a group from the active window (like i3wm's "tabbed" container). Use `changegroupactive` to switch windows within the group.

Group border colors configurable via `col.` settings in the `group` config section.

`lockactivegroup` prevents new windows entering the focused group; `lockgroups` toggles global group lock.

`denywindowfromgroup` prevents a window from being added to or becoming a group. `movewindoworgroup` behaves like `movewindow` if the window has this property.

## Workspaces

Nine choices:

- **ID** — `1`, `2`, `3`
- **Relative ID** — `+1`, `-3`, `+100`
- **Workspace on monitor** — `m+1`, `m-2`, `m~3`
- **Workspace on monitor (including empty)** — `r+1`, `r~3`
- **Open workspace** — `e+1`, `e-10`, `e~2`
- **Name** — `name:Web`, `name:Anime`, `name:Better anime`
- **Previous** — `previous`, `previous_per_monitor`
- **First empty** — `empty` (suffix `m` for monitor-only, `n` for next; e.g. `emptynm`)
- **Special** — `special` or `special:name`

> [!warning]
>`special` only supported on `movetoworkspace` and `movetoworkspacesilent`. Other dispatchers = undocumented behavior.

> [!warning]
>Numerical workspaces must be between `1` and `2147483647` (inclusive). `0` and negative numbers not allowed.

## Special Workspace

A special workspace is a "scratchpad" — toggle on/off on any monitor. Limited to 97 named special workspaces.

```ini
bind = SUPER, C, movetoworkspace, special
# SUPER + C moves window to special workspace
# Use togglespecialworkspace to reveal hidden window
```

## Executing with Rules

`exec` records the spawned process PID and filters by it. Forked processes opening windows may not match.

```ini
bind = mod, key, exec, [rules...] command
bind = SUPER, E, exec, [workspace 2 silent; float; move 0 0] kitty
```

### setprop

Props are any *dynamic effects* from [[048-configuring-window-rules#dynamic-effects | Window Rules]]:

```sh
address:0x13371337 no_anim 1
address:0x13371337 no_max_size 0
address:0x13371337 opaque toggle
address:0x13371337 immediate unset
address:0x13371337 border_size relative -2
address:0x13371337 rounding_power relative 0.1
```

Props expanded from window rule parents:

- `border_color` -> `active_border_color`, `inactive_border_color`
- `opacity` -> `opacity`, `opacity_inactive`, `opacity_fullscreen`, `opacity_override`, `opacity_inactive_override`, `opacity_fullscreen_override`

### fullscreenstate

`fullscreenstate internal client`

Decouples Hyprland's internal fullscreen state from what the client receives.

| Value | State | Description |
|---|---|---|
| -1 | Current | Maintains current fullscreen state |
| 0 | None | Window allocates space defined by current layout |
| 1 | Maximize | Window takes entire working space, keeping margins |
| 2 | Fullscreen | Window takes entire screen |
| 3 | Maximize + Fullscreen | Fullscreened maximized window (same as fullscreen) |

`fullscreenstate 2 0` — Fullscreen app but keep client non-fullscreen (prevents Chromium-based browsers from entering presentation mode).

`fullscreenstate 0 2` — Window non-fullscreen but client in fullscreen mode within window.

#dispatchers #window-management #wayland-compositor #configuration-reference
