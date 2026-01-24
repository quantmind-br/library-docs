---
title: docker network ls
url: https://docs.docker.com/reference/cli/docker/network/ls/
source: llms
fetched_at: 2026-01-24T14:39:06.234897959-03:00
rendered_js: false
word_count: 561
summary: This document provides a detailed reference for the docker network ls command, covering its syntax, filtering options, and output formatting capabilities.
tags:
    - docker
    - docker-network
    - cli-reference
    - filtering
    - formatting
    - network-management
category: reference
---

DescriptionList networksUsage`docker network ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker network list`

Lists all the networks the Engine `daemon` knows about. This includes the networks that span across multiple hosts in a cluster.

OptionDefaultDescription[`-f, --filter`](#filter)Provide filter values (e.g. `driver=bridge`)[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates[`--no-trunc`](#no-trunc)Do not truncate the output`-q, --quiet`Only display network IDs

### [List all networks](#list-all-networks)

### [List networks without truncating the ID column (--no-trun)](#no-trunc)

Use the `--no-trunc` option to display the full network id:

### [Filtering (--filter)](#filter)

The filtering flag (`-f` or `--filter`) format is a `key=value` pair. If there is more than one filter, then pass multiple flags (e.g. `--filter "foo=bar" --filter "bif=baz"`). Multiple filter flags are combined as an `OR` filter. For example, `-f type=custom -f type=builtin` returns both `custom` and `builtin` networks.

The currently supported filters are:

- driver
- id (network's id)
- label (`label=<key>` or `label=<key>=<value>`)
- name (network's name)
- scope (`swarm|global|local`)
- type (`custom|builtin`)

#### [Driver](#driver)

The `driver` filter matches networks based on their driver.

The following example matches networks with the `bridge` driver:

#### [ID](#id)

The `id` filter matches on all or part of a network's ID.

The following filter matches all networks with an ID containing the `63d1ff1f77b0...` string.

You can also filter for a substring in an ID as this shows:

#### [Label](#label)

The `label` filter matches networks based on the presence of a `label` alone or a `label` and a value.

The following filter matches networks with the `usage` label regardless of its value.

The following filter matches networks with the `usage` label with the `prod` value.

#### [Name](#name)

The `name` filter matches on all or part of a network's name.

The following filter matches all networks with a name containing the `foobar` string.

You can also filter for a substring in a name as this shows:

#### [Scope](#scope)

The `scope` filter matches networks based on their scope.

The following example matches networks with the `swarm` scope:

The following example matches networks with the `local` scope:

#### [Type](#type)

The `type` filter supports two values; `builtin` displays predefined networks (`bridge`, `none`, `host`), whereas `custom` displays user defined networks.

The following filter matches all user defined networks:

By having this flag it allows for batch cleanup. For example, use this filter to delete all user defined networks:

A warning will be issued when trying to remove a network that has containers attached.

### [Format the output (--format)](#format)

The formatting options (`--format`) pretty-prints networks output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.ID`Network ID`.Name`Network name`.Driver`Network driver`.Scope`Network scope (local, global)`.IPv6`Whether IPv6 is enabled on the network or not.`.Internal`Whether the network is internal or not.`.Labels`All labels assigned to the network.`.Label`Value of a specific label for this network. For example `{{.Label "project.version"}}``.CreatedAt`Time when the network was created

When using the `--format` option, the `network ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID` and `Driver` entries separated by a colon (`:`) for all networks:

To list all networks in JSON format, use the `json` directive: