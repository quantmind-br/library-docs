---
title: Binds
url: https://wiki.hypr.land/Configuring/Binds/
source: sitemap
fetched_at: 2026-04-26T09:47:56.560079026-03:00
rendered_js: false
word_count: 1564
summary: Configuration guide for keyboard and mouse bindings in Hyprland — syntax, modifier flags, submaps, mouse binds, global keybinds, and troubleshooting.
tags:
    - hyprland
    - configuration
    - keybinds
    - window-manager
    - linux
    - input-mapping
category: guide
optimized: true
optimized_at: 2026-04-26T18:00:00.000Z
---

## Basic

```ini
bind = MODS, key, dispatcher, params
```

Example:

```ini
bind = SUPER_SHIFT, Q, exec, firefox
```

`SUPER + SHIFT + Q` opens Firefox.

> [!note]
>For binding without a modkey, leave it empty:
```ini
bind = , Print, exec, grim
```

See [[067-configuring-variables| Variables]] for mod list. See [[061-configuring-dispatchers| Dispatchers]] for dispatcher list.

### Comma Syntax

`bind` requires exactly 4 arguments (3 commas):

```ini
bind = MODS, key, dispatcher, params
#      1     2    3          4
```

> [!note]
>Trailing commas make the last argument include the comma itself (e.g. `firefox,` instead of `firefox`):
```ini
bind = SUPER, F, exec, firefox   # OK
bind = , Print, exec, grim       # OK (empty first = no modifier)
bind = SUPER, F, exec, firefox,  # WRONG - exec `firefox,`
bind = SUPER, Tab, cyclenext,    # OK (empty last arg)
```

> [!warning]
>An accidental trailing comma becomes part of the argument. Check for trailing commas if a keybind is not working!

## Binding with Keycode

