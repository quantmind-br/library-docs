---
title: Backups | Dokploy
url: https://docs.dokploy.com/docs/core/backups
source: crawler
fetched_at: 2026-02-14T14:18:06.126117-03:00
rendered_js: true
word_count: 296
summary: This document provides step-by-step instructions for creating, scheduling, and restoring full system backups for Dokploy applications using S3 destinations.
tags:
    - dokploy
    - backup-and-restore
    - s3-storage
    - postgresql
    - disaster-recovery
    - server-maintenance
category: guide
---

Learn how to create and restore backups of your Dokploy applications and services.

Dokploy provides a comprehensive backup and restore system that saves your entire Dokploy file system and database to ensure your data is safe and recoverable.

Before using the backup feature, you need to have an S3 destination configured in your system. This is where your backups will be stored.

To create a backup:

1. Navigate to Web Server → Backups
2. Select "Create Backup"
3. Choose your S3 destination
4. Configure the backup schedule using cron syntax (optional)

When a backup is created, Dokploy will:

- Back up the PostgreSQL database (`dokploy-postgres`)
- Save the Dokploy file system (`/etc/dokploy`)
- Combine and compress both into a single backup file (.zip)
- Upload the backup to your specified S3 destination

To restore a backup:

1. Navigate to Web Server → Backups
2. Select "Restore Backup"
3. Choose the S3 destination containing your backup
4. Browse and select the backup file you want to restore
5. Review the summary of files to be restored

During restoration, Dokploy will:

- Clear the existing `/etc/dokploy` directory and replace it with the backup contents
- Drop the existing `dokploy-postgres` database
- Disconnect current database users
- Restore the database from the backup

After restoration is complete, you may need to log in again. If necessary, you can restart Traefik to ensure all services are properly configured.

## [Post-Restoration Steps](#post-restoration-steps)

After restoring a backup, especially if you're restoring to a different server, consider the following:

1. If your server IP has changed:
   
   - Update the IP address in Web Server → Server → Update IP
   - Reconfigure Git providers if they were set up using IP addresses
   - Update your DNS records to point to the new IP
   - Recreate Traefik.me domains if you're using them
2. If you're using domain names instead of IPs for Git providers, no additional configuration is needed.