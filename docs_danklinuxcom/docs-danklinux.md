---
title: DankLinux Repository | Dank Linux
url: https://danklinux.com/docs/danklinux/
source: sitemap
fetched_at: 2026-01-24T13:33:15.521031532-03:00
rendered_js: false
word_count: 550
summary: This document provides an overview of the DankLinux repository and detailed installation instructions for desktop components and utilities across various Linux distributions.
tags:
    - linux-repository
    - package-management
    - dankmaterialshell
    - wayland
    - niri
    - installation-guide
category: guide
---

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
██║  ██║███████║██╔██╗ ██║█████╔╝ ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██║  ██║██╔══██║██║╚██╗██║██╔═██╗ ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
██████╔╝██║  ██║██║ ╚████║██║  ██╗███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
```

## Overview[​](#overview "Direct link to Overview")

The **DankLinux Repository** provides pre-built packages for **DankMaterialShell** and **niri**!  
DankMaterialShell is now available on more distributions than ever before!

- [**Fedora**](https://fedoraproject.org/) | [**CentOS**](https://www.centos.org/) | [**OpenSUSE**](https://www.opensuse.org/)
- [**Debian**](https://www.debian.org/) | [**Ubuntu**](https://ubuntu.com/)

### Desktop Environment[​](#desktop-environment "Direct link to Desktop Environment")

- **DankMaterialShell (dms)**: The complete desktop shell with widgets and CLI tools
- **DankMaterialShell (dms-git)**: Development build with latest features

### Compositors[​](#compositors "Direct link to Compositors")

- [**Niri**](https://github.com/YaLTeR/niri): Scrollable-tiling Wayland compositor
- [**Niri-git**](https://github.com/YaLTeR/niri): Development build of niri

### Core Framework[​](#core-framework "Direct link to Core Framework")

- [**Quickshell**](https://github.com/quickshell-mirror/quickshell): QtQuick-based Wayland desktop shell framework
- [**Quickshell-git**](https://github.com/quickshell-mirror/quickshell): Development build of Quickshell

### Utilities[​](#utilities "Direct link to Utilities")

- [**cliphist**](https://github.com/sentriz/cliphist): Wayland clipboard manager with history support
- [**dgop**](https://github.com/AvengeMedia/dgop): Stateless CPU/GPU monitor system by Avenge Media
- [**dsearch**](https://github.com/AvengeMedia/danksearch): a Blazingly fast filesystem search tool by Avenge Media
- [**matugen**](https://github.com/InioX/matugen): Material Design 3 color palette generator for themes
- [**xWayland-Satellite**](https://github.com/Supreeeme/xwayland-satellite): XWayland integration tool
- [**xWayland-Satellite-git**](https://github.com/Supreeeme/xwayland-satellite): Development build of xWayland-Satellite

## How to Install[​](#how-to-install "Direct link to How to Install")

### Installing DankMaterialShell (DMS)[​](#installing-dankmaterialshell-dms "Direct link to Installing DankMaterialShell (DMS)")

For complete DMS installation instructions including repository setup, see the [DankMaterialShell Installation Guide](https://danklinux.com/docs/dankmaterialshell/installation).

Quick Start

- **Fedora**: See the [Fedora & CentOS](https://danklinux.com/docs/dankmaterialshell/installation#fedora--centos) section in the installation guide
- **Ubuntu/Debian**: See the [Ubuntu & Debian](https://danklinux.com/docs/dankmaterialshell/installation#debian--ubuntu) section in the installation guide
- **OpenSUSE**: See the [OpenSUSE](https://danklinux.com/docs/dankmaterialshell/installation#opensuse--derivatives) section in the installation guide

### Installing Standalone Packages[​](#installing-standalone-packages "Direct link to Installing Standalone Packages")

All packages in the DankLinux repository can be installed independently. First, add the DankLinux repository for your distribution, then install the packages you need.

note

**xWayland-Satellite** is automatically installed as a dependency when installing **niri** or **niri-git**. You don't need to install it separately.

### Debian[​](#debian "Direct link to Debian")

**Debian 13 (Trixie)**:

```
# Add DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_13/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_13/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list
sudoapt update

# Install stable packages
sudoaptinstall quickshell niri

# Or install development packages
sudoaptinstall quickshell-git niri-git
```

**Debian Testing**:

```
# Add DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Testing/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Testing/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list
sudoapt update

# Install stable packages
sudoaptinstall quickshell niri

# Or install development packages
sudoaptinstall quickshell-git niri-git
```

**Debian Sid**:

```
# Add DankLinux repository
curl-fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Unstable/Release.key |\
sudo gpg --dearmor-o /etc/apt/keyrings/danklinux.gpg
echo"deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Unstable/ /"|\
sudotee /etc/apt/sources.list.d/danklinux.list
sudoapt update

# Install stable packages
sudoaptinstall quickshell niri

# Or install development packages
sudoaptinstall quickshell-git niri-git
```

### Ubuntu[​](#ubuntu "Direct link to Ubuntu")

```
# Add DankLinux PPA
sudo add-apt-repository ppa:avengemedia/danklinux
sudoapt update

# Install stable packages
sudoaptinstall quickshell niri

# Or install development packages
sudoaptinstall quickshell-git niri-git
```

### OpenSUSE[​](#opensuse "Direct link to OpenSUSE")

**OpenSUSE Tumbleweed**:

```
# Add DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo
sudozypper refresh

