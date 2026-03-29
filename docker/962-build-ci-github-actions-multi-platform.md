---
title: Multi-platform image
url: https://docs.docker.com/build/ci/github-actions/multi-platform/
source: llms
fetched_at: 2026-01-24T14:16:30.292874995-03:00
rendered_js: false
word_count: 324
summary: This document provides instructions for building multi-platform Docker images using GitHub Actions, including methods for single-runner builds, local image loading, and distributed builds across multiple runners. It demonstrates how to utilize tools like Buildx, QEMU, and Docker Bake to optimize architecture-specific build processes.
tags:
    - github-actions
    - docker-buildx
    - multi-platform
    - qemu
    - docker-bake
    - ci-cd
    - container-images
category: guide
---

## Multi-platform image with GitHub Actions

Table of contents

* * *

You can build [multi-platform images](https://docs.docker.com/build/building/multi-platform/) using the `platforms` option, as shown in the following example:

> Note
> 
> - For a list of available platforms, see the [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx) action.
> - If you want support for more platforms, you can use QEMU with the [Docker Setup QEMU](https://github.com/docker/setup-qemu-action) action.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Build and pushuses:docker/build-push-action@v6with:platforms:linux/amd64,linux/arm64push:truetags:user/app:latest
```

## [Build and load multi-platform images](#build-and-load-multi-platform-images)

The default Docker setup for GitHub Actions runners does not support loading multi-platform images to the local image store of the runner after building them. To load a multi-platform image, you need to enable the containerd image store option for the Docker Engine.

There is no way to configure the default Docker setup in the GitHub Actions runners directly, but you can use `docker/setup-docker-action` to customize the Docker Engine and CLI settings for a job.

The following example workflow enables the containerd image store, builds a multi-platform image, and loads the results into the GitHub runner's local image store.

```
name:cion:push:jobs:docker:runs-on:ubuntu-lateststeps:- name:Set up Dockeruses:docker/setup-docker-action@v4with:daemon-config:|            {
              "debug": true,
              "features": {
                "containerd-snapshotter": true
              }
            }- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Build and pushuses:docker/build-push-action@v6with:platforms:linux/amd64,linux/arm64load:truetags:user/app:latest
```

## [Distribute build across multiple runners](#distribute-build-across-multiple-runners)

Building multiple platforms on the same runner can significantly extend build times, particularly when dealing with complex Dockerfiles or a high number of target platforms. By distributing platform-specific builds across multiple runners using a matrix strategy, you can drastically reduce build durations and streamline your CI pipeline. These examples demonstrate how to allocate each platform build to a dedicated runner, including ARM-native runners where applicable, and create a unified manifest list using the [`buildx imagetools create` command](https://docs.docker.com/reference/cli/docker/buildx/imagetools/create/).

The following workflow will build the image for each platform on a dedicated runner using a matrix strategy and push by digest. Then, the `merge` job will create manifest lists and push them to Docker Hub. The [`metadata` action](https://github.com/docker/metadata-action) is used to set tags and labels.

```
name:cion:push:env:REGISTRY_IMAGE:user/appjobs:build:strategy:fail-fast:falsematrix:include:- platform:linux/amd64runner:ubuntu-latest- platform:linux/arm64runner:ubuntu-24.04-armruns-on:${{ matrix.runner }}steps:- name:Preparerun:|          platform=${{ matrix.platform }}
          echo "PLATFORM_PAIR=${platform//\//-}" >> $GITHUB_ENV- name:Docker metaid:metauses:docker/metadata-action@v5with:images:${{ env.REGISTRY_IMAGE }}- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Build and push by digestid:builduses:docker/build-push-action@v6with:platforms:${{ matrix.platform }}labels:${{ steps.meta.outputs.labels }}tags:${{ env.REGISTRY_IMAGE }}outputs:type=image,push-by-digest=true,name-canonical=true,push=true- name:Export digestrun:|          mkdir -p ${{ runner.temp }}/digests
          digest="${{ steps.build.outputs.digest }}"
          touch "${{ runner.temp }}/digests/${digest#sha256:}"- name:Upload digestuses:actions/upload-artifact@v4with:name:digests-${{ env.PLATFORM_PAIR }}path:${{ runner.temp }}/digests/*if-no-files-found:errorretention-days:1merge:runs-on:ubuntu-latestneeds:- buildsteps:- name:Download digestsuses:actions/download-artifact@v4with:path:${{ runner.temp }}/digestspattern:digests-*merge-multiple:true- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Docker metaid:metauses:docker/metadata-action@v5with:images:${{ env.REGISTRY_IMAGE }}tags:|            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}- name:Create manifest list and pushworking-directory:${{ runner.temp }}/digestsrun:|          docker buildx imagetools create $(jq -cr '.tags | map("-t " + .) | join(" ")' <<< "$DOCKER_METADATA_OUTPUT_JSON") \
            $(printf '${{ env.REGISTRY_IMAGE }}@sha256:%s ' *)- name:Inspect imagerun:|          docker buildx imagetools inspect ${{ env.REGISTRY_IMAGE }}:${{ steps.meta.outputs.version }}
```

### [With Bake](#with-bake)

It's also possible to build on multiple runners using Bake, with the [bake action](https://github.com/docker/bake-action).

You can find a live example [in this GitHub repository](https://github.com/crazy-max/docker-linguist).

The following example achieves the same results as described in [the previous section](#distribute-build-across-multiple-runners).

```
variable "DEFAULT_TAG" {
  default = "app:local"
}
// Special target: https://github.com/docker/metadata-action#bake-definition
target "docker-metadata-action" {
  tags = ["${DEFAULT_TAG}"]
}
// Default target if none specified
group "default" {
  targets = ["image-local"]
}
target "image" {
  inherits = ["docker-metadata-action"]
}
target "image-local" {
  inherits = ["image"]
  output = ["type=docker"]
}
target "image-all" {
  inherits = ["image"]
  platforms = [
    "linux/amd64",
    "linux/arm/v6",
    "linux/arm/v7",
    "linux/arm64"
  ]
}
```

```
name:cion:push:env:REGISTRY_IMAGE:user/appjobs:prepare:runs-on:ubuntu-latestoutputs:matrix:${{ steps.platforms.outputs.matrix }}steps:- name:Checkoutuses:actions/checkout@v4- name:Create matrixid:platformsrun:|          echo "matrix=$(docker buildx bake image-all --print | jq -cr '.target."image-all".platforms')" >>${GITHUB_OUTPUT}- name:Show matrixrun:|          echo ${{ steps.platforms.outputs.matrix }}- name:Docker metaid:metauses:docker/metadata-action@v5with:images:${{ env.REGISTRY_IMAGE }}- name:Rename meta bake definition filerun:|          mv "${{ steps.meta.outputs.bake-file }}" "${{ runner.temp }}/bake-meta.json"- name:Upload meta bake definitionuses:actions/upload-artifact@v4with:name:bake-metapath:${{ runner.temp }}/bake-meta.jsonif-no-files-found:errorretention-days:1build:needs:- preparestrategy:fail-fast:falsematrix:platform:${{ fromJson(needs.prepare.outputs.matrix) }}runs-on:${{ startsWith(matrix.platform, 'linux/arm') && 'ubuntu-24.04-arm' || 'ubuntu-latest' }}steps:- name:Preparerun:|          platform=${{ matrix.platform }}
          echo "PLATFORM_PAIR=${platform//\//-}" >> $GITHUB_ENV- name:Download meta bake definitionuses:actions/download-artifact@v4with:name:bake-metapath:${{ runner.temp }}- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Buildid:bakeuses:docker/bake-action@v6with:files:|            ./docker-bake.hcl
            cwd://${{ runner.temp }}/bake-meta.jsontargets:imageset:|            *.tags=${{ env.REGISTRY_IMAGE }}
            *.platform=${{ matrix.platform }}
            *.output=type=image,push-by-digest=true,name-canonical=true,push=true- name:Export digestrun:|          mkdir -p ${{ runner.temp }}/digests
          digest="${{ fromJSON(steps.bake.outputs.metadata).image['containerimage.digest'] }}"
          touch "${{ runner.temp }}/digests/${digest#sha256:}"- name:Upload digestuses:actions/upload-artifact@v4with:name:digests-${{ env.PLATFORM_PAIR }}path:${{ runner.temp }}/digests/*if-no-files-found:errorretention-days:1merge:runs-on:ubuntu-latestneeds:- buildsteps:- name:Download meta bake definitionuses:actions/download-artifact@v4with:name:bake-metapath:${{ runner.temp }}- name:Download digestsuses:actions/download-artifact@v4with:path:${{ runner.temp }}/digestspattern:digests-*merge-multiple:true- name:Login to DockerHubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Create manifest list and pushworking-directory:${{ runner.temp }}/digestsrun:|          docker buildx imagetools create $(jq -cr '.target."docker-metadata-action".tags | map(select(startswith("${{ env.REGISTRY_IMAGE }}")) | "-t " + .) | join(" ")' ${{ runner.temp }}/bake-meta.json) \
            $(printf '${{ env.REGISTRY_IMAGE }}@sha256:%s ' *)- name:Inspect imagerun:|          docker buildx imagetools inspect ${{ env.REGISTRY_IMAGE }}:$(jq -r '.target."docker-metadata-action".args.DOCKER_META_VERSION' ${{ runner.temp }}/bake-meta.json)
```