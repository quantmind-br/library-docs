---
title: Compositor Setup | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/compositors
source: sitemap
fetched_at: 2026-04-26T08:38:57.524018676-03:00
rendered_js: false
word_count: 914
summary: This document provides technical instructions for integrating the DankMaterialShell with various Wayland compositors, specifically detailing configuration files, keybindings, environment variables, and window rules for niri and Hyprland.
tags:
    - wayland
    - linux
    - compositor
    - niri
    - hyprland
    - shell-customization
    - dms
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell works with any Wayland compositor. Optimized configurations are provided for niri, Hyprland, Sway, MangoWC, labwc, and Miracle WM.

## niri Configuration

niri uses KDL format at `~/.config/niri/config.kdl`.

### Auto-Include DMS Files

```kdl
// Add to the end of ~/.config/niri/config.kdl
include "dms/colors.kdl"
include "dms/layout.kdl"
include "dms/alttab.kdl"
include "dms/binds.kdl"
```

> [!tip]
> Ensure all files exist before including:
> ```bash
> mkdir -p ~/.config/niri/dms
> touch ~/.config/niri/dms/{colors,layout,alttab,binds}.kdl
> ```

#### Layout

```kdl
layout {
    gaps 5
    background-color "transparent"
}
```

#### Layer Rules

```kdl
layer-rule {
    match namespace="^quickshell$"
    place-within-backdrop true
}
// Blur wallpaper on overview (if "Blur Layer" enabled)
layer-rule {
    match namespace="dms:blurwallpaper"
    place-within-backdrop true
}
```

#### Startup

```kdl
spawn-at-startup "dms" "run"
// Clipboard history
spawn-at-startup "bash" "-c" "wl-paste --watch cliphist store &"
```

#### Environment Variables

```kdl
environment {
  XDG_CURRENT_DESKTOP "niri"
  QT_QPA_PLATFORM "wayland"
  ELECTRON_OZONE_PLATFORM_HINT "auto"
  QT_QPA_PLATFORMTHEME "gtk3"
  QT_QPA_PLATFORMTHEME_QT6 "gtk3"
}
```

#### DMS Keybindings

See [[075-docs-dankmaterialshell-keybinds-ipc|the IPC reference]] for all available commands.

```kdl
binds {
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
    Mod+Alt+L hotkey-overlay-title="Lock Screen" {
        spawn "dms" "ipc" "call" "lock" "lock";
    }
    XF86AudioRaiseVolume allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "increment" "3";
    }
    XF86AudioLowerVolume allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "decrement" "3";
    }
    XF86AudioMute allow-when-locked=true {
        spawn "dms" "ipc" "call" "audio" "mute";
    }
    XF86MonBrightnessUp allow-when-locked=true {
       spawn "dms" "ipc" "call" "brightness" "increment" "5" "";
    }
    XF86MonBrightnessDown allow-when-locked=true {
       spawn "dms" "ipc" "call" "brightness" "decrement" "5" "";
    }
}
```

#### Window Rules

```kdl
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
window-rule {
    match app-id=r#"org.quickshell$"#
    open-floating true
}
```

## Hyprland Configuration

Hyprland uses `~/.config/hypr/hyprland.conf`.

### Auto-Include DMS Files

```conf
# Add to the end of ~/.config/hypr/hyprland.conf
source = ~/.config/hypr/dms/colors.conf
source = ~/.config/hypr/dms/layout.conf
source = ~/.config/hypr/dms/outputs.conf
```

> [!tip]
> Ensure all files exist:
> ```bash
> mkdir -p ~/.config/hypr/dms
> touch ~/.config/hypr/dms/{colors,layout,outputs}.conf
> ```

#### Startup

```conf
exec-once = dms run
# Clipboard history
exec-once = bash -c "wl-paste --watch cliphist store &"
```

#### Miscellaneous

```conf
misc {
    disable_hyprland_logo = true
    disable_splash_rendering = true
}
```

#### Environment Variables

```conf
env = QT_QPA_PLATFORM,wayland
env = ELECTRON_OZONE_PLATFORM_HINT,auto
env = QT_QPA_PLATFORMTHEME,gtk3
env = QT_QPA_PLATFORMTHEME_QT6,gtk3
```

#### Layer Rules

```conf
layerrule = no_anim on, match:namespace ^(dms)$
```

#### General Layout

```conf
general {
    gaps_in = 5
    gaps_out = 5
    border_size = 0
    col.active_border = rgba(707070ff)
    col.inactive_border = rgba(d0d0d0ff)
    layout = dwindle
}
```

#### Decoration

```conf
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

#### DMS Keybindings

See [[075-docs-dankmaterialshell-keybinds-ipc|the IPC reference]] for all available commands.

```conf
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

#### Window Rules

```conf
windowrule = opacity 0.9 0.9, match:float 0, match:focus 0
windowrule = rounding 12, border_size 0, match:class ^(org\.gnome\.)
windowrule = border_size 0, match:class ^(org\.wezfurlong\.wezterm)$
windowrule = border_size 0, match:class ^(Alacritty)$
windowrule = border_size 0, match:class ^(zen)$
windowrule = border_size 0, match:class ^(com\.mitchellh\.ghostty)$
windowrule = border_size 0, match:class ^(kitty)$
windowrule = float on, match:class ^(gnome-calculator)$
windowrule = float on, match:class ^(blueman-manager)$
windowrule = float on, match:class ^(org\.gnome\.Nautilus)$
windowrule = float on, match:class ^(org.quickshell)$
```

