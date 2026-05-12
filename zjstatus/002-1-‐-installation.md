---
title: !!binary MSDvv72AkCBJbnN0YWxsYXRpb24=
url: https://github.com/dj95/zjstatus/wiki/1-‐-Installation
source: wiki
fetched_at: 2026-04-30T12:58:25.404717926-03:00
rendered_js: false
word_count: 521
summary: This document provides instructions for installing the zjstatus plugin for Zellij, covering manual, automated, and Nix Flakes installation methods along with troubleshooting tips.
tags:
    - zellij
    - zjstatus
    - terminal-plugins
    - installation-guide
    - nix-flakes
    - layout-configuration
category: guide
---

There are several ways to install zjstatus. The main process is downloading the file and including it in your layout. Another option is the way to download it with zellij, when the plugin is specified with the URL.

> [!IMPORTANT]
> Using zjstatus involves creating new layouts and overriding the default one. This will lead to swap layouts not working, when they are not configured correctly. Please follow [this section](https://github.com/dj95/zjstatus/wiki/3-%E2%80%90-Configuration#swap-layouts) for getting swap layouts back to work, if you need them.

You could also refer to the plugin guide from zellij, after downloading the binary: [https://zellij.dev/documentation/plugin-loading](https://zellij.dev/documentation/plugin-loading)

Please ensure, that the configuration is correct.

Sometimes, especially when updating zjstatus, it might come to caching issues, which can be resolved by clearing it. Please keep in
mind, that it will also clear the cache for running sessions and revokes granted permissions for plugins.


> [!IMPORTANT]
> In case you experience any crashes or issues, please in the first step try to clear the cache! (`$HOME/.cache/zellij/` for Linux, `$HOME/Library/Caches/org.Zellij-Contributors.Zellij/` on macOS)


## Automated installation

> [!IMPORTANT]
> Using the manual installation is highly recommend instead of the automatic one! Zellij currently has a bug that corrupts the download, if multiple tabs download the plugin at the same time. For further information check out the issue: [zellij-org/zellij#3479](https://github.com/zellij-org/zellij/issues/3479)



Create a new layout in `$HOME/.config/zellij/layouts/default.kdl` (or `$ZELLIJ_CONFIG_DIR/layouts/default.kdl` if you set it). Start with the following structure, that overrides the default tab template with zjstatus as a bottom bar. When opening the layout, zellij will download the latest release and ask for permissions on the first run or updates.

```javascript
layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="https://github.com/dj95/zjstatus/releases/latest/download/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}
```

## Manual installation

Download the latest binary in the GitHub releases. Place it somewhere, zellij is able to access it. Then the
plugin can be included by referencing it in a layout file, e.g. the default layout one.

For using the default one, create a new layout in `$HOME/.config/zellij/layouts/default.kdl` (or `$ZELLIJ_CONFIG_DIR/layouts/default.kdl` if you set it). Start with the following structure, that overrides the default tab template with zjstatus as a bottom bar. When opening the layout, zellij will ask for permissions on the first run or updates.

```javascript
layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="file:~/path/to/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}
```



## Nix Flakes

Add this repository to your inputs and then with the following overlay to your packages.
Then you are able to install and refer to it with `pkgs.zjstatus`. When templating the
config file, you can use `${pkgs.zjstatus}/bin/zjstatus.wasm` as the path.

```nix
  inputs = {
    # ...

    zjstatus = {
      url = "github:dj95/zjstatus";
    };
  };


  # define the outputs of this flake - especially the home configurations
  outputs = { self, nixpkgs, zjstatus, ... }@inputs:
  let
    inherit (inputs.nixpkgs.lib) attrValues;

    overlays = with inputs; [
      # ...
      (final: prev: {
        zjstatus = zjstatus.packages.${prev.system}.default;
      })
    ];
```

As an example with home-manager, the initial configuration can look like:

```nix
  xdg.configFile."zellij/layouts/default.kdl".text = ''layout {
    default_tab_template {
        children
        pane size=1 borderless=true {
            plugin location="file:${pkgs.zjstatus}/bin/zjstatus.wasm" {
                // plugin configuration...
            }
        }
    }
}'';
```

