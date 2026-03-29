---
title: UndefinedVar
url: https://docs.docker.com/reference/build-checks/undefined-var/
source: llms
fetched_at: 2026-01-24T14:32:44.703657095-03:00
rendered_js: false
word_count: 139
summary: This document explains a Docker build check that identifies undefined or undeclared environment variables and build arguments to prevent unexpected build behavior.
tags:
    - dockerfile
    - build-check
    - environment-variables
    - build-args
    - linting
    - static-analysis
category: reference
---

Table of contents

* * *

## [Output](#output)

```
Usage of undefined variable '$foo'
```

## [Description](#description)

This check ensures that environment variables and build arguments are correctly declared before being used. While undeclared variables might not cause an immediate build failure, they can lead to unexpected behavior or errors later in the build process.

This check does not evaluate undefined variables for `RUN`, `CMD`, and `ENTRYPOINT` instructions where you use the [shell form](https://docs.docker.com/reference/dockerfile/#shell-form). That's because when you use shell form, variables are resolved by the command shell.

It also detects common mistakes like typos in variable names. For example, in the following Dockerfile:

```
FROMalpineENV PATH=$PAHT:/app/bin
```

The check identifies that `$PAHT` is undefined and likely a typo for `$PATH`:

```
Usage of undefined variable '$PAHT' (did you mean $PATH?)
```

## [Examples](#examples)

❌ Bad: `$foo` is an undefined build argument.

```
FROMalpineASbaseCOPY $foo .
```

✅ Good: declaring `foo` as a build argument before attempting to access it.

```
FROMalpineASbaseARG fooCOPY $foo .
```

❌ Bad: `$foo` is undefined.

```
FROMalpineASbaseARG VERSION=$foo
```

✅ Good: the base image defines `$PYTHON_VERSION`

```
FROMpythonASbaseARG VERSION=$PYTHON_VERSION
```