---
title: Build from source
title: Build from source
word_count: 366
summary: This document provides instructions for building the kitty terminal emulator from source code, including dependency requirements, build script usage, and distribution packaging guidelines.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:24Z
---
# Build from source

![Build status](https://github.com/kovidgoyal/kitty/workflows/CI/badge.svg)

Kitty is designed for easy hacking. Dependencies: C compiler + `go compiler <https://go.dev/doc/install>`__ (+ X11 dev libs on Linux).

## Quick Build

```bash
git clone https://github.com/kovidgoyal/kitty.git && cd kitty
./dev.sh build
```

Run with `kitty/launcher/kitty`. The script downloads pre-built dependencies and builds kitty to use them.

> [!NOTE]
> For long-term source runs:
> - Periodically run `./dev.sh deps` to update dependencies
> - Moving/renaming the directory requires `make clean && ./dev.sh build`
> - Create symlinks to kitty/kitten binaries in PATH for convenience

> [!NOTE]
> On macOS, use `kitty/launcher/kitty.app` (unsigned). Notifications won't work. To sign: see `Stack Overflow guide <https://stackoverflow.com/questions/27474751/how-can-i-codesign-an-app-without-being-in-the-mac-developer-program/27474942>`__.

## Build Modes

| Mode | Command | Use Case |
|------|---------|----------|
| Standard | `./dev.sh build` | Normal development |
| Debug symbols | `./dev.sh build --debug` | Debugging |
| Debug + sanitizers | `./dev.sh build --debug --sanitize` | Memory bug hunting |

View all options:

```bash
./dev.sh build -h
```

## Documentation

```bash
# Build docs locally
./dev.sh deps -for-docs && ./dev.sh docs

# Live-reload during development
./dev.sh deps -for-docs && ./dev.sh docs -live-reload
```

## Dependencies

### System Libraries (for system-lib builds only)

**Runtime:**
- `python`
- `harfbuzz` >= 2.2.0
- `zlib`, `libpng`, `liblcms2`, `libxxhash`, `openssl`
- `pixman` (not macOS)
- `cairo`, `freetype`, `fontconfig`, `libcanberra` (not macOS)
- `libsystemd` (optional)
- `ImageMagick` (optional, uncommon image formats)

**Build:**
- `gcc` or `clang`
- `simde`
- `go` >= version in go.mod
- `pkg-config`
- NERD Font Mono (system-wide or `fonts/SymbolsNerdFontMono-Regular.ttf`)

**Linux additional packages:**
- `liblcms2-dev`, `libfontconfig-dev`, `libssl-dev`, `libpython3-dev`, `libxxhash-dev`, `libsimde-dev`, `libcairo2-dev`
- X11: `libdbus-1-dev`, `libxcursor-dev`, `libxrandr-dev`, `libxi-dev`, `libxinerama-dev`, `libgl1-mesa-dev`, `libxkbcommon-x11-dev`, `libx11-xcb-dev`

## Nix Build

```bash
nix-shell
# Then: make (Linux) or make app (macOS)
```

Use `nix-shell --pure` to isolate from the host system.

## Linux Distribution Packages

> [!NOTE]
> Kitty is not a traditional Python package. Do not install in site-packages.

```bash
make linux-package
```

This installs into `linux-package/`. Files:
- Binary: `linux-package/bin/kitty`
- Library: `linux-package/lib/kitty`
- Terminfo: `linux-package/share/terminfo`

Copy to `/usr` to install, or use `--prefix` for custom staging.

### Recommended Package Split

| Package | Contents |
|---------|----------|
| `kitty-terminfo` | Terminfo file |
| `kitty-shell-integration` | Shell scripts to `/usr/share/kitty/shell-integration` |
| `kitty` | Main program |

This allows installing terminfo/shell-integration on SSH servers without the full kitty install.

> [!NOTE]
> Extra build dependencies: `tic` (ncurses dev) for terminfo compilation. For git checkouts, also `docs/requirements.txt`.

## Cross Compilation

```bash
make prepare-for-cross-compile
# Setup CC, CFLAGS, PATH, etc.
make cross-compile
```

Output: `linux-package/` directory. Test suite cannot run on cross-compiled builds.

#kitty #source-code #build-instructions #terminal-emulator #developer-tools
