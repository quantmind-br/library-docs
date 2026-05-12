---
title: NIX
url: https://github.com/sashetophizika/hyprscratch/blob/master/NIX.md
source: git
fetched_at: 2026-04-27T07:41:46.741710344-03:00
rendered_js: false
word_count: 83
summary: This document provides installation instructions and configuration examples for integrating the hyprscratch utility using Nix flakes and Home Manager.
tags:
    - nix
    - hyprland
    - configuration
    - home-manager
    - nix-flakes
    - software-installation
category: configuration
---

## Nix Installation Insctructions:

### Flake:
```nix
inputs = {
  hyprscratch = {
    url = "github:sashetophizika/hyprscratch";
    inputs.nixpkgs.follows = "nixpkgs";
  };
};
```

### Home Manager:
```nix
{inputs, pkgs, ...}: {
  home.packages = [inputs.hyprscratch.packages.${pkgs.system}.default];

  # or

  imports = [inputs.hyprscratch.homeModules.default];
  programs.hyprscratch = {
    enable = true;
    settings = {
      btop = {
        class = "btop";
        command = "kitty --title btop -e btop";
        rules = "size 85% 85%";
        options = "cover persist sticky";
      };
    };
  };
}
```

### Non-NixOS:
```bash
nix profile install github:sashetophizika/hyprscratch
```

