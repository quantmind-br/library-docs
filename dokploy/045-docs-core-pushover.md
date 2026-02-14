---
title: Pushover | Dokploy
url: https://docs.dokploy.com/docs/core/pushover
source: crawler
fetched_at: 2026-02-14T14:18:33.543405-03:00
rendered_js: true
word_count: 159
summary: This document explains how to configure Pushover notifications in Dokploy to receive alerts for application events, detailing the required credentials and priority settings.
tags:
    - pushover
    - notifications
    - dokploy
    - configuration
    - alerting
category: configuration
---

Notifications

Configure Pushover notifications for your applications.

Pushover notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

To start receiving Pushover notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **User Key**: Enter your Pushover user key. eg. `ub3de9kl2q...`
- **API Token**: Enter your Pushover application API token. eg. `a3d9k2q7m4...`
- **Priority**: Enter the priority of the notification (-2 to 2, default: 0).
  
  - `-2`: Lowest priority (no sound/vibration)
  - `-1`: Low priority (no sound/vibration)
  - `0`: Normal priority (default)
  - `1`: High priority (bypasses quiet hours)
  - `2`: Emergency priority (requires acknowledgment)

For emergency priority (2), you must also provide:

- **Retry**: How often (in seconds) Pushover will retry the notification. Minimum 30 seconds.
- **Expire**: How long (in seconds) to keep retrying. Maximum 10800 seconds (3 hours).

To setup the Pushover notifications, you can read the [Pushover Documentation](https://pushover.net/api).