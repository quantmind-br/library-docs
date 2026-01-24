---
title: NoEmptyContinuation
url: https://docs.docker.com/reference/build-checks/no-empty-continuation/
source: llms
fetched_at: 2026-01-24T14:32:24.459740808-03:00
rendered_js: false
word_count: 95
summary: This document explains the deprecation of empty continuation lines in Dockerfile syntax and provides guidance on how to avoid future build errors by removing them or using comments.
tags:
    - dockerfile
    - buildkit
    - syntax-deprecation
    - container-build
    - best-practices
category: reference
---

Table of contents

* * *

## [Output](#output)

```
Empty continuation line found in: RUN apk add     gnupg     curl
```

## [Description](#description)

Support for empty continuation (`/`) lines have been deprecated and will generate errors in future versions of the Dockerfile syntax.

Empty continuation lines are empty lines following a newline escape:

```
FROMalpineRUN apk add \
    gnupg \
    curl
```

Support for such empty lines is deprecated, and a future BuildKit release will remove support for this syntax entirely, causing builds to break. To avoid future errors, remove the empty lines, or add comments, since lines with comments aren't considered empty.

## [Examples](#examples)

❌ Bad: empty continuation line between `EXPOSE` and 80.

✅ Good: comments do not count as empty lines.

```
FROMalpineEXPOSE \
# Port80
```