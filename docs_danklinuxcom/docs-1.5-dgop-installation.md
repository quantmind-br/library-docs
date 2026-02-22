---
title: Installation | Dank Linux
url: https://danklinux.com/docs/1.5/dgop/installation
source: sitemap
fetched_at: 2026-02-22T18:44:45.512632-03:00
rendered_js: false
word_count: 99
summary: This document provides comprehensive instructions for installing, building, and verifying the dgop system metrics tool on various Linux distributions.
tags:
    - installation-guide
    - linux-monitoring
    - system-metrics
    - dgop
    - binary-installation
    - go-development
category: guide
---

```
██████╗  ██████╗  ██████╗ ██████╗
██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗
██║  ██║██║  ███╗██║   ██║██████╔╝
██║  ██║██║   ██║██║   ██║██╔═══╝
██████╔╝╚██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝
                                
```

note

`dgop` has zero dependencies and compiles to a single static binary.

### Distribution Packages[​](#distribution-packages "Direct link to Distribution Packages")

#### Arch Linux[​](#arch-linux "Direct link to Arch Linux")

#### Fedora[​](#fedora "Direct link to Fedora")

```
sudo dnf copr enable avengemedia/danklinux
sudo dnf install dgop
```

### Pre-built Binaries[​](#pre-built-binaries "Direct link to Pre-built Binaries")

Download the latest release for your architecture:

```
# Download and install
wget https://github.com/AvengeMedia/dgop/releases/latest/download/dgop-linux-amd64.gz
gunzip dgop-linux-amd64.gz
chmod +x dgop-linux-amd64
sudomv dgop-linux-amd64 /usr/local/bin/dgop
```

### From Source[​](#from-source "Direct link to From Source")

Requirements: Go 1.24+

```
git clone https://github.com/AvengeMedia/dgop
cd dgop
make
sudomakeinstall
```

## Verification[​](#verification "Direct link to Verification")

Test the installation:

```
# Check version
dgop version

# Get system metrics
dgop system

# Run API server
dgop server

# See available commands
dgop --help
```

## System Requirements[​](#system-requirements "Direct link to System Requirements")

- **Operating System**: Linux (uses `/proc` and `/sys` filesystems)
- **Go Version**: 1.24+ (for building from source)

### Optional Dependencies[​](#optional-dependencies "Direct link to Optional Dependencies")

For enhanced functionality:

- `nvidia-smi` - NVIDIA GPU monitoring

## Integration with DMS[​](#integration-with-dms "Direct link to Integration with DMS")

tip

DankMaterialShell users gain access to system widgets (CPU, RAM, GPU, Disk, Network) and process monitoring when dgop is installed.

## Next Steps[​](#next-steps "Direct link to Next Steps")

- [Configuration](https://danklinux.com/docs/1.5/dgop/configuration) - Configure dgop
- [Usage](https://danklinux.com/docs/1.5/dgop/usage) - Learn CLI commands and API usage