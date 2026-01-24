---
title: Compositor Setup | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/compositors
source: sitemap
fetched_at: 2026-01-24T13:33:37.103569217-03:00
rendered_js: false
word_count: 837
summary: This document provides configuration guidelines and optimized settings for integrating DankMaterialShell with Wayland compositors like niri and Hyprland. It covers the setup of keybindings, layer rules, startup procedures, and environment variables to ensure a seamless shell experience.
tags:
    - dankmaterialshell
    - wayland-compositor
    - niri-config
    - hyprland-configuration
    - linux-desktop
    - desktop-shell
category: configuration
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell works with any Wayland compositor, but we provide optimized configurations for niri, Hyprland, Sway, MangoWC, and labwc. These configs include DMS-specific keybindings, proper layer shell rules, and recommended settings.

## niri Configuration[​](#niri-configuration "Direct link to niri Configuration")

niri uses the KDL configuration format. DankMaterialShell integrates seamlessly with niri's scrollable tiling layout.

### Key Configuration Sections[​](#key-configuration-sections "Direct link to Key Configuration Sections")

DMS will automatically apply key binds, gaps, window radius, and colors if you include the following files in your niri config. You can customize gaps, border radius, and window radius in **Settings → Compositor**.

```
// Add to the end of ~/.config/niri/config.kdl
include "dms/colors.kdl"
include "dms/layout.kdl"
include "dms/alttab.kdl"
include "dms/binds.kdl"
```

tip

Be sure that all files exist before including them in the niri configuration.

```
mkdir-p ~/.config/niri/dms
touch ~/.config/niri/dms/{colors,layout,alttab,binds}.kdl
```

For manual configuration recommendations, continue below.

#### Layout[​](#layout "Direct link to Layout")

The niri layout should have a transparent background, in order to integrate wallpapers onto the overview.

```
layout {
    // You can tailor the gaps to fit dms spacing.
    gaps 5
    background-color "transparent"
}
```

#### Layer Rules[​](#layer-rules "Direct link to Layer Rules")

Tell niri to place the wallpaper on the overview.

```
layer-rule {
    match namespace="^quickshell$"
    place-within-backdrop true
}
```

If "Blur Layer" is enabled, you can place the blurred wallpaper on the overview.

```
layer-rule {
    match namespace="dms:blurwallpaper"
    place-within-backdrop true
}
```

For more about layer rules see [layer rules](https://danklinux.com/docs/dankmaterialshell/layers).

#### Startup[​](#startup "Direct link to Startup")

niri has native systemd session integration. Bind DMS to niri's service so it only runs under niri (won't start in Plasma/GNOME):

```
systemctl --user add-wants niri.service dms
```

**Optional services:**

```
// Clipboard history
spawn-at-startup "bash" "-c" "wl-paste --watch cliphist store &"
```

**Alternative: Direct launch (if not using systemd)**

```
spawn-at-startup "dms" "run"
```

#### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

```
environment {
  XDG_CURRENT_DESKTOP "niri"
  QT_QPA_PLATFORM "wayland"
  ELECTRON_OZONE_PLATFORM_HINT "auto"
  QT_QPA_PLATFORMTHEME "gtk3"
  QT_QPA_PLATFORMTHEME_QT6 "gtk3"
}
```

#### DMS Keybindings[​](#dms-keybindings "Direct link to DMS Keybindings")

For the full list of available IPC commands see [IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc)

