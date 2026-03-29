---
title: docker node ls
url: https://docs.docker.com/reference/cli/docker/node/ls/
source: llms
fetched_at: 2026-01-24T14:39:12.071759177-03:00
rendered_js: false
word_count: 573
summary: This document provides a technical reference for the docker node ls command, detailing how to list, filter, and format information about nodes within a Docker Swarm cluster.
tags:
    - docker-swarm
    - cluster-management
    - node-management
    - cli-reference
    - container-orchestration
    - docker-node-ls
category: reference
---

DescriptionList nodes in the swarmUsage`docker node ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker node list`

Swarm This command works with the Swarm orchestrator.

Lists all the nodes that the Docker Swarm manager knows about. You can filter using the `-f` or `--filter` flag. Refer to the [filtering](#filter) section for more information about available filter options.

> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

OptionDefaultDescription[`-f, --filter`](#filter)Filter output based on conditions provided[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`-q, --quiet`Only display IDs

> In the above example output, there is a hidden column of `.Self` that indicates if the node is the same node as the current docker daemon. A `*` (e.g., `e216jshn25ckzbvmwlnh5jr3g *`) means this node is the current docker daemon.

### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`)

The currently supported filters are:

- [id](#id)
- [label](#label)
- [node.label](#nodelabel)
- [membership](#membership)
- [name](#name)
- [role](#role)

#### [id](#id)

The `id` filter matches all or part of a node's id.

#### [label](#label)

The `label` filter matches nodes based on engine labels and on the presence of a `label` alone or a `label` and a value. Engine labels are configured in the [daemon configuration](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file). To filter on Swarm `node` labels, use [`node.label` instead](#nodelabel).

The following filter matches nodes with the `foo` label regardless of its value.

#### [node.label](#nodelabel)

The `node.label` filter matches nodes based on node labels and on the presence of a `node.label` alone or a `node.label` and a value.

The following filter updates nodes to have a `region` node label:

Show all nodes that have a `region` node label set:

Show all nodes that have a `region` node label, with value `region-a`:

#### [membership](#membership)

The `membership` filter matches nodes based on the presence of a `membership` and a value `accepted` or `pending`.

The following filter matches nodes with the `membership` of `accepted`.

#### [name](#name)

The `name` filter matches on all or part of a node hostname.

The following filter matches the nodes with a name equal to `swarm-master` string.

#### [role](#role)

The `role` filter matches nodes based on the presence of a `role` and a value `worker` or `manager`.

The following filter matches nodes with the `manager` role.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints nodes output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Node ID`.Self`Node of the daemon (`true/false`, `true`indicates that the node is the same as current docker daemon)`.Hostname`Node hostname`.Status`Node status`.Availability`Node availability ("active", "pause", or "drain")`.ManagerStatus`Manager status of the node`.TLSStatus`TLS status of the node ("Ready", or "Needs Rotation" has TLS certificate signed by an old CA)`.EngineVersion`Engine version

When using the `--format` option, the `node ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID`, `Hostname`, and `TLS Status` entries separated by a colon (`:`) for all nodes:

To list all nodes in JSON format, use the `json` directive: