---
title: Inline cache
url: https://docs.docker.com/build/cache/backends/inline/
source: llms
fetched_at: 2026-01-24T14:15:57.235845692-03:00
rendered_js: false
word_count: 186
summary: This document explains how to use the inline cache storage backend with Docker Buildx to embed cache metadata directly into built images. It provides instructions for exporting and importing inline cache using command-line flags and build arguments.
tags:
    - docker-buildx
    - inline-cache
    - build-caching
    - buildkit
    - container-images
category: reference
---

Table of contents

* * *

The `inline` cache storage backend is the simplest way to get an external cache and is easy to get started using if you're already building and pushing an image.

The downside of inline cache is that it doesn't scale with multi-stage builds as well as the other drivers do. It also doesn't offer separation between your output artifacts and your cache output. This means that if you're using a particularly complex build flow, or not exporting your images directly to a registry, then you may want to consider the [registry](https://docs.docker.com/build/cache/backends/registry/) cache.

## [Synopsis](#synopsis)

```
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=inline \
  --cache-from type=registry,ref=<registry>/<image> .
```

No additional parameters are supported for the `inline` cache.

To export cache using `inline` storage, pass `type=inline` to the `--cache-to` option:

```
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=inline .
```

Alternatively, you can also export inline cache by setting the build argument `BUILDKIT_INLINE_CACHE=1`, instead of using the `--cache-to` flag:

```
$ docker buildx build --push -t <registry>/<image> \
  --build-arg BUILDKIT_INLINE_CACHE=1 .
```

To import the resulting cache on a future build, pass `type=registry` to `--cache-from` which lets you extract the cache from inside a Docker image in the specified registry:

```
$ docker buildx build --push -t <registry>/<image> \
  --cache-from type=registry,ref=<registry>/<image> .
```

## [Further reading](#further-reading)

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `inline` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#inline-push-image-and-cache-together).