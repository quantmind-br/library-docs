---
title: Delete objects · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/objects/delete-objects/index.md
source: llms
fetched_at: 2026-01-24T15:21:22.762024751-03:00
rendered_js: false
word_count: 164
summary: This document provides instructions on how to delete objects from Cloudflare R2 storage using the dashboard, Workers API, S3-compatible APIs, and the Wrangler command-line tool.
tags:
    - cloudflare-r2
    - object-storage
    - data-management
    - workers-api
    - s3-api
    - wrangler-cli
    - developer-tools
category: guide
---

You can delete objects from R2 using the dashboard, Workers API, S3 API, or command-line tools.

## Delete via dashboard

1. In the Cloudflare dashboard, go to the **R2 object storage** page.

   [Go to **Overview**](https://dash.cloudflare.com/?to=/:account/r2/overview)

2. Locate and select your bucket.

3. Locate the object you want to delete. You can select multiple objects to delete at one time.

4. Select your objects and select **Delete**.

5. Confirm your choice by selecting **Delete**.

## Delete via Workers API

Use R2 [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) in Workers to delete objects:

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    await env.MY_BUCKET.delete("image.png");
    return new Response("Deleted");
  },
} satisfies ExportedHandler<Env>;
```

For complete documentation, refer to [Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/).

## Delete via S3 API

Use S3-compatible SDKs to delete objects. You'll need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [R2 API token](https://developers.cloudflare.com/r2/api/tokens/).

* JavaScript

  ```ts
  import { S3Client, DeleteObjectCommand } from "@aws-sdk/client-s3";


  const S3 = new S3Client({
    region: "auto", // Required by SDK but not used by R2
    // Provide your Cloudflare account ID
    endpoint: `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`,
    // Retrieve your S3 API credentials for your R2 bucket via API tokens (see: https://developers.cloudflare.com/r2/api/tokens)
    credentials: {
      accessKeyId: '<ACCESS_KEY_ID>',
      secretAccessKey: '<SECRET_ACCESS_KEY>',
    },
  });


  await S3.send(
    new DeleteObjectCommand({
      Bucket: "my-bucket",
      Key: "image.png",
    }),
  );
  ```

* Python

  ```python
  import boto3


  s3 = boto3.client(
    service_name="s3",
    # Provide your Cloudflare account ID
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    # Retrieve your S3 API credentials for your R2 bucket via API tokens (see: https://developers.cloudflare.com/r2/api/tokens)
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto", # Required by SDK but not used by R2
  )


  s3.delete_object(Bucket="my-bucket", Key="image.png")
  ```

For complete S3 API documentation, refer to [S3 API](https://developers.cloudflare.com/r2/api/s3/api/).

## Delete via Wrangler

Warning

Deleting objects from a bucket is irreversible.

Use [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) to delete objects. Run the [`r2 object delete` command](https://developers.cloudflare.com/workers/wrangler/commands/#r2-object-delete):

```sh
wrangler r2 object delete test-bucket/image.png
```