## MangoWC Configuration

[MangoWC](https://github.com/DreamMaoMao/mangowc) uses `~/.config/mango/config.conf`.

### Auto-Include DMS Files

```conf
# Add to the end of ~/.config/mango/config.conf
source=~/.config/mango/dms/colors.conf
source=~/.config/mango/dms/layout.conf
source=~/.config/mango/dms/outputs.conf
```

> [!tip]
> Ensure all files exist:
> ```bash
> mkdir -p ~/.config/mango/dms
> touch ~/.config/mango/dms/{colors,layout,outputs}.conf
> ```

#### Startup

```conf
exec-once=dms run
exec-once=wl-paste --type text --watch cliphist store
```

#### Environment Variables

```conf
env=QT_QPA_PLATFORM,wayland
env=ELECTRON_OZONE_PLATFORM_HINT,auto
env=QT_QPA_PLATFORMTHEME,gtk3
```

#### Appearance

```conf
border_radius=12
borderpx=0
focused_opacity=1.0
unfocused_opacity=0.9
gappih=5
gappiv=5
gappoh=5
gappov=5
shadows=1
shadow_only_floating=1
shadows_size=10
shadows_blur=15
```

#### Layer Rules

```conf
layerrule=noanim:1,layer_name:^dms
```

#### DMS Keybindings

```conf
bind=SUPER,space,spawn,dms ipc call spotlight toggle
bind=SUPER,v,spawn,dms ipc call clipboard toggle
bind=SUPER,m,spawn,dms ipc call processlist focusOrToggle
bind=SUPER,comma,spawn,dms ipc call settings focusOrToggle
bind=SUPER,n,spawn,dms ipc call notifications toggle
bind=SUPER,y,spawn,dms ipc call dankdash wallpaper
bind=SUPER+ALT,l,spawn,dms ipc call lock lock
bind=NONE,XF86AudioRaiseVolume,spawn,dms ipc call audio increment 3
bind=NONE,XF86AudioLowerVolume,spawn,dms ipc call audio decrement 3
bind=NONE,XF86AudioMute,spawn,dms ipc call audio mute
bind=NONE,XF86MonBrightnessUp,spawn,dms ipc call brightness increment 5
bind=NONE,XF86MonBrightnessDown,spawn,dms ipc call brightness decrement 5
```

#### Window Rules

```conf
windowrule=isnoborder:1,appid:^org\.gnome\.
windowrule=isnoborder:1,appid:^org\.wezfurlong\.wezterm$
windowrule=isnoborder:1,appid:^Alacritty$
windowrule=isnoborder:1,appid:^com\.mitchellh\.ghostty$
windowrule=isnoborder:1,appid:^kitty$
windowrule=isfloating:1,appid:^org\.quickshell$
```

## Sway Configuration

[Sway](https://swaywm.org/) is i3-compatible. See [[009-docs-dankmaterialshell-installation|the Installation guide]] for systemd autostart setup.

#### Startup

```conf
exec dms run
exec wl-paste --watch cliphist store
```

#### DMS Keybindings

```conf
bindsym $mod+space exec dms ipc call spotlight toggle
bindsym $mod+v exec dms ipc call clipboard toggle
bindsym $mod+m exec dms ipc call processlist focusOrToggle
bindsym $mod+comma exec dms ipc call settings focusOrToggle
bindsym XF86AudioRaiseVolume exec dms ipc call audio increment 3
bindsym XF86AudioLowerVolume exec dms ipc call audio decrement 3
bindsym XF86AudioMute exec dms ipc call audio mute
bindsym XF86MonBrightnessUp exec dms ipc call brightness increment 5
bindsym XF86MonBrightnessDown exec dms ipc call brightness decrement 5
```

## labwc Configuration

[labwc](https://labwc.github.io/) is a wlroots-based window-stacking compositor. See [[084-docs-dankmaterialshell-keybinds-ipc|the IPC reference]] for available commands.

## Miracle WM Configuration

[Miracle WM](https://github.com/miracle-wm-org/miracle-wm) is a tiling compositor built on Mir. See [[009-docs-dankmaterialshell-installation|the Installation guide]] for systemd autostart setup.

## Other Compositors

DankMaterialShell requires:
- Layer shell protocol
- Session lock protocol
- ext-workspace-v1 protocol
- wlr-output-management-unstable-v1 protocol

Some features (e.g., workspace switching) are unavailable on unsupported compositors.

### Basic Integration

1. Auto-start DMS
2. Configure keybindings via [[075-docs-dankmaterialshell-keybinds-ipc|IPC commands]]
3. Set environment variables in `~/.config/environment.d/90-dms.conf` or compositor config

## Troubleshooting

### DMS doesn't start automatically

Check compositor logs. Manually run `dms run` to see errors.

### Keybindings don't work

- Verify DMS is running: `pgrep -f "dms run"`
- Check keybinding syntax matches compositor format

## Next Steps

- [[062-docs-dankmaterialshell-application-themes|Customize themes]]
- [[075-docs-dankmaterialshell-keybinds-ipc|Explore IPC commands]]
- [[004-docs-dankmaterialshell-plugins-overview|Add plugins]]
