---
title: Migration Strategies · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/data-migration/migration-strategies/index.md
source: llms
fetched_at: 2026-01-24T15:21:07.387426214-03:00
rendered_js: false
word_count: 336
summary: This document explains how to migrate data to Cloudflare R2 using Super Slurper and Sippy, covering strategies for minimal downtime and performance optimization through parallel migration jobs.
tags:
    - cloudflare-r2
    - data-migration
    - super-slurper
    - sippy
    - cloud-storage
    - performance-optimization
category: guide
---

You can use a combination of Super Slurper and Sippy to effectively migrate all objects with minimal downtime.

### When the source bucket is actively being read from / written to

1. Enable Sippy and start using the R2 bucket in your application.

   * This copies objects from your previous bucket into the R2 bucket on demand when they are requested by the application.
   * New uploads will go to the R2 bucket.

2. Use Super Slurper to trigger a one-off migration to copy the remaining objects into the R2 bucket.
   * In the **Destination R2 bucket** > **Overwrite files?**, select "Skip existing".

### When the source bucket is not being read often

1. Use Super Slurper to copy all objects to the R2 bucket.
   * Note that Super Slurper may skip some objects if they are uploaded after it lists the objects to be copied.

2. Enable Sippy on your R2 bucket, then start using the R2 bucket in your application.

   * New uploads will go to the R2 bucket.
   * Objects which were uploaded while Super Slurper was copying the objects will be copied on-demand (by Sippy) when they are requested by the application.

### Optimizing your Slurper data migration performance

For an account, you can run three concurrent Slurper migration jobs at any given time, and each Slurper migration job can process a set amount of requests per second.

To increase overall throughput and reliability, we recommend splitting your migration into smaller, concurrent jobs using the prefix (or bucket subpath) option.

When creating a migration job:

1. Go to the **Source bucket** step.
2. Under **Define rules**, in **Bucket subpath**, specify subpaths to divide your data by prefix.
3. Complete the data migration set up.

For example, suppose your source bucket contains:

You can create separate jobs with prefixes such as:

* `/photos/2024` to migrate all 2024 files
* `/photos/202` to migrate all files from 2023 and 2024

Each prefix runs as an independent migration job, allowing Slurper to transfer data in parallel. This improves total transfer speed and ensures that a failure in one job does not interrupt the others.