---
title: FAQs
url: https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/faq/
source: llms
fetched_at: 2026-01-24T14:26:34.613367237-03:00
rendered_js: false
word_count: 337
summary: This document provides answers to frequently asked questions about Enhanced Container Isolation (ECI), addressing administrative concerns regarding workflow impact, performance, and security configurations in Docker Desktop.
tags:
    - enhanced-container-isolation
    - docker-security
    - container-security
    - sysbox-runtime
    - docker-desktop
    - eci
category: reference
---

## Enhanced Container Isolation FAQs

Subscription: Business

For: Administrators

This page answers common questions about Enhanced Container Isolation (ECI) that aren't covered in the main documentation.

No. ECI works automatically in the background by creating more secure containers. You can continue using all your existing Docker commands, workflows, and development tools without any changes.

Most container workloads run without issues when ECI is turned on. However, some advanced workloads that require specific kernel-level access may not work. For details about which workloads are affected, see [ECI limitations](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/limitations/).

Privileged containers serve legitimate purposes like Docker-in-Docker, Kubernetes-in-Docker, and accessing hardware devices. ECI provides a better solution by allowing these advanced workloads to run securely while preventing them from compromising the Docker Desktop VM.

ECI has minimal impact on container performance. The only exception is containers that perform many `mount` and `umount` system calls, as these are inspected by the Sysbox runtime for security. Most development workloads see no noticeable performance difference.

No. When ECI is turned on, all containers use the Sysbox runtime regardless of any `--runtime` flags:

The `--runtime` flag is ignored to prevent users from bypassing ECI security by running containers as true root in the Docker Desktop VM.

No. ECI only protects containers created after it's turned on. Remove existing containers before turning on ECI:

For more details, see [Enable Enhanced Container Isolation](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/enable-eci/).

ECI protection varies by container type and Docker Desktop version:

### [Always protected](#always-protected)

- Containers created with `docker run` and `docker create`
- Containers using the `docker-container` build driver

### [Version dependent](#version-dependent)

- Docker Build: Protected in Docker Desktop 4.30+ (except WSL 2)
- Kubernetes: Protected in Docker Desktop 4.38+ when using the kind provisioner

### [Not protected](#not-protected)

- Docker Extensions
- Docker Debug containers
- Kubernetes with Kubeadm provisioner

For complete details, see [ECI limitations](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/limitations/).

By default, no. ECI blocks Docker socket bind mounts for security. However, you can configure exceptions for trusted images like Testcontainers.

For configuration details, see [Configure Docker socket exceptions](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/).

ECI restricts bind mounts of Docker Desktop VM directories but allows host directory mounts configured in Docker Desktop Settings.