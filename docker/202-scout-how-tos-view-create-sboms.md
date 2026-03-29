---
title: Docker Scout SBOMs
url: https://docs.docker.com/scout/how-tos/view-create-sboms/
source: llms
fetched_at: 2026-01-24T14:28:46.328160689-03:00
rendered_js: false
word_count: 339
summary: This document explains how Docker Scout uses and generates Software Bill of Materials (SBOM) for image analysis and provides instructions for viewing, attaching, and extracting SBOM data.
tags:
    - docker-scout
    - sbom
    - software-bill-of-materials
    - image-analysis
    - docker-build
    - attestations
    - container-security
category: guide
---

[Image analysis](https://docs.docker.com/scout/explore/analysis/) uses image SBOMs to understand what packages and versions an image contains. Docker Scout uses SBOM attestations if available on the image (recommended). If no SBOM attestation is available, Docker Scout creates one by indexing the image contents.

To view the contents of the SBOM that Docker Scout generates, you can use the `docker scout sbom` command.

By default, this prints the SBOM in a JSON format to stdout. The default JSON format produced by `docker scout sbom` isn't SPDX-JSON. To output SPDX, use the `--format spdx` flag:

To generate a human-readable list, use the `--format list` flag:

For more information about the `docker scout sbom` command, refer to the [CLI reference](https://docs.docker.com/reference/cli/docker/scout/sbom/).

You can generate the SBOM and attach it to the image at build-time as an [attestation](https://docs.docker.com/build/metadata/attestations/). BuildKit provides a default SBOM generator which is different from what Docker Scout uses. You can configure BuildKit to use the Docker Scout SBOM generator using the `--attest` flag for the `docker build` command. The Docker Scout SBOM indexer provides richer results and ensures better compatibility with the Docker Scout image analysis.

To build images with SBOM attestations, you must use either the [containerd image store](https://docs.docker.com/desktop/features/containerd/) feature, or use a `docker-container` builder together with the `--push` flag to push the image (with attestations) directly to a registry. The classic image store doesn't support manifest lists or image indices, which is required for adding attestations to an image.

The command for extracting the SBOM of an image to an SPDX JSON file is different depending on whether the image has been pushed to a registry or if it's a local image.

### [Remote image](#remote-image)

To extract the SBOM of an image and save it to a file, you can use the `docker buildx imagetools inspect` command. This command only works for images in a registry.

### [Local image](#local-image)

To extract the SPDX file for a local image, build the image with the `local` exporter and use the `scout-sbom-indexer` SBOM generator plugin.

The following command saves the SBOM to a file at `build/sbom.spdx.json`.