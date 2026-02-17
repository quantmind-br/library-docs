---
title: Docker Installation Failed
url: https://coolify.io/docs/troubleshoot/installation/docker-install-failed.md
source: llms
fetched_at: 2026-02-17T14:41:38.993211-03:00
rendered_js: false
word_count: 87
summary: This document provides troubleshooting instructions for Docker installation failures during the Coolify setup process, typically caused by using non-LTS operating system versions.
tags:
    - coolify
    - docker-installation
    - troubleshooting
    - ubuntu-lts
    - linux-setup
category: guide
---

# Docker Installation Failed

If the Coolify install script fails at the **“Installing Docker”** step, it’s most often due to the server running a **non-LTS version of the operating system** — especially common on **Ubuntu** systems.

## Symptoms

Coolify install script fails with an error like:

```sh
ERROR: '27.0' not found amongst apt-cache madison results
```

## Solution

* Manually Install Docker
  * Follow the official [Docker installation guide](https://docs.docker.com/engine/install/#server) to manually install Docker (version **24+**)

OR

* Use an LTS Version of Your OS
  * Switch to a **Long-Term Support (LTS)** version of your operating system, such as **Ubuntu 22.04 LTS** or  **Debian 12**