---
title: DankGreeter Installation | Dank Linux
url: https://danklinux.com/docs/dankgreeter/installation
source: sitemap
fetched_at: 2026-04-26T08:38:21.720572688-03:00
rendered_js: false
word_count: 770
summary: This document provides instructions for installing the dms-greeter display manager component across various Linux distributions including Arch, Fedora, Debian, Ubuntu, openSUSE, and others.
tags:
    - linux
    - display-manager
    - dms-greeter
    - installation
    - greetd
    - danklinux
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

> [!warning]
> This replaces your current display manager.

DMS or another DankLinux package already configures the repository. Install the package to handle all configuration automatically.

## Installation Methods

If DMS or another DankLinux package is already installed, the repository is already configured. Install the package and configuration is handled automatically.

Otherwise, install the package manually then proceed to [[#completing-setup|Completing Setup]]:

- **Arch**: `paru -S greetd-dms-greeter-git` or `yay -S greetd-dms-greeter-git`
- **Fedora**: `sudo dnf install dms-greeter`
- **Debian/Ubuntu**: `sudo apt install dms-greeter`
- **openSUSE**: `sudo zypper install dms-greeter`

## Distro Installation

### Arch Linux (AUR)

```bash
paru -S greetd-dms-greeter-git
# Or with yay
yay -S greetd-dms-greeter-git
```

Proceed to [[#completing-setup|Completing Setup]].

### Fedora

```bash
sudo dnf copr enable avengemedia/danklinux
sudo dnf install dms-greeter
```

Proceed to [[#completing-setup|Completing Setup]].

### Debian

**Debian 13 (Trixie)**:

```bash
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_13/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
  echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_13/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
  sudo apt update
  sudo apt install dms-greeter
```

**Debian Testing**:

```bash
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Testing/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
  echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Testing/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
  sudo apt update
  sudo apt install dms-greeter
```

**Debian Sid (Unstable)**:

```bash
curl -fsSL https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/Debian_Unstable/Release.key |\
  sudo gpg --dearmor -o /etc/apt/keyrings/danklinux.gpg
  echo "deb [signed-by=/etc/apt/keyrings/danklinux.gpg] https://download.opensuse.org/repositories/home:/AvengeMedia:/danklinux/Debian_Unstable/ /" |\
  sudo tee /etc/apt/sources.list.d/danklinux.list
  sudo apt update
  sudo apt install dms-greeter
```

Proceed to [[#completing-setup|Completing Setup]].

### Ubuntu

```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo apt update
sudo apt install dms-greeter
```

Proceed to [[#completing-setup|Completing Setup]].

### openSUSE

**Tumbleweed**:

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Tumbleweed/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install dms-greeter
```

**Leap 16**:

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.0/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install dms-greeter
```

**Leap 16.1**:

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/16.1/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install dms-greeter
```

**Slowroll**:

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:AvengeMedia:danklinux/openSUSE_Slowroll/home:AvengeMedia:danklinux.repo
sudo zypper refresh
sudo zypper install dms-greeter
```

Proceed to [[#completing-setup|Completing Setup]].

### Gentoo

> [!note]
> DMS must already be installed on your system before running this command. The greeter wrapper is sourced from your local DMS installation.

Installs `greetd` via Portage, copies the greeter wrapper from your local DMS installation, configures permissions, and sets up greetd to use DMS. To start immediately without rebooting:

```bash
sudo systemctl start greetd
```

### NixOS

NixOS uses a separate installation method. See [[036-docs-dankgreeter-nixos-flake|NixOS Flake Installation]].

## Installer & Manual Installation

### DankInstall Users (Niri and Hyprland only)

`dms-greeter` is **opt-in** in the DankInstaller, skipped by default since it replaces your current display manager.

If enabled in DankInstall, the full greeter setup runs automatically at the end of the install process. No further steps required.

If skipped during installation, install the package for your distro and proceed to [[#completing-setup|Completing Setup]].

> [!warning]
> Enabling `dms-greeter` will replace your current display manager.

### Manual installation (DMS already installed)

Install `greetd` then the greeter wrapper:

```bash
sudo wget https://raw.githubusercontent.com/AvengeMedia/DankMaterialShell/refs/heads/master/quickshell/Modules/Greetd/assets/dms-greeter -O /usr/local/bin/dms-greeter
sudo chmod +x /usr/local/bin/dms-greeter
```

Set `/etc/greetd/config.toml`:

```toml
command = "dms-greeter --command niri -p /usr/share/quickshell/dms"
```

### Manual installation (without DMS)

Install `greetd`, `quickshell`, then the greeter:

```bash
sudo mkdir -p /etc/xdg/quickshell
sudo git clone https://github.com/AvengeMedia/DankMaterialShell.git /etc/xdg/quickshell/dms-greeter
sudo mkdir /var/cache/dms-greeter
sudo chown greeter:greeter /var/cache/dms-greeter
```

> [!note]
> Some distributions may have different user/group names for the greetd user.

#### Theme Syncing Prerequisites

ACLs are required to allow the greeter user to traverse your home directory and access configuration files. The `acl` package is installed automatically when running `dms greeter sync` or `dms greeter install`.

## Completing Setup

### Automated Setup (All users)

If you used `dms greeter install` (Arch with paru/yay, Ubuntu, Fedora, Debian, openSUSE, Gentoo):

Configuration, permissions, theme syncing, and greetd service enablement are handled automatically. To start immediately without rebooting:

```bash
sudo systemctl start greetd
```

Verify setup with `dms greeter status`. Re-run `dms greeter sync` after theme changes.

### Manual Setup

Run these two commands to complete setup:

#### 1. Enable the Greeter

Configures `/etc/greetd/config.toml` with the correct compositor command, disables conflicting display managers (gdm, lightdm, sddm), and enables/starts the greetd service.

#### 2. Sync with Your User Theme

Installs `acl` if needed, adds your user to the `greeter` group, sets up ACL permissions on parent directories for greeter access, configures group permissions on DMS config directories, and creates symlinks to sync settings, wallpapers, and color themes.

> [!note]
> After running `dms greeter sync`, log out and back in for group membership changes to take effect.

> [!info]
> NixOS users: `dms greeter enable` and `dms greeter sync` are not available. Follow the manual steps or see [[036-docs-dankgreeter-nixos-flake|NixOS installation]].

### For all users

Check greeter configuration at any time with `dms greeter status`. See [[060-docs-dankgreeter-configuration#checking-sync-status|Configuration guide]] for details.

### Full Manual Setup (all distros)

> [!tip]
> Use `dms greeter enable` to automate this process instead.

1. Edit `/etc/greetd/config.toml` and set `command` to use dms-greeter:

```toml
[terminal]
vt = 1

[default_session]
user = "greeter"
command = "dms-greeter --command niri"

### Uncomment the below line to run the greeter on Hyprland
# command = "dms-greeter --command Hyprland"

### Uncomment to run the greeter on sway
# command = "dms-greeter --command sway"

### Uncomment to run the greeter on Miracle WM
# command = "dms-greeter --command miracle-wm"
```

2. Disable any existing conflicting greeters:

> [!warning]
> Disabling a greeter while logged in under that greeter will log you out and bring you to a non-graphical TTY.

```bash
sudo systemctl disable gdm lightdm sddm
```

3. Enable and start the greeter:

```bash
sudo systemctl enable greetd
sudo systemctl start greetd
```

#dms-greeter #installation #linux
