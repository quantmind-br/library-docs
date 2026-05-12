---
title: Managing Your Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/managing
source: sitemap
fetched_at: 2026-04-26T08:39:09.545791888-03:00
rendered_js: false
word_count: 584
summary: This guide provides instructions for managing, configuring, updating, and troubleshooting the DankMaterialShell (DMS) desktop environment component.
tags:
    - dms
    - linux
    - systemd
    - compositor
    - configuration
    - shell-management
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

## Service Management

DMS runs as a systemd user service or manually. The `dms` CLI handles both transparently.

> [!tip] DankInstall Users
> [[037-docs-dankinstall|dankinstall]] configures DMS as a systemd service by default. The installer runs `systemctl --user enable --now dms`. Remove any `dms run` lines from your compositor config.

### Systemd (Recommended)

```bash
systemctl --user enable --now dms
```

**Common operations:**

| Operation | Command |
|-----------|---------|
| Check status | `systemctl --user status dms` |
| View logs | `journalctl --user -u dms -f` |
| Restart | `systemctl --user restart dms` |
| Stop | `systemctl --user stop dms` |
| Disable | `systemctl --user disable dms` |

> [!warning]
> Remove `dms run` / `spawn "dms" "run"` from compositor config to avoid duplicate instances.

#### niri: Per-Session Control

niri has proper systemd session integration. Tie DMS to niri only:

```bash
systemctl --user add-wants niri.service dms
```

DMS won't start under other desktop environments.

#### Other Compositors

Hyprland, Sway, MangoWC, and Miracle WM lack systemd session targets. To restrict DMS to one compositor:

```bash
systemctl --user disable dms
# Then add `dms run` to compositor autostart
```

### Manual Launch

**Compositor autostart:**

```bash
# Hyprland (~/.config/hypr/hyprland.conf)
exec-once = dms run
# Sway (~/.config/sway/config)
exec dms run
# niri (~/.config/niri/config.kdl)
spawn-at-startup "dms" "run"
```

**Direct control:**

```bash
dms run        # foreground
dms run -d     # background/daemon
dms restart
dms kill
```

### Switching Methods

**Manual to systemd:**
1. Remove `dms run` from compositor config
2. `systemctl --user enable --now dms`
3. Restart compositor or log out/in

**Systemd to manual:**
1. `systemctl --user disable --now dms`
2. Add `dms run` to compositor autostart
3. Restart compositor or log out/in

## Environment Variables

DMS and themed applications need specific environment variables.

> [!tip] DankInstall Users
> [[037-docs-dankinstall|dankinstall]] creates `~/.config/environment.d/90-dms.conf`. Edit this file to change Qt theming. Alternatively, use `systemctl --user edit dms` to add `Environment=VAR=Value` under `[Service]` — this only affects DMS and its launched apps.

### Checking Your Environment

```bash
env | grep -E "QT_|GTK|XDG"
cat ~/.config/environment.d/90-dms.conf
```

### Manual Configuration

Set variables in compositor config:

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

Or `~/.config/environment.d/90-dms.conf`:
```ini
QT_QPA_PLATFORM=wayland
QT_QPA_PLATFORMTHEME=gtk3
ELECTRON_OZONE_PLATFORM_HINT=auto
```

> [!note]
> Changes to `environment.d` require logging out and back in.

## Updating

### Package Installations

| Distro | Command |
|--------|---------|
| Arch | `sudo pacman -Syu dms-shell` |
| Debian/Ubuntu | `sudo apt update && sudo apt upgrade dms` |
| OpenSUSE | `sudo zypper refresh && sudo zypper update dms` |
| NixOS | `sudo nixos-rebuild switch` (after updating flake inputs) |

After package updates, restart DMS: `dms restart`

### Manual Installations

For source builds or non-packaged setups, use the interactive TUI:

```bash
dms
# Navigate to Update → select packages to rebuild
```

## After Updating

1. Restart DMS: `dms restart`
2. Check [[https://github.com/AvengeMedia/DankMaterialShell/releases|release notes]] for breaking changes
3. Review Settings for new options
4. Update plugins if needed

## Uninstalling

### Package Installations

| Distro | Stable | Git |
|--------|--------|-----|
| Arch | `sudo pacman -Rns dms-shell` | — |
| Fedora | `sudo dnf remove dms` | `sudo dnf remove dms-git` |
| Debian/Ubuntu | `sudo apt remove dms` | `sudo apt remove dms-git` |
| OpenSUSE | `sudo zypper remove dms` | `sudo zypper remove dms-git` |

### Manual/Source Installs

```bash
systemctl --user disable --now dms
rm -rf ~/.config/quickshell/dms
sudo rm /usr/local/bin/dms
```

### Cleanup

```bash
rm -rf ~/.config/DankMaterialShell ~/.local/state/DankMaterialShell ~/.cache/DankMaterialShell
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| DMS won't start | Check logs: `journalctl --user -u dms -n 50` or run `dms run` in terminal |
| | Verify quickshell installed: `which qs` |
| | Kill stuck processes: `dms kill` |
| Settings not applying | Backup and remove `~/.config/DankMaterialShell/settings.json`, restart DMS |
| Environment variables not working | For `environment.d`: log out/in; for compositor config: restart compositor |
| Multiple instances | Run `dms kill` to stop duplicates |
