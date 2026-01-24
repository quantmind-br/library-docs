---
title: SecretsUsedInArgOrEnv
url: https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/
source: llms
fetched_at: 2026-01-24T14:32:35.216203095-03:00
rendered_js: false
word_count: 96
summary: This document describes a security rule prohibiting the use of sensitive data in Dockerfile ARG and ENV commands to prevent secrets from persisting in image metadata.
tags:
    - docker-security
    - dockerfile-best-practices
    - secret-management
    - container-security
    - linting-rules
category: reference
---

Table of contents

* * *

## [Output](#output)

```
Potentially sensitive data should not be used in the ARG or ENV commands
```

## [Description](#description)

While it is common to pass secrets to running processes through environment variables during local development, setting secrets in a Dockerfile using `ENV` or `ARG` is insecure because they persist in the final image. This rule reports violations where `ENV` and `ARG` keys indicate that they contain sensitive data.

Instead of `ARG` or `ENV`, you should use secret mounts, which expose secrets to your builds in a secure manner, and do not persist in the final image or its metadata. See [Build secrets](https://docs.docker.com/build/building/secrets/).

## [Examples](#examples)

❌ Bad: `AWS_SECRET_ACCESS_KEY` is a secret value.

```
FROMscratchARG AWS_SECRET_ACCESS_KEY
```