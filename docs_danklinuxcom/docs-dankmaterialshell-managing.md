---
title: Managing Your Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/managing
source: sitemap
fetched_at: 2026-01-24T13:33:50.225213472-03:00
rendered_js: false
word_count: 508
summary: This guide provides instructions for managing, updating, and configuring DankMaterialShell, covering service management via systemd, environment variable setup, and troubleshooting common issues.
tags:
    - dankmaterialshell
    - systemd
    - wayland
    - linux-configuration
    - troubleshooting
    - update-guide
category: guide
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

This guide covers how to manage, update, and configure DankMaterialShell after installation.

## Service Management[​](#service-management "Direct link to Service Management")

DMS can run as a systemd user service or be launched manually. The `dms` CLI handles both transparently - commands like `dms restart` work regardless of how DMS was started.

DankInstall Users

If you installed via [dankinstall](https://danklinux.com/docs/dankinstall), DMS is configured as a systemd service by default. The installer runs `systemctl --user enable --now dms` during setup. You don't need to add `dms run` to your compositor config.

### Systemd (Recommended)[​](#systemd-recommended "Direct link to Systemd (Recommended)")

Systemd provides automatic startup, proper session integration, and logging via journalctl.

**Enable and start:**

```
systemctl --userenable--now dms
```

**Common operations:**

```
# Check status
systemctl --user status dms

# View logs
journalctl --user-u dms -f

# Restart (or just use: dms restart)
systemctl --user restart dms

# Stop
systemctl --user stop dms

# Disable autostart
systemctl --user disable dms
```

warning

If using systemd, remove any `dms run` / `spawn "dms" "run"` lines from your compositor config to avoid running DMS twice.

#### niri: Per-Session Control[​](#niri-per-session-control "Direct link to niri: Per-Session Control")

niri has proper systemd session integration. You can make DMS only start under niri (not Plasma, GNOME, etc.):

```
systemctl --user add-wants niri.service dms
```

This ties the dms service to niri's session, so it won't start under other desktop environments.

#### Other Compositors[​](#other-compositors "Direct link to Other Compositors")

Hyprland, Sway, and MangoWC don't have systemd session targets. If you use multiple desktop environments and only want DMS on one of them, disable the systemd unit and start DMS from your compositor config instead:

```
systemctl --user disable dms
```

Then add `dms run` to your compositor's autostart (see [Manual Launch](#manual-launch) below).

### Manual Launch[​](#manual-launch "Direct link to Manual Launch")

For testing, debugging, or if you prefer compositor-managed startup:

**Compositor autostart:**

```
# Hyprland (~/.config/hypr/hyprland.conf)
exec-once = dms run

# Sway (~/.config/sway/config)
exec dms run

# niri (~/.config/niri/config.kdl)
spawn-at-startup "dms""run"
```

**Manual control:**

```
# Launch (foreground)
dms run

# Launch (background/daemon)
dms run -d

# Restart
dms restart

# Kill
dms kill
```

### Switching Between Methods[​](#switching-between-methods "Direct link to Switching Between Methods")

**From manual to systemd:**

1. Remove `dms run` from your compositor config
2. Enable the service: `systemctl --user enable --now dms`
3. Restart your compositor or log out/in

**From systemd to manual:**

1. Disable the service: `systemctl --user disable --now dms`
2. Add `dms run` to your compositor's autostart
3. Restart your compositor or log out/in

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

DMS and its themed applications need certain environment variables set. Where these live depends on your setup.

DankInstall Users

dankinstall creates `~/.config/environment.d/90-dms.conf` with the necessary variables. This file is loaded by systemd for all user sessions. If you need to change Qt theming (e.g., switching to qt6ct), edit this file.

### Checking Your Environment[​](#checking-your-environment "Direct link to Checking Your Environment")

```
# See what's currently set
env|grep-E"QT_|GTK|XDG"

# Check dankinstall's environment file (if it exists)
cat ~/.config/environment.d/90-dms.conf
```

### Manual Configuration[​](#manual-configuration "Direct link to Manual Configuration")

If you didn't use dankinstall, set environment variables in your compositor config:

**niri** (`~/.config/niri/config.kdl`):

```
environment {
  QT_QPA_PLATFORM "wayland"
  QT_QPA_PLATFORMTHEME "gtk3"
  ELECTRON_OZONE_PLATFORM_HINT "auto"
}
```

**Hyprland** (`~/.config/hypr/hyprland.conf`):

```
env = QT_QPA_PLATFORM,wayland
env = QT_QPA_PLATFORMTHEME,gtk3
env = ELECTRON_OZONE_PLATFORM_HINT,auto
```

Or create `~/.config/environment.d/90-dms.conf`:

```
QT_QPA_PLATFORM=wayland
QT_QPA_PLATFORMTHEME=gtk3
ELECTRON_OZONE_PLATFORM_HINT=auto
```

Changes to `environment.d` require logging out and back in (or rebooting) to take effect.

## Updating[​](#updating "Direct link to Updating")

### Package Installations[​](#package-installations "Direct link to Package Installations")

**Arch & Derivatives:**

```
paru -Syu dms-shell-bin
# or
paru -Syu dms-shell-git
```

**Fedora & Derivatives:**

**Debian & Ubuntu:**

```
sudoapt update &&sudoapt upgrade dms
# or dms-git
```

**OpenSUSE:**

```
sudozypper refresh &&sudozypper update dms
```

**NixOS:**

```
# Update flake inputs, then:
sudo nixos-rebuild switch
```

After package updates, restart the shell:

### Manual Installations[​](#manual-installations "Direct link to Manual Installations")

For source builds or dankinstall setups:

For manually compiled dependencies (quickshell, niri, etc.), use the interactive TUI:

```
dms
# Navigate to Update → select packages to rebuild
```

## After Updating[​](#after-updating "Direct link to After Updating")

1. Restart DMS: `dms restart`
2. Check [release notes](https://github.com/AvengeMedia/DankMaterialShell/releases) for breaking changes
3. Review Settings if new options are available
4. Update plugins if needed

## Uninstalling[​](#uninstalling "Direct link to Uninstalling")

### Package Installations[​](#package-installations-1 "Direct link to Package Installations")

**Arch & Derivatives:**

```
# Whichever you have installed
sudo pacman -Rns dms-shell-bin
# or
sudo pacman -Rns dms-shell-git
```

**Fedora, Debian, Ubuntu, OpenSUSE:**

```
# Stable
sudo dnf remove dms      # Fedora
sudoapt remove dms      # Debian/Ubuntu
sudozypper remove dms   # OpenSUSE

# Or git version
sudo dnf remove dms-git
sudoapt remove dms-git
sudozypper remove dms-git
```

### Manual/Source Installs[​](#manualsource-installs "Direct link to Manual/Source Installs")

```
# Stop and disable the service
systemctl --user disable --now dms

# Remove the binary and shell config
rm-rf ~/.config/quickshell/dms
sudorm /usr/local/bin/dms
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**DMS won't start:**

- Check logs: `journalctl --user -u dms -n 50` (systemd) or run `dms run` in a terminal
- Verify quickshell is installed: `which qs`
- Kill stuck processes: `dms kill`

**Settings not applying:**

- Backup and remove `~/.config/DankMaterialShell/settings.json`
- Restart DMS to regenerate defaults

**Environment variables not working:**

- For `environment.d` changes: log out and back in
- For compositor config changes: restart the compositor
- Verify with `echo $QT_QPA_PLATFORMTHEME`

**Multiple instances running:**