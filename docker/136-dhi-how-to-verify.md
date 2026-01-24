---
title: Verify an image or chart
url: https://docs.docker.com/dhi/how-to/verify/
source: llms
fetched_at: 2026-01-24T14:21:05.883663158-03:00
rendered_js: false
word_count: 984
summary: This document provides instructions for verifying the security posture and build integrity of Docker Hardened Images and Helm charts using Docker Scout and cosign. It explains how to authenticate, list available attestations, and validate signatures for SBOMs, provenance, and vulnerability reports.
tags:
    - docker-scout
    - docker-hardened-images
    - attestations
    - security-verification
    - helm-charts
    - cosign
    - sbom
category: guide
---

## Verify a Docker Hardened Image or chart

Docker Hardened Images (DHI) and charts include signed attestations that verify the build process, contents, and security posture. These attestations are available for each image variant and chart and can be verified using [cosign](https://docs.sigstore.dev/) or the Docker Scout CLI.

Docker's public key for DHI images and charts is published at:

- [https://registry.scout.docker.com/keyring/dhi/latest.pub](https://registry.scout.docker.com/keyring/dhi/latest.pub)
- [https://github.com/docker-hardened-images/keyring](https://github.com/docker-hardened-images/keyring)

> You must authenticate to the Docker Hardened Images registry (`dhi.io`) to pull images. Use your Docker ID credentials (the same username and password you use for Docker Hub) when signing in. If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

You can use the [Docker Scout](https://docs.docker.com/scout/) CLI to list and retrieve attestations for Docker Hardened Images.

> Before you run `docker scout attest` commands, ensure any image that you have pulled locally is up to date with the remote image. You can do this by running `docker pull`. If you don't do this, you may see `No attestation found`.

### [Why use Docker Scout instead of cosign directly?](#why-use-docker-scout-instead-of-cosign-directly)

While you can use cosign to verify attestations manually, the Docker Scout CLI offers several key advantages when working with Docker Hardened Images and charts:

- Purpose-built experience: Docker Scout understands the structure of DHI attestations and naming conventions, so you don't have to construct full digests or URIs manually.
- Automatic platform resolution: With Scout, you can specify the platform (e.g., `--platform linux/amd64`), and it automatically verifies the correct image variant. Cosign requires you to look up the digest yourself.
- Human-readable summaries: Scout returns summaries of attestation contents (e.g., package counts, provenance steps), whereas cosign only returns raw signature validation output.
- One-step validation: The `--verify` flag in `docker scout attest get` validates the attestation and shows the equivalent cosign command, making it easier to understand what's happening behind the scenes.
- Integrated with Docker Hub and DHI trust model: Docker Scout is tightly integrated with Docker’s attestation infrastructure and public keyring, ensuring compatibility and simplifying verification for users within the Docker ecosystem.

In short, Docker Scout streamlines the verification process and reduces the chances of human error, while still giving you full visibility and the option to fall back to cosign when needed.

### [List available attestations](#list-available-attestations)

To list attestations for a mirrored DHI image:

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

This command shows all available attestations, including SBOMs, provenance, vulnerability reports, and more.

### [Retrieve a specific attestation](#retrieve-a-specific-attestation)

To retrieve a specific attestation, use the `--predicate-type` flag with the full predicate type URI:

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

To retrieve only the predicate body:

For example:

### [Validate the attestation with Docker Scout](#validate-the-attestation-with-docker-scout)

To validate the attestation using Docker Scout, you can use the `--verify` flag:

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/node:20.19-debian12` instead of `dhi.io/node:20.19-debian12`.

For example, to verify the SBOM attestation for the `dhi.io/node:20.19-debian12` image:

#### [Handle missing transparency log entries](#handle-missing-transparency-log-entries)

When using `--verify`, you may sometimes see an error like:

This occurs because Docker Hardened Images don't always record attestations in the public [Rekor](https://docs.sigstore.dev/logging/overview/) transparency log. In cases where an attestation would contain private user information (for example, your organization's namespace in the image reference), writing it to Rekor would expose that information publicly.

Even if the Rekor entry is missing, the attestation is still signed with Docker's public key and can be verified offline by skipping the Rekor transparency log check.

To skip the transparency log check and validate against Docker's key, use the `--skip-tlog` flag:

> The `--skip-tlog` flag is only available in Docker Scout CLI version 1.18.2 and later.
> 
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

This is equivalent to using `cosign` with the `--insecure-ignore-tlog=true` flag, which validates the signature against Docker's published public key, but ignores the transparency log check.

### [Show the equivalent cosign command](#show-the-equivalent-cosign-command)

When using the `--verify` flag, it also prints the corresponding [cosign](https://docs.sigstore.dev/) command to verify the image signature:

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

If verification succeeds, Docker Scout prints the full `cosign verify` command.

Example output:

> When using cosign, you must first authenticate to both the DHI registry and the Docker Scout registry.
> 
> For example:

Docker Hardened Image Helm charts include the same comprehensive attestations as container images. The verification process for charts is identical to that for images, using the same Docker Scout CLI commands.

### [List available chart attestations](#list-available-chart-attestations)

To list attestations for a DHI Helm chart:

For example, to list attestations for the external-dns chart:

This command shows all available chart attestations, including SBOMs, provenance, vulnerability reports, and more.

### [Retrieve a specific chart attestation](#retrieve-a-specific-chart-attestation)

To retrieve a specific attestation from a Helm chart, use the `--predicate-type` flag with the full predicate type URI:

For example:

To retrieve only the predicate body:

### [Validate chart attestations with Docker Scout](#validate-chart-attestations-with-docker-scout)

To validate a chart attestation using Docker Scout, use the `--verify` flag:

For example, to verify the SBOM attestation for the external-dns chart:

The same `--skip-tlog` flag described in [Handle missing transparency log entries](#handle-missing-transparency-log-entries) can also be used with chart attestations when needed.

See [available attestations](https://docs.docker.com/dhi/core-concepts/attestations/#image-attestations) for a list of attestations available for each DHI image and [Helm chart attestations](https://docs.docker.com/dhi/core-concepts/attestations/#helm-chart-attestations) for a list of attestations available for each DHI chart.

You can also browse attestations visually when [exploring an image variant](https://docs.docker.com/dhi/how-to/explore/#view-image-variant-details). The **Attestations** section lists each available attestation with its:

- Type (e.g. SBOM, VEX)
- Predicate type URI
- Digest reference for use with `cosign`

These attestations are generated and signed automatically as part of the Docker Hardened Image or chart build process.