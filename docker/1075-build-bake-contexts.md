---
title: Contexts
url: https://docs.docker.com/build/bake/contexts/
source: llms
fetched_at: 2026-01-24T14:15:03.16543445-03:00
rendered_js: false
word_count: 504
summary: This document explains how to use additional named build contexts in Bake files to define and share resources across multiple build targets. It also provides strategies for optimizing build performance by deduplicating context transfers in large-scale build configurations.
tags:
    - docker-bake
    - buildx
    - build-context
    - docker-build
    - build-optimization
    - buildkit
category: guide
---

## Using Bake with additional contexts

In addition to the main `context` key that defines the build context, each target can also define additional named contexts with a map defined with key `contexts`. These values map to the `--build-context` flag in the [build command](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context).

Inside the Dockerfile these contexts can be used with the `FROM` instruction or `--from` flag.

Supported context values are:

- Local filesystem directories
- Container images
- Git URLs
- HTTP URLs
- Name of another target in the Bake file

## [Using a target as a build context](#using-a-target-as-a-build-context)

To use a result of one target as a build context of another, specify the target name with `target:` prefix.

In most cases you should just use a single multi-stage Dockerfile with multiple targets for similar behavior. This case is only recommended when you have multiple Dockerfiles that can't be easily merged into one.

## [Deduplicate context transfer](#deduplicate-context-transfer)

> As of Buildx version 0.17.0 and later, Bake automatically de-duplicates context transfer for targets that share the same context. In addition to Buildx version 0.17.0, the builder must be running BuildKit version 0.16.0 or later, and the Dockerfile syntax must be `docker/dockerfile:1.10` or later.
> 
> If you meet these requirements, you don't need to manually de-duplicate context transfer as described in this section.
> 
> - To check your Buildx version, run `docker buildx version`.
> - To check your BuildKit version, run `docker buildx inspect --bootstrap` and look for the `BuildKit version` field.
> - To check your Dockerfile syntax version, check the `syntax` [parser directive](https://docs.docker.com/reference/dockerfile/#syntax) in your Dockerfile. If it's not present, the default version whatever comes bundled with your current version of BuildKit. To set the version explicitly, add `#syntax=docker/dockerfile:1.10` at the top of your Dockerfile.

When you build targets concurrently, using groups, build contexts are loaded independently for each target. If the same context is used by multiple targets in a group, that context is transferred once for each time it's used. This can result in significant impact on build time, depending on your build configuration. For example, say you have a Bake file that defines the following group of targets:

In this case, the context `.` is transferred twice when you build the default group: once for `target1` and once for `target2`.

If your context is small, and if you are using a local builder, duplicate context transfers may not be a big deal. But if your build context is big, or you have a large number of targets, or you're transferring the context over a network to a remote builder, context transfer becomes a performance bottleneck.

To avoid transferring the same context multiple times, you can define a named context that only loads the context files, and have each target that needs those files reference that named context. For example, the following Bake file defines a named target `ctx`, which is used by both `target1` and `target2`:

The named context `ctx` represents a Dockerfile stage, which copies the files from its context (`.`). Other stages in the Dockerfile can now reference the `ctx` named context and, for example, mount its files with `--mount=from=ctx`.