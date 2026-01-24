---
title: Local and tar exporters
url: https://docs.docker.com/build/exporters/local-tar/
source: llms
fetched_at: 2026-01-24T14:16:54.340212692-03:00
rendered_js: false
word_count: 208
summary: This document explains how to use the local and tar exporters in Docker Buildx to output build results as files or tarballs. It details configuration parameters and directory organization for single and multi-platform builds.
tags:
    - docker-buildx
    - build-exporters
    - local-exporter
    - tar-exporter
    - multi-platform-builds
    - buildkit
category: guide
---

Table of contents

* * *

The `local` and `tar` exporters output the root filesystem of the build result into a local directory. They're useful for producing artifacts that aren't container images.

- `local` exports files and directories.
- `tar` exports the same, but bundles the export into a tarball.

## [Synopsis](#synopsis)

Build a container image using the `local` exporter:

```
$ docker buildx build --output type=local[,parameters] .
$ docker buildx build --output type=tar[,parameters] .
```

The following table describes the available parameters:

ParameterTypeDefaultDescription`dest`StringPath to copy files to`platform-split`Boolean`true``local` exporter only. Split multi-platform outputs into platform subdirectories.

## [Multi-platform builds with local exporter](#multi-platform-builds-with-local-exporter)

The `platform-split` parameter controls how multi-platform build outputs are organized.

Consider this Dockerfile that creates platform-specific files:

```
FROMbusyboxASbuildARG TARGETOSARG TARGETARCHRUN mkdir /out && echo foo > /out/hello-$TARGETOS-$TARGETARCHFROMscratchCOPY --from=build /out /
```

### [Split by platform (default)](#split-by-platform-default)

By default, the local exporter creates a separate subdirectory for each platform:

```
$ docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --output type=local,dest=./output \
  .
```

This produces the following directory structure:

```
output/
├── linux_amd64/
│   └── hello-linux-amd64
└── linux_arm64/
    └── hello-linux-arm64
```

### [Merge all platforms](#merge-all-platforms)

To merge files from all platforms into the same directory, set `platform-split=false`:

```
$ docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --output type=local,dest=./output,platform-split=false \
  .
```

This produces a flat directory structure:

```
output/
├── hello-linux-amd64
└── hello-linux-arm64
```

Files from all platforms merge into a single directory. If multiple platforms produce files with identical names, the export fails with an error.

### [Single-platform builds](#single-platform-builds)

Single-platform builds export directly to the destination directory without creating a platform subdirectory:

```
$ docker buildx build \
  --platform linux/amd64 \
  --output type=local,dest=./output \
  .
```

This produces:

```
output/
└── hello-linux-amd64
```

To include the platform subdirectory even for single-platform builds, explicitly set `platform-split=true`:

```
$ docker buildx build \
  --platform linux/amd64 \
  --output type=local,dest=./output,platform-split=true \
  .
```

This produces:

```
output/
└── linux_amd64/
    └── hello-linux-amd64
```

## [Further reading](#further-reading)

For more information on the `local` or `tar` exporters, see the [BuildKit README](https://github.com/moby/buildkit/blob/master/README.md#local-directory).