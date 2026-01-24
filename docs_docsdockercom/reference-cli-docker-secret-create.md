---
title: docker secret create
url: https://docs.docker.com/reference/cli/docker/secret/create/
source: llms
fetched_at: 2026-01-24T14:40:44.003635361-03:00
rendered_js: false
word_count: 110
summary: This document provides a technical reference for the docker secret create command, used to securely store sensitive information within a Docker Swarm cluster from files or standard input.
tags:
    - docker
    - docker-swarm
    - secrets-management
    - cli-reference
    - cluster-management
    - security
category: reference
---

DescriptionCreate a secret from a file or STDIN as contentUsage`docker secret create [OPTIONS] SECRET [file|-]`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Creates a secret using standard input or from a file for the secret content.

For detailed information about using secrets, refer to [manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/).

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription`-d, --driver`API 1.31+ Secret driver[`-l, --label`](#label)Secret labels`--template-driver`API 1.37+ Template driver

## [Examples](#examples)

### [Create a secret](#create-a-secret)

```
$ printf "my super secret password" | docker secret create my_secret -
onakdyv307se2tl7nl20anokv
$ docker secret ls
ID                          NAME                CREATED             UPDATED
onakdyv307se2tl7nl20anokv   my_secret           6 seconds ago       6 seconds ago
```

### [Create a secret with a file](#create-a-secret-with-a-file)

```
$ docker secret create my_secret ./secret.json
dg426haahpi5ezmkkj5kyl3sn
$ docker secret ls
ID                          NAME                CREATED             UPDATED
dg426haahpi5ezmkkj5kyl3sn   my_secret           7 seconds ago       7 seconds ago
```

### [Create a secret with labels (--label)](#label)

```
$ docker secret create \
  --label env=dev \
  --label rev=20170324 \
  my_secret ./secret.json
eo7jnzguqgtpdah3cm5srfb97
```

```
$ docker secret inspect my_secret
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