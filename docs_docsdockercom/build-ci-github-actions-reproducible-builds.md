---
title: Reproducible builds
url: https://docs.docker.com/build/ci/github-actions/reproducible-builds/
source: llms
fetched_at: 2026-01-24T14:16:40.105329091-03:00
rendered_js: false
word_count: 101
summary: This document explains how to achieve reproducible Docker builds in GitHub Actions by configuring the SOURCE_DATE_EPOCH environment variable using various timestamp sources.
tags:
    - github-actions
    - docker
    - reproducible-builds
    - buildx
    - source-date-epoch
    - ci-cd
category: guide
---

## Reproducible builds with GitHub Actions

`SOURCE_DATE_EPOCH` is a [standardized environment variable](https://reproducible-builds.org/docs/source-date-epoch/) for instructing build tools to produce a reproducible output. Setting the environment variable for a build makes the timestamps in the image index, config, and file metadata reflect the specified Unix time.

To set the environment variable in GitHub Actions, use the built-in `env` property on the build step.

## [Unix epoch timestamps](#unix-epoch-timestamps)

The following example sets the `SOURCE_DATE_EPOCH` variable to 0, Unix epoch.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Builduses:docker/build-push-action@v6with:tags:user/app:latestenv:SOURCE_DATE_EPOCH:0
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Builduses:docker/bake-action@v6env:SOURCE_DATE_EPOCH:0
```

## [Git commit timestamps](#git-commit-timestamps)

The following example sets `SOURCE_DATE_EPOCH` to the Git commit timestamp.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Get Git commit timestampsrun:echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV- name:Builduses:docker/build-push-action@v6with:tags:user/app:latestenv:SOURCE_DATE_EPOCH:${{ env.TIMESTAMP }}
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Get Git commit timestampsrun:echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV- name:Builduses:docker/bake-action@v6env:SOURCE_DATE_EPOCH:${{ env.TIMESTAMP }}
```

## [Additional information](#additional-information)

For more information about the `SOURCE_DATE_EPOCH` support in BuildKit, see [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/build-repro.md#source_date_epoch).