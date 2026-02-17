---
title: Cap
url: https://coolify.io/docs/services/cap.md
source: llms
fetched_at: 2026-02-17T14:42:45.378389-03:00
rendered_js: false
word_count: 309
summary: This document provides instructions for self-hosting Cap, including storage configuration for S3 or MinIO, email setup via Resend, and database commands to manage user limits.
tags:
    - cap
    - self-hosting
    - s3-storage
    - minio
    - deployment
    - configuration
    - open-source
category: guide
---

## What is Cap?

Cap is the open source alternative to Loom. Lightweight, powerful, and cross-platform. Record and share in seconds.

## How to self-host

There are two storage options: you can store the video data on a remote storage service like S3 or R2, or you can choose the less recommended option of storing it directly on the local VPS (or another VPS) via a MinIO service.

### Option 1: Remote S3-compatible storage (AWS S3, Cloudflare R2, etc.)

Set these environment variables:

* `CAP_AWS_ACCESS_KEY`: Your S3/R2 access key
* `CAP_AWS_SECRET_KEY`: Your S3/R2 secret key
* `CAP_AWS_BUCKET`: Your S3/R2 bucket name
* `CAP_AWS_REGION`: Your S3/R2 region (e.g., us-east-1, auto for R2)
* `CAP_AWS_ENDPOINT`: Your S3/R2 endpoint URL
* `S3_PUBLIC_ENDPOINT`: Public endpoint for your bucket (same as CAP\_AWS\_ENDPOINT for most cases)
* `S3_INTERNAL_ENDPOINT`: Internal endpoint (same as CAP\_AWS\_ENDPOINT for most cases)
* `S3_PATH_STYLE`: true for R2/most S3-compatible, false for AWS S3 virtual-hosted style

### Option 2: Local MinIO storage

Deploy MinIO as a separate service in the same network and set:

* `CAP_AWS_ACCESS_KEY`: MinIO root user
* `CAP_AWS_SECRET_KEY`: MinIO root password
* `CAP_AWS_BUCKET`: Your bucket name (e.g., capso)
* `CAP_AWS_REGION`: us-east-1 (or any region)
* `CAP_AWS_ENDPOINT`: http://minio:9000 (internal MinIO endpoint)
* `S3_PUBLIC_ENDPOINT`: http://your-minio-domain:9000 (public MinIO endpoint)
* `S3_INTERNAL_ENDPOINT`: http://minio:9000 (internal MinIO endpoint)
* `S3_PATH_STYLE`: true

## Email Login Links

If the `RESEND_API_KEY` and `RESEND_FROM_DOMAIN` environment variables are not set, login links will be written to the server logs. To send login links via email, you'll need to configure [Resend](https://resend.com):

1. Create an account at [Resend](https://resend.com)
2. Connect a domain and set it as `RESEND_FROM_DOMAIN`
3. Generate an API key and set it as `RESEND_API_KEY`

## How to unlock limits (organization seats and recordings)

1. Open the terminal of the MySQL service
2. Connect to the database: `mysql -u root -p planetscale` and use the `MYSQL_ROOT_PASSWORD` when prompted
3. Run the SQL command below, replacing `your-user-id` with your actual user ID
   ```sql
   UPDATE users SET inviteQuota = 100, stripeSubscriptionId = '12345', subscriptionStatus = 'active' WHERE id = 'your-user-id';
   ```
4. You can verify the changes by running the following command:
   ```sql
   SELECT * FROM users WHERE id = 'your-user-id';
   ```

## Screenshots

## Links

* [The official website ›](https://cap.so/)
* [GitHub ›](https://github.com/CapSoftware/Cap)