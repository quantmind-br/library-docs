---
title: Merge
url: https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
source: llms
fetched_at: 2026-01-24T14:17:42.077213333-03:00
rendered_js: false
word_count: 813
summary: This document explains how to merge and override multiple Docker Compose files to create environment-specific configurations. It details the rules for combining service attributes, path resolution, and the use of command-line flags or environment variables to manage composite setups.
tags:
    - docker-compose
    - compose-file
    - configuration-merging
    - environment-overrides
    - deployment-strategies
    - yaml-configuration
category: guide
---

## Merge Compose files

Docker Compose lets you merge and override a set of Compose files together to create a composite Compose file.

By default, Compose reads two files, a `compose.yaml` and an optional `compose.override.yaml` file. By convention, the `compose.yaml` contains your base configuration. The override file can contain configuration overrides for existing services or entirely new services.

If a service is defined in both files, Compose merges the configurations using the rules described below and in the [Compose Specification](https://docs.docker.com/reference/compose-file/merge/).

To use multiple override files, or an override file with a different name, you can either use the pre-defined [COMPOSE\_FILE](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_file) environment variable, or use the `-f` option to specify the list of files.

Compose merges files in the order they're specified on the command line. Subsequent files may merge, override, or add to their predecessors.

For example:

The `compose.yaml` file might specify a `webapp` service.

The `compose.admin.yaml` may also specify this same service:

Any matching fields override the previous file. New values, add to the `webapp` service configuration:

- Paths are evaluated relative to the base file. When you use multiple Compose files, you must make sure all paths in the files are relative to the base Compose file (the first Compose file specified with `-f`). This is required because override files need not be valid Compose files. Override files can contain small fragments of configuration. Tracking which fragment of a service is relative to which path is difficult and confusing, so to keep paths easier to understand, all paths must be defined relative to the base file.
  
  > You can use `docker compose config` to review your merged configuration and avoid path-related issues.
- Compose copies configurations from the original service over to the local one. If a configuration option is defined in both the original service and the local service, the local value replaces or extends the original value.
  
  - For single-value options like `image`, `command` or `mem_limit`, the new value replaces the old value.
    
    original service:
    
    local service:
    
    result:
  - For the multi-value options `ports`, `expose`, `external_links`, `dns`, `dns_search`, and `tmpfs`, Compose concatenates both sets of values:
    
    original service:
    
    local service:
    
    result:
  - In the case of `environment`, `labels`, `volumes`, and `devices`, Compose "merges" entries together with locally defined values taking precedence. For `environment` and `labels`, the environment variable or label name determines which value is used:
    
    original service:
    
    local service:
    
    result:
  - Entries for `volumes` and `devices` are merged using the mount path in the container:
    
    original service:
    
    local service:
    
    result:

For more merging rules, see [Merge and override](https://docs.docker.com/reference/compose-file/merge/) in the Compose Specification.

### [Additional information](#additional-information)

- Using `-f` is optional. If not provided, Compose searches the working directory and its parent directories for a `compose.yaml` and a `compose.override.yaml` file. You must supply at least the `compose.yaml` file. If both files exist on the same directory level, Compose combines them into a single configuration.
- You can use a `-f` with `-` (dash) as the filename to read the configuration from `stdin`. For example:
  
  When `stdin` is used, all paths in the configuration are relative to the current working directory.
- You can use the `-f` flag to specify a path to a Compose file that is not located in the current directory, either from the command line or by setting up a [COMPOSE\_FILE environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_file) in your shell or in an environment file.
  
  For example, if you are running the [Compose Rails sample](https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/rails/README.md), and have a `compose.yaml` file in a directory called `sandbox/rails`. You can use a command like [docker compose pull](https://docs.docker.com/reference/cli/docker/compose/pull/) to get the postgres image for the `db` service from anywhere by using the `-f` flag as follows: `docker compose -f ~/sandbox/rails/compose.yaml pull db`
  
  Here's the full example:

A common use case for multiple files is changing a development Compose app for a production-like environment (which may be production, staging or CI). To support these differences, you can split your Compose configuration into a few different files:

Start with a base file that defines the canonical configuration for the services.

`compose.yaml`

In this example the development configuration exposes some ports to the host, mounts our code as a volume, and builds the web image.

`compose.override.yaml`

When you run `docker compose up` it reads the overrides automatically.

To use this Compose app in a production environment, another override file is created, which might be stored in a different git repository or managed by a different team.

`compose.prod.yaml`

To deploy with this production Compose file you can run

This deploys all three services using the configuration in `compose.yaml` and `compose.prod.yaml` but not the dev configuration in `compose.override.yaml`.

For more information, see [Using Compose in production](https://docs.docker.com/compose/how-tos/production/).

Docker Compose supports relative paths for the many resources to be included in the application model: build context for service images, location of file defining environment variables, path to a local directory used in a bind-mounted volume. With such a constraint, code organization in a monorepo can become hard as a natural choice would be to have dedicated folders per team or component, but then the Compose files relative paths become irrelevant.

- [Merge rules](https://docs.docker.com/reference/compose-file/merge/)