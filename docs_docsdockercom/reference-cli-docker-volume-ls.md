---
title: docker volume ls
url: https://docs.docker.com/reference/cli/docker/volume/ls/
source: llms
fetched_at: 2026-01-24T14:41:51.624747819-03:00
rendered_js: false
word_count: 439
summary: This document provides a technical reference for the `docker volume ls` command, explaining how to list, filter, and format information about Docker volumes.
tags:
    - docker-cli
    - docker-volume
    - volume-management
    - container-storage
    - cli-reference
category: reference
---

DescriptionList volumesUsage`docker volume ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker volume list`

List all the volumes known to Docker. You can filter using the `-f` or `--filter` flag. Refer to the [filtering](#filter) section for more information about available filter options.

OptionDefaultDescription`--cluster`API 1.42+ Swarm Display only cluster volumes, and use cluster volume list formatting  
[`-f, --filter`](#filter)Provide filter values (e.g. `dangling=true`)[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`-q, --quiet`Only display volume names

### [Create a volume](#create-a-volume)

### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`)

The currently supported filters are:

- dangling (Boolean - true or false, 0 or 1)
- driver (a volume driver's name)
- label (`label=<key>` or `label=<key>=<value>`)
- name (a volume's name)

#### [dangling](#dangling)

The `dangling` filter matches on all volumes not referenced by any containers

#### [driver](#driver)

The `driver` filter matches volumes based on their driver.

The following example matches volumes that are created with the `local` driver:

#### [label](#label)

The `label` filter matches volumes based on the presence of a `label` alone or a `label` and a value.

First, create some volumes to illustrate this;

The following example filter matches volumes with the `is-timelord` label regardless of its value.

As the above example demonstrates, both volumes with `is-timelord=yes`, and `is-timelord=no` are returned.

Filtering on both `key` *and* `value` of the label, produces the expected result:

Specifying multiple label filter produces an "and" search; all conditions should be met;

#### [name](#name)

The `name` filter matches on all or part of a volume's name.

The following filter matches all volumes with a name containing the `rose` string.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints volumes output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.Name`Volume name`.Driver`Volume driver`.Scope`Volume scope (local, global)`.Mountpoint`The mount point of the volume on the host`.Labels`All labels assigned to the volume`.Label`Value of a specific label for this volume. For example `{{.Label "project.version"}}`

When using the `--format` option, the `volume ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Driver` entries separated by a colon (`:`) for all volumes:

To list all volumes in JSON format, use the `json` directive: