---
title: DankInstall | Dank Linux
url: https://danklinux.com/docs/dankinstall
source: sitemap
fetched_at: 2026-01-24T13:33:12.39748497-03:00
rendered_js: false
word_count: 731
summary: This document provides instructions and technical details for using dankinstall, an interactive script that automates the setup of the DankMaterialShell desktop environment across multiple Linux distributions. It covers core component installation, distribution-specific package management, and system configuration for Wayland-based workflows.
tags:
    - dankmaterialshell
    - linux-installation
    - wayland-compositor
    - desktop-environment
    - automation-script
    - hyprland
    - niri-compositor
    - package-management
category: guide
---

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║
██║  ██║███████║██╔██╗ ██║█████╔╝ ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║
██║  ██║██╔══██║██║╚██╗██║██╔═██╗ ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
```

`dankinstall` sets up the full [DankMaterialShell](https://danklinux.com/docs/dankmaterialshell/overview) desktop experience - wallpapers, auto-theming, notifications, lock screen, and everything else you'd expect from a modern desktop. It installs packages and configures user-level settings for your compositor and terminal. If you already have niri or Hyprland set up, dankinstall can work around your existing config (and always backs things up before making changes).

## Quickstart[​](#quickstart "Direct link to Quickstart")

```
curl-fsSL https://install.danklinux.com |sh
```

tip

The installer is interactive and guides you through setup for your distribution. You can also download the [latest release](https://github.com/AvengeMedia/DankMaterialShell/releases) manually.

## What Gets Installed[​](#what-gets-installed "Direct link to What Gets Installed")

### Core Components[​](#core-components "Direct link to Core Components")

- [**DankMaterialShell**](https://danklinux.com/docs/dankmaterialshell/overview) - The desktop shell built with quickshell & Go.
- **Compositor** - Your choice of [niri](https://github.com/YaLTeR/niri) or [Hyprland](https://hypr.land)
- **Terminal** - Ghostty, with Kitty and Alacritty as alternatives
- **dms CLI** - Backend service providing dbus APIs, plugin management, and wayland protocol implementations

### Desktop Utilities[​](#desktop-utilities "Direct link to Desktop Utilities")

- **quickshell** - The QML-based shell framework powering DMS
- **matugen** - Auto-theming engine that generates color schemes from wallpapers
- **dgop** - System resource monitoring (CPU, RAM, GPU, temperatures)
- **dsearch** - Blazingly fast filesystem search.
- **cliphist** - Clipboard history manager
- **wl-clipboard** - Clipboard utilities for Wayland

### System Packages[​](#system-packages "Direct link to System Packages")

Build dependencies: git, jq, curl, wget, go, cmake, rustup. The exact package list varies by distribution.

## Supported Distributions[​](#supported-distributions "Direct link to Supported Distributions")

### Arch Linux & Derivatives[​](#arch-linux--derivatives "Direct link to Arch Linux & Derivatives")

**Supported:** Arch, ArchARM, Archcraft, CachyOS, EndeavourOS, Manjaro

Uses `pacman` for system packages from official repos. Builds quickshell, matugen (pre-compiled binary), and dgop from AUR using `makepkg` - no AUR helper needed. niri and hyprland are available in official repos.

If you're using archinstall, the `minimal` profile with `NetworkManager` for networking is a good starting point.

### Fedora & Derivatives[​](#fedora--derivatives "Direct link to Fedora & Derivatives")

**Supported:** Fedora, Nobara, Fedora Asahi Remix

Almost everything comes from official repos or COPR repositories (`avengemedia/danklinux`, `avengemedia/dms`, `solopasha/hyprland`, `yalter/niri`). Only dgop needs to be built from source with Go.

dankinstall is tested on Workstation Edition but should work fine on any Fedora flavor.

### Ubuntu[​](#ubuntu "Direct link to Ubuntu")

**Supported:** Ubuntu 25.04+

Packages come from the [DankLinux PPA](https://danklinux.com/docs/danklinux#ubuntu) (`ppa:avengemedia/danklinux`). Hyprland comes from `ppa:cppiber/hyprland`.

### Debian[​](#debian "Direct link to Debian")

**Supported:** Debian 13+ (Trixie), Debian Testing, Debian Sid

Packages come from the [DankLinux OBS repository](https://danklinux.com/docs/danklinux#debian). **niri only** - Debian doesn't have Hyprland packages yet.

### openSUSE Tumbleweed[​](#opensuse-tumbleweed "Direct link to openSUSE Tumbleweed")

Good package availability out of the box. niri, hyprland, ghostty, and most tools are in standard repos. Additional packages come from the [DankLinux OBS repository](https://danklinux.com/docs/danklinux#opensuse).

### Gentoo[​](#gentoo "Direct link to Gentoo")

warning

Gentoo requires a **systemd** installation. OpenRC is not supported.

**Special Notes:**

- Gentoo installs are **highly variable** and user-specific, success is not guaranteed.
  
  - `dankinstall` is most likely to succeed on a fresh stage3/systemd system
- Uses Portage package manager with GURU overlay for additional packages
- Automatically configures global USE flags in `/etc/portage/make.conf`
  
  - Will create or append to your existing USE flags.
- Automatically configures package-specific USE flags in `/etc/portage/package.use/danklinux`
- Unmasks packages as-needed with architecture keywords in `/etc/portage/package.accept_keywords/danklinux`
- Supports both `amd64` and `arm64` architectures dynamically
- If not using bin packages, prepare for long compilation times
- **Ghostty** is removed from the options, due to extremely long compilation time of its

**Package Sources:**

PackageSourceNotesSystem packages (git, etc.)Official reposVia `emerge`niriGURU overlayWith dbus and screencast USE flagshyprlandOfficial repos (GURU for -git)Depends on variant selection, with X USE flagquickshellGURU overlayAlways uses live ebuild (`**` keywords), full feature setmatugenGURU overlayColor generation toolcliphistGURU overlayClipboard managerxdg-desktop-portal-gtkOfficial reposWith wayland and X USE flagsmate-polkitOfficial reposPolicyKit authentication agentaccountsserviceOfficial reposUser account managementdgopManualBuilt from source with Goxwayland-satelliteManualFor niri X11 app supportDankMaterialShellManualGit clone to `~/.config/quickshell/dms`

**Global USE Flags:** `dbus udev alsa policykit jpeg png webp gif tiff svg brotli gdbm accessibility gtk qt6 egl gbm`

**Package-Specific USE Flags:**

- `sys-apps/xdg-desktop-portal-gtk`: wayland X
- `gui-wm/niri`: dbus screencast
- `gui-wm/hyprland`: X
- `dev-qt/qtbase`: wayland opengl vulkan widgets
- `dev-qt/qtdeclarative`: opengl vulkan
- `media-libs/mesa`: opengl vulkan
- `gui-apps/quickshell`: breakpad jemalloc sockets wayland layer-shell session-lock toplevel-management screencopy X pipewire tray mpris pam hyprland hyprland-global-shortcuts hyprland-focus-grab i3 i3-ipc bluetooth

## What About Manual Building?[​](#what-about-manual-building "Direct link to What About Manual Building?")

Most distros now have pre-built packages via the [DankLinux Repository](https://danklinux.com/docs/danklinux). The installer handles any remaining builds automatically:

- **dgop** - Built from Go source on distros without packages. Installs to `/usr/local/bin`.
- **Gentoo** - Still builds most packages from source via Portage (see above).

## Managing Your Setup[​](#managing-your-setup "Direct link to Managing Your Setup")

dankinstall configures DMS as a **systemd user service** by default. The shell starts automatically when you log in - no need to add anything to your compositor config.

```
# Restart the shell (works with both systemd and manual setups)
dms restart

# Check service status
systemctl --user status dms

# View logs
journalctl --user-u dms -f

# Interactive management TUI
dms

# Send IPC commands to running shell
dms ipc <command>
```

tip

See [Managing Your Installation](https://danklinux.com/docs/dankmaterialshell/managing) for details on switching between systemd and manual startup, environment variable configuration, and more.

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

dankinstall creates `~/.config/environment.d/90-dms.conf` with environment variables for Qt/GTK theming and Wayland compatibility. If you need to change Qt platform theming (e.g., switching from `gtk3` to `qt6ct`), edit this file and log out/in for changes to take effect.