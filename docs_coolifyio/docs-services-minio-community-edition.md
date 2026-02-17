---
title: MinIO Community Edition
url: https://coolify.io/docs/services/minio-community-edition.md
source: llms
fetched_at: 2026-02-17T14:46:05.530008-03:00
rendered_js: false
word_count: 126
summary: This document provides an overview of MinIO Community Edition, a high-performance S3-compatible object storage system, including its distribution via Coolify and basic troubleshooting for authentication.
tags:
    - minio
    - object-storage
    - s3-api
    - open-source
    - coolify
    - cloud-native
category: reference
---

# MinIO Community Edition

![MinIO](/images/services/minio-logo.svg)

::: info NOTE
MinIO team stopped providing pre-built Docker images for new releases, [this repository](https://github.com/coollabsio/minio) by Coolify team automatically builds and publishes them to both GitHub Container Registry and Docker Hub based on MinIO official codebase on [GitHub](https://github.com/minio/minio?utm_source=coolify.io)

:::

## What is MinIO?

MinIO is a high-performance, distributed object storage system compatible with Amazon S3 APIs. It is software-defined, runs on industry-standard hardware, and is 100% open source under the AGPL v3.0 license. MinIO delivers high-performance, Kubernetes-native object storage that is designed for large scale AI/ML, data lake and database workloads.

## Links

* [The official website](https://min.io?utm_source=coolify.io)
* [MinIO GitHub](https://github.com/minio/minio?utm_source=coolify.io)
* [Community Edition Github](https://github.com/coollabsio/minio?utm_source=coolify.io)

## FAQ

### Invalid login credentials

You need to run MinIO on `https` (not self-signed) to avoid this issue. MinIO doesn't support http based authentication.