# Install stable packages
sudozypperinstall quickshell niri

# Or install development packages
sudozypperinstall quickshell-git niri-git
```

**OpenSUSE Leap 16**:

```
# Add DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo
sudozypper refresh

# Install stable packages
sudozypperinstall quickshell niri

# Or install development packages
sudozypperinstall quickshell-git niri-git
```

**OpenSUSE Leap 16.1**:

```
# Add DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo
sudozypper refresh

# Install stable packages
sudozypperinstall quickshell niri

# Or install development packages
sudozypperinstall quickshell-git niri-git
```

**OpenSUSE Slowroll**:

```
# Add DankLinux repository
sudozypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo
sudozypper refresh

# Install stable packages
sudozypperinstall quickshell niri

# Or install development packages
sudozypperinstall quickshell-git niri-git
```

### Fedora & CentOS[​](#fedora--centos "Direct link to Fedora & CentOS")

The COPR repositories provide packages for Fedora 41/42/43 rawhide and CentOS 10:

```
# Add DankLinux COPR
sudo dnf copr enable avengemedia/danklinux

# Install stable packages
sudo dnf install quickshell niri

# Or install development packages
sudo dnf install quickshell-git niri-git
```

note

Package availability may vary by distribution. Some packages may only be available on Debian, Ubuntu, and OpenSUSE via OBS/PPA.

### Niri Scrollable-Tiling Wayland Compositor[​](#niri-scrollable-tiling-wayland-compositor "Direct link to Niri Scrollable-Tiling Wayland Compositor")

Niri packages are available in both stable and development variants. Supported on distributions where niri is not available in the official repositories.

**xWayland-Satellite** is automatically installed as a dependency when installing **niri** or **niri-git**, providing XWayland integration out of the box.

[**Wiki**](https://yalter.github.io/niri/) | [**GitHub**](https://github.com/YaLTeR/niri)

## Repository Links[​](#repository-links "Direct link to Repository Links")

### Fedora COPR[​](#fedora-copr "Direct link to Fedora COPR")

The COPR provides packages for Fedora 41/42/43 rawhide and CentOS 10:

- **DankLinux Core Repository**: [avengemedia/danklinux](https://copr.fedorainfracloud.org/coprs/avengemedia/danklinux/)
- **DMS Stable**: [avengemedia/dms](https://copr.fedorainfracloud.org/coprs/avengemedia/dms/)
- **DMS Development**: [avengemedia/dms-git](https://copr.fedorainfracloud.org/coprs/avengemedia/dms-git/)

### Open Build Service (OBS)[​](#open-build-service-obs "Direct link to Open Build Service (OBS)")

The OBS provides packages for OpenSUSE and Debian based distributions:

- **DankLinux Core Repository**: [home:AvengeMedia:danklinux](https://build.opensuse.org/project/show/home:AvengeMedia:danklinux)
- **DMS Stable**: [home:AvengeMedia:dms](https://build.opensuse.org/project/show/home:AvengeMedia:dms)
- **DMS Development**: [home:AvengeMedia:dms-git](https://build.opensuse.org/project/show/home:AvengeMedia:dms-git)

### Launchpad PPA[​](#launchpad-ppa "Direct link to Launchpad PPA")

The Launchpad PPAs provide packages for Ubuntu distributions:

- **AvengeMedia Team Page**: [~avengemedia](https://launchpad.net/~avengemedia)
- **DankLinux Core PPA**: [ppa:avengemedia/danklinux](https://launchpad.net/~avengemedia/+archive/ubuntu/danklinux)
- **DMS Stable PPA**: [ppa:avengemedia/dms](https://launchpad.net/~avengemedia/+archive/ubuntu/dms)
- **DMS Development PPA**: [ppa:avengemedia/dms-git](https://launchpad.net/~avengemedia/+archive/ubuntu/dms-git)

## GitHub Repository[​](#github-repository "Direct link to GitHub Repository")

The packaging configurations and build scripts are maintained in the official DankLinux repository:

**Repository**: [github.com/AvengeMedia/DankLinux](https://github.com/AvengeMedia/DankLinux)

note

**Official Avenge Media packages**: `dms`, `dms-cli`, `dgop`, `danksearch`, `dank-greeteer`, `dms-color-picker`, and `dms clipboard` are developed and maintained by the Avenge Media team under the MIT License. External packages in these repositories are maintained by Avenge Media, but originate from upstream projects by their respective authors, credited in the package listings. They are considered unofficial Avenge Media packages unless stated otherwise by the project authors. Packages retain their upstream licenses: Niri (GPL-3.0), Quickshell (LGPL-3.0), Matugen (GPL-2.0), Cliphist (GPL-3.0).

## Support[​](#support "Direct link to Support")

If you encounter issues with the repositories or packages:

1. Check the [DankMaterialShell Installation Guide](https://danklinux.com/docs/dankmaterialshell/installation) for common solutions
2. Visit the [Support Page](https://danklinux.com/docs/support) for community resources
3. Report packaging issues on the [DankLinux Repository](https://github.com/AvengeMedia/DankLinux/issues)
4. Report application issues on the [DankMaterialShell Repository](https://github.com/AvengeMedia/DankMaterialShell/issues)

## Contributing[​](#contributing "Direct link to Contributing")

Interested in maintaining packages for other distributions? Contributions to the DankLinux repository are welcome! Check out the [Contributing Guide](https://danklinux.com/docs/contributing) to get started.