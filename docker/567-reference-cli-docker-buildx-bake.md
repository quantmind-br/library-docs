---
title: docker buildx bake
url: https://docs.docker.com/reference/cli/docker/buildx/bake/
source: llms
fetched_at: 2026-01-24T14:32:50.925219748-03:00
rendered_js: false
word_count: 1101
summary: This document provides a comprehensive command-line reference for the docker buildx bake command, explaining how to execute complex, multi-target builds in parallel using configuration files.
tags:
    - docker-buildx
    - bake
    - cli-reference
    - container-build
    - parallel-execution
    - hcl
    - buildkit
category: reference
---

DescriptionBuild from a fileUsage`docker buildx bake [OPTIONS] [TARGET...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker buildx f`

Bake is a high-level build command. Each specified target runs in parallel as part of the build.

Read [High-level build options with Bake](https://docs.docker.com/build/bake/) guide for introduction to writing bake files.

> `buildx bake` command may receive backwards incompatible features in the future if needed. We are looking for feedback on improving the command and extending the functionality further.

OptionDefaultDescription[`--allow`](#allow)Allow build to access specified resources[`--call`](#call)`build`Set method for evaluating build (`check`, `outline`, `targets`)[`--check`](#check)Shorthand for `--call=check`[`-f, --file`](#file)Build definition file[`--list`](#list)List targets or variables[`--load`](#load)Shorthand for `--set=*.output=type=docker`. Conditional.[`--metadata-file`](#metadata-file)Write build result metadata to a file[`--no-cache`](#no-cache)Do not use cache when building the image[`--print`](#print)Print the options without building[`--progress`](#progress)`auto`Set type of progress output (`auto`, `none`, `plain`, `quiet`, `rawjson`, `tty`). Use plain to show container output  
[`--provenance`](#provenance)Shorthand for `--set=*.attest=type=provenance`[`--pull`](#pull)Always attempt to pull all referenced images[`--push`](#push)Shorthand for `--set=*.output=type=registry`. Conditional.[`--sbom`](#sbom)Shorthand for `--set=*.attest=type=sbom`[`--set`](#set)Override target value (e.g., `targetpattern.key=value`)

### [Allow extra privileged entitlement (--allow)](#allow)

Entitlements are designed to provide controlled access to privileged operations. By default, Buildx and BuildKit operates with restricted permissions to protect users and their systems from unintended side effects or security risks. The `--allow` flag explicitly grants access to additional entitlements, making it clear when a build or bake operation requires elevated privileges.

In addition to BuildKit's `network.host` and `security.insecure` entitlements (see [`docker buildx build --allow`](https://docs.docker.com/reference/cli/docker/buildx/build/#allow)), Bake supports file system entitlements that grant granular control over file system access. These are particularly useful when working with builds that need access to files outside the default working directory.

Bake supports the following filesystem entitlements:

- `--allow fs=<path|*>` - Grant read and write access to files outside of the working directory.
- `--allow fs.read=<path|*>` - Grant read access to files outside of the working directory.
- `--allow fs.write=<path|*>` - Grant write access to files outside of the working directory.

The `fs` entitlements take a path value (relative or absolute) to a directory on the filesystem. Alternatively, you can pass a wildcard (`*`) to allow Bake to access the entire filesystem.

### [Example: fs.read](#example-fsread)

Given the following Bake configuration, Bake would need to access the parent directory, relative to the Bake file.

Assuming `docker buildx bake app` is executed in the same directory as the `docker-bake.hcl` file, you would need to explicitly allow Bake to read from the `../src` directory. In this case, the following invocations all work:

### [Example: fs.write](#example-fswrite)

The following `docker-bake.hcl` file requires write access to the `/tmp` directory.

Assuming `docker buildx bake app` is executed outside of the `/tmp` directory, you would need to allow the `fs.write` entitlement, either by specifying the path or using a wildcard:

### [Override the configured builder instance (--builder)](#builder)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

### [Invoke a frontend method (--call)](#call)

Same as [`build --call`](https://docs.docker.com/reference/cli/docker/buildx/build/#call).

#### [Call: check (--check)](#check)

Same as [`build --check`](https://docs.docker.com/reference/cli/docker/buildx/build/#check).

### [Specify a build definition file (-f, --file)](#file)

Use the `-f` / `--file` option to specify the build definition file to use. The file can be an HCL, JSON or Compose file. If multiple files are specified, all are read and the build configurations are combined.

Alternatively, the environment variable `BUILDX_BAKE_FILE` can be used to specify the build definition to use. This is mutually exclusive with `-f` / `--file`; if both are specified, the environment variable is ignored. Multiple definitions can be specified by separating them with the system's path separator (typically `;` on Windows and `:` elsewhere), but can be changed with `BUILDX_BAKE_PATH_SEPARATOR`.

You can pass the names of the targets to build, to build only specific target(s). The following example builds the `db` and `webapp-release` targets that are defined in the `docker-bake.dev.hcl` file:

See the [Bake file reference](https://docs.docker.com/build/bake/reference/) for more details.

### [List targets and variables (--list)](#list)

The `--list` flag displays all available targets or variables in the Bake configuration, along with a description (if set using the `description` property in the Bake file).

To list all targets:

To list variables:

Variable types will be shown when set using the `type` property in the Bake file.

By default, the output of `docker buildx bake --list` is presented in a table format. Alternatively, you can use a long-form CSV syntax and specify a `format` attribute to output the list in JSON.

### [Load images into Docker (--load)](#load)

The `--load` flag is a convenience shorthand for adding an image export of type `docker`:

However, its behavior is conditional:

- If the build definition has no output defined, `--load` adds `type=docker`.
- If the build definition’s outputs are `docker`, `image`, `registry`, `oci`, `--load` will add a `type=docker` export if one is not already present.
- If the build definition contains `local` or `tar` outputs, `--load` does nothing. It will not override those outputs.

For example, with the following bake file:

With `--load`:

The `tar` output remains unchanged.

### [Write build results metadata to a file (--metadata-file)](#metadata-file)

Similar to [`buildx build --metadata-file`](https://docs.docker.com/reference/cli/docker/buildx/build/#metadata-file) but writes a map of results for each target such as:

> Build record [provenance](https://docs.docker.com/build/metadata/attestations/slsa-provenance/#provenance-attestation-example) (`buildx.build.provenance`) includes minimal provenance by default. Set the `BUILDX_METADATA_PROVENANCE` environment variable to customize this behavior:
> 
> - `min` sets minimal provenance (default).
> - `max` sets full provenance.
> - `disabled`, `false` or `0` does not set any provenance.

> Build warnings (`buildx.build.warnings`) are not included by default. Set the `BUILDX_METADATA_WARNINGS` environment variable to `1` or `true` to include them.

### [Don't use cache when building the image (--no-cache)](#no-cache)

Same as `build --no-cache`. Don't use cache when building the image.

### [Print the options without building (--print)](#print)

Prints the resulting options of the targets desired to be built, in a JSON format, without starting a build.

### [Set type of progress output (--progress)](#progress)

Same as [`build --progress`](https://docs.docker.com/reference/cli/docker/buildx/build/#progress).

### [Create provenance attestations (--provenance)](#provenance)

Same as [`build --provenance`](https://docs.docker.com/reference/cli/docker/buildx/build/#provenance).

### [Always attempt to pull a newer version of the image (--pull)](#pull)

Same as `build --pull`.

### [Push images to a registry (--push)](#push)

The `--push` flag follows the same logic as `--load`:

- If no outputs are defined, it adds a `type=image,push=true` export.
- For existing `image` outputs, it sets `push=true`.
- If outputs are set to `local` or `tar`, it does not override them.

### [Create SBOM attestations (--sbom)](#sbom)

Same as [`build --sbom`](https://docs.docker.com/reference/cli/docker/buildx/build/#sbom).

### [Override target configurations from command line (--set)](#set)

Override target configurations from command line. The pattern matching syntax is defined in [https://golang.org/pkg/path/#Match](https://golang.org/pkg/path/#Match).

> `--set` is a repeatable flag. For array fields such as `tags`, repeat `--set` to provide multiple values or use the `+=` operator to append without replacing. Array literal syntax like `--set target.tags=[a,b]` is not supported.

You can override the following fields:

- `annotations`
- `attest`
- `args`
- `cache-from`
- `cache-to`
- `call`
- `context`
- `dockerfile`
- `entitlements`
- `extra-hosts`
- `labels`
- `load`
- `no-cache`
- `no-cache-filter`
- `output`
- `platform`
- `pull`
- `push`
- `secrets`
- `ssh`
- `tags`
- `target`

You can append using `+=` operator for the following fields:

- `annotations`¹
- `attest`¹
- `cache-from`
- `cache-to`
- `entitlements`¹
- `no-cache-filter`
- `output`
- `platform`
- `secrets`
- `ssh`
- `tags`

> ¹ These fields already append by default.