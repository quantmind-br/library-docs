---
title: Marketplace extensions
url: https://docs.docker.com/extensions/marketplace/
source: llms
fetched_at: 2026-01-24T14:28:06.851214009-03:00
rendered_js: false
word_count: 292
summary: This document explains how to manage extensions within Docker Desktop, covering the differences between extension types and providing procedures for installation, updates, and removal.
tags:
    - docker-desktop
    - docker-extensions
    - extension-marketplace
    - software-management
    - installation-guide
category: guide
---

There are two types of extensions available in the Extensions Marketplace:

- Docker-reviewed extensions
- Self-published extensions

Docker-reviewed extensions are manually reviewed by the Docker Extensions team to ensure an extra level of trust and quality. They appear as **Reviewed** in the Marketplace.

Self-published extensions are autonomously published by extension developers and go through an automated validation process. They appear as **Not reviewed** in the Marketplace.

## [Install an extension](#install-an-extension)

> Note
> 
> For some extensions, a separate account needs to be created before use.

To install an extension:

1. Open Docker Desktop.
2. From the Docker Desktop Dashboard, select the **Extensions** tab. The Extensions Marketplace opens on the **Browse** tab.
3. Browse the available extensions. You can sort the list of extensions by **Recently added**, **Most installed**, or alphabetically. Alternatively, use the **Content** or **Categories** drop-down menu to search for extensions by whether they have been reviewed or not, or by category.
4. Choose an extension and select **Install**.

From here, you can select **Open** to access the extension or install additional extensions. The extension also appears in the left-hand menu and in the **Manage** tab.

## [Update an extension](#update-an-extension)

You can update any extension outside of Docker Desktop releases. To update an extension to the latest version, navigate to the Docker Desktop Dashboard and select the **Manage** tab.

The **Manage** tab displays with all your installed extensions. If an extension has a new version available, it displays an **Update** button.

## [Uninstall an extension](#uninstall-an-extension)

You can uninstall an extension at any time.

> Note
> 
> Any data used by the extension that's stored in a volume must be manually deleted.

1. Navigate to the Docker Desktop Dashboard and select the **Manage** tab. This displays a list of extensions you've installed.
2. Select the ellipsis to the right of extension you want to uninstall.
3. Select **Uninstall**.