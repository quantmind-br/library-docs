---
title: LegacyKeyValueFormat
url: https://docs.docker.com/reference/build-checks/legacy-key-value-format/
source: llms
fetched_at: 2026-01-24T14:32:18.682654343-03:00
rendered_js: false
word_count: 118
summary: This document explains the requirement to use the equals sign format instead of the legacy space-separated format for environment variables and build arguments in Dockerfiles.
tags:
    - docker
    - dockerfile
    - best-practices
    - env-instruction
    - arg-instruction
    - syntax-standards
category: reference
---

Table of contents

* * *

## [Output](#output)

```
"ENV key=value" should be used instead of legacy "ENV key value" format
```

## [Description](#description)

The correct format for declaring environment variables and build arguments in a Dockerfile is `ENV key=value` and `ARG key=value`, where the variable name (`key`) and value (`value`) are separated by an equals sign (`=`). Historically, Dockerfiles have also supported a space separator between the key and the value (for example, `ARG key value`). This legacy format is deprecated, and you should only use the format with the equals sign.

## [Examples](#examples)

❌ Bad: using a space separator for variable key and value.

✅ Good: use an equals sign to separate key and value.

❌ Bad: multi-line variable declaration with a space separator.

```
ENV DEPS \
    curl \
    git \
    make
```

✅ Good: use an equals sign and wrap the value in quotes.

```
ENV DEPS="\
    curl \
    git \
    make"
```