```
binds {
    // Application Launchers
    Mod+Space hotkey-overlay-title="Application Launcher" {
        spawn "dms" "ipc" "call" "spotlight" "toggle";
    }
    Mod+V hotkey-overlay-title="Clipboard Manager" {
        spawn "dms" "ipc" "call" "clipboard" "toggle";
    }
    Mod+M hotkey-overlay-title="Task Manager" {
        spawn "dms" "ipc" "call" "processlist" "focusOrToggle";
    }
    Mod+Comma hotkey-overlay-title="Settings" {
        spawn "dms" "ipc" "call" "settings" "focusOrToggle";
    }
    Mod+N hotkey-overlay-title="Notification Center" {
        spawn "dms" "ipc" "call" "notifications" "toggle";
    }
    Mod+Y hotkey-overlay-title="Browse Wallpapers" {
        spawn "dms" "ipc" "call" "dankdash" "wallpaper";
    }

    // Security
    Mod+Alt+L hotkey-overlay-title="Lock Screen" {
        spawn "dms" "ipc" "call" "lock" "lock";
    }

    // Audio Controls
    XF86AudioRaiseVolume allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "increment" "3";
    }
    XF86AudioLowerVolume allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "decrement" "3";
    }
    XF86AudioMute allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "mute";
    }

    // Brightness Controls
    XF86MonBrightnessUp allow-when-locked=true {
       spawn "dms" "ipc" "call" "brightness" "increment" "5" "";
    }
    XF86MonBrightnessDown allow-when-locked=true {
       spawn "dms" "ipc" "call" "brightness" "decrement" "5" "";
    }
}
```

### Window Rules[​](#window-rules "Direct link to Window Rules")

Recommended window rules, tailor to your preferences:

```
window-rule {
    match app-id=r#"^org\.gnome\."#
    draw-border-with-background false
    geometry-corner-radius 12
    clip-to-geometry true
}

window-rule {
    match app-id=r#"^org\.wezfurlong\.wezterm$"#
    match app-id="Alacritty"
    match app-id="zen"
    match app-id="com.mitchellh.ghostty"
    match app-id="kitty"
    draw-border-with-background false
}

window-rule {
    match is-active=false
    opacity 0.9
}

window-rule {
    geometry-corner-radius 12
    clip-to-geometry true
}

// Open DMS windows as floating by default
window-rule {
    match app-id=r#"org.quickshell$"#
    open-floating true
}
```

## Hyprland Configuration[​](#hyprland-configuration "Direct link to Hyprland Configuration")

Hyprland uses a simple config file format at `~/.config/hypr/hyprland.conf`.

### Key Configuration Sections[​](#key-configuration-sections-1 "Direct link to Key Configuration Sections")

DMS will automatically apply gaps, window radius, and colors if you include the following files in your Hyprland config. You can customize gaps, border radius, and window radius in **Settings → Compositor**.

```
# Add to the end of ~/.config/hypr/hyprland.conf
source = ~/.config/hypr/dms/colors.conf
source = ~/.config/hypr/dms/layout.conf
source = ~/.config/hypr/dms/outputs.conf
```

tip

Be sure that all files exist before including them in the Hyprland configuration.

```
mkdir-p ~/.config/hypr/dms
touch ~/.config/hypr/dms/{colors,layout,outputs}.conf
```

For manual configuration recommendations, continue below.

#### Startup[​](#startup-1 "Direct link to Startup")

Hyprland doesn't initialize the systemd user session by default. Export the environment and start a session target:

```
exec-once = dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
exec-once = systemctl --user start hyprland-session.target
```

