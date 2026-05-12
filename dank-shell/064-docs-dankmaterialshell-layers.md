---
title: Layer Namespaces | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/layers
source: sitemap
fetched_at: 2026-04-26T08:39:07.643094789-03:00
rendered_js: false
word_count: 621
summary: This document provides a comprehensive list of layer shell namespaces for Dank Material Shell (DMS) components and instructions for applying compositor-specific blur and layer rules in Wayland environments like Hyprland and Niri.
tags:
    - wayland
    - layer-shell
    - dms
    - compositor-config
    - blur-effects
    - hyprland
    - niri
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Layer Namespaces

DMS uses Wayland's layer shell protocol for all UI components: bar, popups, modals, OSDs, and notifications. Each component type gets its own namespace, allowing compositors to target them individually for blur effects.

Layer shell surfaces are UI overlays positioned at specific layers (background, bottom, top, overlay). By assigning unique namespaces, you can apply blur selectively (e.g., "blur all modals") without affecting other elements.

## Component Namespaces

Every component namespace starts with `dms:`. DMS uses the following namespaces:

### Modals

Full-screen modal dialogs including settings, power menu, and clipboard history. These overlay the entire screen and optionally dim the background.

| Component | Namespace |
|---|---|
| Clipboard history | `dms:clipboard` |
| File browser | `dms:file-browser` |
| Settings | `dms:settings` |
| Launcher | `dms:spotlight` |
| Bluetooth pairing | `dms:bluetooth-pairing` |
| Color picker | `dms:color-picker` |
| Hyprkeybinds | `dms:hyprkeybinds` |
| Network info | `dms:network-info` |
| Network info (wired) | `dms:network-info-wired` |
| Notification | `dms:notification-center-modal` |
| Polkit | `dms:polkit` |
| Power menu | `dms:power-menu` |
| Process list | `dms:process-list-modal` |
| Wifi password | `dms:wifi-password` |
| Confirm modal | `dms:confirm-modal` |
| Fallback namespace | `dms:modal` |

### Popouts

Popup panels triggered by bar widgets, anchored to the bar and sliding out.

| Component | Namespace |
|---|---|
| App drawer | `dms:app-launcher` |
| Control center | `dms:control-center` |
| Battery | `dms:battery` |
| Vpn | `dms:vpn` |
| DankDash | `dms:dash` |
| Notification center | `dms:notification-center-popout` |
| Process list | `dms:process-list-popout` |
| Fallback namespace | `dms:popout` |
| Plugin | `dms:plugins:<namespace>` |
| Fallback plugin namespace | `dms:plugins:plugin` |

### Desktop Widgets

Desktop widgets (builtins and plugins) and related layers.

| Component | Namespace |
|---|---|
| Desktop widget | `dms:desktop-widget:<plugin id>` |
| Preview | `dms:desktop-widget-preview` |
| Grid | `dms:desktop-widget-grid` |
| Helper | `dms:desktop-widget-helper` |

### Misc Components

Namespaces for components that are neither modals nor popouts.

| Component | Namespace | Use |
|---|---|---|
| UseDankBar | `dms:bar` | The main panel, positionable at any screen edge |
| Dock | `dms:dock` | Application dock (optional) |
| Workspace overview | `dms:workspace-overview` | Workspace overview for Hyprland |
| Notification popup | `dms:notification-popup` | Toast notifications for user attention |
| OSD | `dms:osd` | On-screen displays for volume/brightness, auto-fade |
| Slideout | `dms:slideout` | Sliding panels from screen edges (optional) |
| Tooltip | `dms:tooltip` | Tooltip shown on dock hover |
| Dock context menu | `dock-context-menu` | Right-click context menu on dock apps |
| Toast | `dms:toast` | Toast appearing at top middle of screen |
| Tray menu window | `dms:tray-menu-window` | Right-click menu for system tray applets |

