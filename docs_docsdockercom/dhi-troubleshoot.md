---
title: Troubleshoot
url: https://docs.docker.com/dhi/troubleshoot/
source: llms
fetched_at: 2026-01-24T14:21:21.490697416-03:00
rendered_js: false
word_count: 451
summary: This document provides troubleshooting steps and solutions for common issues encountered when using Docker Hardened Images, such as debugging, permission constraints, and environment limitations.
tags:
    - docker-hardened-images
    - troubleshooting
    - container-security
    - docker-debug
    - non-root
    - port-binding
category: guide
---

The following are common issues you may encounter while migrating to or using Docker Hardened Images (DHIs), along with recommended solutions.

Docker Hardened Images are optimized for security and runtime performance. As such, they typically don't include a shell or standard debugging tools. The recommended way to troubleshoot containers built on DHIs is by using [Docker Debug](https://docs.docker.com/dhi/how-to/debug/).

Docker Debug allows you to:

- Attach a temporary debug container to your existing container.
- Use a shell and familiar tools such as `curl`, `ps`, `netstat`, and `strace`.
- Install additional tools as needed in a writable, ephemeral layer that disappears after the session.

DHIs run as a nonroot user by default for enhanced security. This can result in permission issues when accessing files or directories. Ensure your application files and runtime directories are owned by the expected UID/GID or have appropriate permissions.

To find out which user a DHI runs as, check the repository page for the image on Docker Hub. See [View image variant details](https://docs.docker.com/dhi/how-to/explore/#view-image-variant-details) for more information.

Nonroot containers cannot bind to ports below 1024 by default. This is enforced by both the container runtime and the kernel (especially in Kubernetes and Docker Engine &lt; 20.10).

Inside the container, configure your application to listen on an unprivileged port (1025 or higher). For example `docker run -p 80:8080 my-image` maps port 8080 in the container to port 80 on the host, allowing you to access it without needing root privileges.

Runtime DHIs omit interactive shells like `sh` or `bash`. If your build or tooling assumes a shell is present (e.g., for `RUN` instructions), use a `dev` variant of the image in an earlier build stage and copy the final artifact into the runtime image.

To find out which shell, if any, a DHI has, check the repository page for the image on Docker Hub. See [View image variant details](https://docs.docker.com/dhi/how-to/explore/#view-image-variant-details) for more information.

Also, use [Docker Debug](https://docs.docker.com/dhi/how-to/debug/) when you need shell access to a running container.

## [Entry point differences](#entry-point-differences)

DHIs may define different entry points compared to Docker Official Images (DOIs) or other community images.

To find out the ENTRYPOINT or CMD for a DHI, check the repository page for the image on Docker Hub. See [View image variant details](https://docs.docker.com/dhi/how-to/explore/#view-image-variant-details) for more information.

Runtime Docker Hardened Images are stripped down for security and minimal attack surface. As a result, they don't include a package manager such as `apk` or `apt`. This means you can't install additional software directly in the runtime image.

If your build or application setup requires installing packages (for example, to compile code, install runtime dependencies, or add diagnostic tools), use a `dev` variant of the image in a build stage. Then, copy only the necessary artifacts into the final runtime image.