---
title: Include
url: https://docs.docker.com/reference/compose-file/include/
source: llms
fetched_at: 2026-01-24T14:42:16.673699285-03:00
rendered_js: false
word_count: 557
summary: This document explains how to use the include top-level section in Docker Compose to modularize and reuse configuration files across different projects or sub-domains. It covers syntax options, path resolution, and variable interpolation for included files.
tags:
    - docker-compose
    - include-directive
    - modular-configuration
    - yaml-syntax
    - container-orchestration
category: guide
---

## Use include to modularize Compose files

Requires: Docker Compose [2.20.0](https://github.com/docker/compose/releases/tag/v2.20.0) and later

You can reuse and modularize Docker Compose configurations by including other Compose files. This is useful if:

- You want to reuse other Compose files.
- You need to factor out parts of your application model into separate Compose files so they can be managed separately or shared with others.
- Teams need to maintain a Compose file with only necessary complexity for the limited amount of resources it has to declare for its own sub-domain within a larger deployment.

The `include` top-level section is used to define the dependency on another Compose application, or sub-domain. Each path listed in the `include` section is loaded as an individual Compose application model, with its own project directory, in order to resolve relative paths.

Once the included Compose application is loaded, all resource definitions are copied into the current Compose application model. Compose displays a warning if resource names conflict and doesn't try to merge them. To enforce this, `include` is evaluated after the Compose file(s) selected to define the Compose application model have been parsed and merged, so that conflicts between Compose files are detected.

`include` applies recursively so an included Compose file which declares its own `include` section triggers those other files to be included as well.

Any volumes, networks, or other resources pulled in from the included Compose file can be used by the current Compose application for cross-service references. For example:

Compose also supports the use of interpolated variables with `include`. It's recommended that you [specify mandatory variables](https://docs.docker.com/reference/compose-file/interpolation/). For example:

The short syntax only defines paths to other Compose files. The file is loaded with the parent folder as the project directory, and an optional `.env` file that is loaded to define any variables' default values by interpolation. The local project's environment can override those values.

In the previous example, both `../commons/compose.yaml` and `../another_domain/compose.yaml` are loaded as individual Compose projects. Relative paths in Compose files being referred by `include` are resolved relative to their own Compose file path, not based on the local project's directory. Variables are interpolated using values set in the optional `.env` file in same folder and are overridden by the local project's environment.

The long syntax offers more control over the sub-project parsing:

### [`path`](#path)

`path` is required and defines the location of the Compose file(s) to be parsed and included into the local Compose model.

`path` can be set as:

- A string: When using a single Compose file.
- A list of strings: When multiple Compose files need to be [merged together](https://docs.docker.com/reference/compose-file/merge/) to define the Compose model for the local application.

### [`project_directory`](#project_directory)

`project_directory` defines a base path to resolve relative paths set in the Compose file. It defaults to the directory of the included Compose file.

### [`env_file`](#env_file)

`env_file` defines an environment file(s) to use to define default values when interpolating variables in the Compose file being parsed. It defaults to `.env` file in the `project_directory` for the Compose file being parsed.

`env_file` can be set to either a string or a list of strings when multiple environment files need to be merged to define a project environment.

The local project's environment has precedence over the values set by the Compose file, so that the local project can override values for customization.

For more information on using `include`, see [Working with multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/)