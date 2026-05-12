---
title: System Diagnostics (doctor) | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-doctor
source: sitemap
fetched_at: 2026-04-26T08:38:45.875635508-03:00
rendered_js: false
word_count: 906
summary: This document explains the functionality of the dms doctor command, which is used to diagnose system configurations, verify dependencies, and troubleshoot the Dank Material Shell installation.
tags:
    - dms
    - troubleshooting
    - cli-tools
    - system-diagnostics
    - dank-material-shell
    - linux-configuration
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Version: 1.4

`dms doctor` diagnoses your DMS installation, verifies dependencies, and checks system configuration.

## Usage

```bash
dms doctor           # Standard output
dms doctor -v        # Verbose output with paths and details
dms doctor -j        # JSON output for scripting
```

## Status Indicators

| Icon | Status   | Meaning                                      |
|------|----------|----------------------------------------------|
| 🟢   | OK       | Check passed                                 |
| 🟡   | Warning  | Non-critical issue, may affect some features |
| 🔴   | Error    | Critical issue that needs attention          |
| ⚪   | Info     | Informational, no action needed              |

## System Checks

### Operating System

All GNU/Linux distributions are supported — informational only.

### Architecture

Officially supported: `amd64` / `arm64`. Other architectures may work with manual compilation.

### Display Server

DMS only supports Wayland. This check verifies X11 is not in use.

## Version Checks

| Check         | Description                                                       |
|---------------|-------------------------------------------------------------------|
| DMS CLI       | Backend CLI version (should match quickshell config version)      |
| Quickshell    | Framework version (older versions may reduce feature set)         |
| DMS Shell     | Shell configuration version (should match DMS CLI version)        |

## Installation Checks

| Check           | Description                                                    |
|-----------------|----------------------------------------------------------------|
| DMS Configuration | Config directory exists at `$XDG_CONFIG_HOME/.config/DankMaterialShell/` |
| shell.qml       | Installed location of DMS shell configuration                   |
| Install Type    | `system` (package manager), `user` (manual), `nix` (Nix)       |

## Compositor Checks

All Wayland compositors implementing [layer shell protocol](https://wayland.app/protocols/wlr-layer-shell-unstable-v1) are supported with varying feature sets.

### Supported Compositors

| Compositor   | Detection Command           |
|--------------|-----------------------------|
| niri         | `niri --version`            |
| Hyprland     | `hyprctl version`           |
| mangowc      | `mangowc --version`         |
| labwc        | `labwc --version`           |
| Sway         | `sway --version`            |
| Miracle WM   | `miracle-wm --version`      |
| River        | `river -version`            |
| Wayfire      | `wayfire --version`         |

### Active Compositor

Currently running compositor.

## Quickshell Features

These depend on how Quickshell was built. Using `quickshell-git` provides full feature support.

> [!info]
> All features require `quickshell-git` or `quickshell` from Dank Linux repositories (Fedora, Debian, Ubuntu, OpenSUSE).

| Feature             | Purpose                                                    |
|---------------------|------------------------------------------------------------|
| Polkit              | Escalation prompts for root authorization                  |
| IdleMonitor         | Auto lock, power off monitors, suspend, hibernate          |
| IdleInhibitor       | Prevent system from idling/sleeping                        |
| ShortcutInhibitor   | Manage keyboard shortcuts (niri-specific)                  |

## Optional Features

| Feature                  | Description                                                           |
|--------------------------|-----------------------------------------------------------------------|
| `accountsservice`        | Persist user profile changes (e.g., profile picture)                  |
| `power-profiles-daemon`  | Manage power profiles (performance, balanced, power-saver)            |
| `cups-pk-helper`         | Printer management (D-Bus: `org.opensuse.CupsPkHelper.Mechanism`)   |
| `i2c-tools` + `i2c` group | External monitor brightness control (DDC/I2C)                        |
| `matugen`                | Color generation with dank16 enrichment for themes                    |
| `dgop`                   | System monitoring widgets/applets (CPU, RAM, Disk, Network, Processes) — see [[086-docs-dgop]] |
| `cava`                   | Audio visualization in media players                                   |
| `khal`                   | Calendar event enrichment (local, CalDAV, etc.)                      |
| `NetworkManager`         | Full network integration (Wifi, Ethernet, VPN)                         |
| `iwd`                    | Wifi only (no Ethernet/VPN)                                           |
| `systemd-networkd`       | Ethernet only (no Wifi/VPN)                                           |
| `iwd+systemd-networkd`   | Wifi + Ethernet (no VPN)                                              |
| `gp-saml-gui`            | GlobalProtect SAML VPN browser auth — see [[085-docs-danksearch]] docs |
| `openconnect`            | Converts SAML cookie to full auth for GlobalProtect SAML VPNs         |
| `danksearch`             | Indexed filesystem search in launcher — see [[085-docs-danksearch]]   |
| `loginctl`               | Session management (lock, lock before suspend) — systemd/elogind      |
| `fprintd`                | Fingerprint authentication support                                     |

> [!info]
> `gp-saml-gui` and `openconnect` are only needed for GlobalProtect VPNs with SAML authentication. Standard username/password VPNs work without them.

## Configuration Files

| File                  | Location                                           | Purpose                       |
|-----------------------|---------------------------------------------------|-------------------------------|
| `settings.json`       | `~/.config/DankMaterialShell/`                   | Main settings                 |
| `clsettings.json`     | `~/.config/DankMaterialShell/`                   | Clipboard settings            |
| `plugin_settings.json`| `~/.config/DankMaterialShell/`                   | Plugin configuration          |
| `session.json`        | `~/.local/state/DankMaterialShell/`              | Session state                 |
| `dms-colors.json`     | `~/.cache/DankMaterialShell/`                     | Cached color scheme           |

## Services

| Service      | Description                                                       |
|--------------|-------------------------------------------------------------------|
| `dms.service`| Optional systemd lifecycle management (can also start manually)   |
| `greetd`     | Required for Dank Greeter — see [[104-docs-dankgreeter]]          |

## Environment Variables

| Variable              | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `QT_QPA_PLATFORMTHEME`| Qt platform theme (`gtk3`, `qt6ct`, `kde`) — affects Qt app theming |
| `QS_ICON_THEME`       | Icon theme for DMS only (does not affect other applications)   |

## JSON Output

`dms doctor -j` returns machine-readable output:

```json
{
  "summary": {
    "errors": 0,
    "warnings": 1,
    "ok": 15,
    "info": 5
  },
  "results": [
    {
      "category": "System",
      "name": "Operating System",
      "status": "ok",
      "message": "Arch Linux",
      "details": "ID: arch, Version: rolling, Arch: amd64"
    }
  ]
}
```

## Welcome Wizard Integration

System checks are available in the Welcome Wizard at **Settings → About → Tools → System Check**, or via:

```bash
dms ipc call welcome doctor
```

#dms #troubleshooting #cli-tools #system-diagnostics
