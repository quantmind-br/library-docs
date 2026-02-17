---
title: Upgrading Coolify
url: https://coolify.io/docs/get-started/upgrade.md
source: llms
fetched_at: 2026-02-17T14:38:32.815503-03:00
rendered_js: false
word_count: 383
summary: This document explains the three methods for upgrading a self-hosted Coolify instance, including automatic, semi-automatic, and manual procedures. It provides technical details on how updates are fetched and instructions for executing the upgrade script.
tags:
    - coolify
    - self-hosting
    - software-updates
    - server-maintenance
    - installation-script
    - automation
category: guide
---

If you're using [Coolify Cloud](https://coolify.io/pricing/), the Coolify team handles all updates so you don’t need to worry about them.

For those who **self-host** Coolify, there are three ways to upgrade your instance:

* [Automatic Upgrade:](#_1-automatic-upgrade) For users who want easy, hands-off updates.
* [Semi-Automatic Upgrade:](#_2-semi-automatic-upgrade) For users who want control over when to apply updates.
* [Manual Upgrade:](#_3-manual-upgrade) For advanced users who prefer to manage the upgrade process themselves.

::: danger Backup First!

* Always back up your Coolify data before starting an upgrade.
  :::

## 1. Automatic Upgrade

Coolify can update itself automatically. This option keeps your instance always up-to-date without any extra effort.

### How it works?

Coolify periodically checks the [CDN](https://cdn.coollabs.io/coolify/versions.json) for updates. When a new version is available, it automatically fetches the latest release from the [official repository](https://github.com/orgs/coollabsio/packages?repo_name=coolify) and starts the upgrade process on its own.

### Customize Automatic Updates

If you’d rather manage updates yourself, you can disable auto-updates in your Coolify dashboard’s Settings.

::: info Tip
Turning off automatic updates lets you test a new version on a staging setup before updating your live environment.
:::

## 2. Semi-Automatic Upgrade

This option gives you a bit more control. Coolify notifies you when an update is available, and you decide when to apply it.

### How it works?

Coolify periodically checks the [CDN](https://cdn.coollabs.io/coolify/versions.json) for updates. When a new version is available, you will see an "**Upgrade**" button in the sidebar of your Coolify dashboard.

Click the upgrade button to start the update process.

### Set Update Frequency

You can also choose how often Coolify checks for updates by adjusting the settings (daily, weekly, etc.).

::: info Tip:
This method is perfect if you want to review update details or test the upgrade before applying it.
:::

## 3. Manual Upgrade

For those who prefer full control, you can upgrade Coolify manually.

### How to do this?

Open your server's terminal and run the command below:

```sh
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

To upgrade to a specific version, run the following command in your terminal:

```sh
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash -s 4.0.0-beta.400
```

Replace `4.0.0-beta.400` with the version number you want to upgrade to.

### How it works?

This command runs the official [Coolify installation script](https://github.com/coollabsio/coolify/blob/main/scripts/install.sh). The script checks the [CDN](https://cdn.coollabs.io/coolify/versions.json) for the latest version and updates your Coolify Instance.

::: success Tip
In the Automatic and Semi-Automatic methods, Coolify runs the installation script automatically in the background.

In the Manual upgrade method, you run the script yourself.
:::