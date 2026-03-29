---
title: Limits · Cloudflare Sandbox SDK docs
url: https://developers.cloudflare.com/sandbox/platform/limits/index.md
source: llms
fetched_at: 2026-01-24T15:22:59.873500915-03:00
rendered_js: false
word_count: 114
summary: This document outlines the resource limits, pricing structure, and operational best practices for deploying sandboxes using the Sandbox SDK on the Cloudflare Containers platform.
tags:
    - sandbox-sdk
    - cloudflare-containers
    - resource-limits
    - best-practices
    - container-optimization
category: reference
---

Since the Sandbox SDK is built on top of the [Containers](https://developers.cloudflare.com/containers/) platform, it shares the same underlying platform characteristics. Refer to these pages to understand how pricing and limits work for your sandbox deployments.

## Container Limits

Refer to [Containers limits](https://developers.cloudflare.com/containers/platform-details/limits/) for complete details on:

* Memory, vCPU, and disk limits for concurrent container instances
* Instance types and their resource allocations
* Image size and storage limits

## Best Practices

To work within these limits:

* **Right-size your instances** - Choose the appropriate [instance type](https://developers.cloudflare.com/containers/platform-details/limits/#instance-types) based on your workload requirements
* **Clean up unused sandboxes** - Terminate sandbox sessions when they're no longer needed to free up resources
* **Optimize images** - Keep your [custom Dockerfiles](https://developers.cloudflare.com/sandbox/configuration/dockerfile/) lean to reduce image size