---
title: docker system events
url: https://docs.docker.com/reference/cli/docker/system/events/
source: llms
fetched_at: 2026-01-24T14:41:32.6576414-03:00
rendered_js: false
word_count: 742
summary: This document provides a technical reference for the docker system events command, explaining how to stream and filter real-time server events for various Docker objects.
tags:
    - docker-cli
    - docker-events
    - real-time-monitoring
    - event-logging
    - system-administration
category: reference
---

DescriptionGet real time events from the serverUsage`docker system events [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker events`

Use `docker events` to get real-time events from the server. These events differ per Docker object type. Different event types have different scopes. Local scoped events are only seen on the node they take place on, and Swarm scoped events are seen on all managers.

Only the last 256 log events are returned. You can use filters to further limit the number of events returned.

### [Object types](#object-types)

#### [Containers](#containers)

Docker containers report the following events:

- `attach`
- `commit`
- `copy`
- `create`
- `destroy`
- `detach`
- `die`
- `exec_create`
- `exec_detach`
- `exec_die`
- `exec_start`
- `export`
- `health_status`
- `kill`
- `oom`
- `pause`
- `rename`
- `resize`
- `restart`
- `start`
- `stop`
- `top`
- `unpause`
- `update`

#### [Images](#images)

Docker images report the following events:

- `delete`
- `import`
- `load`
- `pull`
- `push`
- `save`
- `tag`
- `untag`

#### [Plugins](#plugins)

Docker plugins report the following events:

- `enable`
- `disable`
- `install`
- `remove`

#### [Volumes](#volumes)

Docker volumes report the following events:

- `create`
- `destroy`
- `mount`
- `unmount`

#### [Networks](#networks)

Docker networks report the following events:

- `create`
- `connect`
- `destroy`
- `disconnect`
- `remove`

#### [Daemons](#daemons)

Docker daemons report the following events:

- `reload`

#### [Services](#services)

Docker services report the following events:

- `create`
- `remove`
- `update`

#### [Nodes](#nodes)

Docker nodes report the following events:

- `create`
- `remove`
- `update`

#### [Secrets](#secrets)

Docker secrets report the following events:

- `create`
- `remove`
- `update`

#### [Configs](#configs)

Docker configs report the following events:

- `create`
- `remove`
- `update`

### [Limiting, filtering, and formatting the output](#limiting-filtering-and-formatting-the-output)

#### [Limit events by time (--since, --until)](#since)

The `--since` and `--until` parameters can be Unix timestamps, date formatted timestamps, or Go duration strings supported by [ParseDuration](https://pkg.go.dev/time#ParseDuration) (e.g. `10m`, `1h30m`) computed relative to the client machine’s time. If you do not provide the `--since` option, the command returns only new and/or live events. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, `2006-01-02T15:04:05`, `2006-01-02T15:04:05.999999999`, `2006-01-02T07:00`, and `2006-01-02`. The local timezone on the client will be used if you do not provide either a `Z` or a `+-00:00` timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds\[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long.

Only the last 256 log events are returned. You can use filters to further limit the number of events returned.

#### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is of "key=value". If you would like to use multiple filters, pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`)

Using the same filter multiple times is interpreted as a logical `OR`; for example, `--filter container=588a23dac085 --filter container=a8f7720b8c22` displays events for container `588a23dac085` or container `a8f7720b8c22`.

Using multiple filters is interpreted as a logical `AND`; for example, `--filter container=588a23dac085 --filter event=start` displays events for container `588a23dac085` and where the event type is `start`.

The currently supported filters are:

- config (`config=<name or id>`)
- container (`container=<name or id>`)
- daemon (`daemon=<name or id>`)
- event (`event=<event action>`)
- image (`image=<repository or tag>`)
- label (`label=<key>` or `label=<key>=<value>`)
- network (`network=<name or id>`)
- node (`node=<id>`)
- plugin (`plugin=<name or id>`)
- scope (`scope=<local or swarm>`)
- secret (`secret=<name or id>`)
- service (`service=<name or id>`)
- type (`type=<container or image or volume or network or daemon or plugin or service or node or secret or config>`)
- volume (`volume=<name>`)

#### [Format the output (--format)](#format)

If you specify a format (`--format`), the given template is executed instead of the default format. Go's [text/template](https://pkg.go.dev/text/template) package describes all the details of the format.

If a format is set to `{{json .}}`, events are streamed in the JSON Lines format. For information about JSON Lines, see [https://jsonlines.org/](https://jsonlines.org/).

OptionDefaultDescription`-f, --filter`Filter output based on conditions provided`--format`Format output using a custom template:  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`--since`Show all events created since timestamp`--until`Stream events until this timestamp

### [Basic example](#basic-example)

You'll need two shells for this example.

**Shell 1: Listening for events:**

**Shell 2: Start and Stop containers:**

**Shell 1: (Again .. now showing events):**

To exit the `docker events` command, use `CTRL+C`.

### [Filter events by time](#filter-events-by-time)

You can filter the output by an absolute timestamp or relative time on the host machine, using the following different time formats:

### [Filter events by criteria](#filter-events-by-criteria)

The following commands show several different ways to filter the `docker event` output.

### [Format the output](#format-the-output)

#### [Format as JSON](#format-as-json)

To list events in JSON format, use the `json` directive, which is the same `--format '{{ json . }}`.