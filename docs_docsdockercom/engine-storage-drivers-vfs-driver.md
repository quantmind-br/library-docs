---
title: VFS storage driver
url: https://docs.docker.com/engine/storage/drivers/vfs-driver/
source: llms
fetched_at: 2026-01-24T14:25:39.978205003-03:00
rendered_js: false
word_count: 382
summary: This document explains the functionality, trade-offs, and configuration process for the Docker VFS storage driver, which uses deep copies instead of copy-on-write for layer management.
tags:
    - docker
    - storage-driver
    - vfs
    - container-storage
    - filesystem-layers
    - daemon-configuration
category: guide
---

The VFS storage driver isn't a union filesystem. Each layer is a directory on disk, and there is no copy-on-write support. To create a new layer, a "deep copy" is done of the previous layer. This leads to lower performance and more space used on disk than other storage drivers. However, it is robust, stable, and works in every environment. It can also be used as a mechanism to verify other storage back-ends against, in a testing environment.

1. Stop Docker.
2. Edit `/etc/docker/daemon.json`. If it doesn't yet exist, create it. Assuming that the file was empty, add the following contents.
   
   If you want to set a quota to control the maximum size the VFS storage driver can use, set the `size` option on the `storage-opts` key.
   
   Docker doesn't start if the `daemon.json` file contains invalid JSON.
3. Start Docker.
4. Verify that the daemon is using the `vfs` storage driver. Use the `docker info` command and look for `Storage Driver`.

Docker is now using the `vfs` storage driver. Docker has automatically created the `/var/lib/docker/vfs/` directory, which contains all the layers used by running containers.

Each image layer and the writable container layer are represented on the Docker host as subdirectories within `/var/lib/docker/`. The union mount provides the unified view of all layers. The directory names don't directly correspond to the IDs of the layers themselves.

VFS doesn't support copy-on-write (COW). Each time a new layer is created, it's a deep copy of its parent layer. These layers are all located under `/var/lib/docker/vfs/dir/`.

### [Example: Image and container on-disk constructs](#example-image-and-container-on-disk-constructs)

The following `docker pull` command shows a Docker host downloading a Docker image comprising five layers.

After pulling, each of these layers is represented as a subdirectory of `/var/lib/docker/vfs/dir/`. The directory names do not correlate with the image layer IDs shown in the `docker pull` command. To see the size taken up on disk by each layer, you can use the `du -sh` command, which gives the size as a human-readable value.

The above output shows that three layers each take 104M and two take 125M. These directories have only small differences from each other, but they all consume the same amount of disk space. This is one of the disadvantages of using the `vfs` storage driver.

- [Understand images, containers, and storage drivers](https://docs.docker.com/engine/storage/drivers/)
- [Select a storage driver](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)