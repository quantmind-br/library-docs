---
title: NIX
url: https://github.com/sashetophizika/hyprscratch/blob/master/NIX.md
source: git
fetched_at: 2026-02-02T02:42:38.361274415-03:00
rendered_js: false
word_count: 83
summary: This document provides step-by-step instructions for installing and configuring the hyprscratch utility using Nix Flakes, Home Manager, and the Nix profile command.
tags:
    - nix
    - nix-flakes
    - home-manager
    - hyprscratch
    - installation-guide
category: Installation & Setup
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

