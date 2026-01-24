---
title: docker secret inspect
url: https://docs.docker.com/reference/cli/docker/secret/inspect/
source: llms
fetched_at: 2026-01-24T14:40:47.421061844-03:00
rendered_js: false
word_count: 205
summary: This document provides a reference for the docker secret inspect command, which is used to retrieve detailed information about secrets in a Docker Swarm cluster.
tags:
    - docker-swarm
    - docker-secret
    - cli-reference
    - cluster-management
    - json-output
category: reference
---

DescriptionDisplay detailed information on one or more secretsUsage`docker secret inspect [OPTIONS] SECRET [SECRET...]`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Inspects the specified secret.

By default, this renders all results in a JSON array. If a format is specified, the given template will be executed for each result.

Go's [text/template](https://pkg.go.dev/text/template) package describes all the details of the format.

For detailed information about using secrets, refer to [manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/).

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription[`-f, --format`](#format)Format output using a custom template:  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`--pretty`Print the information in a human friendly format

## [Examples](#examples)

### [Inspect a secret by name or ID](#inspect-a-secret-by-name-or-id)

You can inspect a secret, either by its name or ID.

For example, given the following secret:

```
$ docker secret ls
ID                          NAME                CREATED             UPDATED
eo7jnzguqgtpdah3cm5srfb97   my_secret           3 minutes ago       3 minutes ago
```

```
$ docker secret inspect secret.json
```

The output is in JSON format, for example:

```
[
  {
    "ID": "eo7jnzguqgtpdah3cm5srfb97",
    "Version": {
      "Index": 17
    },
    "CreatedAt": "2017-03-24T08:15:09.735271783Z",
    "UpdatedAt": "2017-03-24T08:15:09.735271783Z",
    "Spec": {
      "Name": "my_secret",
      "Labels": {
        "env": "dev",
        "rev": "20170324"
      }
    }
  }
]
```

### [Format the output (--format)](#format)

You can use the `--format` option to obtain specific information about a secret. The following example command outputs the creation time of the secret.

```
$ docker secret inspect --format='{{.CreatedAt}}' eo7jnzguqgtpdah3cm5srfb97
2017-03-24 08:15:09.735271783 +0000 UTC
```