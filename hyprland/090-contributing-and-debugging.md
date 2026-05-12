---
title: Contributing and Debugging
url: https://wiki.hypr.land/Contributing-and-Debugging/
source: sitemap
fetched_at: 2026-04-26T09:49:03.03128796-03:00
rendered_js: false
word_count: 470
summary: This document provides instructions for setting up a development environment, building Hyprland in debug mode, and performing debugging tasks such as analyzing crashes and logs.
tags:
    - hyprland
    - debugging
    - development-setup
    - c-plus-plus
    - cmake
    - nix
    - gdb
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

PR guidelines, code styling, and code FAQs are at [[087-contributing-and-debugging-pr-guidelines|PR Guidelines]].

For issues, see [the guidelines](https://github.com/hyprwm/Hyprland/blob/main/docs/ISSUE_GUIDELINES.md).

## Build in debug mode[](#build-in-debug-mode)

### Required packages[](#required-packages)

See [[001-getting-started-installation|manual build deps]].

### Recommended: CMake + VSCode[](#recommended-cmake)

Install the VSCode C/C++ and CMake Tools extensions. Copy the [example launch.json](https://github.com/hyprwm/Hyprland/blob/main/example/launch.json) to `.vscode/` in the repo root. Build in debug, go to the debugging tab, and hit `(gdb) Launch`.

> [!note]
> Set `watchdog_timeout = 0` in the `debug {}` section of your config — otherwise Hyprland will crash after continuing from a breakpoint when it notices the hang.

### Custom: CLI[](#custom-cli)

```sh
make debug
```

Attach and profile in your preferred way.

### Nix[](#nix)

```nix
hyprland.override {
  debug = true;
};
```

Place in the `package` attribute of NixOS or Home Manager modules.

## Development environment[](#development-environment)

### Setup[](#setup)

Copy your config to `~/.config/hypr/hyprlandd.conf`. Debug builds automatically use this file, or pass `--config ~/path/to/conf.conf` to override.

#### Recommended debug config changes[](#recommended-debug-config-changes)

- Remove all `exec=` and `exec-once=` directives.
- Change the default modifier for binds (e.g. `SUPER` -> `ALT`).

#### Launch the dev env[](#launch-the-dev-env)

Launch the `Hyprland` binary from `./build/` while logged into a Hyprland session. A nested session opens, letting you test without nuking your actual session.

Launch with a debugger (e.g. `gdb ./build/Hyprland` or your IDE's graphical debugger). On crash, gdb stops and lets you inspect state with `bt`, `frame`, `print`, etc.

## LSP and formatting[](#lsp-and-formatting)

For LSP support, use `clangd`. Generate compile commands first:

```sh
cmake -S . -B build/ -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

Before submitting a PR, format with clang-format:

```sh
git-clang-format
```

## Logs and coredumps[](#logs-dumps-etc)

Use logs and GDB. Debug-compiled Hyprland provides more insight into random bugs.

On crash, use `coredumpctl` then `coredumpctl info PID` to inspect. See [`ISSUE_GUIDELINES.md`](https://github.com/hyprwm/Hyprland/blob/main/docs/ISSUE_GUIDELINES.md) for details.

Live log watching:

```sh
watch -n 0.1 "grep -v 'arranged' $XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/hyprland.log | tail -n 40"
```

Replace `hyprland` with `hyprlandd` for debug builds.
