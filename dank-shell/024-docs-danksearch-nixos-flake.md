---
title: NixOS Installation (Flake) | Dank Linux
url: https://danklinux.com/docs/danksearch/nixos-flake
source: sitemap
fetched_at: 2026-04-26T08:39:29.568335468-03:00
rendered_js: false
word_count: 360
summary: This document provides instructions for installing and configuring DankSearch on NixOS systems using home-manager and Nix flakes.
tags:
    - nixos
    - home-manager
    - nix-flakes
    - danksearch
    - systemd
    - configuration
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

```
██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

```

DankSearch can be installed on NixOS using home-manager with flakes. This guide covers the flake-based installation method for per-user installation.

> [!info]
> DankSearch is now available in nixpkgs unstable! On NixOS unstable, see [[025-docs-danksearch-nixos|Installation - NixOS]] for the native nixpkgs installation method which doesn't require flakes.

## Installation

### 1. Add Flake Inputs

Add the DankSearch flake to your `flake.nix`:

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

### 2. Import the home-manager Module

Add the DankSearch home-manager module to your imports:

```nix
imports = [
  inputs.danksearch.homeModules.dsearch
];
```

You can also use the `default` module alias:

```nix
imports = [
  inputs.danksearch.homeModules.default
];
```

### 3. Enable DankSearch

In your home-manager configuration, enable DankSearch:

```nix
programs.dsearch.enable = true;
```

Rebuild your configuration and DankSearch will be installed with sensible defaults.

## Configuration Options

### Basic Configuration

```nix
programs.dsearch = {
  enable = true;
  # Use a custom package (optional)
  package = pkgs.dsearch;
  # Custom configuration (TOML format)
  config = {
    # Server configuration
    listen_addr = ":43654";
    # Index settings
    index_path = "~/.cache/danksearch/index";
    max_file_bytes = 2097152;  # 2MB
    worker_count = 4;
    index_all_files = true;
    # Auto-reindex settings
    auto_reindex = false;
    reindex_interval_hours = 24;
    # Text file extensions
    text_extensions = [".txt" ".md" ".go" ".py" ".js" ".ts" ".jsx" ".tsx" ".json" ".yaml" ".yml" ".toml" ".html" ".css" ".rs"];
    # Index paths configuration
    index_paths = [
      {
        path = "~/Documents";
        max_depth = 6;
        exclude_hidden = true;
        exclude_dirs = ["node_modules" "venv" "target"];
      }
      {
        path = "~/Projects";
        max_depth = 8;
        exclude_hidden = true;
        exclude_dirs = ["node_modules" ".git" "target" "dist"];
      }
    ];
  };
};
```

The configuration follows TOML format and is written to `~/.config/danksearch/config.toml`. See [[065-docs-danksearch-configuration|Configuration]] for all available options.

### Systemd Service

The home-manager module automatically creates a systemd user service that:

- Runs the DankSearch API server with `dsearch serve`
- Automatically starts on login (when `default.target` is reached)
- Restarts on failure with a 5-second delay
- Logs output to the systemd journal

Check service status and logs:

```bash
# Check service status
systemctl --user status dsearch
# View logs
journalctl --user -u dsearch -f
# Restart service
systemctl --user restart dsearch
```

### Example: Custom Paths Configuration

```nix
programs.dsearch = {
  enable = true;
  config = {
    listen_addr = ":43654";
    max_file_bytes = 5242880;  # 5MB
    worker_count = 8;
    index_paths = [
      {
        path = "~/Documents";
        max_depth = 0;  # No limit
        exclude_hidden = false;
        exclude_dirs = [];
      }
      {
        path = "~/Projects";
        max_depth = 8;
        exclude_hidden = true;
        exclude_dirs = ["node_modules" "venv" "target" ".git" "dist" "build"];
      }
      {
        path = "/mnt/shared";
        max_depth = 5;
        watch = false;  # Disable watchers for network mount
        exclude_dirs = [".cache"];
      }
    ];
  };
};
```

## Rebuilding

After making configuration changes, rebuild:

```bash
# For home-manager standalone
home-manager switch
# For NixOS with home-manager as a module
sudo nixos-rebuild switch
```

The systemd service will automatically restart with the new configuration.

## Troubleshooting

### Service doesn't start automatically

Check that the service is running:

```bash
systemctl --user status dsearch
```

If the service failed to start, check the logs:

```bash
journalctl --user -u dsearch -f
```

### Port already in use

If port 43654 is already in use, customize the port:

```nix
programs.dsearch = {
  enable = true;
  config.listen_addr = ":9876";  # Use a different port
};
```

### Index not updating

The service monitors filesystem changes automatically. To manually rebuild the index:

### Configuration not applied

Ensure your configuration is valid TOML and rebuild:

```bash
home-manager switch --show-trace
```

The `--show-trace` flag will show detailed error messages.

## Advanced Configuration

### Using a Custom Package

```nix
programs.dsearch = {
  enable = true;
  package = pkgs.dsearch.overrideAttrs (oldAttrs: {
    version = "0.2.0";
    # Custom package attributes
  });
};
```

### Multiple Index Paths

```nix
programs.dsearch = {
  enable = true;
  config.index = {
    paths = ["~" "/mnt/storage" "/opt/projects"];
    max_depth = 8;
  };
};
```

## Next Steps

- [[065-docs-danksearch-configuration|Configuration]] options
- [[026-docs-danksearch-usage|Usage]] guide for CLI and API usage
- [[044-docs-dankmaterialshell-overview|DankMaterialShell integration]]