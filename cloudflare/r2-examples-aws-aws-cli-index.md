---
title: aws CLI · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/examples/aws/aws-cli/index.md
source: llms
fetched_at: 2026-01-24T15:22:00.564251185-03:00
rendered_js: false
word_count: 112
summary: This document provides instructions on how to configure the AWS CLI for use with Cloudflare R2 and demonstrates how to manage buckets and generate presigned URLs.
tags:
    - cloudflare-r2
    - aws-cli
    - s3-api
    - configuration
    - object-storage
    - presigned-urls
category: tutorial
---

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.



With the [`aws`](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) CLI installed, you may run [`aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) to configure a new profile. You will be prompted with a series of questions for the new profile's details.

```shell
aws configure
```

```sh
AWS Access Key ID [None]: <ACCESS_KEY_ID>
AWS Secret Access Key [None]: <SECRET_ACCESS_KEY>
Default region name [None]: auto
Default output format [None]: json
```

The `region` value can be set to `auto` since it is required by the SDK but not used by R2.

You may then use the `aws` CLI for any of your normal workflows.

```sh
# Provide your Cloudflare account ID
aws s3api list-buckets --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com
# {
#     "Buckets": [
#         {
#             "Name": "my-bucket",
#             "CreationDate": "2022-05-18T17:19:59.645000+00:00"
#         }
#     ],
#     "Owner": {
#         "DisplayName": "134a5a2c0ba47b38eada4b9c8ead10b6",
#         "ID": "134a5a2c0ba47b38eada4b9c8ead10b6"
#     }
# }


aws s3api list-objects-v2 --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com --bucket my-bucket
# {
#     "Contents": [
#         {
#             "Key": "ferriswasm.png",
#             "LastModified": "2022-05-18T17:20:21.670000+00:00",
#             "ETag": "\"eb2b891dc67b81755d2b726d9110af16\"",
#             "Size": 87671,
#             "StorageClass": "STANDARD"
#         }
#     ]
# }
```

## Generate presigned URLs

You can also generate presigned links which allow you to share public access to a file temporarily.

```sh
# You can pass the --expires-in flag to determine how long the presigned link is valid.
aws s3 presign --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com  s3://my-bucket/ferriswasm.png --expires-in 3600
# https://<ACCOUNT_ID>.r2.cloudflarestorage.com/my-bucket/ferriswasm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<credential>&X-Amz-Date=<timestamp>&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=<signature>
```