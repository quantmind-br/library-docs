---
title: docker service ls
url: https://docs.docker.com/reference/cli/docker/service/ls/
source: llms
fetched_at: 2026-01-24T14:40:57.237230703-03:00
rendered_js: false
word_count: 434
summary: This document provides a reference for the docker service ls command, which lists services running in a Docker Swarm and includes details on filtering and output formatting.
tags:
    - docker-swarm
    - docker-cli
    - service-management
    - container-orchestration
    - command-line-interface
    - swarm-mode
category: reference
---

DescriptionList servicesUsage`docker service ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker service list`

Swarm This command works with the Swarm orchestrator.

This command lists services that are running in the swarm.

> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

OptionDefaultDescription[`-f, --filter`](#filter)Filter output based on conditions provided[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`-q, --quiet`Only display IDs

On a manager node:

The `REPLICAS` column shows both the actual and desired number of tasks for the service. If the service is in `replicated-job` or `global-job`, it will additionally show the completion status of the job as completed tasks over total tasks the job will execute.

### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`).

The currently supported filters are:

- [id](https://docs.docker.com/reference/cli/docker/service/ls/#id)
- [label](https://docs.docker.com/reference/cli/docker/service/ls/#label)
- [mode](https://docs.docker.com/reference/cli/docker/service/ls/#mode)
- [name](https://docs.docker.com/reference/cli/docker/service/ls/#name)

#### [id](#id)

The `id` filter matches all or the prefix of a service's ID.

The following filter matches services with an ID starting with `0bcjw`:

#### [label](#label)

The `label` filter matches services based on the presence of a `label` alone or a `label` and a value.

The following filter matches all services with a `project` label regardless of its value:

The following filter matches only services with the `project` label with the `project-a` value.

#### [mode](#mode)

The `mode` filter matches on the mode (either `replicated` or `global`) of a service.

The following filter matches only `global` services.

#### [name](#name)

The `name` filter matches on all or the prefix of a service's name.

The following filter matches services with a name starting with `redis`.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints services output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Service ID`.Name`Service name`.Mode`Service mode (replicated, global)`.Replicas`Service replicas`.Image`Service image`.Ports`Service ports published in ingress mode

When using the `--format` option, the `service ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID`, `Mode`, and `Replicas` entries separated by a colon (`:`) for all services:

To list all services in JSON format, use the `json` directive: