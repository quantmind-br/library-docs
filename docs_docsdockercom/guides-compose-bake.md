---
title: Building Compose projects with Bake
url: https://docs.docker.com/guides/compose-bake/
source: llms
fetched_at: 2026-01-24T14:08:40.09178712-03:00
rendered_js: false
word_count: 1351
summary: This guide explains how to use Docker Buildx Bake to extend and customize Docker Compose build configurations for production environments. It demonstrates how to orchestrate complex image builds by merging Compose service definitions with declarative Bake files.
tags:
    - docker-buildx
    - docker-compose
    - image-building
    - bake
    - build-orchestration
    - production-builds
category: guide
---

This guide explores how you can use Bake to build images for Docker Compose projects with multiple services.

[Docker Buildx Bake](https://docs.docker.com/build/bake/) is a build orchestration tool that enables declarative configuration for your builds, much like Docker Compose does for defining runtime stacks. For projects where Docker Compose is used to spin up services for local development, Bake offers a way of seamlessly extending the project with a production-ready build configuration.

This guide assumes that you're familiar with

- Docker Compose
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)

This guide will use the [dvdksn/example-voting-app](https://github.com/dvdksn/example-voting-app) repository as an example of a monorepo using Docker Compose that can be extended with Bake.

This repository uses Docker Compose to define the runtime configurations for running the application, in the `compose.yaml` file. This app consists of the following services:

ServiceDescription`vote`A front-end web app in Python which lets you vote between two options.`result`A Node.js web app which shows the results of the voting in real time.`worker`A .NET worker which consumes votes and stores them in the database.`db`A Postgres database backed by a Docker volume.`redis`A Redis instance which collects new votes.`seed`A utility container that seeds the database with mock data.

The `vote`, `result`, and `worker` services are built from code in this repository, whereas `db` and `redis` use pre-existing Postgres and Redis images from Docker Hub. The `seed` service is a utility that invokes requests against the front-end service to populate the database, for testing purposes.

When you spin up a Docker Compose project, any services that define the `build` property are automatically built before the service is started. Here's the build configuration for the `vote` service in the example repository:

The `vote`, `result`, and `worker` services all have a build configuration specified. Running `docker compose up` will trigger a build of these services.

Did you know that you can also use Compose just to build the service images? The `docker compose build` command lets you invoke a build using the build configuration specified in the Compose file. For example, to build the `vote` service with this configuration, run:

Omit the service name to build all services at once:

The `docker compose build` command is useful when you only need to build images without running services.

The Compose file format supports a number of properties for defining your build's configuration. For example, to specify the tag name for the images, set the `image` property on the service.

Running `docker compose build` creates three service images with fully qualified image names that you can push to Docker Hub.

The `build` property supports a [wide range](https://docs.docker.com/reference/compose-file/build/) of options for configuring builds. However, building production-grade images are often different from images used in local development. To avoid cluttering your Compose file with build configurations that might not be desirable for local builds, consider separating the production builds from the local builds by using Bake to build images for release. This approach separates concerns: using Compose for local development and Bake for production-ready builds, while still reusing service definitions and fundamental build configurations.

Like Compose, Bake parses the build definition for a project from a configuration file. Bake supports HashiCorp Configuration Language (HCL), JSON, and the Docker Compose YAML format. When you use Bake with multiple files, it will find and merge all of the applicable configuration files into one unified build configuration. The build options defined in your Compose file are extended, or in some cases overridden, by options specified in the Bake file.

The following section explores how you can use Bake to extend the build options defined in your Compose file for production.

### [View the build configuration](#view-the-build-configuration)

Bake automatically creates a build configuration from the `build` properties of your services. Use the `--print` flag for Bake to view the build configuration for a given Compose file. This flag evaluates the build configuration and outputs the build definition in JSON format.

The JSON-formatted output shows the group that would be executed, and all the targets of that group. A group is a collection of builds, and a target represents a single build.

As you can see, Bake has created a `default` group that includes four targets:

- `seed`
- `vote`
- `result`
- `worker`

This group is created automatically from your Compose file; it includes all of your services containing a build configuration. To build this group of services with Bake, run:

### [Customize the build group](#customize-the-build-group)

Start by redefining the default build group that Bake executes. The current default group includes a `seed` target — a Compose service used solely to populate the database with mock data. Since this target doesn't produce a production image, it doesn’t need to be included in the build group.

To customize the build configuration that Bake uses, create a new file at the root of the repository, alongside your `compose.yaml` file, named `docker-bake.hcl`.

Open the Bake file and add the following configuration:

Save the file and print your Bake definition again.

The JSON output shows that the `default` group only includes the targets you care about.

Here, the build configuration for each target (context, tags, etc.) is picked up from the `compose.yaml` file. The group is defined by the `docker-bake.hcl` file.

### [Customize targets](#customize-targets)

The Compose file currently defines the `dev` stage as the build target for the `vote` service. That's appropriate for the image that you would run in local development, because the `dev` stage includes additional development dependencies and configurations. For the production image, however, you'll want to target the `final` image instead.

To modify the target stage used by the `vote` service, add the following configuration to the Bake file:

This overrides the `target` property specified in the Compose file with a different value when you run the build with Bake. The other build options in the Compose file (tag, context) remain unmodified. You can verify by inspecting the build configuration for the `vote` target with `docker buildx bake --print vote`:

### [Additional build features](#additional-build-features)

Production-grade builds often have different characteristics from development builds. Here are a few examples of things you might want to add for production images.

Multi-platform

For local development, you only need to build images for your local platform, since those images are just going to run on your machine. But for images that are pushed to a registry, it's often a good idea to build for multiple platforms, arm64 and amd64 in particular.

Attestations

[Attestations](https://docs.docker.com/build/metadata/attestations/) are manifests attached to the image that describe how the image was created and what components it contains. Attaching attestations to your images helps ensure that your images follow software supply chain best practices.

Annotations

[Annotations](https://docs.docker.com/build/metadata/annotations/) provide descriptive metadata for images. Use annotations to record arbitrary information and attach it to your image, which helps consumers and tools understand the origin, contents, and how to use the image.

> Why not just define these additional build options in the Compose file directly?
> 
> The `build` property in the Compose file format does not support all build features. Additionally, some features, like multi-platform builds, can drastically increase the time it takes to build a service. For local development, you're better off keeping your build step simple and fast, saving the bells and whistles for release builds.

To add these properties to the images you build with Bake, update the Bake file as follows:

This defines a new `_common` target that defines reusable build configuration for adding multi-platform support, annotations, and attestations to your images. The reusable target is inherited by the build targets.

With these changes, building the project with Bake produces three sets of multi-platform images for the `linux/amd64` and `linux/arm64` architectures. Each image is decorated with an author annotation, and both SBOM and provenance attestation records.

The pattern demonstrated in this guide provides a useful approach for managing production-ready Docker images in projects using Docker Compose. Using Bake gives you access to all the powerful features of Buildx and BuildKit, and also helps separate your development and build configuration in a reasonable way.

### [Further reading](#further-reading)

For more information about how to use Bake, check out these resources:

- [Bake documentation](https://docs.docker.com/build/bake/)
- [Building with Bake from a Compose file](https://docs.docker.com/build/bake/compose-file/)
- [Bake file reference](https://docs.docker.com/build/bake/reference/)
- [Mastering multi-platform builds, testing, and more with Docker Buildx Bake](https://docs.docker.com/guides/bake/)
- [Bake GitHub Action](https://github.com/docker/bake-action)