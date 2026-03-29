---
title: OCI and Docker exporters
url: https://docs.docker.com/build/exporters/oci-docker/
source: llms
fetched_at: 2026-01-24T14:16:54.945593708-03:00
rendered_js: false
word_count: 170
summary: This document provides a technical overview and usage guide for the OCI and Docker exporters in Buildx, detailing available parameters and annotation support.
tags:
    - docker-buildx
    - oci-exporter
    - docker-exporter
    - image-layout
    - buildkit
    - container-images
category: reference
---

Table of contents

* * *

The `oci` exporter outputs the build result into an [OCI image layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md) tarball. The `docker` exporter behaves the same way, except it exports a Docker image layout instead.

The [`docker` driver](https://docs.docker.com/build/builders/drivers/docker/) doesn't support these exporters. You must use `docker-container` or some other driver if you want to generate these outputs.

## [Synopsis](#synopsis)

Build a container image using the `oci` and `docker` exporters:

```
$ docker buildx build --output type=oci[,parameters] .
```

```
$ docker buildx build --output type=docker[,parameters] .
```

The following table describes the available parameters:

ParameterTypeDefaultDescription`name`StringSpecify image name(s)`dest`StringPath`tar``true`,`false``true`Bundle the output into a tarball layout`compression``uncompressed`,`gzip`,`estargz`,`zstd``gzip`Compression type, see [compression](https://docs.docker.com/build/exporters/#compression)`compression-level``0..22`Compression level, see [compression](https://docs.docker.com/build/exporters/#compression)`force-compression``true`,`false``false`Forcefully apply compression, see [compression](https://docs.docker.com/build/exporters/#compression)`oci-mediatypes``true`,`false`Use OCI media types in exporter manifests. Defaults to `true` for `type=oci`, and `false` for `type=docker`. See [OCI Media types](https://docs.docker.com/build/exporters/#oci-media-types)`annotation.<key>`StringAttach an annotation with the respective `key` and `value` to the built image,see [annotations](#annotations)

## [Annotations](#annotations)

These exporters support adding OCI annotation using `annotation` parameter, followed by the annotation name using dot notation. The following example sets the `org.opencontainers.image.title` annotation:

```
$ docker buildx build \
    --output "type=<type>,name=<registry>/<image>,annotation.org.opencontainers.image.title=<title>" .
```

For more information about annotations, see [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/annotations.md).

## [Further reading](#further-reading)

For more information on the `oci` or `docker` exporters, see the [BuildKit README](https://github.com/moby/buildkit/blob/master/README.md#docker-tarball).