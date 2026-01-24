---
title: Deploy with Intune
url: https://docs.docker.com/enterprise/enterprise-deployment/use-intune/
source: llms
fetched_at: 2026-01-24T14:26:24.138967946-03:00
rendered_js: false
word_count: 114
summary: This document provides instructions for configuring the installation of Docker Desktop via Microsoft Intune, including custom install commands and handling system reboots.
tags:
    - docker-desktop
    - microsoft-intune
    - windows-installation
    - msiexec
    - deployment-configuration
category: configuration
---

Optional: On the **Program** tab, you can update the **Install command** field to suit your needs. The field is pre-populated with `msiexec /i "DockerDesktop.msi" /qn`. See the [Common installation scenarios](https://docs.docker.com/enterprise/enterprise-deployment/msi-install-and-configure/) for examples on the changes you can make.

It's recommended you configure the Intune deployment to schedule a reboot of the machine on successful installs.

This is because the Docker Desktop installer installs Windows features depending on your engine selection and also updates the membership of the `docker-users` local group.

You may also want to set Intune to determine behaviour based on return codes and watch for a return code of `3010`. Return code 3010 means the installation succeeded but a reboot is required.