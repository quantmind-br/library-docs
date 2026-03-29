---
title: Include
url: https://docs.docker.com/compose/how-tos/multiple-compose-files/include/
source: llms
fetched_at: 2026-01-24T14:17:39.47144225-03:00
rendered_js: false
word_count: 411
summary: This document explains how to use the Docker Compose include directive to modularize application configurations and manage external dependencies. It covers path resolution, remote file support, and strategies for overriding included resources to avoid conflicts.
tags:
    - docker-compose
    - configuration-management
    - include-directive
    - yaml-modularization
    - infrastructure-as-code
category: guide
---

Requires: Docker Compose [2.20.3](https://github.com/docker/compose/releases/tag/v2.20.3) and later

With `include`, you can incorporate a separate `compose.yaml` file directly in your current `compose.yaml` file. This makes it easy to modularize complex applications into sub-Compose files, which in turn enables application configurations to be made simpler and more explicit.

The [`include` top-level element](https://docs.docker.com/reference/compose-file/include/) helps to reflect the engineering team responsible for the code directly in the config file's organization. It also solves the relative path problem that [`extends`](https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/) and [merge](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) present.

Each path listed in the `include` section loads as an individual Compose application model, with its own project directory, in order to resolve relative paths.

Once the included Compose application loads, all resources are copied into the current Compose application model.

> `include` applies recursively so an included Compose file which declares its own `include` section, causes those files to also be included.

`my-compose-include.yaml` manages `serviceB` which details some replicas, web UI to inspect data, isolated networks, volumes for data persistence, etc. The application relying on `serviceB` doesn’t need to know about the infrastructure details, and consumes the Compose file as a building block it can rely on.

This means the team managing `serviceB` can refactor its own database component to introduce additional services without impacting any dependent teams. It also means that the dependent teams don't need to include additional flags on each Compose command they run.

`include` allows you to reference Compose files from remote sources, such as OCI artifacts or Git repositories.  
Here `serviceB` is defined in a Compose file stored on Docker Hub.

Compose reports an error if any resource from `include` conflicts with resources from the included Compose file. This rule prevents unexpected conflicts with resources defined by the included compose file author. However, there may be some circumstances where you might want to customize the included model. This can be achieved by adding an override file to the include directive:

The main limitation with this approach is that you need to maintain a dedicated override file per include. For complex projects with multiple includes this would result in many Compose files.

The other option is to use a `compose.override.yaml` file. While conflicts will be rejected from the file using `include` when same resource is declared, a global Compose override file can override the resulting merged model, as demonstrated in following example:

Main `compose.yaml` file:

Override `compose.override.yaml` file:

Combined together, this allows you to benefit from third-party reusable components, and adjust the Compose model for your needs.

[`include` top-level element](https://docs.docker.com/reference/compose-file/include/)