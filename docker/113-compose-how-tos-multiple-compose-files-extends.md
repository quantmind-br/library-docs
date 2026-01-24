---
title: Extend
url: https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/
source: llms
fetched_at: 2026-01-24T14:17:37.364959254-03:00
rendered_js: false
word_count: 475
summary: Explains how to use the Docker Compose extends attribute to share and reuse service configurations across multiple files or within the same project.
tags:
    - docker-compose
    - configuration-reuse
    - service-extension
    - yaml-configuration
    - devops-tools
category: guide
---

## Extend your Compose file

Docker Compose's [`extends` attribute](https://docs.docker.com/reference/compose-file/services/#extends) lets you share common configurations among different files, or even different projects entirely.

Extending services is useful if you have several services that reuse a common set of configuration options. With `extends` you can define a common set of service options in one place and refer to it from anywhere. You can refer to another Compose file and select a service you want to also use in your own application, with the ability to override some attributes for your own needs.

> When you use multiple Compose files, you must make sure all paths in the files are relative to the base Compose file (i.e. the Compose file in your main-project folder). This is required because extend files need not be valid Compose files. Extend files can contain small fragments of configuration. Tracking which fragment of a service is relative to which path is difficult and confusing, so to keep paths easier to understand, all paths must be defined relative to the base file.

### [Extending services from another file](#extending-services-from-another-file)

Take the following example:

This instructs Compose to re-use only the properties of the `webapp` service defined in the `common-services.yml` file. The `webapp` service itself is not part of the final project.

If `common-services.yml` looks like this:

You get exactly the same result as if you wrote `compose.yaml` with the same `build`, `ports`, and `volumes` configuration values defined directly under `web`.

To include the service `webapp` in the final project when extending services from another file, you need to explicitly include both services in your current Compose file. For example (this is for illustrative purposes only):

Alternatively, you can use [include](https://docs.docker.com/compose/how-tos/multiple-compose-files/include/).

### [Extending services within the same file](#extending-services-within-the-same-file)

If you define services in the same Compose file and extend one service from another, both the original service and the extended service will be part of your final configuration. For example:

### [Extending services within the same file and from another file](#extending-services-within-the-same-file-and-from-another-file)

You can go further and define, or re-define, configuration locally in `compose.yaml`:

Extending an individual service is useful when you have multiple services that have a common configuration. The example below is a Compose app with two services, a web application and a queue worker. Both services use the same codebase and share many configuration options.

The `common.yaml` file defines the common configuration:

The `compose.yaml` defines the concrete services which use the common configuration:

When using `extends` with a `file` attribute which points to another folder, relative paths declared by the service being extended are converted so they still point to the same file when used by the extending service. This is illustrated in the following example:

Base Compose file:

The `commons/compose.yaml` file:

The resulting service refers to the original `container.env` file within the `commons` directory. This can be confirmed with `docker compose config` which inspects the actual model:

- [`extends`](https://docs.docker.com/reference/compose-file/services/#extends)