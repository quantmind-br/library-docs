---
title: Upload objects · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/objects/upload-objects/index.md
source: llms
fetched_at: 2026-01-24T15:21:28.450951536-03:00
rendered_js: false
word_count: 373
summary: This document outlines the various methods for uploading objects to Cloudflare R2, including via the dashboard, Workers API, S3-compatible SDKs, and command-line tools like Wrangler and rclone.
tags:
    - cloudflare-r2
    - object-storage
    - s3-api
    - workers-api
    - wrangler
    - rclone
    - presigned-urls
    - file-upload
category: guide
---

There are several ways to upload objects to R2:

1. Using the [S3 API](https://developers.cloudflare.com/r2/api/s3/api/), which is supported by a wide range of tools and libraries (recommended)
2. Directly from within a Worker using R2's [Workers API](https://developers.cloudflare.com/r2/api/workers/)
3. Using the [Cloudflare dashboard](https://dash.cloudflare.com/?to=/:account/r2/overview)
4. Using the [Wrangler](https://developers.cloudflare.com/r2/reference/wrangler-commands/) command-line (`wrangler r2`)

## Upload via dashboard

To upload objects to your bucket from the Cloudflare dashboard:

1. In the Cloudflare dashboard, go to the **R2 object storage** page.

   [Go to **Overview**](https://dash.cloudflare.com/?to=/:account/r2/overview)

2. Select your bucket.

3. Select **Upload**.

4. Drag and drop your file into the upload area or **select from computer**.

You will receive a confirmation message after a successful upload.

## Upload via Workers API

Use R2 [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) in Workers to upload objects server-side:

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    await env.MY_BUCKET.put("image.png", request.body);
    return new Response("Uploaded");
  },
} satisfies ExportedHandler<Env>;
```

For complete documentation, refer to [Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/).

## Upload via S3 API

Use S3-compatible SDKs to upload objects. You'll need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [R2 API token](https://developers.cloudflare.com/r2/api/tokens/).

* JavaScript

  ```ts
  import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";


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
    new PutObjectCommand({
      Bucket: "my-bucket",
      Key: "image.png",
      Body: fileContent,
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


  s3.put_object(Bucket="my-bucket", Key="image.png", Body=file_content)
  ```

Refer to R2's [S3 API documentation](https://developers.cloudflare.com/r2/api/s3/api/) for all S3 API methods.

### Presigned URLs

For client-side uploads where users upload directly to R2, use presigned URLs. Your server generates a temporary upload URL that clients can use without exposing your API credentials.

1. Your application generates a presigned PUT URL using an S3 SDK
2. Send the URL to your client
3. Client uploads directly to R2 using the presigned URL

For details on generating and using presigned URLs, refer to [Presigned URLs](https://developers.cloudflare.com/r2/api/s3/presigned-urls/).

## Upload via CLI

### Rclone

[Rclone](https://rclone.org/) is a command-line tool for managing files on cloud storage. Rclone works well for uploading multiple files from your local machine or copying data from other cloud storage providers.

To use rclone, install it onto your machine using their official documentation - [Install rclone](https://rclone.org/install/).

Upload files with the `rclone copy` command:

```sh
# Upload a single file
rclone copy /path/to/local/image.png r2:bucket_name


# Upload everything in a directory
rclone copy /path/to/local/folder r2:bucket_name
```

Verify the upload with `rclone ls`:

```sh
rclone ls r2:bucket_name
```

For more information, refer to our [rclone example](https://developers.cloudflare.com/r2/examples/rclone/).

### Wrangler

Note

Wrangler supports uploading files up to 315MB and only allows one object at a time. For large files or bulk uploads, use [rclone](https://developers.cloudflare.com/r2/examples/rclone/) or another [S3-compatible](https://developers.cloudflare.com/r2/api/s3/) tool.

Use [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) to upload objects. Run the [`r2 object put` command](https://developers.cloudflare.com/workers/wrangler/commands/#r2-object-put):

```sh
wrangler r2 object put test-bucket/image.png --file=image.png
```

You can set the `Content-Type` (MIME type), `Content-Disposition`, `Cache-Control` and other HTTP header metadata through optional flags.