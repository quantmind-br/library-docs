---
title: Updating Warp | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/troubleshooting-and-support/updating-warp
source: sitemap
fetched_at: 2026-04-29T15:05:44.16353821-03:00
rendered_js: false
word_count: 197
summary: This document explains how to check for Warp application updates and provides troubleshooting steps for resolving update-related permissions issues on macOS and signature verification errors on Linux distributions.
tags:
    - warp-terminal
    - software-updates
    - troubleshooting
    - macos-permissions
    - linux-package-management
    - signing-keys
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp automatically checks for updates on startup. A notification appears in the top-right corner of the Warp window when a new update is available.

To check for updates, search "update" in the [[101-terminal-command-palette|Command Palette]] or go to **Settings** > **Account** and click **Check for Update**. If nothing happens, you already have the latest stable build.

## macOS: Auto-update permissions issues

Warp cannot auto-update without the correct permissions to replace the running binary. A banner prompts you to manually update when this occurs.

Two main causes:

1. **Opened directly from mounted volume** — Quit Warp, drag the application into `/Applications`, then restart.
2. **Non-admin user** — If you have admin access, open the app as admin to resolve auto-update issues.

## Linux: Refreshing the package signing key

Signature verification errors may occur when the package signing key has expired. Refresh the key per your distribution:

### Debian / Ubuntu (apt)

To fetch the updated signing key, run:

```

```

Then retry your update:

```

```

### Fedora / RHEL / CentOS (dnf/yum)

To fetch the updated signing key, run:

```

```

Then retry your update:

```

```

### Arch Linux (pacman)

To fetch the updated signing key, run:

```

```

Then retry your update:

```

```

#troubleshooting #software-updates #macos-permissions #linux-package-management