Use [xkbcommon-keysyms.h](https://github.com/xkbcommon/libxkbcommon/blob/master/include/xkbcommon/xkbcommon-keysyms.h) — use the segment after `XKB_KEY_`. For keycode, use `code:` prefix:

```ini
bind = SUPER, code:28, exec, amongus
```

(SUPER + t since t is keycode 28)

> [!note]
>Use [`wev`](https://github.com/jwrdegoede/wev) to find a key's name or keycode.

## Workspace Bindings on Non-QWERTY Layouts

Keybinds need keys accessible without modifiers in your layout. For [French AZERTY](https://en.wikipedia.org/wiki/AZERTY), `SHIFT + unmodified key` types `0-9`, so workspace keybinds must use the unmodified key names.

> [!note]
>Get the unmodified key name from the [keycode section](#binding-with-keycode).

```ini
# WRONG on French layout:
# bind = $mainMod, 1, workspace, 1
# RIGHT:
bind = $mainMod, ampersand, workspace, 1
```

See [Hyprland French AZERTY layout guide](https://rherault.dev/articles/hyprland-fr-layout).

### Unbind

```bash
hyprctl keyword unbind SUPER, O
```

> [!note]
>`unbind` key is case-sensitive — must exactly match the original `bind`:

```ini
bind = SUPER, TAB, workspace, e+1
unbind = SUPER, Tab # NO
unbind = SUPER, TAB # YES
```

## Bind Flags

Format: `bind[flag] = MOD, KEY, dispatcher, params`

Available flags:

| Flag | Name | Description |
|---|---|---|
| `l` | locked | Works when an input inhibitor (e.g. lockscreen) is active |
| `r` | release | Triggers on key release |
| `c` | click | Triggers on release inside `binds:drag_threshold` |
| `g` | drag | Triggers on release outside `binds:drag_threshold` |
| `o` | long press | Triggers on long press |
| `e` | repeat | Repeats when held |
| `n` | non-consuming | Events passed to active window + dispatcher fires |
| `m` | mouse | See [[#mouse-binds]] |
| `t` | transparent | Cannot be shadowed by other binds |
| `i` | ignore mods | Ignores modifiers |
| `s` | separate | Arbitrarily combine keys between mods/keys — see [[#keysym-combos]] |
| `d` | description | Allows writing a description for the bind |
| `p` | bypass | Bypasses app's requests to inhibit keybinds |
| `u` | submap universal | Active no matter the submap |
| `k` | per-device | Allow binds per device — see [[#per-device-binds]] |

Examples:

```ini
binde = , XF86AudioRaiseVolume, exec, wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+
bindl = , XF86AudioLowerVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-
bindr = SUPER, SUPER_L, exec, pkill wofi || wofi
bindd = SUPER, Q, Open my favourite terminal, exec, kitty
bindo = SUPER, XF86AudioNext, exec, playerctl next
bind = SUPER, XF86AudioNext, exec, playerctl position +5
```

### Mouse Buttons

```ini
bind = SUPER, mouse:272, exec, amongus  # SUPER + LMB
```

### Modkeys Only

Use TARGET modmask with the `r` flag:

```ini
bindr = SUPER ALT, Alt_L, exec, amongus  # SUPER + ALT
```

### Keysym Combos

Separate keysyms with `&`, use the `s` flag:

```ini
binds = Control_L, A&Z, exec, kitty
binds = Control_L&Shift_L, K, exec, kitty
binds = Control_R&Super_R&Alt_L, J&K&L, exec, kitty
binds = Escape&Apostrophe&F7, T&O&A&D, exec, battletoads 2: retoaded
```

> [!note]
>Only valid for keysyms; all mods become keysyms. Use `wev` to find keysym names.

### Mouse Wheel

```ini
bind = SUPER, mouse_down, workspace, e-1
```

> [!note]
>Control reset time with `binds:scroll_event_delay`.

### Switches

```ini
# Toggle
bindl = , switch:[switch name], exec, swaylock
# Turning on
bindl = , switch:on:[switch name], exec, hyprctl keyword monitor "eDP-1, disable"
# Turning off
bindl = , switch:off:[switch name], exec, hyprctl keyword monitor "eDP-1, 2560x1600, 0x0, 1"
```

> [!warning]
>Systemd `HandleLidSwitch` in `logind.conf` may conflict with Hyprland lid switch configs.

> [!note]
>View switches with `hyprctl devices`.

### Multiple Binds Per Key

```ini
bind = SUPER, Tab, cyclenext
bind = SUPER, Tab, bringactivetotop
```

> [!warning]
>Actions execute top-to-bottom in file order.

### Description

Use the `d` flag. Description goes before dispatcher; no commas allowed:

```ini
bindd = MODS, key, description, dispatcher, params
bindd = SUPER, Q, Open my favourite terminal, exec, kitty
```

View descriptions with `hyprctl binds` — see [[066-configuring-using-hyprctl| Using Hyprctl]].

### Per-Device Binds

Use the `k` flag. Devices in whitespace-separated list before `dispatcher`. Prepend `!` to exclude devices:

```ini
bindk = MODS, key, [!]device1 device2 ..., dispatcher, params
bindk = SUPER, Q, example-keyboard-1, exec, kitty
bindk = SUPER, Q !razer-keyboard asus-keyboard, exec, kitty
```

> [!warning]
>Devices must appear before description:
```ini
binddk = MODS, key, devices, description, dispatcher, params
```

Check device names with `hyprctl devices`.

## Mouse Binds

Binds relying on mouse movement. One fewer arg. `binds:drag_threshold` differentiates clicks/drags:

```ini
binds {
    drag_threshold = 10  # Fire drag after >10px
}
bindm = ALT, mouse:272, movewindow      # ALT + LMB: move window by dragging >10px
bindc = ALT, mouse:272, togglefloating  # ALT + LMB: float window by clicking
```

| Name | Description | Params |
|---|---|---|
| `movewindow` | Move active window | None |
| `resizewindow` | Resize active window | `1` — resize keep aspect; `2` — resize ignore `keepaspectratio`; None/other — normal resize |

Common mouse button key codes (see `wev` for others):

```txt
LMB -> 272
RMB -> 273
MMB -> 274
```

> [!note]
>Mouse binds work like normal binds — use any keys/mods.

### Touchpad

```ini
bindm = SUPER, mouse:272, movewindow
bindm = SUPER, Control_L, movewindow
bindm = SUPER, mouse:273, resizewindow
bindm = SUPER, ALT_L, resizewindow
```

## Global Keybinds

### Classic

Hyprland supports global keybinds for all apps (OBS, Discord, Firefox, etc.). Use [[061-configuring-dispatchers#list-of-dispatchers | `pass`]] and `sendshortcut` dispatchers:

```ini
# OBS Start/Stop Recording -> SUPER + F10
bind = SUPER, F10, pass, class:^(com\.obsproject\.Studio)$
```

`pass` handles PRESS and RELEASE events itself (no `bindr` needed). Works for push-to-talk:

```ini
bind = , mouse:276, pass, class:^(TeamSpeak 3)$  # Pass MOUSE5 to TeamSpeak3
```

Add shortcuts where other keys pass to the window:

```ini
bind = SUPER, F10, sendshortcut, SUPER, F4, class:^(com\.obsproject\.Studio)$
```

> [!warning]
>Works flawlessly with native Wayland apps. XWayland is wonky — make sure the passed binding is a "global Xorg keybind".

### DBus Global Shortcuts

For apps supporting the GlobalShortcuts portal, use `hyprctl globalshortcuts` to list registered shortcuts, then:

```ini
bind = SUPERSHIFT, A, global, coolApp:myToggle
```

> [!note]
>Requires [[011-hypr-ecosystem-xdg-desktop-portal-hyprland| XDPH]].

## Submaps

Submaps (*modes*/*groups*) activate separate keybind sets:

```ini
# Switch to submap
bind = ALT, R, submap, resize
submap = resize
# Repeatable resizing binds
binde = , right, resizeactive, 10 0
binde = , left, resizeactive, -10 0
binde = , up, resizeactive, 0 -10
binde = , down, resizeactive, 0 10
# Return to global submap
bind = , escape, submap, reset
submap = reset
```

> [!warning]
>Do not forget the escape keybind to reset the keymap!

If stuck, use `hyprctl dispatch submap reset`. If no terminal open, you need to restart.

Multiple actions per keybind:

```ini
bind = ALT, R, submap, resize
submap = resize
bind = , right, resizeactive, 10 0
bind = , right, submap, reset
# ...
submap = reset
```

Use the `u` (submap universal) flag for keybinds active in any submap:

```ini
bindu = $mainMod, K, exec, kitty
```

### Nesting

```ini
bind = $mainMod, M, submap, main_submap
submap = main_submap
# ...
bind = , 1, submap, nested_one
submap = nested_one
# ...
bind = SHIFT, escape, submap, reset
bind = , escape, submap, main_submap
submap = main_submap
# /nested_one
bind = , 2, submap, nested_two
submap = nested_two
# ...
bind = SHIFT, escape, submap, reset
bind = , escape, submap, main_submap
submap = main_submap
# /nested_two
bind = , escape, submap, reset
submap = reset
```

### Auto-Close Submap on Dispatch

Append `,` then submap or `reset`:

```ini
bind = SUPER, a, submap, submapA
submap = submapA, submapB
bind = , a, exec, someCoolThing.sh
submap = reset
# Reset submap after pressing a
submap = submapB, reset
bind = , a, exec, someOtherCoolThing.sh
submap = reset
```

### Catch-All

```ini
bind = , catchall, submap, reset
```

Activates on any key — prevents keys from passing to active app in a submap, or exits submap on unknown key press.

## Example Binds

### Media

```ini
bindel = , XF86AudioRaiseVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+
bindel = , XF86AudioLowerVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-
bindl = , XF86AudioMute, exec, wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
bindl = , XF86AudioPlay, exec, playerctl play-pause
bindl = , XF86AudioPrev, exec, playerctl previous
bindl = , XF86AudioNext, exec, playerctl next
```

#keybinds #configuration #window-manager #linux
