---
title: Code signing
url: https://docs.docker.com/dhi/core-concepts/signatures/
source: llms
fetched_at: 2026-01-24T14:19:50.401680385-03:00
rendered_js: false
word_count: 432
summary: A process of digitally signing executables and scripts to confirm the software author's identity and guarantee that the code has not been altered or corrupted since it was signed.
tags:
    - security
    - software development
    - digital signatures
    - authentication
category: guide
---

Code signing is the process of applying a cryptographic signature to software artifacts, such as Docker images, to verify their integrity and authenticity. By signing an image, you ensure that it has not been altered since it was signed and that it originates from a trusted source.

In the context of Docker Hardened Images (DHIs), code signing is achieved using [Cosign](https://docs.sigstore.dev/), a tool developed by the Sigstore project. Cosign enables secure and verifiable signing of container images, enhancing trust and security in the software supply chain.

Code signing plays a crucial role in modern software development and cybersecurity:

- Authenticity: Verifies that the image was created by a trusted source.
- Integrity: Ensures that the image has not been tampered with since it was signed.
- Compliance: Helps meet regulatory and organizational security requirements.

Each DHI is cryptographically signed using Cosign, ensuring that the images have not been tampered with and originate from a trusted source.

Docker Hardened Images are signed by Docker to prove their origin and integrity, but if you're building application images that extend or use DHIs as a base, you should sign your own images as well.

By signing your own images, you can:

- Prove the image was built by your team or pipeline
- Ensure your build hasn't been tampered with after it's pushed
- Support software supply chain frameworks like SLSA
- Enable image verification in deployment workflows

This is especially important in CI/CD environments where you build and push images frequently, or in any scenario where image provenance must be auditable.

### [View signatures](#view-signatures)

You can verify that a Docker Hardened Image is signed and trusted using either Docker Scout or Cosign.

To lists all attestations, including signature metadata, attached to the image, use the following command:

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python` instead of `dhi.io/python`.

To verify a specific signed attestation (e.g., SBOM, VEX, provenance):

> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python:3.13` instead of `dhi.io/python:3.13`.

For example:

If valid, Docker Scout will confirm the signature and display signature payload, as well as the equivalent Cosign command to verify the image.

### [Sign images](#sign-images)

To sign a Docker image, use [Cosign](https://docs.sigstore.dev/). Replace `<image-name>:<tag>` with the image name and tag.

This command will prompt you to authenticate via an OIDC provider (such as GitHub, Google, or Microsoft). Upon successful authentication, Cosign will generate a short-lived certificate and sign the image. The signature will be stored in a transparency log and associated with the image in the registry.