---
title: Server Patching
url: https://coolify.io/docs/knowledge-base/server/patching.md
source: llms
fetched_at: 2026-02-17T14:41:02.492508-03:00
rendered_js: false
word_count: 353
summary: This document explains how to use the Server Patching feature in Coolify to manually manage and install package updates for servers directly from the dashboard.
tags:
    - server-patching
    - coolify
    - package-management
    - server-maintenance
    - linux-updates
category: guide
---

# Server Patching

The **Server Patching** feature lets you update all packages on your server directly from the Coolify dashboard.

::: warning IMPORTANT
This feature is introduced in **v4.0.0-beta.419**. To follow this guide, you **must** be using v4.0.0-beta.419 or a higher version.
:::

## How to Use Server Patching

On this page, you'll see a list of all available package updates.

You can either:

* Update packages **individually** by clicking the **Update** button next to each one.
* Or, click **Update All Packages** to apply all updates at once.

::: info Note
Coolify **does not** automatically install updates. It only checks for available updates and displays them in the dashboard.

Updates are applied only when you manually click the **Update** or **Update All Packages** button.
:::

::: danger Important
Some package updates may break existing features.
Docker-related updates will restart Docker, which means all your applications and Coolify itself will be unavailable until Docker is restarted.

**We highly recommend you to review each package carefully before updating.**
:::

## Server Patching Notifications

Coolify checks for updates weekly and sends notifications if any are available.

* Notifications are **enabled by default**.
* You can manage this setting in your **Notification Settings**.

## Supported Package Managers

As of **v4.0.0-beta.419**, server patching is supported for the following package managers:

* **APT**
* **DNF**
* **Zypper**

Support for additional package managers will be added in future updates.

If you'd like to prioritize support for a specific package manager, feel free to start a discussion here: [Coolify Discussions on GitHub](https://github.com/coollabsio/coolify/discussions)

## FAQ

::: details 1. Can I change how frequently Coolify checks for updates?
No, the update check interval is currently fixed.

However, you can manually trigger a check by clicking the **Check now** button on the Server Patching page.

This feature was introduced in **v4.0.0-beta.419**, and we’re focusing on improving it based on user feedback. If you'd like to request customizable check intervals, feel free to start a discussion here: [Coolify Discussions on GitHub](https://github.com/coollabsio/coolify/discussions)
:::

::: details 2. Does Coolify install updates automatically?
**No**, Coolify does not install updates automatically.

Updates are only applied when you manually click the **Update** or **Update all packages** button on the dashboard.
:::