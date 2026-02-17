---
title: Sonatype Nexus
url: https://coolify.io/docs/services/nexus.md
source: llms
fetched_at: 2026-02-17T14:48:19.919632-03:00
rendered_js: false
word_count: 119
summary: This document provides an overview of Sonatype Nexus as a repository manager and outlines the installation and configuration steps for deploying it through Coolify.
tags:
    - sonatype-nexus
    - repository-manager
    - artifact-storage
    - coolify
    - self-hosted
    - nexus-setup
category: guide
---

## What is Sonatype Nexus

Sonatype Nexus is a repository manager that allows you to store, manage, and distribute your software artifacts. It supports multiple package formats including Maven, npm, Docker, PyPI, and more.

## Versions Available

Coolify offers two versions of Nexus:

* **Nexus (Standard)**: The official x86\_64 architecture version
* **Nexus ARM**: Community Edition for ARM64 architecture, maintained and synced with the official repository

## Setup

* The setup relies on starting as default user "admin" with password "admin123".
* Once the service is running, login with the default credentials and change the password.
* After that, delete `NEXUS_SECURITY_RANDOMPASSWORD=false` line from the compose file and restart the service to apply the changes.

Minimum requirements:

* 4 vCPU
* 3 GB RAM

## Screenshots

## Links

* [The official website](https://help.sonatype.com/en/sonatype-nexus-repository.html?utm_source=coolify.io)
* [GitHub](https://github.com/sonatype/docker-nexus3?utm_source=coolify.io)