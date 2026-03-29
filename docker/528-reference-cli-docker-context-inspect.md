---
title: docker context inspect
url: https://docs.docker.com/reference/cli/docker/context/inspect/
source: llms
fetched_at: 2026-01-24T14:35:44.582153093-03:00
rendered_js: false
word_count: 0
summary: This document displays the JSON output format for the docker context inspect command, providing details on endpoints, storage paths, and metadata for a specific Docker context.
tags:
    - docker
    - docker-context
    - cli-reference
    - context-management
    - docker-inspect
category: reference
---

```
$ docker context inspect "local+aks"
[
  {
    "Name": "local+aks",
    "Metadata": {
      "Description": "Local Docker Engine",
      "StackOrchestrator": "swarm"
    },
    "Endpoints": {
      "docker": {
        "Host": "npipe:////./pipe/docker_engine",
        "SkipTLSVerify": false
      }
    },
    "TLSMaterial": {},
    "Storage": {
      "MetadataPath": "C:\\Users\\simon\\.docker\\contexts\\meta\\cb6d08c0a1bfa5fe6f012e61a442788c00bed93f509141daff05f620fc54ddee",
      "TLSPath": "C:\\Users\\simon\\.docker\\contexts\\tls\\cb6d08c0a1bfa5fe6f012e61a442788c00bed93f509141daff05f620fc54ddee"
    }
  }
]
```