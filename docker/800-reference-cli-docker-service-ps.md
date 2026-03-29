---
title: docker service ps
url: https://docs.docker.com/reference/cli/docker/service/ps/
source: llms
fetched_at: 2026-01-24T14:40:57.480829212-03:00
rendered_js: false
word_count: 429
summary: This document provides a technical reference for the docker service ps command, detailing how to list, filter, and format the output of tasks running within a Docker Swarm.
tags:
    - docker-cli
    - swarm-mode
    - service-management
    - container-orchestration
    - command-reference
category: reference
---

DescriptionList the tasks of one or more servicesUsage`docker service ps [OPTIONS] SERVICE [SERVICE...]`

Swarm This command works with the Swarm orchestrator.

Lists the tasks that are running as part of the specified services.

> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

OptionDefaultDescription[`-f, --filter`](#filter)Filter output based on conditions provided[`--format`](#format)Pretty-print tasks using a Go template`--no-resolve`Do not map IDs to Names`--no-trunc`Do not truncate output`-q, --quiet`Only display task IDs

### [List the tasks that are part of a service](#list-the-tasks-that-are-part-of-a-service)

The following command shows all the tasks that are part of the `redis` service:

In addition to running tasks, the output also shows the task history. For example, after updating the service to use the `redis:7.4.1` image, the output may look like this:

The number of items in the task history is determined by the `--task-history-limit` option that was set when initializing the swarm. You can change the task history retention limit using the [`docker swarm update`](https://docs.docker.com/reference/cli/docker/swarm/update/) command.

When deploying a service, docker resolves the digest for the service's image, and pins the service to that digest. The digest is not shown by default, but is printed if `--no-trunc` is used. The `--no-trunc` option also shows the non-truncated task ID, and error messages, as can be seen in the following example:

### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is a `key=value` pair. If there is more than one filter, then pass multiple flags (e.g. `--filter "foo=bar" --filter "bif=baz"`). Multiple filter flags are combined as an `OR` filter. For example, `-f name=redis.1 -f name=redis.7` returns both `redis.1` and `redis.7` tasks.

The currently supported filters are:

- [id](#id)
- [name](#name)
- [node](#node)
- [desired-state](#desired-state)

#### [id](#id)

The `id` filter matches on all or a prefix of a task's ID.

#### [name](#name)

The `name` filter matches on task names.

#### [node](#node)

The `node` filter matches on a node name or a node ID.

#### [desired-state](#desired-state)

The `desired-state` filter can take the values `running`, `shutdown`, or `accepted`.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints tasks output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Task ID`.Name`Task name`.Image`Task image`.Node`Node ID`.DesiredState`Desired state of the task (`running`, `shutdown`, or `accepted`)`.CurrentState`Current state of the task`.Error`Error`.Ports`Task published ports

When using the `--format` option, the `service ps` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Image` entries separated by a colon (`:`) for all tasks: