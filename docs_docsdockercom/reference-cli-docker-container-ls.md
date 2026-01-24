---
title: docker container ls
url: https://docs.docker.com/reference/cli/docker/container/ls/
source: llms
fetched_at: 2026-01-24T14:35:12.516062789-03:00
rendered_js: false
word_count: 1191
summary: This document provides a technical reference for the docker container ls command, including its various options for filtering, formatting, and inspecting container lists.
tags:
    - docker
    - container-management
    - cli-reference
    - filtering
    - output-formatting
category: reference
---

DescriptionList containersUsage`docker container ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker container list` `docker container ps` `docker ps`

List containers

OptionDefaultDescription[`-a, --all`](#all)Show all containers (default shows just running)[`-f, --filter`](#filter)Filter output based on conditions provided[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`-n, --last``-1`Show n last created containers (includes all states)`-l, --latest`Show the latest created container (includes all states)[`--no-trunc`](#no-trunc)Don't truncate output`-q, --quiet`Only display container IDs[`-s, --size`](#size)Display total file sizes

### [Do not truncate output (--no-trunc)](#no-trunc)

Running `docker ps --no-trunc` showing 2 linked containers.

### [Show both running and stopped containers (-a, --all)](#all)

The `docker ps` command only shows running containers by default. To see all containers, use the `--all` (or `-a`) flag:

`docker ps` groups exposed ports into a single range if possible. E.g., a container that exposes TCP ports `100, 101, 102` displays `100-102/tcp` in the `PORTS` column.

### [Show disk usage by container (--size)](#size)

The `docker ps --size` (or `-s`) command displays two different on-disk-sizes for each container:

- The "size" information shows the amount of data (on disk) that is used for the *writable* layer of each container
- The "virtual size" is the total amount of disk-space used for the read-only *image* data used by the container and the writable layer.

For more information, refer to the [container size on disk](https://docs.docker.com/engine/storage/drivers/#container-size-on-disk) section.

### [Filtering (--filter)](#filter)

The `--filter` (or `-f`) flag format is a `key=value` pair. If there is more than one filter, then pass multiple flags (e.g. `--filter "foo=bar" --filter "bif=baz"`).

The currently supported filters are:

FilterDescription`id`Container's ID`name`Container's name`label`An arbitrary string representing either a key or a key-value pair. Expressed as `<key>` or `<key>=<value>``exited`An integer representing the container's exit code. Only useful with `--all`.`status`One of `created`, `restarting`, `running`, `removing`, `paused`, `exited`, or `dead``ancestor`Filters containers which share a given image as an ancestor. Expressed as `<image-name>[:<tag>]`, `<image id>`, or `<image@digest>``before` or `since`Filters containers created before or after a given container ID or name`volume`Filters running containers which have mounted a given volume or bind mount.`network`Filters running containers connected to a given network.`publish` or `expose`Filters containers which publish or expose a given port. Expressed as `<port>[/<proto>]` or `<startport-endport>/[<proto>]``health`Filters containers based on their healthcheck status. One of `starting`, `healthy`, `unhealthy` or `none`.`isolation`Windows daemon only. One of `default`, `process`, or `hyperv`.`is-task`Filters containers that are a "task" for a service. Boolean option (`true` or `false`)

#### [label](#label)

The `label` filter matches containers based on the presence of a `label` alone or a `label` and a value.

The following filter matches containers with the `color` label regardless of its value.

The following filter matches containers with the `color` label with the `blue` value.

#### [name](#name)

The `name` filter matches on all or part of a container's name.

The following filter matches all containers with a name containing the `nostalgic_stallman` string.

You can also filter for a substring in a name as this shows:

#### [exited](#exited)

The `exited` filter matches containers by exist status code. For example, to filter for containers that have exited successfully:

#### [Filter by exit signal](#filter-by-exit-signal)

You can use a filter to locate containers that exited with status of `137` meaning a `SIGKILL(9)` killed them.

Any of these events result in a `137` status:

- the `init` process of the container is killed manually
- `docker kill` kills the container
- Docker daemon restarts which kills all running containers

#### [status](#status)

The `status` filter matches containers by status. The possible values for the container status are:

StatusDescription`created`A container that has never been started.`running`A running container, started by either `docker start` or `docker run`.`paused`A paused container. See `docker pause`.`restarting`A container which is starting due to the designated restart policy for that container.`exited`A container which is no longer running. For example, the process inside the container completed or the container was stopped using the `docker stop` command.`removing`A container which is in the process of being removed. See `docker rm`.`dead`A "defunct" container; for example, a container that was only partially removed because resources were kept busy by an external process. `dead` containers cannot be (re)started, only removed.

For example, to filter for `running` containers:

To filter for `paused` containers:

#### [ancestor](#ancestor)

The `ancestor` filter matches containers based on its image or a descendant of it. The filter supports the following image representation:

- `image`
- `image:tag`
- `image:tag@digest`
- `short-id`
- `full-id`

If you don't specify a `tag`, the `latest` tag is used. For example, to filter for containers that use the latest `ubuntu` image:

Match containers based on the `ubuntu-c1` image which, in this case, is a child of `ubuntu`:

Match containers based on the `ubuntu` version `24.04` image:

The following matches containers based on the layer `d0e008c6cf02` or an image that have this layer in its layer stack.

#### [Create time](#create-time)

##### [before](#before)

The `before` filter shows only containers created before the container with a given ID or name. For example, having these containers created:

Filtering with `before` would give:

##### [since](#since)

The `since` filter shows only containers created since the container with a given ID or name. For example, with the same containers as in `before` filter:

#### [volume](#volume)

The `volume` filter shows only containers that mount a specific volume or have a volume mounted in a specific path:

#### [network](#network)

The `network` filter shows only containers that are connected to a network with a given name or ID.

The following filter matches all containers that are connected to a network with a name containing `net1`.

The network filter matches on both the network's name and ID. The following example shows all containers that are attached to the `net1` network, using the network ID as a filter:

#### [publish and expose](#publish-and-expose)

The `publish` and `expose` filters show only containers that have published or exposed port with a given port number, port range, and/or protocol. The default protocol is `tcp` when not specified.

The following filter matches all containers that have published port of 80:

The following filter matches all containers that have exposed TCP port in the range of `8000-8080`:

The following filter matches all containers that have exposed UDP port `80`:

### [Format the output (--format)](#format)

The formatting option (`--format`) pretty-prints container output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Container ID`.Image`Image ID`.Command`Quoted command`.CreatedAt`Time when the container was created.`.RunningFor`Elapsed time since the container was started.`.Ports`Exposed ports.`.State`Container status (for example; "created", "running", "exited").`.Status`Container status with details about duration and health-status.`.Size`Container disk size.`.Names`Container names.`.Labels`All labels assigned to the container.`.Label`Value of a specific label for this container. For example `'{{.Label "com.docker.swarm.cpu"}}'``.Mounts`Names of the volumes mounted in this container.`.Networks`Names of the networks attached to this container.

When using the `--format` option, the `ps` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID` and `Command` entries separated by a colon (`:`) for all running containers:

To list all running containers with their labels in a table format you can use:

To list all running containers in JSON format, use the `json` directive: