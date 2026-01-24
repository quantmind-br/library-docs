---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/danksearch/nixos
source: sitemap
fetched_at: 2026-01-24T13:36:06.848486141-03:00
rendered_js: false
word_count: 259
summary: This document provides instructions for installing and configuring DankSearch on NixOS using the native nixpkgs module, covering systemd service setup and flake integration.
tags:
    - nixos
    - danksearch
    - nixpkgs
    - systemd
    - flakes
    - installation-guide
    - configuration
category: guide
---

```
██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                      
```

DankSearch can be installed on NixOS using the NixOS module. This guide covers the native nixpkgs installation method.

NixOS Unstable Required

DankSearch is currently only available in the **unstable** branch of nixpkgs. If you're on NixOS stable, you'll need to use the [Flake Installation](https://danklinux.com/docs/danksearch/nixos-flake) method instead.

## Installation[​](#installation "Direct link to Installation")

### 1. Enable NixOS Unstable[​](#1-enable-nixos-unstable "Direct link to 1. Enable NixOS Unstable")

Ensure you're using NixOS unstable by setting your channel or flake input:

**Using channels:**

```
sudo nix-channel --add https://nixos.org/channels/nixos-unstable nixos
sudo nix-channel --update
```

**Using flakes (in `flake.nix`):**

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";
};
}
```

### 2. Enable DankSearch[​](#2-enable-danksearch "Direct link to 2. Enable DankSearch")

In your NixOS configuration, enable DankSearch:

```
programs.dsearch.enable =true;
```

That's it! Rebuild your system and DankSearch will be installed with sensible defaults.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

DankSearch provides configuration options to customize your installation:

### Basic Configuration[​](#basic-configuration "Direct link to Basic Configuration")

```
programs.dsearch ={
  enable =true;

# Use a custom package (optional)
  package = pkgs.dsearch;

# Systemd service configuration
  systemd ={
    enable =true;# Enable systemd user service
    target ="default.target";# Start with user session
};
};
```

### Systemd Service Options[​](#systemd-service-options "Direct link to Systemd Service Options")

The NixOS module configures a systemd user service. You can customize when it starts:

```
programs.dsearch ={
  enable =true;

  systemd ={
    enable =true;
    target ="graphical-session.target";# Only start in graphical sessions
};
};
```

### Using Flake Package with NixOS Module[​](#using-flake-package-with-nixos-module "Direct link to Using Flake Package with NixOS Module")

You can use the package from the DankSearch flake while still using the native NixOS module. This allows you to get quicker updates while keeping the module configuration:

First, add the flake input to your `flake.nix`:

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";

    danksearch ={
      url ="github:AvengeMedia/danksearch";
      inputs.nixpkgs.follows ="nixpkgs";
};
};
}
```

Then use the flake package with the native module:

```
programs.dsearch ={
  enable =true;
  package = inputs.danksearch.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

warning

When using the flake package with the native nixpkgs module, some dependencies may not be automatically enabled by default, and certain configurations might be missing. You may need to manually install optional dependencies or adjust feature toggles to match your needs.

## Rebuilding[​](#rebuilding "Direct link to Rebuilding")

After making configuration changes, rebuild your system:

```
sudo nixos-rebuild switch
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Service doesn't start automatically[​](#service-doesnt-start-automatically "Direct link to Service doesn't start automatically")

Make sure you have `systemd.enable = true` set:

```
programs.dsearch ={
  enable =true;
  systemd.enable =true;
};
```

### Binary not found[​](#binary-not-found "Direct link to Binary not found")

Ensure DankSearch is properly installed:

```
programs.dsearch.enable =true;
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Learn more about [Configuration](https://danklinux.com/docs/danksearch/configuration) options
- Explore [Usage](https://danklinux.com/docs/danksearch/usage) guide for CLI and API usage
- Check out [DankMaterialShell integration](https://danklinux.com/docs/dankmaterialshell/overview)