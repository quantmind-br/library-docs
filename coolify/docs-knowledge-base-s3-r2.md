---
title: Cloudflare R2
url: https://coolify.io/docs/knowledge-base/s3/r2.md
source: llms
fetched_at: 2026-02-17T14:41:11.079873-03:00
rendered_js: false
word_count: 94
summary: This document explains how to configure Cloudflare R2 as an S3-compatible storage provider for backups within the Coolify platform.
tags:
    - cloudflare-r2
    - s3-storage
    - backups
    - coolify
    - object-storage
category: guide
---

# Cloudflare R2

Cloudflare R2 is an S3 compatible storage. You can use it with Coolify to store your backups.

# Configuration

1. You need to create a bucket first in the Cloudflare R2 dashboard.
2. Then you need to create a R2 API token with `Object Read & Write` permission.
3. You can find the S3 client credentials when the token is created.
   ::: success Tip
   You will need the `Access Key ID`, `Secret Access Key` and the `S3 endpoint` from this view. Save them.
   :::
4. You can use the details from the previous step to configure Coolify.