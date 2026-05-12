---
title: DankLinux Repository | Dank Linux
url: https://danklinux.com/docs/danklinux/
source: sitemap
fetched_at: 2026-04-26T08:38:29.548890362-03:00
rendered_js: false
word_count: 552
summary: This document provides an overview of the DankLinux repository and instructions for installing pre-built packages for DankMaterialShell, niri, and related utilities across multiple Linux distributions.
tags:
    - linux
    - danklinux
    - package-management
    - wayland
    - niri
    - desktop-environment
    - repository-setup
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# DankLinux Repository

The **DankLinux Repository** provides pre-built packages for **DankMaterialShell** and **niri** on Fedora, CentOS, OpenSUSE, Debian, and Ubuntu.

## Available Packages

### Desktop Environment
- **DankMaterialShell (dms)**: Complete desktop shell with widgets and CLI tools
- **DankMaterialShell (dms-git)**: Development build

### Compositors
- [**Niri**](https://github.com/niri-wm/niri): Scrollable-tiling Wayland compositor
- **Niri-git**: Development build of niri

### Core Framework
- [**Quickshell**](https://github.com/quickshell-mirror/quickshell): QtQuick-based Wayland desktop shell framework
- **Quickshell-git**: Development build

### Utilities
- [**cliphist**](https://github.com/sentriz/cliphist): Wayland clipboard manager with history
- [**dgop**](https://github.com/AvengeMedia/dgop): Stateless CPU/GPU monitor by Avenge Media
- [**dsearch**](https://github.com/AvengeMedia/danksearch): Fast filesystem search by Avenge Media
- [**matugen**](https://github.com/InioX/matugen): Material Design 3 color palette generator
- **xWayland-Satellite**: XWayland integration (auto-installed with niri/niri-git)

## Installation

> [!tip]
> - **Fedora/CentOS**: See [[006-docs-1.2-dankmaterialshell-installation#fedora--centos|Fedora & CentOS section]]
> - **Ubuntu/Debian**: See [[006-docs-1.2-dankmaterialshell-installation#debian--ubuntu|Ubuntu & Debian section]]
> - **OpenSUSE**: See [[006-docs-1.2-dankmaterialshell-installation#opensuse--derivatives|OpenSUSE section]]

> [!note]
> **xWayland-Satellite** is automatically installed as a dependency when installing **niri** or **niri-git**.

### Debian

**Debian 13 (Trixie)**:
```bash
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_13/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_13/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
sudo apt update
sudo apt install quickshell niri          # stable
sudo apt install quickshell-git niri-git  # development
```

**Debian Testing**:
```bash
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Testing/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Testing/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
sudo apt update
sudo apt install quickshell niri
sudo apt install quickshell-git niri-git
```

**Debian Sid**:
```bash
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Unstable/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Unstable/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
sudo apt update
sudo apt install quickshell niri
sudo apt install quickshell-git niri-git
```

### Ubuntu
```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo apt update
sudo apt install quickshell niri          # stable
sudo apt install quickshell-git niri-git  # development
```

### OpenSUSE

**OpenSUSE Tumbleweed**:
```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install quickshell niri
sudo zypper install quickshell-git niri-git
```

**OpenSUSE Leap 16**:
```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install quickshell niri
sudo zypper install quickshell-git niri-git
```

**OpenSUSE Leap 16.1**:
```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install quickshell niri
sudo zypper install quickshell-git niri-git
```

**OpenSUSE Slowroll**:
```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install quickshell niri
sudo zypper install quickshell-git niri-git
```

### Fedora & CentOS
```bash
sudo dnf copr enable avengemedia/danklinux
sudo dnf install quickshell niri          # stable
sudo dnf install quickshell-git niri-git # development
```

> [!note]
> Package availability may vary by distribution. Some packages may only be available on Debian, Ubuntu, and OpenSUSE via OBS/PPA.

## Repository Links

| Platform | Links |
|---|---|
| Fedora COPR | [avengemedia/danklinux](https://copr.fedorainfracloud.org/coprs/avengemedia/danklinux/) (core) · [avengemedia/dms](https://copr.fedorainfracloud.org/coprs/avengemedia/dms/) (stable) · [avengemedia/dms-git](https://copr.fedorainfracloud.org/coprs/avengemedia/dms-git/) (dev) |
| Open Build Service | [home:AvengeMedia:danklinux](https://build.opensuse.org/project/show/home:AvengeMedia:danklinux) (core) · [home:AvengeMedia:dms](https://build.opensuse.org/project/show/home:AvengeMedia:dms) (stable) · [home:AvengeMedia:dms-git](https://build.opensuse.org/project/show/home:AvengeMedia:dms-git) (dev) |
| Launchpad PPA | [~avengemedia](https://launchpad.net/~avengemedia) · [ppa:avengemedia/danklinux](https://launchpad.net/~avengemedia/+archive/ubuntu/danklinux) (core) · [ppa:avengemedia/dms](https://launchpad.net/~avengemedia/+archive/ubuntu/dms) (stable) · [ppa:avengemedia/dms-git](https://launchpad.net/~avengemedia/+archive/ubuntu/dms-git) (dev) |

## GitHub Repository

**Repository**: [github.com/AvengeMedia/DankLinux](https://github.com/AvengeMedia/DankLinux)

> [!note]
> **Official Avenge Media packages**: `dms`, `dms-cli`, `dgop`, `danksearch`, `dank-greeter`, `dms-color-picker`, and `dms-clipboard` are developed by Avenge Media (MIT License). External packages retain upstream licenses: Niri (GPL-3.0), Quickshell (LGPL-3.0), Matugen (GPL-2.0), Cliphist (GPL-3.0).

## Support

1. Check the [[006-docs-1.2-dankmaterialshell-installation|DankMaterialShell Installation Guide]]
2. Visit [[105-docs-support.md|Support Page]] for community resources
3. Report packaging issues on the [DankLinux Repository](https://github.com/AvengeMedia/DankLinux/issues)
4. Report application issues on the [DankMaterialShell Repository](https://github.com/AvengeMedia/DankMaterialShell/issues)

## Contributing

Interested in maintaining packages for other distributions? See the [[103-docs-contributing.md|Contributing Guide]] to get started.

#linux #danklinux #package-management #wayland #niri
