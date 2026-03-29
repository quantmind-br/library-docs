---
title: Configure advanced settings
url: https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/
source: llms
fetched_at: 2026-01-24T14:26:32.439580604-03:00
rendered_js: false
word_count: 617
summary: This document explains how to configure Docker socket exceptions and advanced security settings for Enhanced Container Isolation using Docker Desktop settings management.
tags:
    - docker-desktop
    - enhanced-container-isolation
    - security-hardening
    - docker-socket
    - settings-management
    - administration
category: configuration
---

## Configure Docker socket exceptions and advanced settings

Subscription: Business

For: Administrators

This page shows you how to configure Docker socket exceptions and other advanced settings for Enhanced Container Isolation (ECI). These configurations enable trusted tools like Testcontainers to work with ECI while maintaining security.

By default, Enhanced Container Isolation blocks containers from mounting the Docker socket to prevent malicious access to Docker Engine. However, some tools require Docker socket access.

Common scenarios requiring Docker socket access include:

- Testing frameworks: Testcontainers, which manages test containers
- Build tools: Paketo buildpacks that create ephemeral build containers
- CI/CD tools: Tools that manage containers as part of deployment pipelines
- Development utilities: Docker CLI containers for container management

Configure Docker socket exceptions using Settings Management:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization from the top-left account drop-down.
2. Go to **Admin Console** &gt; **Desktop Settings Management**.
3. [Create or edit a setting policy](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/).
4. Find **Enhanced Container Isolation** settings.
5. Configure **Docker socket access control** with your trusted images and command restrictions.

The `imageList` defines which container images can mount the Docker socket.

### [Image reference formats](#image-reference-formats)

FormatDescription`<image_name>[:<tag>]`Name of the image, with optional tag. If the tag is omitted, the `:latest` tag is used. If the tag is the wildcard `*`, then it means "any tag for that image."`<image_name>@<digest>`Name of the image, with a specific repository digest (e.g., as reported by `docker buildx imagetools inspect <image>`). This means only the image that matches that name and digest is allowed.

### [Example configurations](#example-configurations)

Basic allowlist for testing tools:

Wildcard allowlist (Docker Desktop 4.36 and later):

> Using `"*"` allows all containers to mount the Docker socket, which reduces security. Only use this when explicitly listing allowed images isn't feasible.

### [Security validation](#security-validation)

Docker Desktop validates allowed images by:

1. Downloading image digests from registries for allowed images
2. Comparing container image digests against the allowlist when containers start
3. Blocking containers whose digests don't match allowed images

This prevents bypassing restrictions by re-tagging unauthorized images:

For tools like Paketo buildpacks that create ephemeral local images, you can allow images derived from trusted base images.

### [Enable derived images](#enable-derived-images)

When `allowDerivedImages` is true, local images built from allowed base images (using `FROM` in Dockerfile) also gain Docker socket access.

### [Derived images requirements](#derived-images-requirements)

- Local images only: Derived images must not exist in remote registries
- Base image available: The parent image must be pulled locally first
- Performance impact: Adds up to 1 second to container startup for validation
- Version compatibility: Full wildcard support requires Docker Desktop 4.36+

### [Deny list (recommended)](#deny-list-recommended)

Blocks specified commands while allowing all others:

### [Allow list](#allow-list)

Only allows specified commands while blocking all others:

### [Command wildcards](#command-wildcards)

WildcardBlocks/allows`"container\*"`All "docker container ..." commands`"image\*"`All "docker image ..." commands`"volume\*"`All "docker volume ..." commands`"network\*"`All "docker network ..." commands`"build\*"`All "docker build ..." commands`"system\*"`All "docker system ..." commands

### [Command blocking example](#command-blocking-example)

When a blocked command is executed:

### [Testcontainers setup](#testcontainers-setup)

For Java/Python testing with Testcontainers:

### [CI/CD pipeline tools](#cicd-pipeline-tools)

For controlled CI/CD container management:

### [Development environments](#development-environments)

For local development with Docker-in-Docker:

### [Image allowlist best practices](#image-allowlist-best-practices)

- Be restrictive: Only allow images you absolutely trust and need
- Use wildcards carefully: Tag wildcards (`*`) are convenient but less secure than specific tags
- Regular reviews: Periodically review and update your allowlist
- Digest pinning: Use digest references for maximum security in critical environments

### [Command restrictions](#command-restrictions-1)

- Default to deny: Start with a deny list blocking dangerous commands like `push` and `build`
- Principle of least privilege: Only allow commands your tools actually need
- Monitor usage: Track which commands are being blocked to refine your configuration

### [Monitoring and maintenance](#monitoring-and-maintenance)

- Regular validation: Test your configuration after Docker Desktop updates, as image digests may change.
- Handle digest mismatches: If allowed images are unexpectedly blocked:

This resolves digest mismatches when upstream images are updated.

- Review [Enhanced Container Isolation limitations](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/limitations/).
- Review [Enhanced Container Isolation FAQs](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/faq/).