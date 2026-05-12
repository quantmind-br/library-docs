---
title: Install kitty
title: Install kitty
word_count: 224
summary: This document provides comprehensive instructions for installing, configuring, and uninstalling the kitty terminal emulator on macOS and Linux systems.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:24Z
---
# Install kitty

## Binary Install

Install pre-built binaries on macOS or Linux:

```sh
_kitty_install_cmd
```

Install locations:
- macOS: `/Applications/kitty.app`
- Linux: `~/.local/kitty.app`

Re-run the command to update. The installer only touches files in the install directory.

> [!WARNING]
> Do not move the kitty binary out of the installation folder. To add to PATH, create a symlink in `~/.local/bin`, `/usr/bin`, or another systemwide PATH location. Shell rc file PATH additions won't work when running kitty from desktop environments.

## Manual Install

Download from `GitHub releases <https://github.com/kovidgoyal/kitty/releases>`__:

- macOS: download `.dmg`, install normally
- Linux: download tarball, extract. Binary is in the `bin/` subdirectory

## Desktop Integration on Linux

For taskbar icon and menu entries:

```sh
# Symlinks to PATH (assuming ~/.local/bin is in system PATH)
ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/

# Desktop file
cp ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/

# Optional: open files/images in kitty via file manager
cp ~/.local/kitty.app/share/applications/kitty-open.desktop ~/.local/share/applications/

# Fix paths in desktop files
sed -i "s|Icon=kitty|Icon=$(readlink -f ~)/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" ~/.local/share/applications/kitty*.desktop
sed -i "s|Exec=kitty|Exec=$(readlink -f ~)/.local/kitty.app/bin/kitty|g" ~/.local/share/applications/kitty*.desktop

# Register as xdg-terminal
echo 'kitty.desktop' > ~/.config/xdg-terminals.list
```

> [!NOTE]
> `kitty-open.desktop` registers kitty for some MIME types. To use a different file manager for directories:
> ```bash
> xdg-mime default org.kde.dolphin.desktop inode/directory
> ```

> [!NOTE]
> Using GNU Stow for manual installs (with `dest=~/.local/stow`):
> ```bash
> cd ~/.local/stow && stow -v kitty.app
> ```

## Installation Options

| Option | Command |
|--------|---------|
| Nightly build | `installer=nightly` |
| Specific version | `installer=version-0.35.2` |
| Custom location | `dest=/some/other/location` |
| Skip auto-launch | `launch=n` |
| Local tarball/dmg | `installer=/path/to/file` |

Example with multiple options:

```sh
_kitty_install_cmd installer=nightly dest=/opt/kitty-dev launch=n
```

## Uninstall

Delete the installation directory.

## Next Steps

Build from source: see [[024-build]]

#kitty #terminal-emulator #software-installation #linux-desktop #macos-installation
