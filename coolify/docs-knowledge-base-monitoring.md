---
title: Monitoring
url: https://coolify.io/docs/knowledge-base/monitoring.md
source: llms
fetched_at: 2026-02-17T14:40:05.890743-03:00
rendered_js: false
word_count: 59
summary: This document explains Coolify's integrated monitoring system, which tracks resource health, container statuses, and backups to automate cleanup and send notifications.
tags:
    - coolify
    - monitoring
    - disk-usage
    - container-status
    - backup-monitoring
    - resource-management
category: concept
---

# Monitoring

Coolify has a built-in monitoring system, which can be used to monitor your resources and send notifications to your team if something goes wrong.

Currently Coolify monitors the following resources:

* Disk usage - If your disk usage is above the configured threshold, it does an automatic cleanup.
* If any of your containers are stopped or restarted.
* Backup status.