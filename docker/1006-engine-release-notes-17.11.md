---
title: Engine v17.11
url: https://docs.docker.com/engine/release-notes/17.11/
source: llms
fetched_at: 2026-01-24T14:24:52.940362065-03:00
rendered_js: false
word_count: 69
summary: Explains critical upgrade requirements for Docker CE 17.11 regarding containerd integration and the necessity of stopping containers to maintain management control.
tags:
    - docker-ce
    - containerd
    - upgrade-notice
    - container-management
    - live-restore
    - backward-compatibility
category: guide
---

Important

Docker CE 17.11 is the first Docker release based on [containerd 1.0 beta](https://github.com/containerd/containerd/releases/tag/v1.0.0-beta.2). Docker CE 17.11 and later don't recognize containers started with previous Docker versions. If you use Live Restore, you must stop all containers before upgrading to Docker CE 17.11. If you don't, any containers started by Docker versions that predate 17.11 aren't recognized by Docker after the upgrade and keep running, un-managed, on the system.