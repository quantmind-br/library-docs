---
title: Attestations
url: https://docs.docker.com/build/ci/github-actions/attestations/
source: llms
fetched_at: 2026-01-24T14:16:19.727291484-03:00
rendered_js: false
word_count: 348
summary: This document explains how to configure GitHub Actions to add SBOM and provenance attestations to Docker images using the docker/build-push-action. It covers default settings, manual provenance levels, and enabling SBOM generation for enhanced image metadata.
tags:
    - github-actions
    - docker-build
    - sbom
    - provenance
    - attestations
    - container-security
    - software-supply-chain
category: guide
---

## Add SBOM and provenance attestations with GitHub Actions

Software Bill of Material (SBOM) and provenance [attestations](https://docs.docker.com/build/metadata/attestations/) add metadata about the contents of your image, and how it was built.

Attestations are supported with version 4 and later of the `docker/build-push-action`.

## [Default provenance](#default-provenance)

The `docker/build-push-action` GitHub Action automatically adds provenance attestations to your image, with the following conditions:

- If the GitHub repository is public, provenance attestations with `mode=max` are automatically added to the image.
- If the GitHub repository is private, provenance attestations with `mode=min` are automatically added to the image.
- If you're using the [`docker` exporter](https://docs.docker.com/build/exporters/oci-docker/), or you're loading the build results to the runner with `load: true`, no attestations are added to the image. These output formats don't support attestations.

> Warning
> 
> If you're using `docker/build-push-action` to build images for code in a public GitHub repository, the provenance attestations attached to your image by default contains the values of build arguments. If you're misusing build arguments to pass secrets to your build, such as user credentials or authentication tokens, those secrets are exposed in the provenance attestation. Refactor your build to pass those secrets using [secret mounts](https://docs.docker.com/reference/cli/docker/buildx/build/#secret) instead. Also remember to rotate any secrets you may have exposed.

## [Max-level provenance](#max-level-provenance)

It's recommended that you build your images with max-level provenance attestations. Private repositories only add min-level provenance by default, but you can manually override the provenance level by setting the `provenance` input on the `docker/build-push-action` GitHub Action to `mode=max`.

Note that adding attestations to an image means you must push the image to a registry directly, as opposed to loading the image to the local image store of the runner. This is because the local image store doesn't support loading images with attestations.

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Extract metadataid:metauses:docker/metadata-action@v5with:images:${{ env.IMAGE_NAME }}- name:Build and push imageuses:docker/build-push-action@v6with:push:trueprovenance:mode=maxtags:${{ steps.meta.outputs.tags }}
```

## [SBOM](#sbom)

SBOM attestations aren't automatically added to the image. To add SBOM attestations, set the `sbom` input of the `docker/build-push-action` to true.

Note that adding attestations to an image means you must push the image to a registry directly, as opposed to loading the image to the local image store of the runner. This is because the local image store doesn't support loading images with attestations.

```
name:cion:push:env:IMAGE_NAME:user/appjobs:docker:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Extract metadataid:metauses:docker/metadata-action@v5with:images:${{ env.IMAGE_NAME }}- name:Build and push imageuses:docker/build-push-action@v6with:sbom:truepush:truetags:${{ steps.meta.outputs.tags }}
```