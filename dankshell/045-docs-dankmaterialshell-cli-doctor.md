---
title: System Diagnostics (doctor) | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-doctor
source: sitemap
fetched_at: 2026-01-24T13:35:33.406006884-03:00
rendered_js: false
word_count: 726
summary: This document describes the dms doctor command, a diagnostic tool for verifying DankMaterialShell installations, system dependencies, and environment configurations.
tags:
    - dms-doctor
    - diagnostics
    - troubleshooting
    - wayland
    - dependency-verification
    - system-checks
category: reference
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

The `dms doctor` command diagnoses your DMS installation, verifies dependencies, and checks system configuration. Use it to troubleshoot issues or verify your setup is complete.

## Usage[​](#usage "Direct link to Usage")

```
dms doctor           # Standard output
dms doctor -v# Verbose output with paths and details
dms doctor -j# JSON output for scripting
```

## Status Indicators[​](#status-indicators "Direct link to Status Indicators")

IconStatusMeaning🟢OKCheck passed🟡WarningNon-critical issue, may affect some features🔴ErrorCritical issue that needs attention⚪InfoInformational, no action needed

* * *

## System Checks[​](#system-checks "Direct link to System Checks")

### Operating System[​](#operating-system "Direct link to Operating System")

All GNU/Linux distributions are supported - this information is purely informational.

### Architecture[​](#architecture "Direct link to Architecture")

Only amd64/arm64 is officially supported, although other architectures may work with manual compilation.

### Display Server[​](#display-server "Direct link to Display Server")

DMS only supports Wayland, this check verifies you're not using X11.

* * *

## Version Checks[​](#version-checks "Direct link to Version Checks")

### DMS CLI[​](#dms-cli "Direct link to DMS CLI")

DMS CLI is the backend and command-line interface for DMS. Its version should match the version of the quickshell configuration.

### Quickshell[​](#quickshell "Direct link to Quickshell")

Quickshell is the framework used by DMS. Older versions of quickshell may result in a reduced feature set within DMS.

### DMS Shell[​](#dms-shell "Direct link to DMS Shell")

The version of the shell configuration, which should match the DMS CLI version.

* * *

## Installation Checks[​](#installation-checks "Direct link to Installation Checks")

### DMS Configuration[​](#dms-configuration "Direct link to DMS Configuration")

By default DMS installs its configuration, plugins, and themes in `$XDG_CONFIG_HOME/.config/DankMaterialShell/`. This check verifies that the configuration directory exists.

### shell.qml[​](#shellqml "Direct link to shell.qml")

The location of the `shell.qml` is the installed location of the DMS shell configuration.

### Install Type[​](#install-type "Direct link to Install Type")

- `system`: Installed via system package manager (e.g. `apt`, `dnf`, `pacman`)
- `user`: if manually installed via manual compilation & installation
- `nix`: if installed via Nix package manager

* * *

## Compositor Checks[​](#compositor-checks "Direct link to Compositor Checks")

