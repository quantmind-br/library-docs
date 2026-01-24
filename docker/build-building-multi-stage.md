---
title: Multi-stage
url: https://docs.docker.com/build/building/multi-stage/
source: llms
fetched_at: 2026-01-24T14:15:42.422451106-03:00
rendered_js: false
word_count: 559
summary: This document explains how to use multi-stage builds in Docker to create smaller, more efficient production images by separating build environments from runtime environments. It covers techniques for naming stages, copying artifacts between stages, and utilizing specific build targets to optimize the build process.
tags:
    - docker
    - dockerfile
    - multi-stage-builds
    - container-optimization
    - buildkit
    - devops
    - image-size
category: guide
---

## Multi-stage builds

Multi-stage builds are useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain.

With multi-stage builds, you use multiple `FROM` statements in your Dockerfile. Each `FROM` instruction can use a different base, and each of them begins a new stage of the build. You can selectively copy artifacts from one stage to another, leaving behind everything you don't want in the final image.

The following Dockerfile has two separate stages: one for building a binary, and another where the binary gets copied from the first stage into the next stage.

You only need the single Dockerfile. No need for a separate build script. Just run `docker build`.

The end result is a tiny production image with nothing but the binary inside. None of the build tools required to build the application are included in the resulting image.

How does it work? The second `FROM` instruction starts a new build stage with the `scratch` image as its base. The `COPY --from=0` line copies just the built artifact from the previous stage into this new stage. The Go SDK and any intermediate artifacts are left behind, and not saved in the final image.

By default, the stages aren't named, and you refer to them by their integer number, starting with 0 for the first `FROM` instruction. However, you can name your stages, by adding an `AS <NAME>` to the `FROM` instruction. This example improves the previous one by naming the stages and using the name in the `COPY` instruction. This means that even if the instructions in your Dockerfile are re-ordered later, the `COPY` doesn't break.

When you build your image, you don't necessarily need to build the entire Dockerfile including every stage. You can specify a target build stage. The following command assumes you are using the previous `Dockerfile` but stops at the stage named `build`:

A few scenarios where this might be useful are:

- Debugging a specific build stage
- Using a `debug` stage with all debugging symbols or tools enabled, and a lean `production` stage
- Using a `testing` stage in which your app gets populated with test data, but building for production using a different stage which uses real data

When using multi-stage builds, you aren't limited to copying from stages you created earlier in your Dockerfile. You can use the `COPY --from` instruction to copy from a separate image, either using the local image name, a tag available locally or on a Docker registry, or a tag ID. The Docker client pulls the image if necessary and copies the artifact from there. The syntax is:

You can pick up where a previous stage left off by referring to it when using the `FROM` directive. For example:

The legacy Docker Engine builder processes all stages of a Dockerfile leading up to the selected `--target`. It will build a stage even if the selected target doesn't depend on that stage.

[BuildKit](https://docs.docker.com/build/buildkit/) only builds the stages that the target stage depends on.

For example, given the following Dockerfile:

With [BuildKit enabled](https://docs.docker.com/build/buildkit/#getting-started), building the `stage2` target in this Dockerfile means only `base` and `stage2` are processed. There is no dependency on `stage1`, so it's skipped.

On the other hand, building the same target without BuildKit results in all stages being processed:

The legacy builder processes `stage1`, even if `stage2` doesn't depend on it.