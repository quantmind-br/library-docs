---
title: NixOS Installation (Flake) | Dank Linux
url: https://danklinux.com/docs/danksearch/nixos-flake
source: sitemap
fetched_at: 2026-01-24T13:34:09.469766893-03:00
rendered_js: false
word_count: 358
summary: Provides instructions for installing and configuring DankSearch on NixOS using Nix flakes and home-manager. It covers flake inputs, configuration parameters, and managing the systemd user service.
tags:
    - nixos
    - home-manager
    - nix-flakes
    - danksearch
    - systemd
    - configuration-guide
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

DankSearch can be installed on NixOS using home-manager with flakes. This guide covers the flake-based installation method for per-user installation.

Native nixpkgs Available

DankSearch is now available in nixpkgs unstable! If you're on NixOS unstable, see [Installation - NixOS](https://danklinux.com/docs/danksearch/nixos) for the native nixpkgs installation method which doesn't require flakes.

## Installation[​](#installation "Direct link to Installation")

### 1. Add Flake Inputs[​](#1-add-flake-inputs "Direct link to 1. Add Flake Inputs")

First, add the DankSearch flake to your `flake.nix`:

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

### 2. Import the home-manager Module[​](#2-import-the-home-manager-module "Direct link to 2. Import the home-manager Module")

Add the DankSearch home-manager module to your home-manager configuration imports:

```
imports =[
  inputs.danksearch.homeModules.dsearch
];
```

If using home-manager as a NixOS module, you can also use the `default` module which is an alias:

```
imports =[
  inputs.danksearch.homeModules.default
];
```

### 3. Enable DankSearch[​](#3-enable-danksearch "Direct link to 3. Enable DankSearch")

In your home-manager configuration, enable DankSearch:

```
programs.dsearch.enable =true;
```

That's it! Rebuild your system (or standalone home-manager configuration) and DankSearch will be installed with sensible defaults.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

DankSearch provides several configuration options to customize your installation:

### Basic Configuration[​](#basic-configuration "Direct link to Basic Configuration")

```
programs.dsearch ={
  enable =true;

# Use a custom package (optional)
  package = pkgs.dsearch;

# Custom configuration (TOML format)
  config ={
# Server configuration
    listen_addr =":43654";

# Index settings
    index_path ="~/.cache/danksearch/index";
    max_file_bytes =2097152;# 2MB
    worker_count =4;
    index_all_files =true;

# Auto-reindex settings
    auto_reindex =false;
    reindex_interval_hours =24;

# Text file extensions
    text_extensions =[
".txt"".md"".go"".py"".js"".ts"
".jsx"".tsx"".json"".yaml"".yml"
".toml"".html"".css"".rs"
];

# Index paths configuration
    index_paths =[
{
        path ="~/Documents";
        max_depth =6;
        exclude_hidden =true;
        exclude_dirs =["node_modules""venv""target"];
}
{
        path ="~/Projects";
        max_depth =8;
        exclude_hidden =true;
        exclude_dirs =["node_modules"".git""target""dist"];
}
];
};
};
```

The configuration follows the TOML format and will be written to `~/.config/danksearch/config.toml`. The structure directly maps to the TOML configuration - see the [Configuration](https://danklinux.com/docs/danksearch/configuration) guide for all available options.

### Systemd Service[​](#systemd-service "Direct link to Systemd Service")

The home-manager module automatically creates a systemd user service that:

- Runs the DankSearch API server with `dsearch serve`
- Automatically starts on login (when `default.target` is reached)
- Restarts on failure with a 5-second delay
- Logs output to the systemd journal

Check service status and logs:

```
# Check service status
systemctl --user status dsearch

# View logs
journalctl --user-u dsearch -f

# Restart service
systemctl --user restart dsearch
```

### Example: Custom Paths Configuration[​](#example-custom-paths-configuration "Direct link to Example: Custom Paths Configuration")

```
programs.dsearch ={
  enable =true;

  config ={
    listen_addr =":43654";
    max_file_bytes =5242880;# 5MB
    worker_count =8;

    index_paths =[
{
        path ="~/Documents";
        max_depth =0;# No limit
        exclude_hidden =false;
        exclude_dirs =[];
}
{
        path ="~/Projects";
        max_depth =8;
        exclude_hidden =true;
        exclude_dirs =["node_modules""venv""target"".git""dist""build"];
}
{
        path ="/mnt/shared";
        max_depth =5;
        watch =false;# Disable watchers for network mount
        exclude_dirs =[".cache"];
}
];
};
};
```

## Rebuilding[​](#rebuilding "Direct link to Rebuilding")

After making configuration changes, rebuild your system:

```
# For home-manager standalone
home-manager switch

# For NixOS with home-manager as a module
sudo nixos-rebuild switch
```

The systemd service will automatically restart with the new configuration.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Service doesn't start automatically[​](#service-doesnt-start-automatically "Direct link to Service doesn't start automatically")

The service is automatically enabled by default. Check that the service is running:

```
systemctl --user status dsearch
```

If the service failed to start, check the logs:

```
journalctl --user-u dsearch -f
```

### Port already in use[​](#port-already-in-use "Direct link to Port already in use")

If port 43654 is already in use, customize the port in your configuration:

```
programs.dsearch ={
  enable =true;
  config.listen_addr =":9876";# Use a different port
};
```

### Index not updating[​](#index-not-updating "Direct link to Index not updating")

The service monitors filesystem changes automatically. To manually rebuild the index:

### Configuration not applied[​](#configuration-not-applied "Direct link to Configuration not applied")

Ensure your configuration is valid TOML and rebuild your home-manager configuration:

```
home-manager switch --show-trace
```

The `--show-trace` flag will show detailed error messages if there are issues.

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

### Using a Custom Package[​](#using-a-custom-package "Direct link to Using a Custom Package")

You can use a specific version or custom build of DankSearch:

```
programs.dsearch ={
  enable =true;
  package = pkgs.dsearch.overrideAttrs (oldAttrs:{
    version ="0.2.0";
# Custom package attributes
});
};
```

### Multiple Index Paths[​](#multiple-index-paths "Direct link to Multiple Index Paths")

Configure DankSearch to index multiple directory trees:

```
programs.dsearch ={
  enable =true;
  config.index ={
    paths =[
"~"
"/mnt/storage"
"/opt/projects"
];
    max_depth =8;
};
};
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Learn more about [Configuration](https://danklinux.com/docs/danksearch/configuration) options
- Explore [Usage](https://danklinux.com/docs/danksearch/usage) guide for CLI and API usage
- Check out [DankMaterialShell integration](https://danklinux.com/docs/dankmaterialshell/overview)