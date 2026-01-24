---
title: docker stack ps
url: https://docs.docker.com/reference/cli/docker/stack/ps/
source: llms
fetched_at: 2026-01-24T14:41:13.258600675-03:00
rendered_js: false
word_count: 506
summary: This reference document explains how to use the docker stack ps command to list and manage tasks within a Docker Swarm stack. It details command options for filtering results, formatting output with templates, and controlling display attributes like truncation and name resolution.
tags:
    - docker-cli
    - docker-stack
    - swarm-mode
    - container-orchestration
    - task-management
    - command-line-interface
category: reference
---

DescriptionList the tasks in the stackUsage`docker stack ps [OPTIONS] STACK`

Swarm This command works with the Swarm orchestrator.

Lists the tasks that are running as part of the specified stack.

> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

OptionDefaultDescription[`-f, --filter`](#filter)Filter output based on conditions provided[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates[`--no-resolve`](#no-resolve)Do not map IDs to Names[`--no-trunc`](#no-trunc)Do not truncate output[`-q, --quiet`](#quiet)Only display task IDs

### [List the tasks that are part of a stack](#list-the-tasks-that-are-part-of-a-stack)

The following command shows all the tasks that are part of the `voting` stack:

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

The `desired-state` filter can take the values `running`, `shutdown`, `ready` or `accepted`.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints tasks output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Task ID`.Name`Task name`.Image`Task image`.Node`Node ID`.DesiredState`Desired state of the task (`running`, `shutdown`, or `accepted`)`.CurrentState`Current state of the task`.Error`Error`.Ports`Task published ports

When using the `--format` option, the `stack ps` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Image` entries separated by a colon (`:`) for all tasks:

To list all tasks in JSON format, use the `json` directive:

### [Do not map IDs to Names (--no-resolve)](#no-resolve)

The `--no-resolve` option shows IDs for task name, without mapping IDs to Names.

### [Do not truncate output (--no-trunc)](#no-trunc)

When deploying a service, docker resolves the digest for the service's image, and pins the service to that digest. The digest is not shown by default, but is printed if `--no-trunc` is used. The `--no-trunc` option also shows the non-truncated task IDs, and error-messages, as can be seen below:

### [Only display task IDs (-q, --quiet)](#quiet)

The `-q`or `--quiet` option only shows IDs of the tasks in the stack. This example outputs all task IDs of the `voting` stack:

This option can be used to perform batch operations. For example, you can use the task IDs as input for other commands, such as `docker inspect`. The following example inspects all tasks of the `voting` stack: