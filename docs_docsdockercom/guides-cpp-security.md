---
title: Supply-chain security
url: https://docs.docker.com/guides/cpp/security/
source: llms
fetched_at: 2026-01-24T14:08:53.981224475-03:00
rendered_js: false
word_count: 389
summary: This document explains how to generate and attach Software Bill of Materials (SBOM) attestations to C++ Docker images to improve supply-chain security. It specifically covers using Docker Scout and Buildx to handle SBOM creation for scratch-based images.
tags:
    - docker
    - cpp
    - sbom
    - supply-chain-security
    - container-security
    - docker-scout
    - attestations
    - buildx
category: tutorial
---

## Supply-chain security for C++ Docker images

## [Prerequisites](#prerequisites)

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.
- You have a Docker Desktop installed, with containerd enabled for pulling and storing images (it's a checkbox in **Settings** &gt; **General**). Otherwise, if you use Docker Engine:
  
  - You have the [Docker SBOM CLI plugin](https://github.com/docker/sbom-cli-plugin) installed. To install it on Docker Engine, use the following command:
    
    ```
    $ curl -sSfL https://raw.githubusercontent.com/docker/sbom-cli-plugin/main/install.sh | sh -s --
    ```
  - You have the [Docker Scout CLI plugin](https://docs.docker.com/scout/install/) installed. To install it on Docker Engine, use the following command:
    
    ```
    $ curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s --
    ```
  - You have [containerd enabled](https://docs.docker.com/engine/storage/containerd/) for Docker Engine.

## [Overview](#overview)

This section walks you through extracting Software Bill of Materials (SBOMs) from a C++ Docker image using the Docker SBOM CLI plugin. SBOMs provide a detailed list of all the components in a software package, including their versions and licenses. You can use SBOMs to track the provenance of your software and ensure that it complies with your organization's security and licensing policies.

## [Generate an SBOM](#generate-an-sbom)

Here we will use the Docker image that we built in the [Create a multi-stage build for your C++ application](https://docs.docker.com/guides/language/cpp/multistage/) guide. If you haven't already built the image, follow the steps in that guide to build the image. The image is named `hello`. To generate an SBOM for the `hello` image, run the following command:

The command will say "No packages discovered". This is because the final image is a scratch image and doesn't have any packages. Let's try again with Docker Scout:

```
$ docker scout sbom --format=list hello
```

This command will tell you the same thing.

## [Generate an SBOM attestation](#generate-an-sbom-attestation)

The SBOM can be generated during the build process and "attached" to the image. This is called an SBOM attestation. To generate an SBOM attestation for the `hello` image, first let's change the Dockerfile:

```
ARG BUILDKIT_SBOM_SCAN_STAGE=true
FROMubuntu:latestASbuildRUN apt-get update && apt-get install -y build-essentialWORKDIR/appCOPY hello.cpp .RUN g++ -o hello hello.cpp -static# --------------------FROMscratchCOPY --from=build /app/hello /helloCMD ["/hello"]
```

The first line `ARG BUILDKIT_SBOM_SCAN_STAGE=true` enables SBOM scanning in the build stage. Now, build the image with the following command:

```
$ docker buildx build --sbom=true -t hello:sbom .
```

This command will build the image and generate an SBOM attestation. You can verify that the SBOM is attached to the image by running the following command:

```
$ docker scout sbom --format=list hello:sbom
```

Note that the normal `docker sbom` command will not load the SBOM attestation.

## [Summary](#summary)

In this section, you learned how to generate SBOM attestation for a C++ Docker image during the build process. The normal image scanners will not be able to generate SBOMs from scratch images.