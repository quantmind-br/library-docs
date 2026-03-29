---
title: ForgeCode
url: https://forgecode.dev/docs/uninstallation/
source: sitemap
fetched_at: 2026-03-29T14:52:28.28189884-03:00
rendered_js: false
word_count: 153
summary: This document provides instructions for completely uninstalling ForgeCode from your system, including removing the application, configuration files, and project-specific settings.
tags:
    - uninstall
    - forgecode
    - configuration
    - removal
    - cleanup
category: guide
---

Uninstall ForgeCode from your system.

### Uninstall

Run the uninstall command:

This will remove ForgeCode from your system.

### Verify Removal

Check that ForgeCode has been removed:

You should see an error indicating the command is not found, confirming successful removal.

After uninstalling the main application, you may want to remove associated configuration files and data:

### Remove ForgeCode configuration directory

Delete the `forge` folder from your home directory. This folder contains your authentication tokens, custom agents, and local configurations.

**Location:**

- **macOS/Linux**: `~/forge/`
- **Windows**: `%USERPROFILE%\forge\`

### Remove project-specific configurations (optional)

Look for `forge.yaml` files in your project directories and delete them if no longer needed. These files contain project-specific ForgeCode settings and agent configurations.

### Check command availability

The command should return "not found" or a similar error.

If you encounter issues during uninstallation:

- Join our [Discord community](https://discord.gg/kRZBPpkgwq) for real-time help
- Visit our [GitHub Issues](https://github.com/antinomyhq/forge/issues)

* * *

Success

ForgeCode has been removed from your system. Thank you for trying ForgeCode!