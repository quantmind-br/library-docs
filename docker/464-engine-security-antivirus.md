---
title: Antivirus software and Docker
url: https://docs.docker.com/engine/security/antivirus/
source: llms
fetched_at: 2026-01-24T14:25:17.640355033-03:00
rendered_js: false
word_count: 104
summary: This document explains how antivirus software can interfere with Docker operations and provides recommendations for configuring directory exclusions to prevent command hangs.
tags:
    - docker
    - antivirus
    - troubleshooting
    - configuration
    - performance-tuning
category: guide
---

When antivirus software scans files used by Docker, these files may be locked in a way that causes Docker commands to hang.

One way to reduce these problems is to add the Docker data directory (`/var/lib/docker` on Linux, `%ProgramData%\docker` on Windows Server, or `$HOME/Library/Containers/com.docker.docker/` on Mac) to the antivirus's exclusion list. However, this comes with the trade-off that viruses or malware in Docker images, writable layers of containers, or volumes are not detected. If you do choose to exclude Docker's data directory from background virus scanning, you may want to schedule a recurring task that stops Docker, scans the data directory, and restarts Docker.