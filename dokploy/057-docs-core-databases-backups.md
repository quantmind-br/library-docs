---
title: Backups | Dokploy
url: https://docs.dokploy.com/docs/core/databases/backups
source: crawler
fetched_at: 2026-02-14T14:18:23.88383-03:00
rendered_js: true
word_count: 183
summary: This document explains how to configure, schedule, and test automated database backups in Dokploy using S3 buckets for storage.
tags:
    - dokploy
    - database-backups
    - s3-storage
    - backup-automation
    - cron-scheduling
    - data-recovery
category: guide
---

Learn how to schedule and manage backups for your databases in Dokploy, with options for storage in S3 buckets.

Dokploy provides an integrated solution for backing up your databases, ensuring data safety and recovery capabilities.

To configure database backups, navigate to the `Backup` tab within your Dokploy dashboard. Here’s what you’ll need to set up:

- **Select Destination S3 Bucket**: Specify where your backups will be stored. Buckets can be configured in the `/dashboard/settings/destinations` route.
- **Database Name**: Enter the name of the database you want to backup.
- **Schedule Cron**: Define the schedule for your backups using cron syntax.
- **Prefix**: Choose a prefix under which backups will be stored in your bucket.
- **Enabled**: Toggle whether backups are active. The default setting is enabled.

### [Testing Your Backup Configuration](#testing-your-backup-configuration)

To ensure your backup settings are correctly configured:

1. Click the `Test` button.
2. This will initiate a test backup to the S3 bucket you selected.
3. Check the bucket to see the result of the test backup.

This feature provides peace of mind by verifying that your backup process is set up correctly before relying on it for operational backups.