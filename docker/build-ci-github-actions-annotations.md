---
title: Annotations
url: https://docs.docker.com/build/ci/github-actions/annotations/
source: llms
fetched_at: 2026-01-24T14:16:19.589698788-03:00
rendered_js: false
word_count: 166
summary: This document explains how to use Docker GitHub Actions to automatically generate and apply OCI-compliant annotations to container images during the build process. It covers configuring the metadata-action to target specific image components like manifests and indexes using build-push-action and bake-action.
tags:
    - docker
    - github-actions
    - oci-annotations
    - metadata-action
    - container-images
    - build-push-action
    - docker-buildx
category: guide
---

## Add image annotations with GitHub Actions

Table of contents

* * *

Annotations let you specify arbitrary metadata for OCI image components, such as manifests, indexes, and descriptors.

To add annotations when building images with GitHub Actions, use the [metadata-action](https://github.com/docker/metadata-action#overwrite-labels-and-annotations) to automatically create OCI-compliant annotations. The metadata action creates an `annotations` output that you can reference, both with [build-push-action](https://github.com/docker/build-push-action/) and [bake-action](https://github.com/docker/bake-action/).

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Extract metadataid:metauses:docker/metadata-action@v5with:images:${{ env.IMAGE_NAME }}- name:Build and pushuses:docker/build-push-action@v6with:tags:${{ steps.meta.outputs.tags }}annotations:${{ steps.meta.outputs.annotations }}push:true
```

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Extract metadataid:metauses:docker/metadata-action@v5with:images:${{ env.IMAGE_NAME }}- name:Builduses:docker/bake-action@v6with:files:|            ./docker-bake.hcl
            cwd://${{ steps.meta.outputs.bake-file-tags }}
            cwd://${{ steps.meta.outputs.bake-file-annotations }}push:true
```

## [Configure annotation level](#configure-annotation-level)

By default, annotations are placed on image manifests. To configure the [annotation level](https://docs.docker.com/build/metadata/annotations/#specify-annotation-level), set the `DOCKER_METADATA_ANNOTATIONS_LEVELS` environment variable on the `metadata-action` step to a comma-separated list of all the levels that you want to annotate. For example, setting `DOCKER_METADATA_ANNOTATIONS_LEVELS` to `index` results in annotations on the image index instead of the manifests.

The following example creates annotations on both the image index and manifests.

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Extract metadataid:metauses:docker/metadata-action@v5with:images:${{ env.IMAGE_NAME }}env:DOCKER_METADATA_ANNOTATIONS_LEVELS:manifest,index- name:Build and pushuses:docker/build-push-action@v6with:tags:${{ steps.meta.outputs.tags }}annotations:${{ steps.meta.outputs.annotations }}push:true
```

> Note
> 
> The build must produce the components that you want to annotate. For example, to annotate an image index, the build must produce an index. If the build produces only a manifest and you specify `index` or `index-descriptor`, the build fails.