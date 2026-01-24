---
title: Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/installation
source: sitemap
fetched_at: 2026-01-24T13:33:44.261135291-03:00
rendered_js: false
word_count: 873
summary: This guide provides step-by-step instructions for installing DankMaterialShell on various Linux distributions, including dependency requirements and repository configurations for Arch, Fedora, Debian, and Ubuntu.
tags:
    - linux-installation
    - dankmaterialshell
    - package-management
    - arch-aur
    - fedora-copr
    - debian-apt
    - ubuntu-ppa
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

This guide covers installation of DankMaterialShell across different Linux distributions and methods.

## Dependencies[​](#dependencies "Direct link to Dependencies")

- [**Quickshell**](https://github.com/quickshell-mirror/quickshell) (required) - The core framework
- [**cava**](https://github.com/karlstav/cava) (optional) - Audio visualizer widget
- [**cliphist**](https://github.com/sentriz/cliphist) + [**wl-clipboard**](https://github.com/bugaevc/wl-clipboard) (optional) - Clipboard history
- [**dgop**](https://github.com/AvengeMedia/dgop) (optional) - System telemetry for resource widgets
- [**dsearch**](https://github.com/AvengeMedia/danksearch) (optional) - Filesystem search engine
- [**matugen**](https://github.com/InioX/matugen) (optional) - Material Design color palette generation
- [**niri**](https://github.com/YaLTeR/niri) (optional) - DMS Team's choice of Wayland compositor
- [**qt6-multimedia**](https://github.com/qt/qtmultimedia) (optional) - System sound feedback

For pre-built packages on Fedora, Debian, Ubuntu, and OpenSUSE, see the [DankLinux Repository](https://danklinux.com/docs/danklinux) page.

note

Only **Quickshell** is required. All other dependencies are optional and enable specific features.

## Arch & Derivatives[​](#arch--derivatives "Direct link to Arch & Derivatives")

`dms` is available on the [AUR](https://aur.archlinux.org/), it is assumed that you have an aur helper installed such as [paru](https://aur.archlinux.org/packages/paru) or [yay](https://aur.archlinux.org/packages/yay).

For the sake of consistency, we will use `paru` in the examples.

### Stable Release[​](#stable-release "Direct link to Stable Release")

### Latest Development Build[​](#latest-development-build "Direct link to Latest Development Build")

These packages ship the shell, widgets, and CLI. Pair them with `niri`, `hyprland`, `sway`, `mangowc`, or `labwc` packages from the official repositories for a complete desktop stack.

## Fedora & CentOS[​](#fedora--centos "Direct link to Fedora & CentOS")

DankMaterialShell is available through COPR repositories for Fedora 41/42/43 rawhide and CentOS 10. Enable the COPR repositories managed by the team to install prebuilt packages:

### Stable Release[​](#stable-release-1 "Direct link to Stable Release")

```
sudo dnf copr enable avengemedia/dms
sudo dnf install dms
```

### Latest Development Build[​](#latest-development-build-1 "Direct link to Latest Development Build")

```
sudo dnf copr enable avengemedia/dms-git
sudo dnf install dms
```

The COPR repositories also provide companion packages such as `quickshell-git`, `cliphist`, `matugen`, and other utilities used by the default configuration.

## Debian & Ubuntu[​](#debian--ubuntu "Direct link to Debian & Ubuntu")

DankMaterialShell is available through Open Build Service (OBS) for Debian and Launchpad PPA for Ubuntu.

### Debian[​](#debian "Direct link to Debian")

For **Debian 13 (Trixie)**:

```
# DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_13/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_13/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list

# DMS stable repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_13/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_13/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms.list

# DMS development repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_13/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_13/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudoapt update
```

For **Debian Testing**:

```
# DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Testing/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Testing/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list

# DMS stable repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Testing/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Testing/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms.list

# DMS development repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Testing/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Testing/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudoapt update
```

For **Debian Sid**:

```
# DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Unstable/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Unstable/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list

# DMS stable repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Unstable/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/Debian_Unstable/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms.list

# DMS development repository
curl-fsSL https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Unstable/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/avengemedia-dms-git.gpg
echo"deb [signed-by=/etc/apt/keyrings/avengemedia-dms-git.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/Debian_Unstable/ /"|\
sudotee /etc/apt/sources.list.d/avengemedia-dms-git.list
sudoapt update
```

#### Install Packages[​](#install-packages "Direct link to Install Packages")

Install the **stable release**:

Install the **latest development build**:

### Ubuntu[​](#ubuntu "Direct link to Ubuntu")

Ubuntu 25.10+ (Questing) is supported via Launchpad PPA.

#### Stable Release[​](#stable-release-2 "Direct link to Stable Release")

```
sudo add-apt-repository ppa:avengemedia/danklinux
sudo add-apt-repository ppa:avengemedia/dms
sudoapt update
sudoaptinstall dms
```

#### Latest Development Build[​](#latest-development-build-2 "Direct link to Latest Development Build")

```
sudo add-apt-repository ppa:avengemedia/danklinux
sudo add-apt-repository ppa:avengemedia/dms-git
sudoapt update
sudoaptinstall dms-git
```

tip

Visit the [DankLinux Repository](https://danklinux.com/docs/danklinux) page for OBS and PPA links and more information about available packages.  
Add **niri** or **niri-git** to your system to get the best experience.

## OpenSUSE & Derivatives[​](#opensuse--derivatives "Direct link to OpenSUSE & Derivatives")

DankMaterialShell is available through the Open Build Service (OBS) for OpenSUSE Tumbleweed, Leap 16/16.1 & Slowroll.

### OpenSUSE Tumbleweed[​](#opensuse-tumbleweed "Direct link to OpenSUSE Tumbleweed")

#### Stable Release[​](#stable-release-3 "Direct link to Stable Release")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/openSUSE_Tumbleweed/home:AvengeMedia:dms.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms
```

#### Latest Development Build[​](#latest-development-build-3 "Direct link to Latest Development Build")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/openSUSE_Tumbleweed/home:AvengeMedia:dms-git.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms-git
```

### OpenSUSE Leap 16[​](#opensuse-leap-16 "Direct link to OpenSUSE Leap 16")

#### Stable Release[​](#stable-release-4 "Direct link to Stable Release")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/16.0/home:AvengeMedia:dms.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms
```

#### Latest Development Build[​](#latest-development-build-4 "Direct link to Latest Development Build")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/16.0/home:AvengeMedia:dms-git.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms-git
```

### OpenSUSE Leap 16.1[​](#opensuse-leap-161 "Direct link to OpenSUSE Leap 16.1")

#### Stable Release[​](#stable-release-5 "Direct link to Stable Release")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/16.1/home:AvengeMedia:dms.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms
```

#### Latest Development Build[​](#latest-development-build-5 "Direct link to Latest Development Build")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/16.1/home:AvengeMedia:dms-git.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms-git
```

### OpenSUSE Slowroll[​](#opensuse-slowroll "Direct link to OpenSUSE Slowroll")

#### Stable Release[​](#stable-release-6 "Direct link to Stable Release")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms/openSUSE_Slowroll/home:AvengeMedia:dms.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms
```

#### Latest Development Build[​](#latest-development-build-6 "Direct link to Latest Development Build")

```
# DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo

# DMS repository
sudozypper addrepo https://download.opensuse.org/repositories/home:/AvengeMedia:/dms-git/openSUSE_Slowroll/home:AvengeMedia:dms-git.repo
sudozypper refresh

# Install DMS
sudozypperinstall dms-git
```

## NixOS[​](#nixos "Direct link to NixOS")

## All Other Distributions[​](#all-other-distributions "Direct link to All Other Distributions")

warning

This guide doesn't cover compositor installation. You need a compatible Wayland compositor (niri, Hyprland, sway, dwl/MangoWC, etc.).

### 1. Install Essential Dependencies[​](#1-install-essential-dependencies "Direct link to 1. Install Essential Dependencies")

#### Quickshell[​](#quickshell "Direct link to Quickshell")

If your distribution does not provide a quickshell package, you'll need to build it from source. Quickshell requires:

**Base dependencies:**

- cmake, qt6base, qt6declarative, qtshadertools, pkg-config, cli11
- Private Qt headers for qt6declarative (and qt6wayland on Qt &lt; 6.10)
- Qt 6.6 or newer

**Key features and their dependencies:**

- **Wayland support** (enabled by default) - qt6wayland, wayland, wayland-protocols
- **Crash reporter** (recommended) - google-breakpad
- **Jemalloc** (recommended for better memory management) - jemalloc
- **System tray** - qt6dbus
- **PAM authentication** - pam

For complete build instructions and feature flags, see the [Quickshell BUILD.md](https://git.outfoxxed.me/quickshell/quickshell/raw/branch/master/BUILD.md).

#### AccountsService[​](#accountsservice "Direct link to AccountsService")

note

AccountsService is needed to persist user profile configurations such as profile pictures. Available in most repositories as `accountsservice`.

```
# Arch + Friends
sudo pacman -S accountsservice
# Fedora + Friends
sudo dnf install accountsservice
# Debian, Ubuntu + Friends
sudoaptinstall accountsservice
# openSUSE + Friends
sudozypperinstall accountsservice
# Gentoo
sudo emerge --ask sys-apps/accountsservice
```

### 2. Clone the DMS Repository[​](#2-clone-the-dms-repository "Direct link to 2. Clone the DMS Repository")

```
git clone https://github.com/AvengeMedia/DankMaterialShell.git ~/dms
```

### 3. Compile & Install the DMS Backend[​](#3-compile--install-the-dms-backend "Direct link to 3. Compile & Install the DMS Backend")

*Requires GO 1.24+*

```
cd ~/dms
sudomakeinstall
```

note

To uninstall a source build, run `sudo make uninstall` from the repository directory.

### 4. Install Optional Integrations[​](#4-install-optional-integrations "Direct link to 4. Install Optional Integrations")

Install optional components for full functionality using your distribution's package manager:

- `dgop` - Detailed system metrics and process lists
- `dsearch` - Filesystem search engine
- `matugen` - Material Design color palette generation
- `i2c-tools` - ddc monitor backlight control
- `wl-clipboard` + `cliphist` - Clipboard history
- `cava` - Audio visualizer widget
- `qt6-multimedia` - System sound feedback

## Post Install[​](#post-install "Direct link to Post Install")

After completing installation:

1. Enable the systemd service (recommended) or add `dms run` to your compositor config
2. Configure your compositor keybinds - see the [Keybinds & IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc) guide
3. Customize appearance via [Themes](https://danklinux.com/docs/dankmaterialshell/application-themes)
4. Extend functionality with [Plugins](https://danklinux.com/docs/dankmaterialshell/plugins-overview)

See [Managing Your Installation](https://danklinux.com/docs/dankmaterialshell/managing) for detailed guidance on service management, environment variables, and updates.

### Systemd Integration (Recommended)[​](#systemd-integration-recommended "Direct link to Systemd Integration (Recommended)")

DankInstall Users

If you used [dankinstall](https://danklinux.com/docs/dankinstall), this is already configured. The installer runs `systemctl --user enable --now dms` during setup.

**Enable autostart:**

```
systemctl --userenable dms
```

**Manual control:**

```
# Start DMS now
systemctl --user start dms

# Check status
systemctl --user status dms

# View logs
journalctl --user-u dms -f

# Restart DMS
systemctl --user restart dms

# Disable autostart
systemctl --user disable dms
```

warning

If using systemd autostart, remove `dms run` / `spawn "dms" "run"` / `exec-once=dms run` from your compositor's configuration to avoid running DMS twice.

### Compositor-Specific Systemd Setup[​](#compositor-specific-systemd-setup "Direct link to Compositor-Specific Systemd Setup")

Different compositors have different levels of systemd session integration. Choose the section that matches your compositor.

Why use add-wants?

If you have multiple desktop environments installed (e.g., Plasma, GNOME, niri), using `systemctl --user enable dms` starts DMS in *all* of them. Using `add-wants` binds DMS to a specific compositor's service or session target, so it only runs where you want it. DMS won't launch when you log into Plasma or GNOME.

#### niri[​](#niri "Direct link to niri")

niri has native systemd session integration. Bind DMS to niri's service:

```
systemctl --user add-wants niri.service dms
```

DMS starts when niri starts and stops when niri exits. It won't run in other sessions.

#### Hyprland[​](#hyprland "Direct link to Hyprland")

Hyprland doesn't initialize the systemd user session by default. You need to export the environment to systemd for user services to work.

Create a session target:

~/.config/systemd/user/hyprland-session.target

```
[Unit]
Description=Hyprland Session Target
Requires=graphical-session.target
After=graphical-session.target
```

Add to your Hyprland config (after any `env =` lines):

~/.config/hypr/hyprland.conf

```
exec-once = dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
exec-once = systemctl --user start hyprland-session.target
```

Bind DMS to the session target:

```
systemctl --user add-wants hyprland-session.target dms
```

#### MangoWC[​](#mangowc "Direct link to MangoWC")

[MangoWC](https://github.com/DreamMaoMao/mangowc) is a dynamic tiling compositor based on dwl (wlroots). Like other wlroots compositors, it requires manual environment export for systemd user services.

Create a session target:

~/.config/systemd/user/mango-session.target

```
[Unit]
Description=MangoWC Session Target
Requires=graphical-session.target
After=graphical-session.target
```

Add to your MangoWC config:

~/.config/mango/config.conf

```
exec-once=dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
exec-once=systemctl --user start mango-session.target
```

Bind DMS to the session:

```
systemctl --user add-wants mango-session.target dms
```

#### Sway[​](#sway "Direct link to Sway")

Sway (wlroots-based) needs the environment exported for systemd services:

~/.config/sway/config

```
exec dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
```

Create a session target and bind DMS:

```
systemctl --user add-wants sway-session.target dms
```