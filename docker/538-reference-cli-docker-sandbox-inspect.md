---
title: docker sandbox inspect
url: https://docs.docker.com/reference/cli/docker/sandbox/inspect/
source: llms
fetched_at: 2026-01-24T14:39:52.940123332-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates the usage and output of the docker sandbox inspect command for retrieving detailed metadata about a Docker sandbox instance.
tags:
    - docker-cli
    - docker-sandbox
    - sandbox-inspect
    - container-metadata
    - cli-reference
category: reference
---

```
$ docker sandbox inspect abc123def
[
  {
    "id": "abc123def69b16c5c0dab4cf699e26f8d01e1ace3aeee06254e0999492e11647",
    "name": "claude-sandbox-2025-11-04-170333",
    "created_at": "2025-11-04T16:03:33.910642347Z",
    "status": "running",
    "template": "docker/sandbox-templates:claude-code",
    "labels": {
      "com.docker.sandbox.agent": "claude",
      "com.docker.sandbox.workingDirectory": "/Users/moby/code/docker/sandboxes",
      "com.docker.sandbox.workingDirectoryInode": "3041007",
      "com.docker.sandboxes": "templates",
      "com.docker.sandboxes.base": "ubuntu:questing",
      "com.docker.sandboxes.flavor": "claude-code",
      "com.docker.sdk": "true",
      "com.docker.sdk.client": "0.1.0-alpha011",
      "com.docker.sdk.container": "0.1.0-alpha012",
      "com.docker.sdk.lang": "go",
      "docker/sandbox": "true",
      "org.opencontainers.image.ref.name": "ubuntu",
      "org.opencontainers.image.version": "25.10"
    }
  }
]
```