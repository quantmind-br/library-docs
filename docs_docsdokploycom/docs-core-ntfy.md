---
title: Ntfy | Dokploy
url: https://docs.dokploy.com/docs/core/ntfy
source: crawler
fetched_at: 2026-02-14T14:13:38.522616-03:00
rendered_js: true
word_count: 112
summary: This document provides instructions for configuring ntfy notifications within Dokploy to receive alerts and updates about system events.
tags:
    - dokploy
    - ntfy
    - notifications
    - configuration
    - alerting
category: configuration
---

Notifications

Configure ntfy notifications for your applications.

Ntfy notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

For start receiving ntfy notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Server URL**: Enter the ntfy server URL. eg. `https://ntfy.example.com`
- **Access Token**: Enter the ntfy token. You can create one under `https://ntfy.example.com/account`
- **Topic**: Enter the topic you want the notifications to be received.
- **Priority**: Enter the priority of the notification, default is `3` (1-5).

To Setup the ntfy notifications, you can read the [Notify Documentation](https://docs.ntfy.sh/).