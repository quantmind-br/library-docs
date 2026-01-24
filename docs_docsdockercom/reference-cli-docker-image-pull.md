---
title: docker image pull
url: https://docs.docker.com/reference/cli/docker/image/pull/
source: llms
fetched_at: 2026-01-24T14:36:28.603252293-03:00
rendered_js: false
word_count: 927
summary: This document provides a detailed reference for the docker image pull command, explaining how to download images and repositories from Docker Hub or private registries. It covers usage syntax, pulling by tags or digests, and configuring proxy or concurrent download settings.
tags:
    - docker-cli
    - image-management
    - docker-registry
    - container-images
    - docker-pull
    - content-addressable-storage
category: reference
---

DescriptionDownload an image from a registryUsage`docker image pull [OPTIONS] NAME[:TAG|@DIGEST]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker pull`

Most of your images will be created on top of a base image from the [Docker Hub](https://hub.docker.com) registry.

[Docker Hub](https://hub.docker.com) contains many pre-built images that you can `pull` and try without needing to define and configure your own.

To download a particular image, or set of images (i.e., a repository), use `docker pull`.

### [Proxy configuration](#proxy-configuration)

If you are behind an HTTP proxy server, for example in corporate settings, before open a connect to registry, you may need to configure the Docker daemon's proxy settings, refer to the [dockerd command-line reference](https://docs.docker.com/reference/cli/dockerd/#proxy-configuration) for details.

### [Concurrent downloads](#concurrent-downloads)

By default the Docker daemon will pull three layers of an image at a time. If you are on a low bandwidth connection this may cause timeout issues and you may want to lower this via the `--max-concurrent-downloads` daemon option. See the [daemon documentation](https://docs.docker.com/reference/cli/dockerd/) for more details.

OptionDefaultDescription[`-a, --all-tags`](#all-tags)Download all tagged images in the repository`--platform`API 1.32+ Set platform if server is multi-platform capable`-q, --quiet`Suppress verbose output

### [Pull an image from Docker Hub](#pull-an-image-from-docker-hub)

To download a particular image, or set of images (i.e., a repository), use `docker image pull` (or the `docker pull` shorthand). If no tag is provided, Docker Engine uses the `:latest` tag as a default. This example pulls the `debian:latest` image:

Docker images can consist of multiple layers. In the example above, the image consists of a single layer; `e756f3fdd6a3`.

Layers can be reused by images. For example, the `debian:bookworm` image shares its layer with the `debian:latest`. Pulling the `debian:bookworm` image therefore only pulls its metadata, but not its layers, because the layer is already present locally:

To see which images are present locally, use the [`docker images`](https://docs.docker.com/reference/cli/docker/image/ls/) command:

Docker uses a content-addressable image store, and the image ID is a SHA256 digest covering the image's configuration and layers. In the example above, `debian:bookworm` and `debian:latest` have the same image ID because they are the same image tagged with different names. Because they are the same image, their layers are stored only once and do not consume extra disk space.

For more information about images, layers, and the content-addressable store, refer to [understand images, containers, and storage drivers](https://docs.docker.com/engine/storage/drivers/).

### [Pull an image by digest (immutable identifier)](#pull-an-image-by-digest-immutable-identifier)

So far, you've pulled images by their name (and "tag"). Using names and tags is a convenient way to work with images. When using tags, you can `docker pull` an image again to make sure you have the most up-to-date version of that image. For example, `docker pull ubuntu:24.04` pulls the latest version of the Ubuntu 24.04 image.

In some cases you don't want images to be updated to newer versions, but prefer to use a fixed version of an image. Docker enables you to pull an image by its digest. When pulling an image by digest, you specify exactly which version of an image to pull. Doing so, allows you to "pin" an image to that version, and guarantee that the image you're using is always the same.

To know the digest of an image, pull the image first. Let's pull the latest `ubuntu:24.04` image from Docker Hub:

Docker prints the digest of the image after the pull has finished. In the example above, the digest of the image is:

Docker also prints the digest of an image when pushing to a registry. This may be useful if you want to pin to a version of the image you just pushed.

A digest takes the place of the tag when pulling an image, for example, to pull the above image by digest, run the following command:

Digest can also be used in the `FROM` of a Dockerfile, for example:

> Using this feature "pins" an image to a specific version in time. Docker does therefore not pull updated versions of an image, which may include security updates. If you want to pull an updated image, you need to change the digest accordingly.

### [Pull from a different registry](#pull-from-a-different-registry)

By default, `docker pull` pulls images from [Docker Hub](https://hub.docker.com). It is also possible to manually specify the path of a registry to pull from. For example, if you have set up a local registry, you can specify its path to pull from it. A registry path is similar to a URL, but does not contain a protocol specifier (`https://`).

The following command pulls the `testing/test-image` image from a local registry listening on port 5000 (`myregistry.local:5000`):

Registry credentials are managed by [docker login](https://docs.docker.com/reference/cli/docker/login/).

Docker uses the `https://` protocol to communicate with a registry, unless the registry is allowed to be accessed over an insecure connection. Refer to the [insecure registries](https://docs.docker.com/reference/cli/dockerd/#insecure-registries) section for more information.

### [Pull a repository with multiple images (-a, --all-tags)](#all-tags)

By default, `docker pull` pulls a single image from the registry. A repository can contain multiple images. To pull all images from a repository, provide the `-a` (or `--all-tags`) option when using `docker pull`.

This command pulls all images from the `ubuntu` repository:

After the pull has completed use the `docker image ls` command (or the `docker images` shorthand) to see the images that were pulled. The example below shows all the `ubuntu` images that are present locally:

### [Cancel a pull](#cancel-a-pull)

Killing the `docker pull` process, for example by pressing `CTRL-c` while it is running in a terminal, will terminate the pull operation.

The Engine terminates a pull operation when the connection between the daemon and the client (initiating the pull) is cut or lost for any reason or the command is manually terminated.