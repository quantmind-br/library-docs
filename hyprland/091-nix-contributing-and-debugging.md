---
title: Contributing and Debugging
url: https://wiki.hypr.land/Nix/Contributing-and-Debugging/
source: sitemap
fetched_at: 2026-04-26T09:48:14.494158468-03:00
rendered_js: false
word_count: 249
summary: This document outlines the procedures for building, debugging, and troubleshooting Hyprland and related programs within the Nix development environment.
tags:
    - hyprland
    - nix
    - debugging
    - software-build
    - stacktrace
    - development-environment
    - wayland
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

All needed to build and debug Hyprland and hyprwm programs is included in the provided `devShell`s. Run `nix develop` in the cloned repo.

## Build in debug mode

Debug build: `hyprland.packages.${pkgs.stdenv.hostPlatform.system}.hyprland-debug`.

Most hyprwm apps provide their own `-debug` versions. For those that don't, build debug version from CLI using [overrideAttrs](https://wiki.hypr.land/Nix/Options-Overrides/#using-nix-repl) with `cmakeBuildType = "Debug";` or `mesonBuildType = "debug";`.

## Bisecting an issue

Follow the [Bisecting an issue](https://wiki.hypr.land/Crashes-and-Bugs/#bisecting-an-issue) guide. Build with `nix build`.

> [!warning]
> To build with Tracy support, modify `nix/default.nix` to enable the flag, then run `nix build '.?submodules=1'`.

Use `--print-build-logs` (`-L`) to view logs. Use `--keep-failed` to keep failed build directory.

## Building the Wayland stack with ASan

Run `nix develop` first, then follow [Building with ASan](https://wiki.hypr.land/Crashes-and-Bugs/#building-with-asan) guide.

## Getting a debug stacktrace

Debug stacktraces require Hyprland [built in debug mode](#build-in-debug-mode).

```sh
nix shell nixpkgs#gdb # get gdb temporarily
coredumpctl # check the PID of the recent crash
coredumpctl debug <PID> # using the PID found in the previous step
```

Continue from step 3 onwards in the [debug stacktrace guide](https://wiki.hypr.land/Crashes-and-Bugs#obtaining-a-debug-stacktrace).

## Manual building

Nix abstracts Meson, CMake, and Ninja differently than other build systems.

For CMake:
```bash
cmakeConfigurePhase # run CMake configure phase
buildPhase     # run the build phase
installPhase   # run the install phase
```

For Meson:
```bash
mesonConfigurePhase # run Meson configure phase
ninjaBuildPhase     # run Ninja build phase
mesonInstallPhase   # run Meson install phase
```

Last updated on April 20, 2026

[[021-nix-plugins|Plugins]]