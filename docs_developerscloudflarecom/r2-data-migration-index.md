---
title: Data migration · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/data-migration/index.md
source: llms
fetched_at: 2026-01-24T15:21:03.877930541-03:00
rendered_js: false
word_count: 111
summary: This document provides an overview of the tools and strategies available for migrating data from other cloud providers to Cloudflare R2, highlighting both one-time and incremental transfer options.
tags:
    - cloudflare-r2
    - data-migration
    - super-slurper
    - sippy
    - cloud-storage
category: reference
---

Quickly and easily migrate data from other cloud providers to R2. Explore each option further by navigating to their respective documentation page.

| Name | Description | When to use |
| - | - | - |
| [Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) | Quickly migrate large amounts of data from other cloud providers to R2. | * For one-time, comprehensive transfers. |
| [Sippy](https://developers.cloudflare.com/r2/data-migration/sippy/) | Incremental data migration, populating your R2 bucket as objects are requested. | - For gradual migration that avoids upfront egress fees.

- To start serving frequently accessed objects from R2 without a full migration. |

For information on how to leverage these tools effectively, refer to [Migration Strategies](https://developers.cloudflare.com/r2/data-migration/migration-strategies/)