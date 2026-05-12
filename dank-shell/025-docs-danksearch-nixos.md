---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/danksearch/nixos
source: sitemap
fetched_at: 2026-04-26T08:39:27.609867765-03:00
rendered_js: false
word_count: 263
summary: This document provides instructions on how to install and configure DankSearch on the NixOS operating system using the native nixpkgs module. It covers channel setup, configuration options, systemd integration, and troubleshooting common deployment issues.
tags:
    - nixos
    - nixpkgs
    - danksearch
    - systemd
    - linux-configuration
    - package-management
    - installation-guide
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
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

DankSearch can be installed on NixOS using the NixOS module. This guide covers the native nixpkgs installation method.

> [!info]
> DankSearch is currently only available in the **unstable** branch of nixpkgs. On NixOS stable, use the [[024-docs-danksearch-nixos-flake|Flake Installation]] instead.

## Installation

### 1. Enable NixOS Unstable

Ensure you're using NixOS unstable by setting your channel or flake input:

**Using channels:**

```bash
sudo nix-channel --add https://nixos.org/channels/nixos-unstable nixos
sudo nix-channel --update
```

**Using flakes (in `flake.nix`):**

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };
}
```

### 2. Enable DankSearch

In your NixOS configuration, enable DankSearch:

```nix
programs.dsearch.enable = true;
```

Rebuild your system and DankSearch will be installed with sensible defaults.

## Configuration Options

### Basic Configuration

```nix
programs.dsearch = {
  enable = true;
  # Use a custom package (optional)
  package = pkgs.dsearch;
  # Systemd service configuration
  systemd = {
    enable = true;       # Enable systemd user service
    target = "default.target";  # Start with user session
  };
};
```

### Systemd Service Options

The NixOS module configures a systemd user service. You can customize when it starts:

```nix
programs.dsearch = {
  enable = true;
  systemd = {
    enable = true;
    target = "graphical-session.target";  # Only start in graphical sessions
  };
};
```

### Using Flake Package with NixOS Module

Use the package from the DankSearch flake while keeping the native NixOS module for configuration.

First, add the flake input to your `flake.nix`:

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    danksearch = {
      url = "github:AvengeMedia/danksearch";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
}
```

Then use the flake package with the native module:

```nix
programs.dsearch = {
  enable = true;
  package = inputs.danksearch.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

> [!warning]
> When using the flake package with the native nixpkgs module, some dependencies may not be automatically enabled by default. You may need to manually install optional dependencies or adjust feature toggles.

## Rebuilding

After making configuration changes, rebuild your system:

```bash
sudo nixos-rebuild switch
```

## Troubleshooting

### Service doesn't start automatically

Make sure you have `systemd.enable = true` set:

```nix
programs.dsearch = {
  enable = true;
  systemd.enable = true;
};
```

### Binary not found

Ensure DankSearch is properly installed:

```nix
programs.dsearch.enable = true;
```

## Next Steps

- [[065-docs-danksearch-configuration|Configuration]] options
- [[026-docs-danksearch-usage|Usage]] guide for CLI and API usage
- [[044-docs-dankmaterialshell-overview|DankMaterialShell integration]]