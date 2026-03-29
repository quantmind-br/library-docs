---
title: Registry cache
url: https://docs.docker.com/build/cache/backends/registry/
source: llms
fetched_at: 2026-01-24T14:16:00.378544573-03:00
rendered_js: false
word_count: 334
summary: This document explains the registry cache storage backend for Docker builds, detailing its configuration parameters and advantages over inline caching for multi-stage builds.
tags:
    - docker-build
    - buildx
    - cache-storage
    - registry-backend
    - build-optimization
category: reference
---

Table of contents

* * *

The `registry` cache storage can be thought of as an extension to the `inline` cache. Unlike the `inline` cache, the `registry` cache is entirely separate from the image, which allows for more flexible usage - `registry`-backed cache can do everything that the inline cache can do, and more:

- Allows for separating the cache and resulting image artifacts so that you can distribute your final image without the cache inside.
- It can efficiently cache multi-stage builds in `max` mode, instead of only the final stage.
- It works with other exporters for more flexibility, instead of only the `image` exporter.

This cache storage backend is not supported with the default `docker` driver. To use this feature, create a new builder using a different driver. See [Build drivers](https://docs.docker.com/build/builders/drivers/) for more information.

## [Synopsis](#synopsis)

Unlike the simpler `inline` cache, the `registry` cache supports several configuration parameters:

```
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=registry,ref=<registry>/<cache-image>[,parameters...] \
  --cache-from type=registry,ref=<registry>/<cache-image> .
```

The following table describes the available CSV parameters that you can pass to `--cache-to` and `--cache-from`.

NameOptionTypeDefaultDescription`ref``cache-to`,`cache-from`StringFull name of the cache image to import.`mode``cache-to``min`,`max``min`Cache layers to export, see [cache mode](https://docs.docker.com/build/cache/backends/#cache-mode).`oci-mediatypes``cache-to``true`,`false``true`Use OCI media types in exported manifests, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).`image-manifest``cache-to``true`,`false``true`When using OCI media types, generate an image manifest instead of an image index for the cache image, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).`compression``cache-to``gzip`,`estargz`,`zstd``gzip`Compression type, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).`compression-level``cache-to``0..22`Compression level, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).`force-compression``cache-to``true`,`false``false`Forcibly apply compression, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).`ignore-error``cache-to`Boolean`false`Ignore errors caused by failed cache exports.

You can choose any valid value for `ref`, as long as it's not the same as the target location that you push your image to. You might choose different tags (e.g. `foo/bar:latest` and `foo/bar:build-cache`), separate image names (e.g. `foo/bar` and `foo/bar-cache`), or even different repositories (e.g. `docker.io/foo/bar` and `ghcr.io/foo/bar`). It's up to you to decide the strategy that you want to use for separating your image from your cache images.

If the `--cache-from` target doesn't exist, then the cache import step will fail, but the build continues.

## [Further reading](#further-reading)

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `registry` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#registry-push-image-and-cache-separately).