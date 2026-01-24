---
title: Build checks
url: https://docs.docker.com/build/checks/
source: llms
fetched_at: 2026-01-24T14:16:15.105349451-03:00
rendered_js: false
word_count: 812
summary: This document explains how to use Docker build checks to validate Dockerfiles and build configurations, identifying potential issues and anti-patterns before executing a build.
tags:
    - docker-buildx
    - dockerfile
    - build-checks
    - linting
    - continuous-integration
    - validation
category: guide
---

## Checking your build configuration

Availability: Beta

Requires: Docker Buildx [0.15.0](https://github.com/docker/buildx/releases/tag/v0.15.0) and later

Build checks are a feature introduced in Dockerfile 1.8. It lets you validate your build configuration and conduct a series of checks prior to executing your build. Think of it as an advanced form of linting for your Dockerfile and build options, or a dry-run mode for builds.

You can find the list of checks available, and a description of each, in the [Build checks reference](https://docs.docker.com/reference/build-checks/).

Typically, when you run a build, Docker executes the build steps in your Dockerfile and build options as specified. With build checks, rather than executing the build steps, Docker checks the Dockerfile and options you provide and reports any issues it detects.

Build checks are useful for:

- Validating your Dockerfile and build options before running a build.
- Ensuring that your Dockerfile and build options are up-to-date with the latest best practices.
- Identifying potential issues or anti-patterns in your Dockerfile and build options.

> To improve linting, code navigation, and vulnerability scanning of your Dockerfiles in Visual Studio Code see [Docker VS Code Extension](https://marketplace.visualstudio.com/items?itemName=docker.docker).

Build checks are supported in:

- Buildx version 0.15.0 and later
- [docker/build-push-action](https://github.com/docker/build-push-action) version 6.6.0 and later
- [docker/bake-action](https://github.com/docker/bake-action) version 5.6.0 and later

Invoking a build runs the checks by default, and displays any violations in the build output. For example, the following command both builds the image and runs the checks:

In this example, the build ran successfully, but a [JSONArgsRecommended](https://docs.docker.com/reference/build-checks/json-args-recommended/) warning was reported, because `CMD` instructions should use JSON array syntax.

With the GitHub Actions, the checks display in the diff view of pull requests.

![GitHub Actions build check annotations](https://docs.docker.com/build/images/gha-check-annotations.png)

![GitHub Actions build check annotations](https://docs.docker.com/build/images/gha-check-annotations.png)

### [More verbose output](#more-verbose-output)

Check warnings for a regular `docker build` display a concise message containing the rule name, the message, and the line number of where in the Dockerfile the issue originated. If you want to see more detailed information about the checks, you can use the `--debug` flag. For example:

With the `--debug` flag, the output includes a link to the documentation for the check, and a snippet of the Dockerfile where the issue was found.

To run build checks without actually building, you can use the `docker build` command as you typically would, but with the addition of the `--check` flag. Here's an example:

Instead of executing the build steps, this command only runs the checks and reports any issues it finds. If there are any issues, they will be reported in the output. For example:

This output with `--check` shows the [verbose message](#more-verbose-output) for the check.

Unlike a regular build, if any violations are reported when using the `--check` flag, the command exits with a non-zero status code.

Check violations for builds are reported as warnings, with exit code 0, by default. You can configure Docker to fail the build when violations are reported, using a `check=error=true` directive in your Dockerfile. This will cause the build to error out when after the build checks are run, before the actual build gets executed.

Without the `# check=error=true` directive, this build would complete with an exit code of 0. However, with the directive, build check violation results in non-zero exit code:

You can also set the error directive on the CLI by passing the `BUILDKIT_DOCKERFILE_CHECK` build argument:

By default, all checks are run when you build an image. If you want to skip specific checks, you can use the `check=skip` directive in your Dockerfile. The `skip` parameter takes a CSV string of the check IDs you want to skip. For example:

Building this Dockerfile results in no check violations.

You can also skip checks by passing the `BUILDKIT_DOCKERFILE_CHECK` build argument with a CSV string of check IDs you want to skip. For example:

To skip all checks, use the `skip=all` parameter:

To both skip specific checks and error on check violations, pass both the `skip` and `error` parameters separated by a semi-colon (`;`) to the `check` directive in your Dockerfile or in a build argument. For example:

Before checks are promoted to stable, they may be available as experimental checks. Experimental checks are disabled by default. To see the list of experimental checks available, refer to the [Build checks reference](https://docs.docker.com/reference/build-checks/).

To enable all experimental checks, set the `BUILDKIT_DOCKERFILE_CHECK` build argument to `experimental=all`:

You can also enable experimental checks in your Dockerfile using the `check` directive:

To selectively enable experimental checks, you can pass a CSV string of the check IDs you want to enable, either to the `check` directive in your Dockerfile or as a build argument. For example:

Note that the `experimental` directive takes precedence over the `skip` directive, meaning that experimental checks will run regardless of the `skip` directive you have set. For example, if you set `skip=all` and enable experimental checks, the experimental checks will still run:

For more information about using build checks, see:

- [Build checks reference](https://docs.docker.com/reference/build-checks/)
- [Validating build configuration with GitHub Actions](https://docs.docker.com/build/ci/github-actions/checks/)