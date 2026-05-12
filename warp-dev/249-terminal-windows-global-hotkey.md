---
title: "Global hotkey"
url: https://docs.warp.dev/terminal/windows/global-hotkey
source: sitemap
fetched_at: 2026-04-29T15:02:40-03:00
rendered_js: false
word_count: 185
summary: This document explains how to configure and enable global hotkey features in Warp, including dedicated window management and show/hide functionality.
tags:
    - warp-terminal
    - hotkeys
    - window-management
    - keybindings
    - keyboard-shortcuts
    - productivity
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Global Hotkey

Configure system-wide keyboard shortcuts to manage Warp windows.

## Dedicated Window

Enables Quake Mode: pin a Warp window to a fixed position at a configurable width/height ratio.

1. **Settings** > **Features** > **Keys** > select **Dedicated hotkey window** from the Global Hotkey dropdown.
2. Configure the keybinding, position, screen, and relative size.
3. Optionally uncheck **Autohides on the loss of keyboard focus** to keep the window always on top.

> [!warning]
> On Linux and Windows, Warp does not support the "Autohides on the loss of keyboard focus" feature.

![Dedicated Window Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-048acf9fd85b0fa2129bb90a1b3d8a2d1f911f5b%252FDedicated-Window.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f499082c&sv=2)

## Show / Hide All Windows

Toggle visibility of all Warp windows with a single shortcut.

1. **Settings** > **Features** > **Keys** > select **Show/hide all windows** from the Global Hotkey dropdown.
2. Configure your preferred keybinding.

> [!warning]
> On Linux, hidden windows may not appear in `ALT-TAB`. The ordering of windows beyond the top window may change after toggling.

![Show/Hide All Windows Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-af6164e0085e8fa8f3d2ff3602178e4c9343332c%252FShow-Hide-All-Windows.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=55795aa3&sv=2)

## Troubleshooting

If a keybinding doesn't work, check **System Preferences > Security & Privacy > Accessibility** and grant Warp accessibility access.

#terminal #global-hotkey #window-management #keybindings
