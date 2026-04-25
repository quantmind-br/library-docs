---
title: Managing Your Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/managing
source: sitemap
fetched_at: 2026-04-07T21:33:04.998384394-03:00
rendered_js: false
word_count: 580
summary: This guide provides comprehensive instructions on managing the DankMaterialShell service, covering setup via systemd or manual methods, configuring environment variables for various desktop environments, updating the software across multiple package managers, and details on complete uninstallation and troubleshooting.
tags:
    - service-management
    - configuration
    - systemd
    - environment-variables
    - updating
    - uninstallation
    - guide
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

```bash
systemctl --userenable--now dms
```

**Common operations:**

```bash
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

```bash
systemctl --user add-wants niri.service dms
```

This ties the dms service to niri's session, so it won't start under other desktop environments.

#### Other Compositors[​](#other-compositors "Direct link to Other Compositors")

Hyprland, Sway, MangoWC, and Miracle WM don't have systemd session targets. If you use multiple desktop environments and only want DMS on one of them, disable the systemd unit and start DMS from your compositor config instead:

```bash
systemctl --user disable dms
```

Then add `dms run` to your compositor's autostart (see [Manual Launch](#manual-launch) below).

### Manual Launch[​](#manual-launch "Direct link to Manual Launch")

For testing, debugging, or if you prefer compositor-managed startup:

**Compositor autostart:**

```bash
# Hyprland (~/.config/hypr/hyprland.conf)
exec-once = dms run

# Sway (~/.config/sway/config)
exec dms run

# niri (~/.config/niri/config.kdl)
spawn-at-startup "dms""run"
```

**Manual control:**

```bash
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

You can also run `systemctl --user edit dms` and add `Environment=VAR=Value` lines under `[Service]`. This only affects DMS and apps it launches, whereas `90-dms.conf` applies to all user sessions.

### Checking Your Environment[​](#checking-your-environment "Direct link to Checking Your Environment")

```bash
# See what's currently set
env|grep-E"QT_|GTK|XDG"

# Check dankinstall's environment file (if it exists)
cat ~/.config/environment.d/90-dms.conf
```

### Manual Configuration[​](#manual-configuration "Direct link to Manual Configuration")

If you didn't use dankinstall, set environment variables in your compositor config:

**niri** (`~/.config/niri/config.kdl`):

```kdl
environment {
  QT_QPA_PLATFORM "wayland"
  QT_QPA_PLATFORMTHEME "gtk3"
  ELECTRON_OZONE_PLATFORM_HINT "auto"
}
```

**Hyprland** (`~/.config/hypr/hyprland.conf`):

```conf
env = QT_QPA_PLATFORM,wayland
env = QT_QPA_PLATFORMTHEME,gtk3
env = ELECTRON_OZONE_PLATFORM_HINT,auto
```

Or create `~/.config/environment.d/90-dms.conf`:

```ini
QT_QPA_PLATFORM=wayland
QT_QPA_PLATFORMTHEME=gtk3
ELECTRON_OZONE_PLATFORM_HINT=auto
```

Changes to `environment.d` require logging out and back in (or rebooting) to take effect.

You can also run `systemctl --user edit dms` and add `Environment=` lines under `[Service]`:

```ini
[Service]
Environment=QT_QPA_PLATFORM=wayland
Environment=QT_QPA_PLATFORMTHEME=gtk3
Environment=ELECTRON_OZONE_PLATFORM_HINT=auto
```

This only affects DMS and apps it launches, whereas `90-dms.conf` applies to all user sessions.

## Updating[​](#updating "Direct link to Updating")

### Package Installations[​](#package-installations "Direct link to Package Installations")

**Arch & Derivatives:**

```bash
sudo pacman -Syu dms-shell
```

**Fedora & Derivatives:**

**Debian & Ubuntu:**

```bash
sudoapt update &&sudoapt upgrade dms
# or dms-git
```

**OpenSUSE:**

```bash
sudozypper refresh &&sudozypper update dms
```

**NixOS:**

```bash
# Update flake inputs, then:
sudo nixos-rebuild switch
```

After package updates, restart the shell:

### Manual Installations[​](#manual-installations "Direct link to Manual Installations")

For source builds or [non-packaged](https://danklinux.com/docs/dankmaterialshell/installation) distro dankinstall setups:

For manually compiled dependencies (quickshell, niri, etc.), use the interactive TUI:

```bash
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

```bash
sudo pacman -Rns dms-shell
```

**Fedora, Debian, Ubuntu, OpenSUSE:**

```bash
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

```bash
# Stop and disable the service
systemctl --user disable --now dms

# Remove the binary and shell config
rm-rf ~/.config/quickshell/dms
sudorm /usr/local/bin/dms
```

### Cleanup[​](#cleanup "Direct link to Cleanup")

After uninstalling (package or manual), remove leftover user data:

```bash
rm-r ~/.config/DankMaterialShell ~/.local/state/DankMaterialShell ~/.cache/DankMaterialShell
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