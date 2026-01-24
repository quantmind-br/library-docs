---
title: WorkdirRelativePath
url: https://docs.docker.com/reference/build-checks/workdir-relative-path/
source: llms
fetched_at: 2026-01-24T14:32:47.92995701-03:00
rendered_js: false
word_count: 171
summary: This document explains the WorkdirRelativePath build rule, which warns against using relative paths in Dockerfile WORKDIR instructions to prevent unexpected directory hierarchies.
tags:
    - dockerfile
    - build-optimization
    - workdir
    - container-best-practices
    - linting
    - devops
category: reference
---

Table of contents

* * *

## [Output](#output)

```
Relative workdir 'app/src' can have unexpected results if the base image changes
```

## [Description](#description)

When specifying `WORKDIR` in a build stage, you can use an absolute path, like `/build`, or a relative path, like `./build`. Using a relative path means that the working directory is relative to whatever the previous working directory was. So if your base image uses `/usr/local/foo` as a working directory, and you specify a relative directory like `WORKDIR build`, the effective working directory becomes `/usr/local/foo/build`.

The `WorkdirRelativePath` build rule warns you if you use a `WORKDIR` with a relative path without first specifying an absolute path in the same Dockerfile. The rationale for this rule is that using a relative working directory for base image built externally is prone to breaking, since working directory may change upstream without warning, resulting in a completely different directory hierarchy for your build.

## [Examples](#examples)

❌ Bad: this assumes that `WORKDIR` in the base image is `/` (if that changes upstream, the `web` stage is broken).

```
FROMnginxASwebWORKDIRusr/share/nginx/htmlCOPY public .
```

✅ Good: a leading slash ensures that `WORKDIR` always ends up at the desired path.

```
FROMnginxASwebWORKDIR/usr/share/nginx/htmlCOPY public .
```