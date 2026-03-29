---
title: docker buildx rm
url: https://docs.docker.com/reference/cli/docker/buildx/rm/
source: llms
fetched_at: 2026-01-24T14:33:26.528791127-03:00
rendered_js: false
word_count: 146
summary: This document explains how to use the docker buildx rm command to remove one or more builder instances from the Docker environment.
tags:
    - docker
    - buildx
    - cli-command
    - container-builds
    - builder-management
category: reference
---

DescriptionRemove one or more builder instancesUsage`docker buildx rm [OPTIONS] [NAME...]`

## [Description](#description)

Removes the specified or current builder. It is a no-op attempting to remove the default builder.

## [Options](#options)

OptionDefaultDescription[`--all-inactive`](#all-inactive)Remove all inactive builders[`-f, --force`](#force)Do not prompt for confirmation[`--keep-daemon`](#keep-daemon)Keep the BuildKit daemon running[`--keep-state`](#keep-state)Keep BuildKit state

## [Examples](#examples)

### [Remove all inactive builders (--all-inactive)](#all-inactive)

Remove builders that are not in running state.

```
$ docker buildx rm --all-inactive
WARNING! This will remove all builders that are not in running state. Are you sure you want to continue? [y/N] y
```

### [Override the configured builder instance (--builder)](#builder)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

### [Do not prompt for confirmation (--force)](#force)

Do not prompt for confirmation before removing inactive builders.

```
$ docker buildx rm --all-inactive --force
```

### [Keep the BuildKit daemon running (--keep-daemon)](#keep-daemon)

Keep the BuildKit daemon running after the buildx context is removed. This is useful when you manage BuildKit daemons and buildx contexts independently. Only supported by the [`docker-container`](https://docs.docker.com/build/drivers/docker-container/) and [`kubernetes`](https://docs.docker.com/build/drivers/kubernetes/) drivers.

### [Keep BuildKit state (--keep-state)](#keep-state)

Keep BuildKit state, so it can be reused by a new builder with the same name. Currently, only supported by the [`docker-container` driver](https://docs.docker.com/build/drivers/docker-container/).