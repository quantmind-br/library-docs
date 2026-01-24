---
title: Building with Bake from a Compose file
url: https://docs.docker.com/build/bake/compose-file/
source: llms
fetched_at: 2026-01-24T14:14:58.490837646-03:00
rendered_js: false
word_count: 0
summary: This document provides a configuration template for Docker Buildx Bake to define and manage multi-platform container image builds. It outlines how to specify build targets, arguments, caching strategies, and secret handling within a build group.
tags:
    - docker-buildx
    - container-builds
    - bake-file
    - multi-platform
    - build-automation
    - docker-configuration
category: configuration
---

```
{
  "group": {
    "default": {
      "targets": ["addon", "aws"]
    }
  },
  "target": {
    "addon": {
      "context": ".",
      "dockerfile": "./Dockerfile",
      "args": {
        "CT_ECR": "foo",
        "CT_TAG": "bar"
      },
      "tags": ["ct-addon:foo", "ct-addon:alp"],
      "cache-from": [
        {
          "ref": "user/app:cache",
          "type": "registry"
        },
        {
          "src": "path/to/cache",
          "type": "local"
        }
      ],
      "cache-to": [
        {
          "dest": "path/to/cache",
          "type": "local"
        }
      ],
      "platforms": ["linux/amd64", "linux/arm64"],
      "pull": true
    },
    "aws": {
      "context": ".",
      "dockerfile": "./aws.Dockerfile",
      "args": {
        "CT_ECR": "foo",
        "CT_TAG": "bar"
      },
      "tags": ["ct-fake-aws:bar"],
      "secret": [
        {
          "id": "mysecret",
          "src": "./secret"
        },
        {
          "id": "mysecret2",
          "src": "./secret2"
        }
      ],
      "platforms": ["linux/arm64"],
      "output": [
        {
          "type": "docker"
        }
      ],
      "no-cache": true
    }
  }
}
```