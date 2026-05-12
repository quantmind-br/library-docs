---
title: Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/installation
source: sitemap
fetched_at: 2026-04-26T08:39:03.693231211-03:00
rendered_js: false
word_count: 1031
summary: This guide provides instructions for installing the DankMaterialShell (DMS) on various Linux distributions including Arch, Fedora, Debian, Ubuntu, and OpenSUSE, along with its required and optional dependencies.
tags:
    - linux
    - installation
    - desktop-shell
    - dankmaterialshell
    - package-management
    - wayland
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Installation

Install DankMaterialShell across different Linux distributions.

## Dependencies

| Package | Required | Purpose |
|---------|----------|---------|
| [Quickshell](https://github.com/quickshell-mirror/quickshell) | Yes | Core framework |
| [cava](https://github.com/karlstav/cava) | No | Audio visualizer widget |
| [cliphist](https://github.com/sentriz/cliphist) + [wl-clipboard](https://github.com/bugaevc/wl-clipboard) | No | Clipboard history |
| [dgop](https://github.com/AvengeMedia/dgop) | No | System telemetry for resource widgets |
| [dsearch](https://github.com/AvengeMedia/danksearch) | No | Filesystem search engine |
| [matugen](https://github.com/InioX/matugen) | No | Material Design color palette generation |
| [niri](https://github.com/niri-wm/niri) | No | DMS Team's choice of Wayland compositor |
| [qt6-multimedia](https://github.com/qt/qtmultimedia) | No | System sound feedback |

For pre-built packages on Fedora, Debian, Ubuntu, and OpenSUSE, see [[041-docs-danklinux|DankLinux Repository]].

> [!note]
> Only **Quickshell** is required. All other dependencies are optional and enable specific features.

## Arch & Derivatives

`dms` is available in the official Arch repositories (extra). Packages ship the shell, widgets, and CLI. Pair with `niri`, `hyprland`, `sway`, `mangowc`, `labwc`, or `miracle-wm` from official repositories.

## Fedora & CentOS

COPR repositories for Fedora 41/42/43 rawhide and CentOS 10.

### Stable Release

```bash
sudo dnf copr enable avengemedia/dms
sudo dnf install dms
```

### Latest Development Build

```bash
sudo dnf copr enable avengemedia/dms-git
sudo dnf install dms
```

COPR also provides companion packages: `quickshell-git`, `cliphist`, `matugen`, etc.

## Debian & Ubuntu

Available via Open Build Service (OBS) for Debian and Launchpad PPA for Ubuntu.

### Debian

For **Debian 13 (Trixie)**:

```bash
# DankLinux repository
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_13/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_13/ /" | \
sudo tee /etc/apt/sources.list.d/danklinux.list
# DMS stable repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_13/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_13/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms.list
# DMS development repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_13/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_13/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudo apt update
```

For **Debian Testing**:

```bash
# DankLinux repository
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Testing/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Testing/ /" | \
sudo tee /etc/apt/sources.list.d/danklinux.list
# DMS stable repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Testing/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Testing/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms.list
# DMS development repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Testing/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Testing/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudo apt update
```

For **Debian Sid**:

```bash
# DankLinux repository
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Unstable/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Unstable/ /" | \
sudo tee /etc/apt/sources.list.d/danklinux.list
# DMS stable repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Unstable/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Unstable/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms.list
# DMS development repository
curl -fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Unstable/Release.key | \
sudo gpg --dearmor -o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo "deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Unstable/ /" | \
sudo tee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudo apt update
```

#### Install Packages

Install using `apt install dms` or `dms-git`.

### Ubuntu

Ubuntu 25.10+ (Questing) via Launchpad PPA.

#### Stable Release

```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo add-apt-repository ppa:avengemedia/dms
sudo apt update
sudo apt install dms
```

#### Latest Development Build

```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo add-apt-repository ppa:avengemedia/dms-git
sudo apt update
sudo apt install dms-git
```

> [!tip]
> Visit [[041-docs-danklinux|DankLinux Repository]] for OBS and PPA links. Add **niri** or **niri-git** for the best experience.

## OpenSUSE & Derivatives

Available via OBS for OpenSUSE Tumbleweed, Leap 16/16.1 & Slowroll.

### OpenSUSE Tumbleweed

#### Stable Release

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/openSUSE_Tumbleweed/home:AvengeMedia:dms.repo
sudo zypper refresh
sudo zypper install dms
```

#### Latest Development Build

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/openSUSE_Tumbleweed/home:AvengeMedia:dms-git.repo
sudo zypper refresh
sudo zypper install dms-git
```

### OpenSUSE Leap 16

#### Stable Release

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/16.0/home:AvengeMedia:dms.repo
sudo zypper refresh
sudo zypper install dms
```

#### Latest Development Build

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/16.0/home:AvengeMedia:dms-git.repo
sudo zypper refresh
sudo zypper install dms-git
```

### OpenSUSE Leap 16.1

#### Stable Release

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/16.1/home:AvengeMedia:dms.repo
sudo zypper refresh
sudo zypper install dms
```

#### Latest Development Build

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/16.1/home:AvengeMedia:dms-git.repo
sudo zypper refresh
sudo zypper install dms-git
```

### OpenSUSE Slowroll

#### Stable Release

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/openSUSE_Slowroll/home:AvengeMedia:dms.repo
sudo zypper refresh
sudo zypper install dms
```

#### Latest Development Build

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo
sudo zypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/openSUSE_Slowroll/home:AvengeMedia:dms-git.repo
sudo zypper refresh
sudo zypper install dms-git
```

## Gentoo

> [!warning]
> Community maintained. For issues with ebuilds, report to the respective overlay repositories.

Three community overlays provide DMS:

### quilat-overlay

Live ebuild (`gui-shell/dms-9999`) with OpenRC and systemd support. Tracks git master.

```bash
sudo eselect repository add quilat-overlay git https://github.com/Graght/quilat-overlay.git
sudo emaint sync -r quilat-overlay
```

Or manually in `/etc/portage/repos.conf/quilat-overlay.conf`:

```ini
[quilat-overlay]
location = /var/db/repos/quilat-overlay
sync-type = git
sync-uri = https://github.com/Graght/quilat-overlay.git
```

Install:

```bash
# With systemd
sudo emerge --ask gui-shell/dms
# With OpenRC (elogind)
sudo USE="-systemd" emerge --ask gui-shell/dms
```

### tdgentoo

Versioned ebuild (`gui-wm/DankMaterialShell`) pinned to stable releases.

```bash
sudo eselect repository add tdgentoo git https://github.com/timdodge/tdgentoo.git
sudo emaint sync -r tdgentoo
sudo emerge --ask gui-wm/DankMaterialShell
```

### dacyberduck overlay

Under `dank-base/dankmaterialshell`.

```bash
sudo eselect repository add dacyberduck git https://codeberg.org/dacyberduck/gentoo-overlay.git
sudo emaint sync -r dacyberduck
sudo emerge --ask dank-base/dankmaterialshell
```

## NixOS

See [[055-docs-dankmaterialshell-nixos|NixOS Installation]].

## All Other Distributions

> [!warning]
> This guide does not cover compositor installation. You need a compatible Wayland compositor (niri, Hyprland, sway, dwl/MangoWC, Miracle WM, etc.).

### 1. Install Essential Dependencies

#### Quickshell

Build from source if no package is available.

**Base dependencies:** cmake, qt6base, qt6declarative, qtshadertools, pkg-config, cli11; private Qt headers for qt6declarative (and qt6wayland on Qt < 6.10); Qt 6.6+

**Key features and dependencies:**

| Feature | Packages |
|---------|----------|
| Wayland support (default) | qt6wayland, wayland, wayland-protocols |
| Crash reporter (recommended) | google-breakpad |
| Jemalloc (recommended) | jemalloc |
| System tray | qt6dbus |
| PAM authentication | pam |

For complete build instructions, see [Quickshell BUILD.md](https://git.outfoxxed.me/quickshell/quickshell/raw/branch/master/BUILD.md).

#### AccountsService

> [!note]
> AccountsService persists user profile configurations (e.g., profile pictures). Available in most repos as `accountsservice`.

```bash
# Arch
sudo pacman -S accountsservice
# Fedora
sudo dnf install accountsservice
# Debian/Ubuntu
sudo apt install accountsservice
# openSUSE
sudo zypper install accountsservice
# Gentoo
sudo emerge --ask sys-apps/accountsservice
```

### 2. Clone the DMS Repository

```bash
git clone https://github.com/AvengeMedia/DankMaterialShell.git ~/dms
```

### 3. Compile & Install the DMS Backend

*Requires GO 1.24+*

```bash
cd ~/dms
sudo make install
```

> [!note]
> To uninstall: `sudo make uninstall` from the repository directory.

### 4. Install Optional Integrations

- `dgop` — Detailed system metrics and process lists
- `dsearch` — Filesystem search engine
- `matugen` — Material Design color palette generation
- `i2c-tools` — DDC monitor backlight control
- `wl-clipboard` + `cliphist` — Clipboard history
- `cava` — Audio visualizer widget
- `qt6-multimedia` — System sound feedback

## Post Install

1. **Generate compositor config** (niri/Hyprland only): Run `dms setup` to create starter configuration. Other compositors (sway, MangoWC, labwc, Miracle WM) require manual configuration.
2. Enable the systemd service (recommended) or add `dms run` to your compositor config
3. Configure keybinds — see [[084-docs-dankmaterialshell-keybinds-ipc|Keybinds & IPC]]
4. Customize appearance via [[062-docs-dankmaterialshell-application-themes|Themes]]
5. Extend with [[004-docs-dankmaterialshell-plugins-overview|Plugins]]

See [[054-docs-dankmaterialshell-managing|Managing Your Installation]] for service management, environment variables, and updates.

### Systemd Integration (Recommended)

> [!tip]
> If you used [[037-docs-dankinstall|dankinstall]], this is already configured. The installer runs `systemctl --user enable --now dms` during setup.

**Enable autostart:**

```bash
systemctl --user enable dms
```

**Manual control:**

```bash
systemctl --user start dms    # Start now
systemctl --user status dms   # Check status
journalctl --user -u dms -f   # View logs
systemctl --user restart dms  # Restart
systemctl --user disable dms  # Disable autostart
```

> [!warning]
> If using systemd autostart, remove `dms run` / `spawn "dms" "run"` / `exec-once=dms run` from your compositor config to avoid running DMS twice.

### Compositor-Specific Systemd Setup

> [!tip]
> Using `add-wants` binds DMS to a specific compositor's service or session target, so it only runs where you want it.

#### niri

niri has native systemd session integration:

```bash
systemctl --user add-wants niri.service dms
```

DMS starts when niri starts and stops when niri exits.

#### Hyprland

Hyprland does not initialize the systemd user session by default.

`~/.config/systemd/user/hyprland-session.target`:

```ini
[Unit]
Description=Hyprland Session Target
Requires=graphical-session.target
After=graphical-session.target
```

`~/.config/hypr/hyprland.conf`:

```conf
exec-once = dbus-update-activation-environment --systemd --all
exec-once = systemctl --user start hyprland-session.target
```

```bash
systemctl --user add-wants hyprland-session.target dms
```

#### MangoWC

[MangoWC](https://github.com/DreamMaoMao/mangowc) is a dwl-based compositor requiring manual environment export.

`~/.config/systemd/user/mango-session.target`:

```ini
[Unit]
Description=MangoWC Session Target
Requires=graphical-session.target
After=graphical-session.target
```

`~/.config/mango/config.conf`:

```conf
exec-once=dbus-update-activation-environment --systemd --all
exec-once=systemctl --user start mango-session.target
```

```bash
systemctl --user add-wants mango-session.target dms
```

#### Sway

`~/.config/sway/config`:

```conf
exec dbus-update-activation-environment --systemd --all
exec systemctl --user start sway-session.target
```

```bash
systemctl --user add-wants sway-session.target dms
```

#### Miracle WM

[Miracle WM](https://github.com/miracle-wm-org/miracle-wm) is a tiling Wayland compositor built on Mir.

`~/.config/systemd/user/miracle-wm-session.target`:

```ini
[Unit]
Description=Miracle WM Session Target
Requires=graphical-session.target
After=graphical-session.target
```

```bash
systemctl --user add-wants miracle-wm-session.target dms
```