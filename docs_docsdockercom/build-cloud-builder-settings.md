---
title: Builder settings
url: https://docs.docker.com/build-cloud/builder-settings/
source: llms
fetched_at: 2026-01-24T14:14:49.580107902-03:00
rendered_js: false
word_count: 473
summary: This document provides instructions for managing Docker Build Cloud settings such as cache disk allocation, private resource connectivity, and outbound firewall rules.
tags:
    - docker-build-cloud
    - builder-settings
    - disk-allocation
    - private-resource-access
    - firewall-settings
    - cache-management
category: configuration
---

The **Builder settings** page in Docker Build Cloud lets you configure disk allocation, private resource access, and firewall settings for your cloud builders in your organization. These configurations help optimize storage, enable access to private registries, and secure outbound network traffic.

### [Disk allocation](#disk-allocation)

The **Disk allocation** setting lets you control how much of the available storage is dedicated to the build cache. A lower allocation increases storage available for active builds.

To make disk allocation changes, navigate to **Builder settings** in Docker Build Cloud and then adjust the **Disk allocation** slider to specify the percentage of storage used for build caching.

Any changes take effect immediately.

### [Build cache space](#build-cache-space)

Your subscription includes the following Build cache space:

SubscriptionBuild cache spacePersonalN/APro50GBTeam100GBBusiness200GB

### [Multi-architecture storage allocation](#multi-architecture-storage-allocation)

Docker Build Cloud automatically provisions builders for both amd64 and arm64 architectures. Your total build cache space is split equally between these two builders:

- Pro (50GB total): 25GB for amd64 builder + 25GB for arm64 builder
- Team (100GB total): 50GB for amd64 builder + 50GB for arm64 builder
- Business (200GB total): 100GB for amd64 builder + 100GB for arm64 builder

> If you only build for one architecture, be aware that your effective cache space is half of your subscription's total allocation.

### [Get more build cache space](#get-more-build-cache-space)

To get more Build cache space, [upgrade your subscription](https://docs.docker.com/subscription/scale/).

> If you build large images, consider allocating less storage for caching to leave more space for active builds.

Private resource access lets cloud builders pull images and packages from private resources. This feature is useful when builds rely on self-hosted artifact repositories or private OCI registries.

For example, if your organization hosts a private [PyPI](https://pypi.org/) repository on a private network, Docker Build Cloud would not be able to access it by default, since the cloud builder is not connected to your private network.

To enable your cloud builders to access your private resources, enter the host name and port of your private resource and then select **Add**.

### [Authentication](#authentication)

If your internal artifacts require authentication, make sure that you authenticate with the repository either before or during the build. For internal package repositories for npm or PyPI, use [build secrets](https://docs.docker.com/build/building/secrets/) to authenticate during the build. For internal OCI registries, use `docker login` to authenticate before building.

Note that if you use a private registry that requires authentication, you will need to authenticate with `docker login` twice before building. This is because the cloud builder needs to authenticate with Docker to use the cloud builder, and then again to authenticate with the private registry.

Firewall settings let you restrict cloud builder egress traffic to specific IP addresses. This helps enhance security by limiting external network egress from the builder.

1. Select the **Enable firewall: Restrict cloud builder egress to specific public IP address** checkbox.
2. Enter the IP address you want to allow.
3. Select **Add** to apply the restriction.