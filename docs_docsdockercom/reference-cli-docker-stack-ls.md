---
title: docker stack ls
url: https://docs.docker.com/reference/cli/docker/stack/ls/
source: llms
fetched_at: 2026-01-24T14:41:10.173103986-03:00
rendered_js: false
word_count: 218
summary: This document provides a reference for the `docker stack ls` command, detailing how to list stacks in a Swarm cluster and format the output using templates.
tags:
    - docker-stack
    - swarm-mode
    - cli-reference
    - cluster-management
    - output-formatting
category: reference
---

DescriptionList stacksUsage`docker stack ls [OPTIONS]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker stack list`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Lists the stacks.

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates

## [Examples](#examples)

The following command shows all stacks and some additional information:

```
$ docker stack ls
ID                 SERVICES            ORCHESTRATOR
myapp              2                   Kubernetes
vossibility-stack  6                   Swarm
```

### [Format the output (--format)](#format)

The formatting option (`--format`) pretty-prints stacks using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.Name`Stack name`.Services`Number of services`.Orchestrator`Orchestrator name`.Namespace`Namespace

When using the `--format` option, the `stack ls` command either outputs the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Services` entries separated by a colon (`:`) for all stacks:

```
$ docker stack ls --format "{{.Name}}: {{.Services}}"
web-server: 1
web-cache: 4
```

To list all stacks in JSON format, use the `json` directive:

```
$ docker stack ls --format json
{"Name":"myapp","Namespace":"","Orchestrator":"Swarm","Services":"3"}
```