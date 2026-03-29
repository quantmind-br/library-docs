---
title: Secrets
url: https://docs.docker.com/build/building/secrets/
source: llms
fetched_at: 2026-01-24T14:15:47.048656567-03:00
rendered_js: false
word_count: 833
summary: This document explains how to securely manage sensitive information during the Docker build process using secret mounts, SSH mounts, and predefined Git authentication secrets.
tags:
    - docker-build
    - build-secrets
    - security
    - ssh-mounts
    - git-authentication
    - dockerfile
    - buildkit
category: guide
---

## Build secrets

A build secret is any piece of sensitive information, such as a password or API token, consumed as part of your application's build process.

Build arguments and environment variables are inappropriate for passing secrets to your build, because they persist in the final image. Instead, you should use secret mounts or SSH mounts, which expose secrets to your builds securely.

- [Secret mounts](#secret-mounts) are general-purpose mounts for passing secrets into your build. A secret mount takes a secret from the build client and makes it temporarily available inside the build container, for the duration of the build instruction. This is useful if, for example, your build needs to communicate with a private artifact server or API.
- [SSH mounts](#ssh-mounts) are special-purpose mounts for making SSH sockets or keys available inside builds. They're commonly used when you need to fetch private Git repositories in your builds.
- [Git authentication for remote contexts](#git-authentication-for-remote-contexts) is a set of pre-defined secrets for when you build with a remote Git context that's also a private repository. These secrets are "pre-flight" secrets: they are not consumed within your build instruction, but they're used to provide the builder with the necessary credentials to fetch the context.

For secret mounts and SSH mounts, using build secrets is a two-step process. First you need to pass the secret into the `docker build` command, and then you need to consume the secret in your Dockerfile.

To pass a secret to a build, use the [`docker build --secret` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#secret), or the equivalent options for [Bake](https://docs.docker.com/build/bake/reference/#targetsecret).

To consume a secret in a build and make it accessible to the `RUN` instruction, use the [`--mount=type=secret`](https://docs.docker.com/reference/dockerfile/#run---mounttypesecret) flag in the Dockerfile.

Secret mounts expose secrets to the build containers, as files or environment variables. You can use secret mounts to pass sensitive information to your builds, such as API tokens, passwords, or SSH keys.

### [Sources](#sources)

The source of a secret can be either a [file](https://docs.docker.com/reference/cli/docker/buildx/build/#file) or an [environment variable](https://docs.docker.com/reference/cli/docker/buildx/build/#env). When you use the CLI or Bake, the type can be detected automatically. You can also specify it explicitly with `type=file` or `type=env`.

The following example mounts the environment variable `KUBECONFIG` to secret ID `kube`, as a file in the build container at `/run/secrets/kube`.

When you use secrets from environment variables, you can omit the `env` parameter to bind the secret to a file with the same name as the variable. In the following example, the value of the `API_TOKEN` variable is mounted to `/run/secrets/API_TOKEN` in the build container.

### [Target](#target)

When consuming a secret in a Dockerfile, the secret is mounted to a file by default. The default file path of the secret, inside the build container, is `/run/secrets/<id>`. You can customize how the secrets get mounted in the build container using the `target` and `env` options for the `RUN --mount` flag in the Dockerfile.

The following example takes secret id `aws` and mounts it to a file at `/run/secrets/aws` in the build container.

To mount a secret as a file with a different name, use the `target` option in the `--mount` flag.

To mount a secret as an environment variable instead of a file, use the `env` option in the `--mount` flag.

It's possible to use the `target` and `env` options together to mount a secret as both a file and an environment variable.

If the credential you want to use in your build is an SSH agent socket or key, you can use the SSH mount instead of a secret mount. Cloning private Git repositories is a common use case for SSH mounts.

The following example clones a private GitHub repository using a [Dockerfile SSH mount](https://docs.docker.com/reference/dockerfile/#run---mounttypessh).

To pass an SSH socket the build, you use the [`docker build --ssh` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#ssh), or equivalent options for [Bake](https://docs.docker.com/build/bake/reference/#targetssh).

## [Git authentication for remote contexts](#git-authentication-for-remote-contexts)

BuildKit supports two pre-defined build secrets, `GIT_AUTH_TOKEN` and `GIT_AUTH_HEADER`. Use them to specify HTTP authentication parameters when building with remote, private Git repositories, including:

- Building with a private Git repository as build context
- Fetching private Git repositories in a build with `ADD`

For example, say you have a private GitLab project at `https://gitlab.com/example/todo-app.git`, and you want to run a build using that repository as the build context. An unauthenticated `docker build` command fails because the builder isn't authorized to pull the repository:

To authenticate the builder to the Git server, set the `GIT_AUTH_TOKEN` environment variable to contain a valid GitLab access token, and pass it as a secret to the build:

The `GIT_AUTH_TOKEN` also works with `ADD` to fetch private Git repositories as part of your build:

### [HTTP authentication scheme](#http-authentication-scheme)

By default, Git authentication over HTTP uses the Bearer authentication scheme:

If you need to use a Basic scheme, with a username and password, you can set the `GIT_AUTH_HEADER` build secret:

BuildKit currently only supports the Bearer and Basic schemes.

### [Multiple hosts](#multiple-hosts)

You can set the `GIT_AUTH_TOKEN` and `GIT_AUTH_HEADER` secrets on a per-host basis, which lets you use different authentication parameters for different hostnames. To specify a hostname, append the hostname as a suffix to the secret ID: