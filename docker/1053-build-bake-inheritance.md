---
title: Inheritance
url: https://docs.docker.com/build/bake/inheritance/
source: llms
fetched_at: 2026-01-24T14:15:11.411297309-03:00
rendered_js: false
word_count: 342
summary: This document explains how to use the inheritance feature in Docker Bake to share, reuse, and override attributes across build targets.
tags:
    - docker-bake
    - inheritance
    - build-targets
    - configuration-reuse
    - attribute-overriding
    - multiple-inheritance
category: guide
---

## Inheritance in Bake

Targets can inherit attributes from other targets, using the `inherits` attribute. For example, imagine that you have a target that builds a Docker image for a development environment:

You can create a new target that uses the same build configuration, but with slightly different attributes for a production build. In this example, the `app-release` target inherits the `app-dev` target, but overrides the `tags` attribute and adds a new `platforms` attribute:

One common inheritance pattern is to define a common target that contains shared attributes for all or many of the build targets in the project. For example, the following `_common` target defines a common set of build arguments:

You can then inherit the `_common` target in other targets to apply the shared attributes:

When a target inherits another target, it can override any of the inherited attributes. For example, the following target overrides the `args` attribute from the inherited target:

The `GO_VERSION` argument in `app-release` is set to `1.17`, overriding the `GO_VERSION` argument from the `app-dev` target.

For more information about overriding attributes, see the [Overriding configurations](https://docs.docker.com/build/bake/overrides/) page.

The `inherits` attribute is a list, meaning you can reuse attributes from multiple other targets. In the following example, the app-release target reuses attributes from both the `app-dev` and `_common` targets.

When inheriting attributes from multiple targets and there's a conflict, the target that appears last in the inherits list takes precedence. The previous example defines the `BUILDKIT_CONTEXT_KEEP_GIT_DIR` in the `_common` target and overrides it in the `app-dev` target.

The `app-release` target inherits both `app-dev` target and the `_common` target. The `BUILDKIT_CONTEXT_KEEP_GIT_DIR` argument is set to 0 in the `app-dev` target and 1 in the `_common` target. The `BUILDKIT_CONTEXT_KEEP_GIT_DIR` argument in the `app-release` target is set to 1, not 0, because the `_common` target appears last in the inherits list.

If you only want to inherit a single attribute from a target, you can reference an attribute from another target using dot notation. For example, in the following Bake file, the `bar` target reuses the `tags` attribute from the `foo` target: