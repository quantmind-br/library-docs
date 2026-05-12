---
title: Installation
url: https://wiki.hypr.land/Getting-Started/Installation/
source: sitemap
fetched_at: 2026-04-26T09:47:17.187024477-03:00
rendered_js: false
word_count: 662
summary: This document provides comprehensive instructions on how to install and build the Hyprland window manager across various Linux distributions, including guidance on manual compilation, build flags, and virtual machine deployment.
tags:
    - hyprland
    - linux-installation
    - wayland-compositor
    - window-manager
    - build-instructions
    - distro-compatibility
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!warning]
> Hyprland is not a full Desktop Environment — it's a set of tools to build your own. Apps, integrations, shells are your responsibility. Read the wiki before assuming something is not working.

> [!note]
> NVIDIA GPUs often not usable out-of-the-box. Follow [[034-nvidia|Nvidia]] after installing if needed.

## Distros

Officially tested on Arch and NixOS. Other distros may have varying success. Point-release distros (Pop!_OS, Fedora, Ubuntu) will have **major issues**. Rolling-release (openSUSE, Solus) likely fine.

## Installation

Use your distro's package manager. **Prefer distro packages** over manual compilation. Hyprland's ecosystem is vast and intertwined — manual compilation risks `.so` file mismatches.

For beta testing new features, use `hyprland-git` from AUR or build from source.

### Packages

> [!warning]
> I do not maintain any packages. If broken, try building from source first.

| Distro | Status |
|---|---|
| Arch | Official |
| Nix | Official |
| openSUSE* | Community |
| Fedora* | Community |
| Debian* | Community |
| Gentoo* | Community |
| FreeBSD* | Community |
| Ubuntu* | Community |
| Void Linux* | Community |
| Slackware* | Community |
| Alpine* | Community |
| Ximper* | Community |
| Solus* | Community |

*Unofficial, community-driven, no guarantee.*

### Manual Build

> [!note]
> Hyprland uses C++26 — requires `gcc>=15` or `clang>=19`.

Dependencies (hypr* packages):

- aquamarine
- hyprlang
- hyprcursor
- hyprutils
- hyprgraphics
- hyprwayland-scanner (build-only)

#### CMake (recommended)

```sh
git clone --recursive https://github.com/hyprwm/Hyprland
cd Hyprland
make all && sudo make install
```

## Crash on Launch

See [[032-crashes-and-bugs|Crashes and Bugs]].

## Custom Installation (debug build)

Debug build:

```bash
make debug
sudo make install
```

Other presets (`release`, `debug`):

```bash
make <PRESET> && sudo cp ./build/Hyprland /usr/bin && sudo cp ./example/hyprland.desktop /usr/share/wayland-sessions
```

## Custom Build Flags

CMake-required. Supported flags:

```bash
NO_XWAYLAND      # Removes XWayland support
NO_SYSTEMD       # Removes systemd dependencies
NO_UWSM          # Does not install hyprland-uwsm.desktop
NO_HYPRPM        # Does not build/install hyprpm
```

Apply flags:

```bash
cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE:STRING=Release -D<FLAG>:STRING=true -B build
```

Build:

```bash
cmake --build ./build --config Release --target all -j`nproc 2>/dev/null || getconf NPROCESSORS_CONF`
```

Install:

```bash
sudo cmake --install ./build
```

## Running in VM

> [!note]
> YMMV, not officially supported.

### libvirt Setup

```bash
sudo pacman -S libvirt virt-viewer qemu-common
sudo usermod -a -G libvirt USER
systemctl enable --now libvirtd
```

Download Arch QEMU image from [arch-boxes](https://gitlab.archlinux.org/archlinux/arch-boxes/-/packages):

```bash
curl https://geo.mirror.pkgbuild.com/images/latest/Arch-Linux-x86_64-basic.qcow2 \
  -o ~/Downloads/arch-qemu.qcow2
```

Create VM:

```bash
virt-install \
  --graphics spice,listen=none,gl.enable=yes,rendernode=/dev/dri/renderD128 \
  --name hypr-vm \
  --os-variant archlinux \
  --memory 2048 \
  --disk ~/Downloads/arch-qemu.qcow2 \
  --import
```

Connect:

```bash
virt-viewer --attach hypr-vm
```

> [!warning]
> Use `--attach` flag. Without it, virgl disables listen — no direct TCP/UNIX socket connection. `--attach` provides a pre-connected socket.

Inside guest: install `mesa` for OpenGL (virgl included). Then install Hyprland via AUR or manual build.

#linux-installation #wayland-compositor #build-instructions
