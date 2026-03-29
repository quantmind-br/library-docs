---
title: Tags and labels
url: https://docs.docker.com/build/ci/github-actions/manage-tags-labels/
source: llms
fetched_at: 2026-01-24T14:16:30.233913799-03:00
rendered_js: false
word_count: 0
summary: This document defines a GitHub Actions workflow for automating the generation of Docker metadata and building and pushing container images to multiple registries.
tags:
    - github-actions
    - docker-images
    - ci-cd
    - container-registry
    - docker-buildx
    - workflow-automation
category: configuration
---

```
name:cion:schedule:- cron:"0 10 * * *"push:branches:- "**"tags:- "v*.*.*"pull_request:jobs:docker:runs-on:ubuntu-lateststeps:- name:Docker metaid:metauses:docker/metadata-action@v5with:# list of Docker images to use as base name for tagsimages:|            name/app
            ghcr.io/username/app# generate Docker tags based on the following events/attributestags:|            type=schedule
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=semver,pattern={{major}}
            type=sha- name:Login to Docker Hubif:github.event_name != 'pull_request'uses:docker/login-action@v3with:username:${{ vars.DOCKERHUB_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Login to GHCRif:github.event_name != 'pull_request'uses:docker/login-action@v3with:registry:ghcr.iousername:${{ github.repository_owner }}password:${{ secrets.GITHUB_TOKEN }}- name:Set up QEMUuses:docker/setup-qemu-action@v3- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Build and pushuses:docker/build-push-action@v6with:push:${{ github.event_name != 'pull_request' }}tags:${{ steps.meta.outputs.tags }}labels:${{ steps.meta.outputs.labels }}
```