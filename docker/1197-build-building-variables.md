---
title: Variables
url: https://docs.docker.com/build/building/variables/
source: llms
fetched_at: 2026-01-24T14:15:51.191369668-03:00
rendered_js: false
word_count: 2158
summary: Explains the differences, usage, and inheritance rules for build arguments (ARG) and environment variables (ENV) during the Docker build process.
tags:
    - docker-build
    - dockerfile
    - build-arguments
    - environment-variables
    - multi-stage-build
    - build-configuration
category: guide
---

## Build variables

In Docker Build, build arguments (`ARG`) and environment variables (`ENV`) both serve as a means to pass information into the build process. You can use them to parameterize the build, allowing for more flexible and configurable builds.

> Build arguments and environment variables are inappropriate for passing secrets to your build, because they're exposed in the final image. Instead, use secret mounts or SSH mounts, which expose secrets to your builds securely.
> 
> See [Build secrets](https://docs.docker.com/build/building/secrets/) for more information.

Build arguments and environment variables are similar. They're both declared in the Dockerfile and can be set using flags for the `docker build` command. Both can be used to parameterize the build. But they each serve a distinct purpose.

### [Build arguments](#build-arguments)

Build arguments are variables for the Dockerfile itself. Use them to parameterize values of Dockerfile instructions. For example, you might use a build argument to specify the version of a dependency to install.

Build arguments have no effect on the build unless it's used in an instruction. They're not accessible or present in containers instantiated from the image unless explicitly passed through from the Dockerfile into the image filesystem or configuration. They may persist in the image metadata, as provenance attestations and in the image history, which is why they're not suitable for holding secrets.

They make Dockerfiles more flexible, and easier to maintain.

For an example on how you can use build arguments, see [`ARG` usage example](#arg-usage-example).

### [Environment variables](#environment-variables)

Environment variables are passed through to the build execution environment, and persist in containers instantiated from the image.

Environment variables are primarily used to:

- Configure the execution environment for builds
- Set default environment variables for containers

Environment variables, if set, can directly influence the execution of your build, and the behavior or configuration of the application.

You can't override or set an environment variable at build-time. Values for environment variables must be declared in the Dockerfile. You can combine environment variables and build arguments to allow environment variables to be configured at build-time.

For an example on how to use environment variables for configuring builds, see [`ENV` usage example](#env-usage-example).

Build arguments are commonly used to specify versions of components, such as image variants or package versions, used in a build.

Specifying versions as build arguments lets you build with different versions without having to manually update the Dockerfile. It also makes it easier to maintain the Dockerfile, since it lets you declare versions at the top of the file.

Build arguments can also be a way to reuse a value in multiple places. For example, if you use multiple flavors of `alpine` in your build, you can ensure you're using the same version of `alpine` everywhere:

- `golang:1.22-alpine${ALPINE_VERSION}`
- `python:3.12-alpine${ALPINE_VERSION}`
- `nginx:1-alpine${ALPINE_VERSION}`

The following example defines the version of `node` and `alpine` using build arguments.

In this case, the build arguments have default values. Specifying their values when you invoke a build is optional. To override the defaults, you would use the `--build-arg` CLI flag:

For more information on how to use build arguments, refer to:

- [`ARG` Dockerfile reference](https://docs.docker.com/reference/dockerfile/#arg)
- [`docker build --build-arg` reference](https://docs.docker.com/reference/cli/docker/buildx/build/#build-arg)

Declaring an environment variable with `ENV` makes the variable available to all subsequent instructions in the build stage. The following example shows an example setting `NODE_ENV` to `production` before installing JavaScript dependencies with `npm`. Setting the variable makes `npm` omits packages needed only for local development.

Environment variables aren't configurable at build-time by default. If you want to change the value of an `ENV` at build-time, you can combine environment variables and build arguments:

With this Dockerfile, you can use `--build-arg` to override the default value of `NODE_ENV`:

Note that, because the environment variables you set persist in containers, using them can lead to unintended side-effects for the application's runtime.

For more information on how to use environment variables in builds, refer to:

- [`ENV` Dockerfile reference](https://docs.docker.com/reference/dockerfile/#env)

Build arguments declared in the global scope of a Dockerfile aren't automatically inherited into the build stages. They're only accessible in the global scope.

The `echo` command in this example evaluates to `hello !` because the value of the `NAME` build argument is out of scope. To inherit global build arguments into a stage, you must consume them:

Once a build argument is declared or consumed in a stage, it's automatically inherited by child stages.

The following diagram further exemplifies how build argument and environment variable inheritance works for multi-stage builds.

![](https://docs.docker.com/build/images/build-variables.svg)

This section describes pre-defined build arguments available to all builds by default.

### [Multi-platform build arguments](#multi-platform-build-arguments)

Multi-platform build arguments describe the build and target platforms for the build.

The build platform is the operating system, architecture, and platform variant of the host system where the builder (the BuildKit daemon) is running.

- `BUILDPLATFORM`
- `BUILDOS`
- `BUILDARCH`
- `BUILDVARIANT`

The target platform arguments hold the same values for the target platforms for the build, specified using the `--platform` flag for the `docker build` command.

- `TARGETPLATFORM`
- `TARGETOS`
- `TARGETARCH`
- `TARGETVARIANT`

These arguments are useful for doing cross-compilation in multi-platform builds. They're available in the global scope of the Dockerfile, but they aren't automatically inherited by build stages. To use them inside stage, you must declare them:

For more information about multi-platform build arguments, refer to [Multi-platform arguments](https://docs.docker.com/reference/dockerfile/#automatic-platform-args-in-the-global-scope)

### [Proxy arguments](#proxy-arguments)

Proxy build arguments let you specify proxies to use for your build. You don't need to declare or reference these arguments in the Dockerfile. Specifying a proxy with `--build-arg` is enough to make your build use the proxy.

Proxy arguments are automatically excluded from the build cache and the output of `docker history` by default. If you do reference the arguments in your Dockerfile, the proxy configuration ends up in the build cache.

The builder respects the following proxy build arguments. The variables are case insensitive.

- `HTTP_PROXY`
- `HTTPS_PROXY`
- `FTP_PROXY`
- `NO_PROXY`
- `ALL_PROXY`

To configure a proxy for your build:

For more information about proxy build arguments, refer to [Proxy arguments](https://docs.docker.com/reference/dockerfile/#predefined-args).

The following environment variables enable, disable, or change the behavior of Buildx and BuildKit. Note that these variables aren't used to configure the build container; they aren't available inside the build and they have no relation to the `ENV` instruction. They're used to configure the Buildx client, or the BuildKit daemon.

VariableTypeDescription[BUILDKIT\_COLORS](#buildkit_colors)StringConfigure text color for the terminal output.[BUILDKIT\_HOST](#buildkit_host)StringSpecify host to use for remote builders.[BUILDKIT\_PROGRESS](#buildkit_progress)StringConfigure type of progress output.[BUILDKIT\_TTY\_LOG\_LINES](#buildkit_tty_log_lines)StringNumber of log lines (for active steps in TTY mode).[BUILDX\_BAKE\_FILE](#buildx_bake_file)StringSpecify the build definition file(s) for `docker buildx bake`.[BUILDX\_BAKE\_FILE\_SEPARATOR](#buildx_bake_file_separator)StringSpecify the file-path separator for `BUILDX_BAKE_FILE`.[BUILDX\_BAKE\_GIT\_AUTH\_HEADER](#buildx_bake_git_auth_header)StringHTTP authentication scheme for remote Bake files.[BUILDX\_BAKE\_GIT\_AUTH\_TOKEN](#buildx_bake_git_auth_token)StringHTTP authentication token for remote Bake files.[BUILDX\_BAKE\_GIT\_SSH](#buildx_bake_git_ssh)StringSSH authentication for remote Bake files.[BUILDX\_BUILDER](#buildx_builder)StringSpecify the builder instance to use.[BUILDX\_CONFIG](#buildx_config)StringSpecify location for configuration, state, and logs.[BUILDX\_CPU\_PROFILE](#buildx_cpu_profile)StringGenerate a `pprof` CPU profile at the specified location.[BUILDX\_EXPERIMENTAL](#buildx_experimental)BooleanTurn on experimental features.[BUILDX\_GIT\_CHECK\_DIRTY](#buildx_git_check_dirty)BooleanEnable dirty Git checkout detection.[BUILDX\_GIT\_INFO](#buildx_git_info)BooleanRemove Git information in provenance attestations.[BUILDX\_GIT\_LABELS](#buildx_git_labels)String | BooleanAdd Git provenance labels to images.[BUILDX\_MEM\_PROFILE](#buildx_mem_profile)StringGenerate a `pprof` memory profile at the specified location.[BUILDX\_METADATA\_PROVENANCE](#buildx_metadata_provenance)String | BooleanCustomize provenance information included in the metadata file.[BUILDX\_METADATA\_WARNINGS](#buildx_metadata_warnings)StringInclude build warnings in the metadata file.[BUILDX\_NO\_DEFAULT\_ATTESTATIONS](#buildx_no_default_attestations)BooleanTurn off default provenance attestations.[BUILDX\_NO\_DEFAULT\_LOAD](#buildx_no_default_load)BooleanTurn off loading images to image store by default.[EXPERIMENTAL\_BUILDKIT\_SOURCE\_POLICY](#experimental_buildkit_source_policy)StringSpecify a BuildKit source policy file.

BuildKit also supports a few additional configuration parameters. Refer to [BuildKit built-in build args](https://docs.docker.com/reference/dockerfile/#buildkit-built-in-build-args).

You can express Boolean values for environment variables in different ways. For example, `true`, `1`, and `T` all evaluate to true. Evaluation is done using the `strconv.ParseBool` function in the Go standard library. See the [reference documentation](https://pkg.go.dev/strconv#ParseBool) for details.

### [BUILDKIT\_COLORS](#buildkit_colors)

Changes the colors of the terminal output. Set `BUILDKIT_COLORS` to a CSV string in the following format:

Color values can be any valid RGB hex code, or one of the [BuildKit predefined colors](https://github.com/moby/buildkit/blob/master/util/progress/progressui/colors.go).

Setting `NO_COLOR` to anything turns off colorized output, as recommended by [no-color.org](https://no-color.org/).

### [BUILDKIT\_HOST](#buildkit_host)

Requires: Docker Buildx [0.9.0](https://github.com/docker/buildx/releases/tag/v0.9.0) and later

You use the `BUILDKIT_HOST` to specify the address of a BuildKit daemon to use as a remote builder. This is the same as specifying the address as a positional argument to `docker buildx create`.

Usage:

If you specify both the `BUILDKIT_HOST` environment variable and a positional argument, the argument takes priority.

### [BUILDKIT\_PROGRESS](#buildkit_progress)

Sets the type of the BuildKit progress output. Valid values are:

- `auto` (default): automatically uses `tty` in interactive terminals, `plain` otherwise
- `plain`: displays build steps sequentially in simple text format
- `tty`: interactive output with formatted progress bars and build steps
- `quiet`: suppresses progress output, only shows errors and final image ID
- `none`: no progress output, only shows errors
- `rawjson`: outputs build progress as raw JSON (useful for parsing by other tools)

Usage:

### [BUILDKIT\_TTY\_LOG\_LINES](#buildkit_tty_log_lines)

You can change how many log lines are visible for active steps in TTY mode by setting `BUILDKIT_TTY_LOG_LINES` to a number (default to `6`).

### [EXPERIMENTAL\_BUILDKIT\_SOURCE\_POLICY](#experimental_buildkit_source_policy)

Lets you specify a [BuildKit source policy](https://github.com/moby/buildkit/blob/master/docs/build-repro.md#reproducing-the-pinned-dependencies) file for creating reproducible builds with pinned dependencies.

Example:

### [BUILDX\_BAKE\_FILE](#buildx_bake_file)

Requires: Docker Buildx [0.26.0](https://github.com/docker/buildx/releases/tag/v0.26.0) and later

Specify one or more build definition files for `docker buildx bake`.

This environment variable provides an alternative to the `-f` / `--file` command-line flag.

Multiple files can be specified by separating them with the system path separator (":" on Linux/macOS, ";" on Windows):

Or with a custom separator defined by the [BUILDX\_BAKE\_FILE\_SEPARATOR](#buildx_bake_file_separator) variable:

If both `BUILDX_BAKE_FILE` and the `-f` flag are set, only the files provided via `-f` are used.

If a listed file does not exist or is invalid, bake returns an error.

### [BUILDX\_BAKE\_FILE\_SEPARATOR](#buildx_bake_file_separator)

Requires: Docker Buildx [0.26.0](https://github.com/docker/buildx/releases/tag/v0.26.0) and later

Controls the separator used between file paths in the `BUILDX_BAKE_FILE` environment variable.

This is useful if your file paths contain the default separator character or if you want to standardize separators across different platforms.

Requires: Docker Buildx [0.14.0](https://github.com/docker/buildx/releases/tag/v0.14.0) and later

Sets the HTTP authentication scheme when using a remote Bake definition in a private Git repository. This is equivalent to the [`GIT_AUTH_HEADER` secret](https://docs.docker.com/build/building/secrets/#http-authentication-scheme), but facilitates the pre-flight authentication in Bake when loading the remote Bake file. Supported values are `bearer` (default) and `basic`.

Usage:

### [BUILDX\_BAKE\_GIT\_AUTH\_TOKEN](#buildx_bake_git_auth_token)

Requires: Docker Buildx [0.14.0](https://github.com/docker/buildx/releases/tag/v0.14.0) and later

Sets the HTTP authentication token when using a remote Bake definition in a private Git repository. This is equivalent to the [`GIT_AUTH_TOKEN` secret](https://docs.docker.com/build/building/secrets/#git-authentication-for-remote-contexts), but facilitates the pre-flight authentication in Bake when loading the remote Bake file.

Usage:

### [BUILDX\_BAKE\_GIT\_SSH](#buildx_bake_git_ssh)

Requires: Docker Buildx [0.14.0](https://github.com/docker/buildx/releases/tag/v0.14.0) and later

Lets you specify a list of SSH agent socket filepaths to forward to Bake for authenticating to a Git server when using a remote Bake definition in a private repository. This is similar to SSH mounts for builds, but facilitates the pre-flight authentication in Bake when resolving the build definition.

Setting this environment is typically not necessary, because Bake will use the `SSH_AUTH_SOCK` agent socket by default. You only need to specify this variable if you want to use a socket with a different filepath. This variable can take multiple paths using a comma-separated string.

Usage:

### [BUILDX\_BUILDER](#buildx_builder)

Overrides the configured builder instance. Same as the `docker buildx --builder` CLI flag.

Usage:

### [BUILDX\_CONFIG](#buildx_config)

You can use `BUILDX_CONFIG` to specify the directory to use for build configuration, state, and logs. The lookup order for this directory is as follows:

- `$BUILDX_CONFIG`
- `$DOCKER_CONFIG/buildx`
- `~/.docker/buildx` (default)

Usage:

### [BUILDX\_CPU\_PROFILE](#buildx_cpu_profile)

Requires: Docker Buildx [0.18.0](https://github.com/docker/buildx/releases/tag/v0.18.0) and later

If specified, Buildx generates a `pprof` CPU profile at the specified location.

> This property is only useful for when developing Buildx. The profiling data is not relevant for analyzing a build's performance.

Usage:

### [BUILDX\_EXPERIMENTAL](#buildx_experimental)

Enables experimental build features.

Usage:

### [BUILDX\_GIT\_CHECK\_DIRTY](#buildx_git_check_dirty)

Requires: Docker Buildx [0.10.4](https://github.com/docker/buildx/releases/tag/v0.10.4) and later

When set to true, checks for dirty state in source control information for [provenance attestations](https://docs.docker.com/build/metadata/attestations/slsa-provenance/).

Usage:

### [BUILDX\_GIT\_INFO](#buildx_git_info)

Requires: Docker Buildx [0.10.0](https://github.com/docker/buildx/releases/tag/v0.10.0) and later

When set to false, removes source control information from [provenance attestations](https://docs.docker.com/build/metadata/attestations/slsa-provenance/).

Usage:

### [BUILDX\_GIT\_LABELS](#buildx_git_labels)

Requires: Docker Buildx [0.10.0](https://github.com/docker/buildx/releases/tag/v0.10.0) and later

Adds provenance labels, based on Git information, to images that you build. The labels are:

- `com.docker.image.source.entrypoint`: Location of the Dockerfile relative to the project root
- `org.opencontainers.image.revision`: Git commit revision
- `org.opencontainers.image.source`: SSH or HTTPS address of the repository

Example:

Usage:

- Set `BUILDX_GIT_LABELS=1` to include the `entrypoint` and `revision` labels.
- Set `BUILDX_GIT_LABELS=full` to include all labels.

If the repository is in a dirty state, the `revision` gets a `-dirty` suffix.

### [BUILDX\_MEM\_PROFILE](#buildx_mem_profile)

Requires: Docker Buildx [0.18.0](https://github.com/docker/buildx/releases/tag/v0.18.0) and later

If specified, Buildx generates a `pprof` memory profile at the specified location.

> This property is only useful for when developing Buildx. The profiling data is not relevant for analyzing a build's performance.

Usage:

### [BUILDX\_METADATA\_PROVENANCE](#buildx_metadata_provenance)

Requires: Docker Buildx [0.14.0](https://github.com/docker/buildx/releases/tag/v0.14.0) and later

By default, Buildx includes minimal provenance information in the metadata file through [`--metadata-file` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#metadata-file). This environment variable allows you to customize the provenance information included in the metadata file:

- `min` sets minimal provenance (default).
- `max` sets full provenance.
- `disabled`, `false` or `0` does not set any provenance.

### [BUILDX\_METADATA\_WARNINGS](#buildx_metadata_warnings)

Requires: Docker Buildx [0.16.0](https://github.com/docker/buildx/releases/tag/v0.16.0) and later

By default, Buildx does not include build warnings in the metadata file through [`--metadata-file` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#metadata-file). You can set this environment variable to `1` or `true` to include them.

### [BUILDX\_NO\_DEFAULT\_ATTESTATIONS](#buildx_no_default_attestations)

Requires: Docker Buildx [0.10.4](https://github.com/docker/buildx/releases/tag/v0.10.4) and later

By default, BuildKit v0.11 and later adds [provenance attestations](https://docs.docker.com/build/metadata/attestations/slsa-provenance/) to images you build. Set `BUILDX_NO_DEFAULT_ATTESTATIONS=1` to disable the default provenance attestations.

Usage:

### [BUILDX\_NO\_DEFAULT\_LOAD](#buildx_no_default_load)

When you build an image using the `docker` driver, the image is automatically loaded to the image store when the build finishes. Set `BUILDX_NO_DEFAULT_LOAD` to disable automatic loading of images to the local container store.

Usage: