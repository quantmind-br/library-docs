---
title: Use an image
url: https://docs.docker.com/dhi/how-to/use/
source: llms
fetched_at: 2026-01-24T14:21:01.094171221-03:00
rendered_js: false
word_count: 1081
summary: This document explains how to pull and implement Docker Hardened Images (DHIs), focusing on security features like minimal runtimes, non-root defaults, and multi-stage build patterns.
tags:
    - docker-hardened-images
    - container-security
    - dockerfile
    - multi-stage-builds
    - image-hardening
    - security-best-practices
category: guide
---

## Use a Docker Hardened Image

You can use a Docker Hardened Image (DHI) just like any other image on Docker Hub. DHIs follow the same familiar usage patterns. Pull them with `docker pull`, reference them in your Dockerfile, and run containers with `docker run`.

The key difference is that DHIs are security-focused and intentionally minimal to reduce the attack surface. This means some variants don't include a shell or package manager, and may run as a nonroot user by default.

> You must authenticate to the Docker Hardened Images registry (`dhi.io`) to pull images. Use your Docker ID credentials (the same username and password you use for Docker Hub) when signing in. If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

Docker Hardened Images are intentionally minimal to improve security. If you're updating existing Dockerfiles or frameworks to use DHIs, keep the following considerations in mind:

FeatureDetailsNo shell or package managerRuntime images don’t include a shell or package manager. Use `-dev` or `-sdk` variants in build stages to run shell commands or install packages, and then copy artifacts to a minimal runtime image.Non-root runtimeRuntime DHIs default to running as a non-root user. Ensure your application doesn't require privileged access and that all needed files are readable and executable by a non-root user.PortsApplications running as non-root users can't bind to ports below 1024 in older versions of Docker or in some Kubernetes configurations. Use ports above 1024 for compatibility.Entry pointDHIs may not include a default entrypoint or might use a different one than the original image you're familiar with. Check the image configuration and update your `CMD` or `ENTRYPOINT` directives accordingly.Multi-stage buildsAlways use multi-stage builds for frameworks: a `-dev` image for building or installing dependencies, and a minimal runtime image for the final stage.TLS certificatesDHIs include standard TLS certificates. You do not need to manually install CA certs.

If you're migrating an existing application, see [Migrate an existing application to use Docker Hardened Images](https://docs.docker.com/dhi/migration/).

To use a DHI as the base image for your container, specify it in the `FROM` instruction in your Dockerfile:

Replace the image name and tag with the variant you want to use. For example, use a `-dev` tag if you need a shell or package manager during build stages:

To learn how to explore available variants, see [Explore images](https://docs.docker.com/dhi/how-to/explore/).

> Use a multi-stage Dockerfile to separate build and runtime stages, using a `-dev` variant in build stages and a minimal runtime image in the final stage.

Just like any other image, you can pull DHIs using tools such as the Docker CLI or within your CI pipelines.

You can pull Docker Hardened Images from three different locations depending on your needs:

- Directly from `dhi.io`
- From a mirror on Docker Hub
- From a mirror on a third-party registry

To understand which approach is right for your use case, see [Mirror a Docker Hardened Image repository](https://docs.docker.com/dhi/how-to/mirror/).

The following sections show how to pull images from each location.

### [Pull directly from dhi.io](#pull-directly-from-dhiio)

After authenticating to `dhi.io`, you can pull images using standard Docker commands:

Reference images in your Dockerfile:

### [Pull from a mirror on Docker Hub](#pull-from-a-mirror-on-docker-hub)

Once you've mirrored a repository to Docker Hub, you can pull images from your organization's namespace:

Reference mirrored images in your Dockerfile:

To learn how to mirror repositories, see [Mirror a DHI repository to Docker Hub](https://docs.docker.com/dhi/how-to/mirror/#mirror-a-dhi-repository-to-docker-hub).

### [Pull from a mirror on a third-party registry](#pull-from-a-mirror-on-a-third-party-registry)

Once you've mirrored a repository to your third-party registry, you can pull images:

Reference third-party mirrored images in your Dockerfile:

To learn more, see [Mirror to a third-party registry](https://docs.docker.com/dhi/how-to/mirror/#mirror-to-a-third-party-registry).

After pulling the image, you can run it using `docker run`. For example:

Docker Hardened Images work just like any other image in your CI/CD pipelines. You can reference them in Dockerfiles, pull them as part of a pipeline step, or run containers based on them during builds and tests.

Unlike typical container images, DHIs also include signed [attestations](https://docs.docker.com/dhi/core-concepts/attestations/) such as SBOMs and provenance metadata. You can incorporate these into your pipeline to support supply chain security, policy checks, or audit requirements if your tooling supports it.

To strengthen your software supply chain, consider adding your own attestations when building images from DHIs. This lets you document how the image was built, verify its integrity, and enable downstream validation and policy enforcement using tools like Docker Scout.

To learn how to attach attestations during the build process, see [Docker Build Attestations](https://docs.docker.com/build/metadata/attestations/).

Docker Hardened Images include a `static` image repository designed specifically for running compiled executables in an extremely minimal and secure runtime.

Unlike a non-hardened `FROM scratch` image, the DHI `static` image includes all the attestations needed to verify its integrity and provenance. Although it is minimal, it includes the common packages needed to run containers securely, such as `ca-certificates`.

Use a `-dev` or other builder image in an earlier stage to compile your binary, and copy the output into a `static` image.

The following example shows a multi-stage Dockerfile that builds a Go application and runs it in a minimal static image:

This pattern ensures a hardened runtime environment with no unnecessary components, reducing the attack surface to a bare minimum.

If you're building applications with frameworks that require package managers or build tools (such as Python, Node.js, or Go), use a `-dev` variant during the development or build stage. These variants include essential utilities like shells, compilers, and package managers to support local iteration and CI workflows.

Use `-dev` images in your inner development loop or in isolated CI stages to maximize productivity. Once you're ready to produce artifacts for production, switch to a smaller runtime variant to reduce the attack surface and image size.

Dev variants are typically configured with no `ENTRYPOINT` and a default `CMD` that launches a shell (for example, \["/bin/bash"]). In those cases, running the container without additional arguments starts an interactive shell by default.

The following example shows how to build a Python app using a `-dev` variant and run it using the smaller runtime variant:

This pattern separates the build environment from the runtime environment, helping reduce image size and improve security by removing unnecessary tooling from the final image.

Subscription: Docker Hardened Images Enterprise

When you have a Docker Hardened Images Enterprise subscription, you can access compliance variants such as FIPS-enabled and STIG-ready images. These variants help meet regulatory and compliance requirements for secure deployments.

To use a compliance variant, you must first [mirror](https://docs.docker.com/dhi/how-to/mirror/) the repository, and then pull the compliance image from your mirrored repository.