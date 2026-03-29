---
title: GitHub Actions
url: https://docs.docker.com/scout/integrations/ci/gha/
source: llms
fetched_at: 2026-01-24T14:29:01.420817558-03:00
rendered_js: false
word_count: 300
summary: This document explains how to integrate Docker Scout into a GitHub Actions workflow to compare container images between development and production environments. It focuses on using the compare command to visualize policy compliance and vulnerability changes within pull requests.
tags:
    - docker-scout
    - github-actions
    - container-security
    - ci-cd
    - image-comparison
    - policy-compliance
    - vulnerability-analysis
category: tutorial
---

The following example shows how to set up a Docker Scout workflow with GitHub Actions. Triggered by a pull request, the action builds the image and uses Docker Scout to compare the new version to the version of that image running in production.

This workflow uses the [docker/scout-action](https://github.com/docker/scout-action) GitHub Action to run the `docker scout compare` command to visualize how images for pull request stack up against the image you run in production.

First, set up the GitHub Action workflow to build an image. This isn't specific to Docker Scout here, but you'll need to build an image to have something to compare with.

This CI workflow runs a local analysis and evaluation of your image. To evaluate the image locally, you must ensure that the image is loaded the local image store of your runner.

This comparison doesn't work if you push the image to a registry, or if you build an image that can't be loaded to the runner's local image store. For example, multi-platform images or images with SBOM or provenance attestation can't be loaded to the local image store.

With this setup out of the way, you can add the following steps to run the image comparison:

The compare command analyzes the image and evaluates policy compliance, and cross-references the results with the corresponding image in the `production` environment. This example only includes critical and high-severity vulnerabilities, and excludes vulnerabilities that exist in both images, showing only what's changed.

The GitHub Action outputs the comparison results in a pull request comment by default.

Expand the **Policies** section to view the difference in policy compliance between the two images. Note that while the new image in this example isn't fully compliant, the output shows that the standing for the new image has improved compared to the baseline.