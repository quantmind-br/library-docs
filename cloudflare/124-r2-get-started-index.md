---
title: Getting started guide · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/get-started/index.md
source: llms
fetched_at: 2026-01-24T15:20:53.926620265-03:00
rendered_js: false
word_count: 191
summary: This document provides a step-by-step guide to getting started with Cloudflare R2 storage, covering tool installation, bucket creation, and initial object uploads.
tags:
    - cloudflare-r2
    - object-storage
    - wrangler-cli
    - bucket-management
    - cloud-storage
category: tutorial
---

Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.

## 1. Install and authenticate Wrangler

Note

Before you create your first bucket, you must purchase R2 from the Cloudflare dashboard.

1. [Install Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) within your project using npm and Node.js or Yarn.

* npm

  ```sh
  npm i -D wrangler@latest
  ```

* yarn

  ```sh
  yarn add -D wrangler@latest
  ```

* pnpm

  ```sh
  pnpm add -D wrangler@latest
  ```

1. [Authenticate Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/#login) to enable deployments to Cloudflare. When Wrangler automatically opens your browser to display Cloudflare's consent screen, select **Allow** to send the API Token to Wrangler.

```txt
wrangler login
```

## 2. Create a bucket

To create a new R2 bucket from the Cloudflare dashboard:

1. In the Cloudflare dashboard, go to the **R2 object storage** page.

   [Go to **Overview**](https://dash.cloudflare.com/?to=/:account/r2/overview)

2. Select **Create bucket**.

3. Enter a name for the bucket and select **Create bucket**.

## 3. Upload your first object

1. From the **R2** page in the dashboard, locate and select your bucket.
2. Select **Upload**.
3. Choose to either drag and drop your file into the upload area or **select from computer**.

You will receive a confirmation message after a successful upload.

## Bucket access options

Cloudflare provides multiple ways for developers to access their R2 buckets:

* [R2 Workers Binding API](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/)
* [S3 API compatibility](https://developers.cloudflare.com/r2/api/s3/api/)
* [Public buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/)