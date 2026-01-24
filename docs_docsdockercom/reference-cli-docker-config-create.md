---
title: docker config create
url: https://docs.docker.com/reference/cli/docker/config/create/
source: llms
fetched_at: 2026-01-24T14:34:48.791387967-03:00
rendered_js: false
word_count: 105
summary: This document explains how to use the docker config create command to store configuration data in a Docker Swarm cluster from a file or standard input.
tags:
    - docker-swarm
    - docker-config
    - cli-reference
    - configuration-management
    - cluster-management
category: reference
---

DescriptionCreate a config from a file or STDINUsage`docker config create [OPTIONS] CONFIG file|-`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Creates a config using standard input or from a file for the config content.

For detailed information about using configs, refer to [store configuration data using Docker Configs](https://docs.docker.com/engine/swarm/configs/).

> Note
> 
> This is a cluster management command, and must be executed on a Swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription[`-l, --label`](#label)Config labels`--template-driver`API 1.37+ Template driver

## [Examples](#examples)

### [Create a config](#create-a-config)

```
$ printf <config> | docker config create my_config -
onakdyv307se2tl7nl20anokv
$ docker config ls
ID                          NAME                CREATED             UPDATED
onakdyv307se2tl7nl20anokv   my_config           6 seconds ago       6 seconds ago
```

### [Create a config with a file](#create-a-config-with-a-file)

```
$ docker config create my_config ./config.json
dg426haahpi5ezmkkj5kyl3sn
$ docker config ls
ID                          NAME                CREATED             UPDATED
dg426haahpi5ezmkkj5kyl3sn   my_config           7 seconds ago       7 seconds ago
```

### [Create a config with labels (-l, --label)](#label)

```
$ docker config create \
    --label env=dev \
    --label rev=20170324 \
    my_config ./config.json
eo7jnzguqgtpdah3cm5srfb97
```

```
$ docker config inspect my_config
[
    {
        "ID": "eo7jnzguqgtpdah3cm5srfb97",
        "Version": {
            "Index": 17
        },
        "CreatedAt": "2017-03-24T08:15:09.735271783Z",
        "UpdatedAt": "2017-03-24T08:15:09.735271783Z",
        "Spec": {
            "Name": "my_config",
            "Labels": {
                "env": "dev",
                "rev": "20170324"
            },
            "Data": "aGVsbG8K"
        }
    }
]
```