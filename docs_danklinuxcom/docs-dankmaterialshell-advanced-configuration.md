---
title: Advanced Configuration | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/advanced-configuration
source: sitemap
fetched_at: 2026-01-24T13:33:16.223591078-03:00
rendered_js: false
word_count: 446
summary: This document provides a comprehensive reference for configuring DankMaterialShell using environment variables to customize core behavior, display layers, and system integration. It explains how to apply these settings across various environments like systemd, Hyprland, and Sway.
tags:
    - dankmaterialshell
    - environment-variables
    - configuration-guide
    - wayland
    - linux-customization
    - system-integration
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

DankMaterialShell supports several advanced configuration options through environment variables prefixed with `DMS_`.

## Core Configuration[​](#core-configuration "Direct link to Core Configuration")

### DMS\_RUN\_GREETER[​](#dms_run_greeter "Direct link to DMS_RUN_GREETER")

Enables greeter/login screen mode instead of regular shell mode. Used for display manager integration with greetd.

```
DMS_RUN_GREETER=1 dms run
```

### DMS\_GREET\_CFG\_DIR[​](#dms_greet_cfg_dir "Direct link to DMS_GREET_CFG_DIR")

Specifies custom configuration directory for greeter mode (defaults to `/etc/greetd/.dms`). Useful for isolating greeter settings from user settings.

```
DMS_GREET_CFG_DIR=/custom/path dms run
```

### DMS\_SOCKET[​](#dms_socket "Direct link to DMS_SOCKET")

Custom Unix socket path for DMS internal services communication. Used by DMSService, NetworkService, SessionService, and PortalService for IPC.

```
DMS_SOCKET=/tmp/custom-dms.sock dms run
```

## Display & Rendering[​](#display--rendering "Direct link to Display & Rendering")

### DMS\_DISABLE\_MATUGEN[​](#dms_disable_matugen "Direct link to DMS_DISABLE_MATUGEN")

Disables matugen dynamic theming system for troubleshooting or when using static themes. Set to `1` or `true` to disable.

```
DMS_DISABLE_MATUGEN=1 dms run
```

### DMS\_DISABLE\_LAYER[​](#dms_disable_layer "Direct link to DMS_DISABLE_LAYER")

Disables layer effects on popout widgets for performance or compatibility reasons. Set to `true` to disable layer rendering.

```
DMS_DISABLE_LAYER=true dms run
```

### DMS\_DANKBAR\_LAYER[​](#dms_dankbar_layer "Direct link to DMS_DANKBAR_LAYER")

Controls Wayland layer for DankBar panel. Valid values: `bottom`, `overlay`, `background`, or `top` (default). Useful for window stacking issues.

```
DMS_DANKBAR_LAYER=overlay dms run
```

### DMS\_POPOUT\_LAYER[​](#dms_popout_layer "Direct link to DMS_POPOUT_LAYER")

Controls Wayland layer for DankBar popout widgets. Valid values: `bottom`, `overlay`, `background`, or `top` (default). Useful for window stacking issues.

```
DMS_POPOUT_LAYER=overlay dms run
```

### DMS\_MODAL\_LAYER[​](#dms_modal_layer "Direct link to DMS_MODAL_LAYER")

Controls Wayland layer for modal windows like the launcher, settings panel, and other popups. Valid values: `bottom`, `overlay`, `background`, or `top` (default).

```
DMS_MODAL_LAYER=overlay dms run
```

### DMS\_NOTIFICATION\_LAYER[​](#dms_notification_layer "Direct link to DMS_NOTIFICATION_LAYER")

Controls Wayland layer for notification popups. Valid values: `bottom`, `overlay`, `background`, or `top` (default).

```
DMS_NOTIFICATION_LAYER=overlay dms run
```

## System Integration[​](#system-integration "Direct link to System Integration")

### DMS\_DISABLE\_POLKIT[​](#dms_disable_polkit "Direct link to DMS_DISABLE_POLKIT")

Disable's the native polkit integration, if you prefer to use a different polkit agent.

```
DMS_DISABLE_POLKIT=1 dms run
```

### DMS\_PREFERRED\_BATTERY[​](#dms_preferred_battery "Direct link to DMS_PREFERRED_BATTERY")

