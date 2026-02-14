---
title: Cloudflare R2 | Dokploy
url: https://docs.dokploy.com/docs/core/cloudflare-r2
source: crawler
fetched_at: 2026-02-14T14:18:34.329622-03:00
rendered_js: true
word_count: 184
summary: This document provides a step-by-step guide for configuring Cloudflare R2 as an S3-compatible storage destination for backups, including bucket creation and API credential setup.
tags:
    - cloudflare-r2
    - s3-storage
    - backup-configuration
    - object-storage
    - api-tokens
    - dokploy
category: configuration
---

S3 Destinations

Configure R2 buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

Cloudflare is a popular choice for hosting static assets, such as images, videos, and documents. It is a cloud-based service that allows you to store and retrieve data from anywhere in the world. This is a great option for storing backups, as it is easy to set up and manage.

1. Go to `R2 Object Storage`, and create a new bucket with any name you want by clicking `Create bucket` button.
2. Go back to `R2 Object Storage`, and select `Manage API tokens` from the select box.
3. Create a new `User API Token`, and give it a meaninful name.
4. Set `Object Read & Write` Permission.
5. (Optional) Set Specify bucket, by default it will include all buckets.
6. Create the token.

Now copy the following variables:

(from) Cloudflare(to) DokployExample value`Access Key ID``Access Key Id``f3811c6d27415a9s6cv943b6743ad784``Secret Access Key``Secret Access Key``aa55ee40b4049e93b7252bf698408cc22a3c2856d2530s7c1cb7670e318f15e58``Region``Region``WNAM, ENAM, etc` it will depend on the region you are using.`Endpoint``Endpoint``https://8ah554705io7842d54c499fbee1156c1c.r2.cloudflarestorage.com``Bucket``Bucket``dokploy-backups` use the name of the bucket you created.

Test the connection and you should see a success message.