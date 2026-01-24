---
title: Create new buckets · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/buckets/create-buckets/index.md
source: llms
fetched_at: 2026-01-24T15:21:11.785411822-03:00
rendered_js: false
word_count: 229
summary: This document explains how to create, list, and delete Cloudflare R2 buckets using the Wrangler CLI and provides essential information on bucket naming conventions and access management.
tags:
    - cloudflare-r2
    - wrangler-cli
    - bucket-management
    - object-storage
    - cloud-storage
category: guide
---

You can create a bucket from the Cloudflare dashboard or using Wrangler.

Note

Wrangler is [a command-line tool](https://developers.cloudflare.com/workers/wrangler/install-and-update/) for building with Cloudflare's developer products, including R2.

The R2 support in Wrangler allows you to manage buckets and perform basic operations against objects in your buckets. For more advanced use-cases, including bulk uploads or mirroring files from legacy object storage providers, we recommend [rclone](https://developers.cloudflare.com/r2/examples/rclone/) or an [S3-compatible](https://developers.cloudflare.com/r2/api/s3/) tool of your choice.

## Bucket-Level Operations

Create a bucket with the [`r2 bucket create`](https://developers.cloudflare.com/workers/wrangler/commands/#r2-bucket-create) command:

```sh
wrangler r2 bucket create your-bucket-name
```

Note

* Bucket names can only contain lowercase letters (a-z), numbers (0-9), and hyphens (-).
* Bucket names cannot begin or end with a hyphen.
* Bucket names can only be between 3-63 characters in length.

The placeholder text is only for the example.

List buckets in the current account with the [`r2 bucket list`](https://developers.cloudflare.com/workers/wrangler/commands/#r2-bucket-list) command:

```sh
wrangler r2 bucket list
```

Delete a bucket with the [`r2 bucket delete`](https://developers.cloudflare.com/workers/wrangler/commands/#r2-bucket-delete) command. Note that the bucket must be empty and all objects must be deleted.

```sh
wrangler r2 bucket delete BUCKET_TO_DELETE
```

## Notes

* Bucket names and buckets are not public by default. To allow public access to a bucket, refer to [Public buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/).
* For information on controlling access to your R2 bucket with Cloudflare Access, refer to [Protect an R2 Bucket with Cloudflare Access](https://developers.cloudflare.com/r2/tutorials/cloudflare-access/).
* Invalid (unauthorized) access attempts to private buckets do not incur R2 operations charges against that bucket. Refer to the [R2 pricing FAQ](https://developers.cloudflare.com/r2/pricing/#frequently-asked-questions) to understand what operations are billed vs. not billed.