Forces specific battery device when multiple batteries detected (e.g., dual-battery laptops). Provide the UPower device name/path.

```
DMS_PREFERRED_BATTERY=/org/freedesktop/UPower/devices/battery_BAT0 dms run
```

### DMS\_HIDE\_TRAYIDS[​](#dms_hide_trayids "Direct link to DMS_HIDE_TRAYIDS")

Comma-separated list of system tray icon IDs to hide from the system tray bar.

```
DMS_HIDE_TRAYIDS=discord,spotify,steam dms run
```

```
DMS_DWL_TAG_COUNT=5 dms run
```

## Printing Configuration[​](#printing-configuration "Direct link to Printing Configuration")

### DMS\_IPP\_HOST[​](#dms_ipp_host "Direct link to DMS_IPP_HOST")

Specifies the hostname or IP address of the IPP/CUPS print server. Defaults to `localhost` if not set.

```
DMS_IPP_HOST=printserver.local dms run
```

### DMS\_IPP\_PORT[​](#dms_ipp_port "Direct link to DMS_IPP_PORT")

Specifies the port number for the IPP/CUPS print server. Defaults to `631` (standard IPP port) if not set.

### DMS\_IPP\_USERNAME[​](#dms_ipp_username "Direct link to DMS_IPP_USERNAME")

Username for authenticating with the IPP/CUPS print server. Leave unset if authentication is not required.

```
DMS_IPP_USERNAME=printuser dms run
```

### DMS\_IPP\_PASSWORD[​](#dms_ipp_password "Direct link to DMS_IPP_PASSWORD")

Password for authenticating with the IPP/CUPS print server. Leave unset if authentication is not required.

```
DMS_IPP_PASSWORD=secret dms run
```

## Setting Environment Variables[​](#setting-environment-variables "Direct link to Setting Environment Variables")

Systemd / DankInstall Users

If you manage DMS with systemd (including dankinstall users), set environment variables in `~/.config/environment.d/90-dms.conf`:

```
DMS_DISABLE_MATUGEN=1
DMS_DANKBAR_LAYER=overlay
DMS_HIDE_TRAYIDS=discord,spotify
```

Log out and back in for changes to take effect.

### niri[​](#niri "Direct link to niri")

Add to your niri config:

```
environment {
  DMS_DISABLE_MATUGEN "1"
  DMS_DANKBAR_LAYER "overlay"
  DMS_HIDE_TRAYIDS "discord,spotify"
}
```

### Hyprland[​](#hyprland "Direct link to Hyprland")

Add to your Hyprland config:

```
env = DMS_DISABLE_MATUGEN,1
env = DMS_DANKBAR_LAYER,overlay
env = DMS_HIDE_TRAYIDS,discord,spotify
```

### Sway[​](#sway "Direct link to Sway")

Add to your Sway config:

```
set $DMS_DISABLE_MATUGEN 1
set $DMS_DANKBAR_LAYER overlay
set $DMS_HIDE_TRAYIDS discord,spotify
```

### Manual Launch[​](#manual-launch "Direct link to Manual Launch")

Set variables before launching:

```
exportDMS_DISABLE_MATUGEN=1
exportDMS_DANKBAR_LAYER=overlay
dms run
```

## Use Cases[​](#use-cases "Direct link to Use Cases")

**Disable dynamic theming:**

Useful for performance testing or when using only static themes.

**Hide system tray icons:**

```
DMS_HIDE_TRAYIDS=discord,slack,teams
```

Clean up system tray by hiding unwanted application icons.

**Fix bar layering issues:**

```
DMS_DANKBAR_LAYER=overlay
```

If DankBar appears behind windows or other issues, adjust the Wayland layer.

**Dual battery laptops:**

```
DMS_PREFERRED_BATTERY=/org/freedesktop/UPower/devices/battery_BAT0
```

Force DMS to use a specific battery when multiple are detected.

**Performance tuning:**

Disable layer effects to improve performance on lower-end hardware.

**Remote print server:**

```
DMS_IPP_HOST=printserver.local
DMS_IPP_PORT=631
DMS_IPP_USERNAME=printuser
DMS_IPP_PASSWORD=secret
```

Connect to a remote CUPS/IPP print server with authentication.