---
title: InvalidDefinitionDescription
url: https://docs.docker.com/reference/build-checks/invalid-definition-description/
source: llms
fetched_at: 2026-01-24T14:32:18.385791535-03:00
rendered_js: false
word_count: 163
summary: This document explains a Docker build check that validates the formatting of comments used as descriptions for build stages and arguments in Dockerfiles.
tags:
    - docker-build
    - dockerfile
    - build-checks
    - build-arguments
    - documentation-comments
category: reference
---

Table of contents

* * *

> Note
> 
> This check is experimental and is not enabled by default. To enable it, see [Experimental checks](https://docs.docker.com/go/build-checks-experimental/).

## [Output](#output)

```
Comment for build stage or argument should follow the format: `# <arg/stage name> <description>`. If this is not intended to be a description comment, add an empty line or comment between the instruction and the comment.
```

## [Description](#description)

The [`--call=outline`](https://docs.docker.com/reference/cli/docker/buildx/build/#call-outline) and [`--call=targets`](https://docs.docker.com/reference/cli/docker/buildx/build/#call-outline) flags for the `docker build` command print descriptions for build targets and arguments. The descriptions are generated from [Dockerfile comments](https://docs.docker.com/reference/cli/docker/buildx/build/#descriptions) that immediately precede the `FROM` or `ARG` instruction and that begin with the name of the build stage or argument. For example:

```
# build-cli builds the CLI binaryFROMalpineASbuild-cli# VERSION controls the version of the programARG VERSION=1
```

In cases where preceding comments are not meant to be descriptions, add an empty line or comment between the instruction and the preceding comment.

## [Examples](#examples)

❌ Bad: A non-descriptive comment on the line preceding the `FROM` command.

```
# a non-descriptive commentFROMscratchASbase# another non-descriptive commentARG VERSION=1
```

✅ Good: An empty line separating non-descriptive comments.

```
# a non-descriptive commentFROMscratchASbase# another non-descriptive commentARG VERSION=1
```

✅ Good: Comments describing `ARG` keys and stages immediately proceeding the command.

```
# base is a stage for compiling sourceFROMscratchASbase# VERSION This is the version number.ARG VERSION=1
```