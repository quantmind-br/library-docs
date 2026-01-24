---
title: docker image push
url: https://docs.docker.com/reference/cli/docker/image/push/
source: llms
fetched_at: 2026-01-24T14:36:30.34069804-03:00
rendered_js: false
word_count: 375
summary: This document provides a technical reference for the docker image push command, detailing how to upload container images to registries and manage push configurations.
tags:
    - docker-cli
    - container-registry
    - image-management
    - docker-push
    - cli-reference
category: reference
---

DescriptionUpload an image to a registryUsage`docker image push [OPTIONS] NAME[:TAG]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker push`

Use `docker image push` to share your images to the [Docker Hub](https://hub.docker.com) registry or to a self-hosted one.

Refer to the [`docker image tag`](https://docs.docker.com/reference/cli/docker/image/tag/) reference for more information about valid image and tag names.

Killing the `docker image push` process, for example by pressing `CTRL-c` while it is running in a terminal, terminates the push operation.

Progress bars are shown during docker push, which show the uncompressed size. The actual amount of data that's pushed will be compressed before sending, so the uploaded size will not be reflected by the progress bar.

Registry credentials are managed by [docker login](https://docs.docker.com/reference/cli/docker/login/).

### [Concurrent uploads](#concurrent-uploads)

By default the Docker daemon will push five layers of an image at a time. If you are on a low bandwidth connection this may cause timeout issues and you may want to lower this via the `--max-concurrent-uploads` daemon option. See the [daemon documentation](https://docs.docker.com/reference/cli/dockerd/) for more details.

OptionDefaultDescription[`-a, --all-tags`](#all-tags)Push all tags of an image to the repository`--platform`API 1.46+ Push a platform-specific manifest as a single-platform image to the registry.  
Image index won't be pushed, meaning that other manifests, including attestations won't be preserved.  
'os\[/arch\[/variant]]': Explicit platform (eg. linux/amd64)`-q, --quiet`Suppress verbose output

### [Push a new image to a registry](#push-a-new-image-to-a-registry)

First save the new image by finding the container ID (using [`docker container ls`](https://docs.docker.com/reference/cli/docker/container/ls/)) and then committing it to a new image name. Note that only `a-z0-9-_.` are allowed when naming images:

Now, push the image to the registry using the image ID. In this example the registry is on host named `registry-host` and listening on port `5000`. To do this, tag the image with the host name or IP address, and the port of the registry:

Check that this worked by running:

You should see both `rhel-httpd` and `registry-host:5000/myadmin/rhel-httpd` listed.

### [Push all tags of an image (-a, --all-tags)](#all-tags)

Use the `-a` (or `--all-tags`) option to push all tags of a local image.

The following example creates multiple tags for an image, and pushes all those tags to Docker Hub.

The image is now tagged under multiple names:

When pushing with the `--all-tags` option, all tags of the `registry-host:5000/myname/myimage` image are pushed: