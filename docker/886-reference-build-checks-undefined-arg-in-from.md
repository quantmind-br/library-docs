---
title: UndefinedArgInFrom
url: https://docs.docker.com/reference/build-checks/undefined-arg-in-from/
source: llms
fetched_at: 2026-01-24T14:32:40.930588415-03:00
rendered_js: false
word_count: 117
summary: This document explains a Dockerfile linting rule that warns when build arguments are used in FROM instructions without being explicitly declared.
tags:
    - dockerfile
    - build-arguments
    - linting
    - docker-buildx
    - syntax-validation
category: reference
---

Table of contents

* * *

## [Output](#output)

```
FROM argument 'VARIANT' is not declared
```

## [Description](#description)

This rule warns for cases where you're consuming an undefined build argument in `FROM` instructions.

Interpolating build arguments in `FROM` instructions can be a good way to add flexibility to your build, and lets you pass arguments that overriding the base image of a stage. For example, you might use a build argument to specify the image tag:

```
ARG ALPINE_VERSION=3.20FROMalpine:${ALPINE_VERSION}
```

This makes it possible to run the build with a different `alpine` version by specifying a build argument:

```
$ docker buildx build --build-arg ALPINE_VERSION=edge .
```

This check also tries to detect and warn when a `FROM` instruction reference miss-spelled built-in build arguments, like `BUILDPLATFORM`.

## [Examples](#examples)

❌ Bad: the `VARIANT` build argument is undefined.

```
FROMnode:22${VARIANT} AS jsbuilder
```

✅ Good: the `VARIANT` build argument is defined.

```
ARG VARIANT="-alpine3.20"FROMnode:22${VARIANT} AS jsbuilder
```