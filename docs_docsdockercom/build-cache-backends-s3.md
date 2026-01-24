---
title: Amazon S3 cache
url: https://docs.docker.com/build/cache/backends/s3/
source: llms
fetched_at: 2026-01-24T14:16:09.866230788-03:00
rendered_js: false
word_count: 218
summary: This document explains how to configure and use Amazon S3 or S3-compatible services as a remote storage backend for Docker build cache.
tags:
    - docker-build
    - buildx
    - s3-cache
    - amazon-s3
    - build-cache
    - cache-backend
category: reference
---

Availability: Experimental

The `s3` cache storage uploads your resulting build cache to [Amazon S3 file storage service](https://aws.amazon.com/s3/) or other S3-compatible services, such as [MinIO](https://min.io/).

This cache storage backend is not supported with the default `docker` driver. To use this feature, create a new builder using a different driver. See [Build drivers](https://docs.docker.com/build/builders/drivers/) for more information.

## [Synopsis](#synopsis)

```
$ docker buildx build --push -t <user>/<image> \
  --cache-to type=s3,region=<region>,bucket=<bucket>,name=<cache-image>[,parameters...] \
  --cache-from type=s3,region=<region>,bucket=<bucket>,name=<cache-image> .
```

The following table describes the available CSV parameters that you can pass to `--cache-to` and `--cache-from`.

NameOptionTypeDefaultDescription`region``cache-to`,`cache-from`StringRequired. Geographic location.`bucket``cache-to`,`cache-from`StringRequired. Name of the S3 bucket.`name``cache-to`,`cache-from`String`buildkit`Name of the cache image.`endpoint_url``cache-to`,`cache-from`StringEndpoint of the S3 bucket.`prefix``cache-to`,`cache-from`StringPrefix to prepend to all filenames.`blobs_prefix``cache-to`,`cache-from`String`blobs/`Prefix to prepend to blob filenames.`upload_parallelism``cache-to`Integer`4`Number of parallel layer uploads.`touch_refresh``cache-to`Time`24h`Interval for updating the timestamp of unchanged cache layers.`manifests_prefix``cache-to`,`cache-from`String`manifests/`Prefix to prepend to manifest filenames.`use_path_style``cache-to`,`cache-from`Boolean`false`When `true`, uses `bucket` in the URL instead of hostname.`access_key_id``cache-to`,`cache-from`StringSee [authentication](#authentication).`secret_access_key``cache-to`,`cache-from`StringSee [authentication](#authentication).`session_token``cache-to`,`cache-from`StringSee [authentication](#authentication).`mode``cache-to``min`,`max``min`Cache layers to export, see [cache mode](https://docs.docker.com/build/cache/backends/#cache-mode).`ignore-error``cache-to`Boolean`false`Ignore errors caused by failed cache exports.

## [Authentication](#authentication)

Buildx can reuse existing AWS credentials, configured either using a credentials file or environment variables, for pushing and pulling cache to S3. Alternatively, you can use the `access_key_id`, `secret_access_key`, and `session_token` attributes to specify credentials directly on the CLI.

Refer to [AWS Go SDK, Specifying Credentials](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-gosdk.html#specifying-credentials) for details about authentication using environment variables and credentials file.

## [Further reading](#further-reading)

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `s3` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#s3-cache-experimental).