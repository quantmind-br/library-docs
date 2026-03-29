---
title: docker image rm
url: https://docs.docker.com/reference/cli/docker/image/rm/
source: llms
fetched_at: 2026-01-24T14:36:31.406273131-03:00
rendered_js: false
word_count: 403
summary: This document explains how to use the docker image rm command to remove and untag images from a local host, including usage of various flags and platform-specific removal options.
tags:
    - docker
    - docker-cli
    - image-management
    - container-images
    - docker-rmi
    - command-line
category: reference
---

DescriptionRemove one or more imagesUsage`docker image rm [OPTIONS] IMAGE [IMAGE...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker image remove` `docker rmi`

Removes (and un-tags) one or more images from the host node. If an image has multiple tags, using this command with the tag as a parameter only removes the tag. If the tag is the only one for the image, both the image and the tag are removed.

This does not remove images from a registry. You cannot remove an image of a running container unless you use the `-f` option. To see all images on a host use the [`docker image ls`](https://docs.docker.com/reference/cli/docker/image/ls/) command.

OptionDefaultDescription`-f, --force`Force removal of the image`--no-prune`Do not delete untagged parents[`--platform`](#platform)API 1.50+ Remove only the given platform variant. Formatted as `os[/arch[/variant]]` (e.g., `linux/amd64`)

You can remove an image using its short or long ID, its tag, or its digest. If an image has one or more tags referencing it, you must remove all of them before the image is removed. Digest references are removed automatically when an image is removed by tag.

If you use the `-f` flag and specify the image's short or long ID, then this command untags and removes all images that match the specified ID.

An image pulled by digest has no tag associated with it:

To remove an image using its digest:

### [Remove specific platforms (`--platform`)](#platform)

The `--platform` option allows you to specify which platform variants of the image to remove. By default, `docker image remove` removes all platform variants that are present. Use the `--platform` option to specify which platform variant of the image to remove.

Removing a specific platform removes the image from all images that reference the same content, and requires the `--force` option to be used. Omitting the `--force` option produces a warning, and the remove is canceled:

The platform option takes the `os[/arch[/variant]]` format; for example, `linux/amd64` or `linux/arm64/v8`. Architecture and variant are optional, and default to the daemon's native architecture if omitted.

You can pass multiple platforms either by passing the `--platform` flag multiple times, or by passing a comma-separated list of platforms to remove. The following uses of this option are equivalent;

The following example removes the `linux/amd64` and `linux/ppc64le` variants of an `alpine` image that contains multiple platform variants in the image cache:

After the command completes, the given variants of the `alpine` image are removed from the image cache: