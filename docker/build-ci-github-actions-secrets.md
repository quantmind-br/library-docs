---
title: Build secrets
url: https://docs.docker.com/build/ci/github-actions/secrets/
source: llms
fetched_at: 2026-01-24T14:16:41.526018898-03:00
rendered_js: false
word_count: 303
summary: This document explains how to integrate build-time secrets and SSH mounts into Docker builds within GitHub Actions workflows. It covers the necessary configuration for Dockerfiles and the specific inputs required for the build-push-action.
tags:
    - github-actions
    - docker-build
    - docker-secrets
    - ssh-mounts
    - ci-cd
    - build-push-action
category: guide
---

## Using secrets with GitHub Actions

Table of contents

* * *

A build secret is sensitive information, such as a password or API token, consumed as part of the build process. Docker Build supports two forms of secrets:

- [Secret mounts](#secret-mounts) add secrets as files in the build container (under `/run/secrets` by default).
- [SSH mounts](#ssh-mounts) add SSH agent sockets or keys into the build container.

This page shows how to use secrets with GitHub Actions. For an introduction to secrets in general, see [Build secrets](https://docs.docker.com/build/building/secrets/).

## [Secret mounts](#secret-mounts)

In the following example uses and exposes the [`GITHUB_TOKEN` secret](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#about-the-github_token-secret) as provided by GitHub in your workflow.

First, create a `Dockerfile` that uses the secret:

```
# syntax=docker/dockerfile:1FROMalpineRUN --mount=type=secret,id=github_token,env=GITHUB_TOKEN ...
```

In this example, the secret name is `github_token`. The following workflow exposes this secret using the `secrets` input:

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Builduses:docker/build-push-action@v6with:platforms:linux/amd64,linux/arm64tags:user/app:latestsecrets:|            "github_token=${{ secrets.GITHUB_TOKEN }}"
```

> Note
> 
> You can also expose a secret file to the build with the `secret-files` input:
> 
> ```
> secret-files:|  "MY_SECRET=./secret.txt"
> ```

If you're using [GitHub secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) and need to handle multi-line value, you will need to place the key-value pair between quotes:

```
secrets:|  "MYSECRET=${{ secrets.GPG_KEY }}"
  GIT_AUTH_TOKEN=abcdefghi,jklmno=0123456789
  "MYSECRET=aaaaaaaa
  bbbbbbb
  ccccccccc"
  FOO=bar
  "EMPTYLINE=aaaa
  bbbb
  ccc"
  "JSON_SECRET={""key1"":""value1"",""key2"":""value2""}"
```

KeyValue`MYSECRET``***********************``GIT_AUTH_TOKEN``abcdefghi,jklmno=0123456789``MYSECRET``aaaaaaaa\nbbbbbbb\nccccccccc``FOO``bar``EMPTYLINE``aaaa\n\nbbbb\nccc``JSON_SECRET``{"key1":"value1","key2":"value2"}`

> Note
> 
> Double escapes are needed for quote signs.

## [SSH mounts](#ssh-mounts)

SSH mounts let you authenticate with SSH servers. For example to perform a `git clone`, or to fetch application packages from a private repository.

The following Dockerfile example uses an SSH mount to fetch Go modules from a private GitHub repository.

```
# syntax=docker/dockerfile:1ARG GO_VERSION="1.24"FROMgolang:${GO_VERSION}-alpineASbaseENV CGO_ENABLED=0
ENV GOPRIVATE="github.com/foo/*"RUN apk add --no-cache file git rsync openssh-clientRUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hostsWORKDIR/srcFROMbaseASvendor# this step configure git and checks the ssh key is loadedRUN --mount=type=ssh <<EOT  set -e  echo "Setting Git SSH protocol"  git config --global url."git@github.com:".insteadOf "https://github.com/"  (    set +e    ssh -T git@github.com    if [ ! "$?" = "1" ]; then      echo "No GitHub SSH key loaded exiting..."      exit 1    fi  )EOT# this one download go modulesRUN --mount=type=bind,target=. \
    --mount=type=cache,target=/go/pkg/mod \
    --mount=type=ssh \
    go mod download -xFROMvendorASbuildRUN --mount=type=bind,target=. \
    --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache \
    go build ...
```

To build this Dockerfile, you must specify an SSH mount that the builder can use in the steps with `--mount=type=ssh`.

The following GitHub Action workflow uses the `MrSquaare/ssh-setup-action` third-party action to bootstrap SSH setup on the GitHub runner. The action creates a private key defined by the GitHub Action secret `SSH_GITHUB_PPK` and adds it to the SSH agent socket file at `SSH_AUTH_SOCK`. The SSH mount in the build step assume `SSH_AUTH_SOCK` by default, so there's no need to specify the ID or path for the SSH agent socket explicitly.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up SSHuses:MrSquaare/ssh-setup-action@2d028b70b5e397cf8314c6eaea229a6c3e34977a# v3.1.0with:host:github.comprivate-key:${{ secrets.SSH_GITHUB_PPK }}private-key-name:github-ppk- name:Build and pushuses:docker/build-push-action@v6with:ssh:defaultpush:truetags:user/app:latest
```

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up SSHuses:MrSquaare/ssh-setup-action@2d028b70b5e397cf8314c6eaea229a6c3e34977a# v3.1.0with:host:github.comprivate-key:${{ secrets.SSH_GITHUB_PPK }}private-key-name:github-ppk- name:Builduses:docker/bake-action@v6with:set:|            *.ssh=default
```