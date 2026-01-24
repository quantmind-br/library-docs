---
title: docker buildx imagetools create
url: https://docs.docker.com/reference/cli/docker/buildx/imagetools/create/
source: llms
fetched_at: 2026-01-24T14:33:21.605846022-03:00
rendered_js: false
word_count: 408
summary: This document explains how to use the docker buildx imagetools create command to generate new images or manifest lists based on existing source manifests.
tags:
    - docker
    - buildx
    - imagetools
    - manifest-list
    - container-images
    - cli-reference
category: reference
---

DescriptionCreate a new image based on source imagesUsage`docker buildx imagetools create [OPTIONS] [SOURCE...]`

Create a new manifest list based on source manifests. The source manifests can be manifest lists or single platform distribution manifests and must already exist in the registry where the new manifest is created.

If only one source is specified and that source is a manifest list or image index, create performs a carbon copy. If one source is specified and that source is *not* a list or index, the output will be a manifest list, however you can disable this behavior with `--prefer-index=false` which attempts to preserve the source manifest format in the output.

OptionDefaultDescription[`--annotation`](#annotation)Add annotation to the image[`--append`](#append)Append to existing manifest[`--dry-run`](#dry-run)Show final image instead of pushing[`-f, --file`](#file)Read source descriptor from file`-p, --platform`Filter specified platforms of target image`--prefer-index``true`When only a single source is specified, prefer outputting an image index or manifest list instead of performing a carbon copy  
`--progress``auto`Set type of progress output (`auto`, `none`, `plain`, `rawjson`, `tty`). Use plain to show container output  
[`-t, --tag`](#tag)Set reference for new image

### [Add annotations to an image (--annotation)](#annotation)

The `--annotation` flag lets you add annotations the image index, manifest, and descriptors when creating a new image.

The following command creates a `foo/bar:latest` image with the `org.opencontainers.image.authors` annotation on the image index.

> The `imagetools create` command supports adding annotations to the image index and descriptor, using the following type prefixes:
> 
> - `index:`
> - `manifest-descriptor:`
> 
> It doesn't support annotating manifests or OCI layouts.

For more information about annotations, see [Annotations](https://docs.docker.com/build/building/annotations/).

### [Append new sources to an existing manifest list (--append)](#append)

Use the `--append` flag to append the new sources to an existing manifest list in the destination.

### [Override the configured builder instance (--builder)](#builder)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

### [Show final image instead of pushing (--dry-run)](#dry-run)

Use the `--dry-run` flag to not push the image, just show it.

### [Read source descriptor from a file (-f, --file)](#file)

Reads source from files. A source can be a manifest digest, manifest reference, or a JSON of OCI descriptor object.

In order to define annotations or additional platform properties like `os.version` and `os.features` you need to add them in the OCI descriptor object encoded in JSON.

The descriptor in the file is merged with existing descriptor in the registry if it exists.

The supported fields for the descriptor are defined in [OCI spec](https://github.com/opencontainers/image-spec/blob/master/descriptor.md#properties) .

### [Set reference for new image (-t, --tag)](#tag)

Use the `-t` or `--tag` flag to set the name of the image to be created.