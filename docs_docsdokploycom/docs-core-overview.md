---
title: Overview | Dokploy
url: https://docs.dokploy.com/docs/core/overview
source: crawler
fetched_at: 2026-02-14T14:13:17.56678-03:00
rendered_js: true
word_count: 206
summary: This document explains how to configure notifications in Dokploy, detailing the specific application events that trigger alerts and the various supported messaging platforms.
tags:
    - dokploy
    - notifications
    - alerting
    - slack-integration
    - discord-integration
    - webhooks
    - event-triggers
category: guide
---

Notifications

Configure general notifications for your applications and services.

Dokploy offers multiple notification options to notify you about important events in your applications and services.

You can select which actions trigger notifications:

1. **App Deploy**: Trigger the action when an app is deployed.
2. **App Build Error**: Trigger the action when the build fails.
3. **Database Backup**: Trigger the action when a database backup is created.
4. **Volume Backup**: Trigger the action when a volume backup is created.
5. **Docker Cleanup**: Trigger the action when the docker cleanup is performed.
6. **Dokploy Restart**: Trigger the action when Dokploy is restarted.

Dokploy supports the following notification providers:

1. **Slack**: Slack is a platform for team communication and collaboration.
2. **Telegram**: Telegram is a messaging platform that allows users to send and receive messages.
3. **Discord**: Discord is generally used for communication between users in a chat or voice channel.
4. **Lark**: Lark is a collaboration platform that provides messaging and team communication features.
5. **Email**: Email is a popular method for sending messages to a group of recipients.
6. **Gotify**: Gotify is a self-hosted push notification service.
7. **Ntfy**: Ntfy is a simple HTTP-based pub-sub notification service.
8. **Pushover**: Pushover is a service for sending real-time notifications to Android, iOS, and desktop devices.
9. **Webhook**: Webhook is a generic webhook notification service.