> [!tip] Finding a component's namespace
> - **Hyprland**: Run `hyprctl layers` with the layer open
> - **Niri**: Run `niri msg layers` to list active layer surfaces

For plugin development, see [[011-docs-dankmaterialshell-plugin-development#widget-with-popout|plugin development]] to add a layer namespace.

## Compositor Examples

Each compositor has its own syntax for layer rules.

### Hyprland

> [!info] Animations and dim effects
> For layer rules like `animation`, `blur`, and `dimaround`, disable shell animations and dim effect:
> - Disable animations in **Settings > Personalization > Animation Speed** set to **None**
> - Disable dim in **Theme & Colors > Widget Styling**, untoggle **Darken Modal Background**

#### Blur Settings

```conf
decoration {
    blur {
        enabled = true
        size = 10
        passes = 4
        ignore_opacity = true
        new_optimizations = true
        xray = false
        noise = 0.02
        contrast = 1.1
        vibrancy = 0.2
        vibrancy_darkness = 0.3
    }
    drop_shadow = true
    shadow_range = 20
    shadow_render_power = 3
    col.shadow = rgba(00000099)
}
```

#### Layer Rules

Enable blur for DMS components:

```conf
# Animations
layerrule {
    animation = slide right
    match:namespace = dms:control-center
}
layerrule {
    animation = slide top
    match:namespace = dms:workspace-overview
}
# Available animations: https://wiki.hypr.land/Configuring/Animations/#animation-tree

# Blur — use match:namespace with regex to target multiple layers
layerrule {
    blur = on
    ignore_alpha = 0
    match:namespace = dms:(color-picker|clipboard|spotlight|settings)
}

# Dim instead of blur
layerrule {
    dimaround = on
    match:namespace = dms:(color-picker|clipboard|spotlight|settings)
}
```

#### Examples

**Add a blur effect on shell components:**

Lower opacity in **Theme & Colors > Widget Styling**:

```conf
# Modals
layerrule {
    blur = on
    ignore_alpha = 0
    match:namespace = dms:(polkit|notification-center-modal|workspace-overview|color-picker|clipboard|spotlight|settings|process-list-modal)
}
# Shell components (bar, popouts, etc.)
layerrule {
    blur = on
    ignore_alpha = 0
    match:namespace = dms:(bar|tooltip|toast|dock-context-menu|tray-menu-window|control-center|notification-center-popout|dash|system-update|process-list-popout|battery|popout|app-launcher)
}
```

#### Performance Tuning

If blur impacts performance:

1. **Reduce passes**: Set `passes = 2` instead of 4
2. **Reduce size**: Set `size = 6` instead of 10
3. **Use xray mode**: Set `xray = true` to reduce blur on stacked layers

Test blur impact in real-time:

```bash
hyprctl keyword decoration:blur:enabled false
# Test performance
hyprctl keyword decoration:blur:enabled true
```

More about Hyprland layer rules: https://wiki.hypr.land/Configuring/Window-Rules/#layer-rules

### Niri

Niri uses `layer-rule` blocks with regex namespace matching.

#### Layer Rules

```kdl
// Block sensitive components from screencasts
layer-rule {
    match namespace="^dms:clipboard$"
    block-out-from "screencast"
}
// Match all DMS layers with a regex
layer-rule {
    match namespace=r#"^dms:.*"#
}
```

#### Shadow Settings

```kdl
layer-rule {
    match namespace="^dms:bar$"
    match namespace="^dms:dock$"
    shadow {
        on
        softness 40
        spread 5
        offset x=0 y=5
        draw-behind-window true
        color "#00000064"
    }
}
```

More about Niri layer rules: https://github.com/niri-wm/niri/wiki/Configuration:-Layer-Rules

## Other Compositors

Not all compositors support blur or layer rules. DMS is compositor-agnostic — it only sets namespaces and lets the compositor handle effects.

- MangoWC layer rules: https://github.com/DreamMaoMao/mangowc/wiki#layer-rules

#layer-shell #dms #compositor-config #blur-effects
