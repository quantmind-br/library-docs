---
title: Remote Bake file definition
url: https://docs.docker.com/build/bake/remote-definition/
source: llms
fetched_at: 2026-01-24T14:15:21.83946308-03:00
rendered_js: false
word_count: 485
summary: This document explains how to execute Docker Bake builds using remote definitions from Git repositories or URLs while managing local execution contexts. It covers combining remote and local configurations using the cwd:// prefix and authenticating with private repositories.
tags:
    - docker-bake
    - buildx
    - remote-definitions
    - build-context
    - git-authentication
    - cwd-prefix
category: guide
---

You can build Bake files directly from a remote Git repository or HTTPS URL:

This fetches the Bake definition from the specified remote location and executes the groups or targets defined in that file. If the remote Bake definition doesn't specify a build context, the context is automatically set to the Git remote. For example, [this case](https://github.com/docker/cli/blob/2776a6d694f988c0c1df61cad4bfac0f54e481c8/docker-bake.hcl#L17-L26) uses `https://github.com/docker/cli.git`:

## [Use the local context with a remote definition](#use-the-local-context-with-a-remote-definition)

When building with a remote Bake definition, you may want to consume local files relative to the directory where the Bake command is executed. You can define contexts as relative to the command context using a `cwd://` prefix.

You can append a path to the `cwd://` prefix if you want to use a specific local directory as a context. Note that if you do specify a path, it must be within the working directory where the command gets executed. If you use an absolute path, or a relative path leading outside of the working directory, Bake will throw an error.

### [Local named contexts](#local-named-contexts)

You can also use the `cwd://` prefix to define local directories in the Bake execution context as named contexts.

The following example defines the `docs` context as `./src/docs/content`, relative to the current working directory where Bake is run as a named context.

By contrast, if you omit the `cwd://` prefix, the path would be resolved relative to the build context.

When loading a Bake file from a remote Git repository, if the repository contains more than one Bake file, you can specify which Bake definition to use with the `--file` or `-f` flag:

You can also combine remote definitions with local ones using the `cwd://` prefix with `-f`.

Given the following local Bake definition in the current working directory:

The following example uses `-f` to specify two Bake definitions:

- `-f bake.hcl`: this definition is loaded relative to the Git URL.
- `-f cwd://local.hcl`: this definition is loaded relative to the current working directory where the Bake command is executed.

One case where combining local and remote Bake definitions becomes necessary is when you're building with a remote Bake definition in GitHub Actions and want to use the [metadata-action](https://github.com/docker/metadata-action) to generate tags, annotations, or labels. The metadata action generates a Bake file available in the runner's local Bake execution context. To use both the remote definition and the local "metadata-only" Bake file, specify both files and use the `cwd://` prefix for the metadata Bake file:

If you want to use a remote definition that lives in a private repository, you may need to specify credentials for Bake to use when fetching the definition.

If you can authenticate to the private repository using the default `SSH_AUTH_SOCK`, then you don't need to specify any additional authentication parameters for Bake. Bake automatically uses your default agent socket.

For authentication using an HTTP token, or custom SSH agents, use the following environment variables to configure Bake's authentication strategy:

- [`BUILDX_BAKE_GIT_AUTH_TOKEN`](https://docs.docker.com/build/building/variables/#buildx_bake_git_auth_token)
- [`BUILDX_BAKE_GIT_AUTH_HEADER`](https://docs.docker.com/build/building/variables/#buildx_bake_git_auth_header)
- [`BUILDX_BAKE_GIT_SSH`](https://docs.docker.com/build/building/variables/#buildx_bake_git_ssh)