---
title: Logging Out & Uninstalling | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/troubleshooting-and-support/logging-out-and-uninstalling
source: sitemap
fetched_at: 2026-04-29T15:05:47.572432554-03:00
rendered_js: false
word_count: 118
summary: This document provides instructions on how to log out of the Warp application and details the manual steps required to completely uninstall the software and its associated data files.
tags:
    - warp
    - account-management
    - uninstallation
    - system-maintenance
    - cleanup
    - user-settings
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
## Logging out

Log out via **Settings** > **Account** > **Log out**.

![Logout Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F2974137108-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FD4dBaHbuMVNs0iB2iqZ1%252Fuploads%252Fgit-blob-5906d41458bb7f76b7df89941c20e995c6cfab94%252Flogout.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f2a644ac&sv=2)

### Known issues

1. Logging out loses all running processes and unsaved objects.
2. Logging in with another account preserves: Theme, Keybindings, and Settings (autosuggestion, notifications, font size, welcome tips status).
3. Logging in triggers the onboarding survey.

## Uninstalling Warp

> [!info]
> For Warp Preview, replace `Warp-Stable` with `Warp-Preview` in the commands below (e.g., `defaults delete dev.warp.Warp-Preview`).

### Uninstall by dmg

- `sudo rm -r /Applications/Warp.app`
- Open **Finder** > **Applications**, right-click Warp, select **Move to Trash**

### Uninstall by Homebrew

- `brew uninstall warp`

### Remove settings, files, logs, and database

```bash
# Remove Warp settings defaults
defaults delete dev.warp.Warp-Stable

# Remove Warp logs
sudo rm -r $HOME/Library/Logs/warp.log

# Remove Warp database, Codebase Context, and MCP logs
sudo rm -r "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable"

# Remove Warp user files, themes, and launch configurations
sudo rm -r $HOME/.warp
# Note: Removing $HOME/.warp deletes files for both Stable and Preview.
```

### Warp Preview users

```bash
# Remove Warp Preview settings defaults
defaults delete dev.warp.Warp-Preview

# Remove Warp Preview logs
sudo rm -r $HOME/Library/Logs/warp_preview.log

# Remove Warp Preview database, Codebase Context, and MCP logs
sudo rm -r "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Preview"

# Remove shared user files
sudo rm -r $HOME/.warp
```

#warp #account-management #uninstallation #system-maintenance #cleanup #user-settings