All wayland compositors that implement the [layer shell protocol](https://wayland.app/protocols/wlr-layer-shell-unstable-v1) are supported, with varying feature sets.

### Supported Compositors[​](#supported-compositors "Direct link to Supported Compositors")

CompositorDetectionVersion Parsingniri`niri``niri --version`Hyprland`hyprland`, `Hyprland``hyprctl version`mangowc`mangowc``mangowc --version`labwc`labwc``labwc --version`Sway`sway``sway --version`River`river``river -version`Wayfire`wayfire``wayfire --version`

### Active Compositor[​](#active-compositor "Direct link to Active Compositor")

Currently running compositor.

* * *

## Quickshell Features[​](#quickshell-features "Direct link to Quickshell Features")

These features depend on how Quickshell was built. Using `quickshell-git` provides full feature support, some builds of quickshell can exclude features based on compilation options.

note

All of these features currently require `quickshell-git` or `quickshell` from the Dank Linux repositories (Fedora, Debian, Ubuntu, OpenSUSE)

### Polkit[​](#polkit "Direct link to Polkit")

Polkit is used for escalation prompts, items that require root authorization.

### IdleMonitor[​](#idlemonitor "Direct link to IdleMonitor")

Used to automatically lock, power off monitors, suspend, or hibernate.

### IdleInhibitor[​](#idleinhibitor "Direct link to IdleInhibitor")

Used to prevent the system from idling or sleeping.

### ShortcutInhibitor[​](#shortcutinhibitor "Direct link to ShortcutInhibitor")

## Used to manage keyboard shortcuts, specific to the niri compositor.[​](#used-to-manage-keyboard-shortcuts-specific-to-the-niri-compositor "Direct link to Used to manage keyboard shortcuts, specific to the niri compositor.")

## Optional Features[​](#optional-features "Direct link to Optional Features")

### accountsservice[​](#accountsservice "Direct link to accountsservice")

Required to persist user profile changes, such as profile picture.

### power-profiles-daemon[​](#power-profiles-daemon "Direct link to power-profiles-daemon")

Required to manage power profiles. (e.g. performance, balanced, power-saver)

### I2C/DDC[​](#i2cddc "Direct link to I2C/DDC")

Required for external monitor brightness control, on most distributions requires `i2c-tools` and the user to be in the `i2c` group.

### Terminal[​](#terminal "Direct link to Terminal")

Detected terminals (in priority order): `ghostty`, `kitty`, `alacritty`, `foot`, `wezterm`

### matugen[​](#matugen "Direct link to matugen")

DMS leverages matugen with custom color enrichment (dank16) to generate themes for itself and various applications, terminals, and IDEs.

### dgop[​](#dgop "Direct link to dgop")

Required to use system monitoring widgets and applets (CPU, RAM, Disk, Network, Processes). See [dgop documentation](https://danklinux.com/docs/dgop/) for more information.

### cava[​](#cava "Direct link to cava")

Required for audio visualization in media players.

### khal[​](#khal "Direct link to khal")

Required to enrich calendar with events from local, CalDAV, or other sources supported by khal.

### Network[​](#network "Direct link to Network")

Detected backends: NetworkManager, iwd, systemd-networkd, iwd+systemd-networkd.

DMS supports different network stacks, NetworkManager is recommended for the vast majority of use cases as its also compatible with Gnome, KDE, etc. This is purely for integration within the shell itself (such as conencting to networks, viewing network status, etc.)

- NetworkManager : all features supported (Wifi, Ethernet, VPN)
- iwd : Wifi only, no Ethernet or VPN support
- systemd-networkd : Ethernet only, no Wifi or VPN support
- iwd+systemd-networkd : Wifi and Ethernet supported, no VPN support

### danksearch[​](#danksearch "Direct link to danksearch")

Used for indexed filesystem search in the launcher. Use `/` to initiate a fs search. See [DankSearch documentation](https://danklinux.com/docs/danksearch/) for more information.

### loginctl[​](#loginctl "Direct link to loginctl")

Available on systems using `systemd` or `elogind`. Used for various session management features such as lock integration, lock before suspend, etc.

### fprintd[​](#fprintd "Direct link to fprintd")

Adds fingerprint authentication support to the lock screen.

* * *

## Configuration Files[​](#configuration-files "Direct link to Configuration Files")

FileLocationPurpose`settings.json``~/.config/DankMaterialShell/`Main settings`clsettings.json``~/.config/DankMaterialShell/`Clipboard settings`plugin_settings.json``~/.config/DankMaterialShell/`Plugin configuration`session.json``~/.local/state/DankMaterialShell/`Session state`dms-colors.json``~/.cache/DankMaterialShell/`Cached color scheme

* * *

## Services[​](#services "Direct link to Services")

### dms.service[​](#dmsservice "Direct link to dms.service")

If in use, DMS lifecycle will be managed by systemd. This is optional, DMS can also be started manually or via other init systems.

### greetd[​](#greetd "Direct link to greetd")

Required for the Dank Greeter. (See [DankGreeter documentation](https://danklinux.com/docs/dankgreeter/) for more information.)

* * *

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

### QT\_QPA\_PLATFORMTHEME[​](#qt_qpa_platformtheme "Direct link to QT_QPA_PLATFORMTHEME")

Used to set the Qt platform theme - usually one of `gtk3`, `qt6ct`, or `kde`. This will define how QT applications are themed. Including some elements of DMS (such as icon themes)

### QS\_ICON\_THEME[​](#qs_icon_theme "Direct link to QS_ICON_THEME")

Optional environment variable to set the icon theme for DMS only. Will not effect other applications.

* * *

## JSON Output[​](#json-output "Direct link to JSON Output")

Use `dms doctor -j` for machine-readable output:

```
{
"summary":{
"errors":0,
"warnings":1,
"ok":15,
"info":5
},
"results":[
{
"category":"System",
"name":"Operating System",
"status":"ok",
"message":"Arch Linux",
"details":"ID: arch, Version: rolling, Arch: amd64"
}
]
}
```

## Welcome Wizard Integration[​](#welcome-wizard-integration "Direct link to Welcome Wizard Integration")

The doctor checks are also available in the Welcome Wizard's System Check page. Access it via:

```
dms ipc call welcome doctor
```

Or through Settings → About → Tools → System Check.