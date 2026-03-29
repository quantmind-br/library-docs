---
title: Mastering Docker Buildx Bake
url: https://docs.docker.com/guides/bake/
source: llms
fetched_at: 2026-01-24T14:08:35.637089294-03:00
rendered_js: false
word_count: 1568
summary: This guide explains how to use Docker Buildx Bake to simplify and automate complex image building, testing, and artifact generation workflows using declarative HCL files. It covers advanced features like build matrices for parallel variant builds and using BuildKit as a task runner for testing.
tags:
    - docker-buildx
    - bake
    - docker-bake-hcl
    - multi-platform-builds
    - build-automation
    - buildkit
    - ci-cd
category: guide
---

## Mastering multi-platform builds, testing, and more with Docker Buildx Bake

This guide demonstrates how to simplify and automate the process of building images, testing, and generating build artifacts using Docker Buildx Bake. By defining build configurations in a declarative `docker-bake.hcl` file, you can eliminate manual scripts and enable efficient workflows for complex builds, testing, and artifact generation.

This guide assumes that you're familiar with:

- Docker
- [Buildx](https://docs.docker.com/build/concepts/overview/#buildx)
- [BuildKit](https://docs.docker.com/build/concepts/overview/#buildkit)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)

<!--THE END-->

- You have a recent version of Docker installed on your machine.
- You have Git installed for cloning repositories.
- You're using the [containerd](https://docs.docker.com/desktop/features/containerd/) image store.

This guide uses an example project to demonstrate how Docker Buildx Bake can streamline your build and test workflows. The repository includes both a Dockerfile and a `docker-bake.hcl` file, giving you a ready-to-use setup to try out Bake commands.

Start by cloning the example repository:

The Bake file, `docker-bake.hcl`, defines the build targets in a declarative syntax, using targets and groups, allowing you to manage complex builds efficiently.

Here's what the Bake file looks like out-of-the-box:

The `target` keyword defines a build target for Bake. The `default` target defines the target to build when no specific target is specified on the command line. Here's a quick summary of the options for the `default` target:

- `target`: The target build stage in the Dockerfile.
- `tags`: Tags to assign to the image.
- `attest`: [Attestations](https://docs.docker.com/build/metadata/attestations/) to attach to the image.
  
  > The attestations provide metadata such as build provenance, which tracks the source of the image's build, and an SBOM (Software Bill of Materials), useful for security audits and compliance.
- `platforms`: Platform variants to build.

To execute this build, simply run the following command in the root of the repository:

With Bake, you avoid long, hard-to-remember command-line incantations, simplifying build configuration management by replacing manual, error-prone scripts with a structured configuration file.

For contrast, here's what this build command would look like without Bake:

Bake isn't just for defining build configurations and running builds. You can also use Bake to run your tests, effectively using BuildKit as a task runner. Running your tests in containers is great for ensuring reproducible results. This section shows how to add two types of tests:

- Unit testing with `go test`.
- Linting for style violations with `golangci-lint`.

In Test-Driven Development (TDD) fashion, start by adding a new `test` target to the Bake file:

> Using `type=cacheonly` ensures that the build output is effectively discarded; the layers are saved to BuildKit's cache, but Buildx will not attempt to load the result to the Docker Engine's image store.
> 
> For test runs, you don't need to export the build output — only the test execution matters.

To execute this Bake target, run `docker buildx bake test`. At this time, you'll receive an error indicating that the `test` stage does not exist in the Dockerfile.

To satisfy this target, add the corresponding Dockerfile target. The `test` stage here is based on the same base stage as the build stage.

> The [`--mount=type=cache` directive](https://docs.docker.com/build/cache/optimize/#use-cache-mounts) caches Go modules between builds, improving build performance by avoiding the need to re-download dependencies. This shared cache ensures that the same dependency set is available across build, test, and other stages.

Now, running the `test` target with Bake will evaluate the unit tests for this project. If you want to verify that it works, you can make an arbitrary change to `main_test.go` to cause the test to fail.

Next, to enable linting, add another target to the Bake file, named `lint`:

And in the Dockerfile, add the build stage. This stage will use the official `golangci-lint` image on Docker Hub.

> Because this stage relies on executing an external dependency, it's generally a good idea to define the version you want to use as a build argument. This lets you more easily manage version upgrades in the future by collocating dependency versions to the beginning of the Dockerfile.

Lastly, to enable running both tests simultaneously, you can use the `groups` construct in the Bake file. A group can specify multiple targets to run with a single invocation.

Now, running both tests is as simple as:

Sometimes you need to build more than one version of a program. The following example uses Bake to build separate "release" and "debug" variants of the program, using [matrices](https://docs.docker.com/build/bake/matrices/). Using matrices lets you run parallel builds with different configurations, saving time and ensuring consistency.

A matrix expands a single build into multiple builds, each representing a unique combination of matrix parameters. This means you can orchestrate Bake into building both the production and development build of your program in parallel, with minimal configuration changes.

The example project for this guide is set up to use a build-time option to conditionally enable debug logging and tracing capabilities.

- If you compile the program with `go build -tags="debug"`, the additional logging and tracing capabilities are enabled (development mode).
- If you build without the `debug` tag, the program is compiled with a default logger (production mode).

Update the Bake file by adding a matrix attribute which defines the variable combinations to build:

The `matrix` attribute defines the variants to build ("release" and "debug"). The `name` attribute defines how the matrix gets expanded into multiple distinct build targets. In this case, the matrix attribute expands the build into two workflows: `image-release` and `image-debug`, each using different configuration parameters.

Next, define a build argument named `BUILD_TAGS` which takes the value of the matrix variable.

You'll also want to change how the image tags are assigned to these builds. Currently, both matrix paths would generate the same image tag names, and overwrite each other. Update the `tags` attribute use a conditional operator to set the tag depending on the matrix variable value.

- If `mode` is `release`, the tag name is `bakeme:latest`
- If `mode` is `debug`, the tag name is `bakeme:dev`

Finally, update the Dockerfile to consume the `BUILD_TAGS` argument during the compilation stage. When the `-tags="${BUILD_TAGS}"` option evaluates to `-tags="debug"`, the compiler uses the `configureLogging` function in the [`debug.go`](https://github.com/dvdksn/bakeme/blob/75c8a41e613829293c4bd3fc3b4f0c573f458f42/debug.go#L1) file.

That's all. With these changes, your `docker buildx bake` command now builds two multi-platform image variants. You can introspect the canonical build configuration that Bake generates using the `docker buildx bake --print` command. Running this command shows that Bake will run a `default` group with two targets with different build arguments and image tags.

Factoring in all of the platform variants as well, this means that the build configuration generates 6 different images.

Exporting build artifacts like binaries can be useful for deploying to environments without Docker or Kubernetes. For example, if your programs are meant to be run on a user's local machine.

> The techniques discussed in this section can be applied not only to build output like binaries, but to any type of artifacts, such as test reports.

With programming languages like Go and Rust where the compiled binaries are usually portable, creating alternate build targets for exporting only the binary is trivial. All you need to do is add an empty stage in the Dockerfile containing nothing but the binary that you want to export.

First, let's add a quick way to build a binary for your local platform and export it to `./build/local` on the local filesystem.

In the `docker-bake.hcl` file, create a new `bin` target. In this stage, set the `output` attribute to a local filesystem path. Buildx automatically detects that the output looks like a filepath, and exports the results to the specified path using the [local exporter](https://docs.docker.com/build/exporters/local-tar/).

Notice that this stage specifies a `local` platform. By default, if `platforms` is unspecified, builds target the OS and architecture of the BuildKit host. If you're using Docker Desktop, this often means builds target `linux/amd64` or `linux/arm64`, even if your local machine is macOS or Windows, because Docker runs in a Linux VM. Using the `local` platform forces the target platform to match your local environment.

Next, add the `bin` stage to the Dockerfile which copies the compiled binary from the build stage.

Now you can export your local platform version of the binary with `docker buildx bake bin`. For example, on macOS, this build target generates an executable in the [Mach-O format](https://en.wikipedia.org/wiki/Mach-O) — the standard executable format for macOS.

Next, let's add a target to build all of the platform variants of the program. To do this, you can [inherit](https://docs.docker.com/build/bake/inheritance/) the `bin` target that you just created, and extend it by adding the desired platforms.

Now, building the `bin-cross` target creates binaries for all platforms. Subdirectories are automatically created for each variant.

To also generate "release" and "debug" variants, you can use a matrix just like you did with the default target. When using a matrix, you also need to differentiate the output directory based on the matrix value, otherwise the binary gets written to the same location for each matrix run.

Docker Buildx Bake streamlines complex build workflows, enabling efficient multi-platform builds, testing, and artifact export. By integrating Buildx Bake into your projects, you can simplify your Docker builds, make your build configuration portable, and wrangle complex configurations more easily.

Experiment with different configurations and extend your Bake files to suit your project's needs. You might consider integrating Bake into your CI/CD pipelines to automate builds, testing, and artifact deployment. The flexibility and power of Buildx Bake can significantly improve your development and deployment processes.

### [Further reading](#further-reading)

For more information about how to use Bake, check out these resources:

- [Bake documentation](https://docs.docker.com/build/bake/)
- [Matrix targets](https://docs.docker.com/build/bake/matrices/)
- [Bake file reference](https://docs.docker.com/build/bake/reference/)
- [Bake GitHub Action](https://github.com/docker/bake-action)