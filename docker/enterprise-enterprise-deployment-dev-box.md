---
title: Microsoft Dev Box
url: https://docs.docker.com/enterprise/enterprise-deployment/dev-box/
source: llms
fetched_at: 2026-01-24T14:26:18.854950187-03:00
rendered_js: false
word_count: 363
summary: This document provides an overview and step-by-step instructions for setting up and using Docker Desktop within the Microsoft Dev Box cloud environment.
tags:
    - docker-desktop
    - microsoft-dev-box
    - azure-marketplace
    - cloud-development
    - containerization
    - wsl2
    - dev-box-setup
category: guide
---

## Docker Desktop in Microsoft Dev Box

Table of contents

* * *

Docker Desktop is available as a pre-configured image in the Microsoft Azure Marketplace for use with Microsoft Dev Box, allowing developers to quickly set up consistent development environments in the cloud.

Microsoft Dev Box provides cloud-based, pre-configured developer workstations that allow you to code, build, and test applications without configuring a local development environment. The Docker Desktop image for Microsoft Dev Box comes with Docker Desktop and its dependencies pre-installed, giving you a ready-to-use containerized development environment.

## [Key benefits](#key-benefits)

- Pre-configured environment: Docker Desktop, WSL2, and other requirements come pre-installed and configured
- Consistent development: Ensure all team members work with the same Docker environment
- Powerful resources: Access more compute power and storage than might be available on local machines
- State persistence: Dev Box maintains your state between sessions, similar to hibernating a local machine
- Seamless licensing: Use your existing Docker subscription or purchase a new one directly through Azure Marketplace

## [Setup](#setup)

### [Prerequisites](#prerequisites)

- An Azure subscription
- Access to Microsoft Dev Box
- A Docker subscription (Pro, Team, or Business). You can use Docker Desktop in Microsoft Dev Box with any of the following subscription options:
  
  - An existing or new Docker subscription
  - A new Docker subscription purchased through Azure Marketplace
  - A Docker Business subscription with SSO configured for your organization

### [Set up Docker Desktop in Dev Box](#set-up-docker-desktop-in-dev-box)

1. Navigate to the [Docker Desktop for Microsoft Dev Box](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dockerinc1694120899427.devbox_azuremachine?tab=Overview) listing in Azure Marketplace.
2. Select **Get It Now** to add the virtual machine image to your subscription.
3. Follow the Azure workflow to complete the setup.
4. Use the image to create VMs, assign to Dev Centers, or create Dev Box Pools according to your organization's setup.

### [Activate Docker Desktop](#activate-docker-desktop)

Once your Dev Box is provisioned with the Docker Desktop image:

1. Start your Dev Box instance.
2. Launch Docker Desktop.
3. Sign in with your Docker ID.

## [Support](#support)

For issues related to:

- Docker Desktop configuration, usage, or licensing: Create a support ticket through [Docker Support](https://hub.docker.com/support).
- Dev Box creation, Azure portal configuration, or networking: Contact Azure Support.

## [Limitations](#limitations)

- Microsoft Dev Box is currently only available on Windows 10 and 11 (Linux VMs are not supported).
- Performance may vary based on your Dev Box configuration and network conditions.