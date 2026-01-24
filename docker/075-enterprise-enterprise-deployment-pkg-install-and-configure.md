---
title: PKG installer
url: https://docs.docker.com/enterprise/enterprise-deployment/pkg-install-and-configure/
source: llms
fetched_at: 2026-01-24T14:26:22.787812921-03:00
rendered_js: false
word_count: 123
summary: This document explains how the Docker Desktop PKG package facilitates enterprise deployment via MDM solutions and outlines its specific update management procedures.
tags:
    - docker-desktop
    - mdm-solutions
    - pkg-package
    - enterprise-deployment
    - software-updates
category: guide
---

The PKG package supports various MDM (Mobile Device Management) solutions, making it ideal for bulk installations and eliminating the need for manual setups by individual users. With this package, IT administrators can ensure standardized, policy-driven installations of Docker Desktop, enhancing efficiency and software management across their organizations.

When installing Docker Desktop with the PKG, in-app updates are automatically disabled. This ensures organizations can maintain version consistency and prevent unapproved updates. For Docker Desktop installed with the `.dmg` installer, in-app updates remain supported.

Docker Desktop notifies you when an update is available. To update Docker Desktop, download the latest installer from the Docker Admin Console. Navigate to the **Enterprise deployment** page.

To keep up to date with new releases, check the [release notes](https://docs.docker.com/desktop/release-notes/) page.