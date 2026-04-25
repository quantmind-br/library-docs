---
title: Installation | Dank Linux
url: https://danklinux.com/docs/danksearch/installation
source: sitemap
fetched_at: 2026-04-07T21:33:21.71993546-03:00
rendered_js: false
word_count: 198
summary: This document provides comprehensive instructions on multiple methods for installing the dsearch tool, including dedicated guides for NixOS users, package manager instructions for Arch and Fedora, procedures for using pre-built binaries, building from source, and includes verification steps.
tags:
    - installation
    - dsearch
    - nixos
    - linux
    - binary
    - setup
category: guide
---

Version: 1.4

```
██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                      
```

`dsearch` has zero dependencies and compiles to a single static binary.

NixOS Users

If you're using NixOS, see the dedicated [NixOS Installation guides](https://danklinux.com/docs/danksearch/nixos-flake) for declarative installation with flakes or native nixpkgs modules.

## Installation Methods[​](#installation-methods "Direct link to Installation Methods")

Choose the installation method that best fits your system:

### NixOS[​](#nixos "Direct link to NixOS")

For NixOS users, we recommend using the declarative installation methods:

- [**Flake Installation (home-manager)**](https://danklinux.com/docs/danksearch/nixos-flake) - Recommended for most users, provides per-user installation with home-manager
- [**NixOS Module**](https://danklinux.com/docs/danksearch/nixos) - System-wide installation using native nixpkgs (when available)

### Distribution Packages[​](#distribution-packages "Direct link to Distribution Packages")

#### Arch Linux (AUR)[​](#arch-linux-aur "Direct link to Arch Linux (AUR)")

```bash
paru -S dsearch-bin

# Development version
paru -S dsearch-git
```

#### Fedora[​](#fedora "Direct link to Fedora")

```bash
sudo dnf copr enable avengemedia/danklinux
sudo dnf install dsearch
```

Distribution packages include the systemd user service. Enable it for automatic index updates:

```bash
systemctl --userenable--now dsearch
```

### Pre-built Binaries[​](#pre-built-binaries "Direct link to Pre-built Binaries")

Download the latest release for your architecture:

```bash
# Download and install
wget https://github.com/AvengeMedia/danksearch/releases/latest/download/dsearch-linux-amd64.gz
gunzip dsearch-linux-amd64.gz
chmod +x dsearch-linux-amd64
sudomv dsearch-linux-amd64 /usr/local/bin/dsearch
```

Install and enable the systemd user service for automatic index updates:

```bash
mkdir-p ~/.config/systemd/user
wget https://raw.githubusercontent.com/AvengeMedia/danksearch/refs/heads/master/assets/dsearch.service -O ~/.config/systemd/user/dsearch.service
systemctl --userenable--now dsearch
```

The service runs the API server with file watching, automatically updating the index when files change.

### From Source[​](#from-source "Direct link to From Source")

Requirements: Go 1.24+

```bash
git clone https://github.com/AvengeMedia/danksearch
cd danksearch
make
sudomakeinstall
make install-service
systemctl --userenable--now dsearch
```

## Verification[​](#verification "Direct link to Verification")

Test the installation:

```bash
# Check version
dsearch version

# Build initial index
dsearch index generate
```

## System Requirements[​](#system-requirements "Direct link to System Requirements")

- **Operating System**: Unix-based, compatible with most Unix-based operating systems (Linux, MacOS, BSD)
- **Go Version**: 1.24+ (for building from source)

## Integration with DMS[​](#integration-with-dms "Direct link to Integration with DMS")

tip

DankMaterialShell users can initiate filesystem search by typing `/` in the launcher when dsearch is installed.

## Next Steps[​](#next-steps "Direct link to Next Steps")

- [Configuration](https://danklinux.com/docs/danksearch/configuration) - Configure dsearch
- [Usage](https://danklinux.com/docs/danksearch/usage) - Learn CLI commands and API usage