Then bind DMS to the session target so it only runs under Hyprland (won't start in Plasma/GNOME):

```
systemctl --user add-wants hyprland-session.target dms
```

See the [Installation guide](https://danklinux.com/docs/dankmaterialshell/installation#hyprland) for creating the session target.

**Optional services:**

```
exec-once = bash -c "wl-paste --watch cliphist store &"
```

**Alternative: Direct launch (if not using systemd)**

#### Miscellaneous[​](#miscellaneous "Direct link to Miscellaneous")

Disables the hyprland backdrop/logo

```
misc {
    disable_hyprland_logo = true
    disable_splash_rendering = true
}
```

#### Environment Variables[​](#environment-variables-1 "Direct link to Environment Variables")

```
env = QT_QPA_PLATFORM,wayland
env = ELECTRON_OZONE_PLATFORM_HINT,auto
env = QT_QPA_PLATFORMTHEME,gtk3
env = QT_QPA_PLATFORMTHEME_QT6,gtk3
```

#### Layer Rules[​](#layer-rules-1 "Direct link to Layer Rules")

```
layerrule = noanim, ^(dms)$
```

For more about layer rules see [layer rules](https://danklinux.com/docs/dankmaterialshell/layers).

#### General Layout[​](#general-layout "Direct link to General Layout")

```
general {
    gaps_in = 5
    gaps_out = 5
    border_size = 0

    col.active_border = rgba(707070ff)
    col.inactive_border = rgba(d0d0d0ff)

    layout = dwindle
}
```

#### Decoration[​](#decoration "Direct link to Decoration")

```
decoration {
    rounding = 12

    active_opacity = 1.0
    inactive_opacity = 0.9

    shadow {
        enabled = true
        range = 30
        render_power = 5
        offset = 0 5
        color = rgba(00000070)
    }
}
```

#### DMS Keybindings[​](#dms-keybindings-1 "Direct link to DMS Keybindings")

For the full list of available IPC commands see [IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc)

```
$mod = SUPER

# Application Launchers
bind = $mod, space, exec, dms ipc call spotlight toggle
bind = $mod, V, exec, dms ipc call clipboard toggle
bind = $mod, M, exec, dms ipc call processlist focusOrToggle
bind = $mod, comma, exec, dms ipc call settings focusOrToggle
bind = $mod, N, exec, dms ipc call notifications toggle
bind = $mod, Y, exec, dms ipc call dankdash wallpaper
bind = $mod, TAB, exec, dms ipc call hypr toggleOverview

# Security
bind = $mod ALT, L, exec, dms ipc call lock lock

# Audio Controls
bindel = , XF86AudioRaiseVolume, exec, dms ipc call audio increment 3
bindel = , XF86AudioLowerVolume, exec, dms ipc call audio decrement 3
bindl = , XF86AudioMute, exec, dms ipc call audio mute

# Brightness Controls
bindel = , XF86MonBrightnessUp, exec, dms ipc call brightness increment 5
bindel = , XF86MonBrightnessDown, exec, dms ipc call brightness decrement 5
```

### Window Rules[​](#window-rules-1 "Direct link to Window Rules")

```
# Opacity for inactive windows
windowrulev2 = opacity 0.9 0.9, floating:0, focus:0

# GNOME apps
windowrulev2 = rounding 12, class:^(org\.gnome\.)
windowrulev2 = noborder, class:^(org\.gnome\.)

# Terminal apps - no borders
windowrulev2 = noborder, class:^(org\.wezfurlong\.wezterm)$
windowrulev2 = noborder, class:^(Alacritty)$
windowrulev2 = noborder, class:^(zen)$
windowrulev2 = noborder, class:^(com\.mitchellh\.ghostty)$
windowrulev2 = noborder, class:^(kitty)$

# Floating windows
windowrulev2 = float, class:^(gnome-calculator)$
windowrulev2 = float, class:^(blueman-manager)$
windowrulev2 = float, class:^(org\.gnome\.Nautilus)$

# Open DMS windows as floating by default
windowrulev2 = float, class:^(org.quickshell)$
```

## MangoWC Configuration[​](#mangowc-configuration "Direct link to MangoWC Configuration")

[MangoWC](https://github.com/DreamMaoMao/mangowc) is a dynamic tiling Wayland compositor based on dwl (wlroots). Configuration lives at `~/.config/mango/config.conf`.

### Key Configuration Sections[​](#key-configuration-sections-2 "Direct link to Key Configuration Sections")

DMS will automatically apply gaps, window radius, and colors if you include the following files in your MangoWC config. You can customize gaps, border radius, and window radius in **Settings → Compositor**.

```
# Add to the end of ~/.config/mango/config.conf
source=~/.config/mango/dms/colors.conf
source=~/.config/mango/dms/layout.conf
source=~/.config/mango/dms/outputs.conf
```

tip

Be sure that all files exist before including them in the MangoWC configuration.

```
mkdir-p ~/.config/mango/dms
touch ~/.config/mango/dms/{colors,layout,outputs}.conf
```

For manual configuration recommendations, continue below.

#### Startup[​](#startup-2 "Direct link to Startup")

MangoWC is wlroots-based and requires manual environment export for systemd services. Export the environment and start a session target:

```
exec-once=dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
exec-once=systemctl --user start mango-session.target
```

Then bind DMS to the session target so it only runs under MangoWC (won't start in Plasma/GNOME):

```
systemctl --user add-wants mango-session.target dms
```

See the [Installation guide](https://danklinux.com/docs/dankmaterialshell/installation#mangowc) for creating the session target.

**Optional services:**

```
exec-once=wl-paste --type text --watch cliphist store
```

**Alternative: Direct launch (if not using systemd)**

#### Environment Variables[​](#environment-variables-2 "Direct link to Environment Variables")

```
env=QT_QPA_PLATFORM,wayland
env=ELECTRON_OZONE_PLATFORM_HINT,auto
env=QT_QPA_PLATFORMTHEME,gtk3
```

#### Appearance[​](#appearance "Direct link to Appearance")

Recommended appearance settings for DMS integration:

```
# Window appearance
border_radius=12
borderpx=0
focused_opacity=1.0
unfocused_opacity=0.9

# Gaps
gappih=5
gappiv=5
gappoh=5
gappov=5

# Shadows (optional)
shadows=1
shadow_only_floating=1
shadows_size=10
shadows_blur=15
```

#### Layer Rules[​](#layer-rules-2 "Direct link to Layer Rules")

```
# Disable animation on DMS layers
layerrule=noanim:1,layer_name:^dms
```

For more about layer rules see [layer rules](https://danklinux.com/docs/dankmaterialshell/layers).

#### DMS Keybindings[​](#dms-keybindings-2 "Direct link to DMS Keybindings")

For the full list of available IPC commands see [IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc).

```
# Application Launchers
bind=SUPER,space,spawn,dms ipc call spotlight toggle
bind=SUPER,v,spawn,dms ipc call clipboard toggle
bind=SUPER,m,spawn,dms ipc call processlist focusOrToggle
bind=SUPER,comma,spawn,dms ipc call settings focusOrToggle
bind=SUPER,n,spawn,dms ipc call notifications toggle
bind=SUPER,y,spawn,dms ipc call dankdash wallpaper

# Security
bind=SUPER+ALT,l,spawn,dms ipc call lock lock

# Audio Controls
bind=NONE,XF86AudioRaiseVolume,spawn,dms ipc call audio increment 3
bind=NONE,XF86AudioLowerVolume,spawn,dms ipc call audio decrement 3
bind=NONE,XF86AudioMute,spawn,dms ipc call audio mute

# Brightness Controls
bind=NONE,XF86MonBrightnessUp,spawn,dms ipc call brightness increment 5
bind=NONE,XF86MonBrightnessDown,spawn,dms ipc call brightness decrement 5
```

### Window Rules[​](#window-rules-2 "Direct link to Window Rules")

```
# GNOME apps
windowrule=isnoborder:1,appid:^org\.gnome\.

# Terminal apps - no borders
windowrule=isnoborder:1,appid:^org\.wezfurlong\.wezterm$
windowrule=isnoborder:1,appid:^Alacritty$
windowrule=isnoborder:1,appid:^com\.mitchellh\.ghostty$
windowrule=isnoborder:1,appid:^kitty$

# Float DMS windows
windowrule=isfloating:1,appid:^org\.quickshell$
```

## Sway Configuration[​](#sway-configuration "Direct link to Sway Configuration")

[Sway](https://swaywm.org/) is an i3-compatible Wayland compositor. DankMaterialShell integrates with Sway's tiling layout.

### Key Configuration Sections[​](#key-configuration-sections-3 "Direct link to Key Configuration Sections")

Coming Soon

Detailed Sway configuration sections are coming soon. Sway configuration will include:

- Startup commands
- Environment variables
- DMS keybindings
- Layer rules
- Window rules

For now, refer to the [Example for Sway](#example-for-sway) in the "Other Compositors" section below for basic setup.

#### Startup[​](#startup-3 "Direct link to Startup")

Launch DankMaterialShell and optional services at compositor startup:

```
exec dms run
exec wl-paste --watch cliphist store
```

#### DMS Keybindings[​](#dms-keybindings-3 "Direct link to DMS Keybindings")

For the full list of available IPC commands see [IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc). Basic Sway keybinding examples are available in the [Example for Sway](#example-for-sway) section below.

## labwc Configuration[​](#labwc-configuration "Direct link to labwc Configuration")

[labwc](https://labwc.github.io/) is a wlroots-based window-stacking compositor for Wayland, inspired by Openbox.

### Key Configuration Sections[​](#key-configuration-sections-4 "Direct link to Key Configuration Sections")

Coming Soon

Detailed labwc configuration sections are coming soon. labwc configuration will include:

- Startup commands
- Environment variables
- DMS keybindings
- Layer rules
- Window rules

For now, refer to the [labwc documentation](https://labwc.github.io/manual.html) for basic setup.

#### DMS Keybindings[​](#dms-keybindings-4 "Direct link to DMS Keybindings")

For the full list of available IPC commands see [IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc). labwc keybinding configuration coming soon.

## Other Compositors[​](#other-compositors "Direct link to Other Compositors")

DankMaterialShell works with any Wayland compositor that supports:

- Layer shell protocol (for panels and overlays)
- Session lock protocol (for lock screen)
- ext-workspace-v1 protocol (for workspace management)
- wlr-output-management-unstable-v1 protocol (for interface scaling + output management)

**Note:** Some compositor-specific features will be unavailable, such as workspace switching.

### Basic Integration[​](#basic-integration "Direct link to Basic Integration")

For other compositors, you need to:

1. **Auto-start DMS:**
2. **Configure keybindings** using the IPC commands from the [Keybinds & IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc) guide
3. **Set environment variables** in `~/.config/environment.d/90-dms.conf` (for systemd users) or your compositor config:

### Example for Sway[​](#example-for-sway "Direct link to Example for Sway")

Add to `~/.config/sway/config`:

```
# Startup
exec dms run
exec wl-paste --watch cliphist store

# DMS Keybindings
bindsym $mod+space exec dms ipc call spotlight toggle
bindsym $mod+v exec dms ipc call clipboard toggle
bindsym $mod+m exec dms ipc call processlist focusOrToggle
bindsym $mod+comma exec dms ipc call settings focusOrToggle

# Audio controls
bindsym XF86AudioRaiseVolume exec dms ipc call audio increment 3
bindsym XF86AudioLowerVolume exec dms ipc call audio decrement 3
bindsym XF86AudioMute exec dms ipc call audio mute

# Brightness controls
bindsym XF86MonBrightnessUp exec dms ipc call brightness increment 5
bindsym XF86MonBrightnessDown exec dms ipc call brightness decrement 5
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### DMS doesn't start automatically[​](#dms-doesnt-start-automatically "Direct link to DMS doesn't start automatically")

Check your compositor's logs to ensure the `exec-once` or equivalent startup command is running. You can also manually start DMS with `dms run` to see any error messages.

### Keybindings don't work[​](#keybindings-dont-work "Direct link to Keybindings don't work")

Verify that:

- DMS is running (`pgrep -f "dms run"`)
- Your keybinding syntax matches your compositor's format

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Customize your shell appearance in [Themes](https://danklinux.com/docs/dankmaterialshell/application-themes)
- Explore all available IPC commands in [Keybinds & IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc)
- Add functionality with [Plugins](https://danklinux.com/docs/dankmaterialshell/plugins-overview)