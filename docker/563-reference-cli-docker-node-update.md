---
title: docker node update
url: https://docs.docker.com/reference/cli/docker/node/update/
source: llms
fetched_at: 2026-01-24T14:39:17.212422521-03:00
rendered_js: false
word_count: 212
summary: This document provides a reference for the docker node update command, which allows administrators to modify node attributes like availability, roles, and labels within a Docker Swarm cluster.
tags:
    - docker-swarm
    - node-management
    - cli-reference
    - container-orchestration
    - swarm-mode
category: reference
---

DescriptionUpdate a nodeUsage`docker node update [OPTIONS] NODE`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Update metadata about a node, such as its availability, labels, or roles.

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription`--availability`Availability of the node (`active`, `pause`, `drain`)[`--label-add`](#label-add)Add or update a node label (`key=value`)`--label-rm`Remove a node label if exists`--role`Role of the node (`worker`, `manager`)

## [Examples](#examples)

### [Add label metadata to a node (--label-add)](#label-add)

Add metadata to a swarm node using node labels. You can specify a node label as a key with an empty value:

```
$ docker node update --label-add foo worker1
```

To add multiple labels to a node, pass the `--label-add` flag for each label:

```
$ docker node update --label-add foo --label-add bar worker1
```

When you [create a service](https://docs.docker.com/reference/cli/docker/service/create/), you can use node labels as a constraint. A constraint limits the nodes where the scheduler deploys tasks for a service.

For example, to add a `type` label to identify nodes where the scheduler should deploy message queue service tasks:

```
$ docker node update --label-add type=queue worker1
```

The labels you set for nodes using `docker node update` apply only to the node entity within the swarm. Do not confuse them with the docker daemon labels for [dockerd](https://docs.docker.com/reference/cli/dockerd/).

For more information about labels, refer to [apply custom metadata](https://docs.docker.com/engine/userguide/labels-custom-metadata/).