---
title: Build checks
url: https://docs.docker.com/build/ci/github-actions/checks/
source: llms
fetched_at: 2026-01-24T14:16:23.652621208-03:00
rendered_js: false
word_count: 148
summary: This document explains how to validate Docker build configurations within GitHub Actions workflows using the build check feature in both the build-push-action and bake-action.
tags:
    - docker-build
    - github-actions
    - build-checks
    - docker-bake
    - ci-cd
    - automation
category: guide
---

## Validating build configuration with GitHub Actions

Table of contents

* * *

[Build checks](https://docs.docker.com/build/checks/) let you validate your `docker build` configuration without actually running the build.

## [Run checks with `docker/build-push-action`](#run-checks-with-dockerbuild-push-action)

To run build checks in a GitHub Actions workflow with the `build-push-action`, set the `call` input parameter to `check`. With this set, the workflow fails if any check warnings are detected for your build's configuration.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ secrets.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Validate build configurationuses:docker/build-push-action@v6with:call:check- name:Build and pushuses:docker/build-push-action@v6with:push:truetags:user/app:latest
```

## [Run checks with `docker/bake-action`](#run-checks-with-dockerbake-action)

If you're using Bake and `docker/bake-action` to run your builds, you don't need to specify any special inputs in your GitHub Actions workflow configuration. Instead, define a Bake target that calls the `check` method, and invoke that target in your CI.

```
target "build" {
  dockerfile = "Dockerfile"
  args = {
    FOO = "bar"
  }
}
target "validate-build" {
  inherits = ["build"]
  call = "check"
}
```

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Validate build configurationuses:docker/bake-action@v6with:targets:validate-build- name:Builduses:docker/bake-action@v6with:targets:buildpush:true
```

### [Using the `call` input directly](#using-the-call-input-directly)

You can also set the build method with the `call` input which is equivalent to using the `--call` flag with `docker buildx bake`

For example, to run a check without defining `call` in your Bake file:

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Validate build configurationuses:docker/bake-action@v6with:targets:buildcall:check
```