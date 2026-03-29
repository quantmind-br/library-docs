---
title: Targets
url: https://docs.docker.com/build/bake/targets/
source: llms
fetched_at: 2026-01-24T14:15:24.078362109-03:00
rendered_js: false
word_count: 319
summary: This document explains how to define, group, and execute build targets within Docker Bake files, including support for default targets and pattern matching.
tags:
    - docker-buildx
    - docker-bake
    - build-targets
    - target-groups
    - pattern-matching
    - automation
category: guide
---

## Bake targets

A target in a Bake file represents a build invocation. It holds all the information you would normally pass to a `docker build` command using flags.

```
target "webapp" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
```

To build a target with Bake, pass name of the target to the `bake` command.

```
$ docker buildx bake webapp
```

You can build multiple targets at once by passing multiple target names to the `bake` command.

```
$ docker buildx bake webapp api tests
```

## [Default target](#default-target)

If you don't specify a target when running `docker buildx bake`, Bake will build the target named `default`.

```
target "default" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
```

To build this target, run `docker buildx bake` without any arguments:

## [Target properties](#target-properties)

The properties you can set for a target closely resemble the CLI flags for `docker build`, with a few additional properties that are specific to Bake.

For all the properties you can set for a target, see the [Bake reference](https://docs.docker.com/build/bake/reference#target).

## [Grouping targets](#grouping-targets)

You can group targets together using the `group` block. This is useful when you want to build multiple targets at once.

```
group "all" {
  targets = ["webapp", "api", "tests"]
}
target "webapp" {
  dockerfile = "webapp.Dockerfile"
  tags = ["docker.io/username/webapp:latest"]
  context = "https://github.com/username/webapp"
}
target "api" {
  dockerfile = "api.Dockerfile"
  tags = ["docker.io/username/api:latest"]
  context = "https://github.com/username/api"
}
target "tests" {
  dockerfile = "tests.Dockerfile"
  contexts = {
    webapp = "target:webapp"
    api = "target:api"
  }
  output = ["type=local,dest=build/tests"]
  context = "."
}
```

To build all the targets in a group, pass the name of the group to the `bake` command.

## [Pattern matching for targets and groups](#pattern-matching-for-targets-and-groups)

Bake supports shell-style wildcard patterns when specifying target or grouped targets. This makes it easier to build multiple targets without listing each one explicitly.

Supported patterns:

- `*` matches any sequence of characters
- `?` matches any single character
- `[abc]` matches any character in brackets

> Note
> 
> Always wrap wildcard patterns in quotes. Without quotes, your shell will expand the wildcard to match files in the current directory, which usually causes errors.

Examples:

```
# Match all targets starting with 'foo-'
$ docker buildx bake "foo-*"
# Match all targets
$ docker buildx bake "*"
# Matches: foo-baz, foo-caz, foo-daz, etc.
$ docker buildx bake "foo-?az"
# Matches: foo-bar, boo-bar
$ docker buildx bake "[fb]oo-bar"
# Matches: mtx-a-b-d, mtx-a-b-e, mtx-a-b-f
$ docker buildx bake "mtx-a-b-*"
```

You can also combine multiple patterns:

```
$ docker buildx bake "foo*" "tests"
```

## [Additional resources](#additional-resources)

Refer to the following pages to learn more about Bake's features:

- Learn how to use [variables](https://docs.docker.com/build/bake/variables/) in Bake to make your build configuration more flexible.
- Learn how you can use matrices to build multiple images with different configurations in [Matrices](https://docs.docker.com/build/bake/matrices/).
- Head to the [Bake file reference](https://docs.docker.com/build/bake/reference/) to learn about all the properties you can set in a Bake file, and its syntax.