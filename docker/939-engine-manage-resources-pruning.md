---
title: Prune unused Docker objects
url: https://docs.docker.com/engine/manage-resources/pruning/
source: llms
fetched_at: 2026-01-24T14:24:17.304916309-03:00
rendered_js: false
word_count: 611
summary: This document explains how to use Docker prune commands to remove unused images, containers, volumes, and networks to reclaim disk space. It provides instructions for specific object types and the comprehensive system prune command, including usage of filters and force flags.
tags:
    - docker-cleanup
    - disk-management
    - docker-images
    - docker-containers
    - docker-volumes
    - docker-cli
    - garbage-collection
category: guide
---

Docker takes a conservative approach to cleaning up unused objects (often referred to as "garbage collection"), such as images, containers, volumes, and networks. These objects are generally not removed unless you explicitly ask Docker to do so. This can cause Docker to use extra disk space. For each type of object, Docker provides a `prune` command. In addition, you can use `docker system prune` to clean up multiple types of objects at once. This topic shows how to use these `prune` commands.

The `docker image prune` command allows you to clean up unused images. By default, `docker image prune` only cleans up *dangling* images. A dangling image is one that isn't tagged, and isn't referenced by any container. To remove dangling images:

To remove all images which aren't used by existing containers, use the `-a` flag:

By default, you are prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

You can limit which images are pruned using filtering expressions with the `--filter` flag. For example, to only consider images created more than 24 hours ago:

Other filtering expressions are available. See the [`docker image prune` reference](https://docs.docker.com/reference/cli/docker/image/prune/) for more examples.

When you stop a container, it isn't automatically removed unless you started it with the `--rm` flag. To see all containers on the Docker host, including stopped containers, use `docker ps -a`. You may be surprised how many containers exist, especially on a development system! A stopped container's writable layers still take up disk space. To clean this up, you can use the `docker container prune` command.

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all stopped containers are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes stopped containers older than 24 hours:

Other filtering expressions are available. See the [`docker container prune` reference](https://docs.docker.com/reference/cli/docker/container/prune/) for more examples.

Volumes can be used by one or more containers, and take up space on the Docker host. Volumes are never removed automatically, because to do so could destroy data.

By default, you are prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused volumes are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes volumes which aren't labelled with the `keep` label:

Other filtering expressions are available. See the [`docker volume prune` reference](https://docs.docker.com/reference/cli/docker/volume/prune/) for more examples.

Docker networks don't take up much disk space, but they do create `iptables` rules, bridge network devices, and routing table entries. To clean these things up, you can use `docker network prune` to clean up networks which aren't used by any containers.

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused networks are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes networks older than 24 hours:

Other filtering expressions are available. See the [`docker network prune` reference](https://docs.docker.com/reference/cli/docker/network/prune/) for more examples.

The `docker system prune` command is a shortcut that prunes images, containers, and networks. Volumes aren't pruned by default, and you must specify the `--volumes` flag for `docker system prune` to prune volumes.

To also prune volumes, add the `--volumes` flag:

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused containers, networks, and images are removed. You can limit the scope using the `--filter` flag. For instance, the following command removes items older than 24 hours:

Other filtering expressions are available. See the [`docker system prune` reference](https://docs.docker.com/reference/cli/docker/system/prune/) for more examples.