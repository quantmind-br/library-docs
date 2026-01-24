---
title: docker stack rm
url: https://docs.docker.com/reference/cli/docker/stack/rm/
source: llms
fetched_at: 2026-01-24T14:41:13.491143596-03:00
rendered_js: false
word_count: 132
summary: This document provides a technical reference for the docker stack rm command, which is used to remove one or more stacks and their associated services, networks, and secrets from a Docker Swarm.
tags:
    - docker-swarm
    - docker-stack
    - cli-reference
    - stack-management
    - container-orchestration
category: reference
---

DescriptionRemove one or more stacksUsage`docker stack rm [OPTIONS] STACK [STACK...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker stack remove` `docker stack down`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Remove the stack from the swarm.

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription`-d, --detach``true`Do not wait for stack removal

## [Examples](#examples)

### [Remove a stack](#remove-a-stack)

This will remove the stack with the name `myapp`. Services, networks, and secrets associated with the stack will be removed.

```
$ docker stack rm myapp
Removing service myapp_redis
Removing service myapp_web
Removing service myapp_lb
Removing network myapp_default
Removing network myapp_frontend
```

### [Remove multiple stacks](#remove-multiple-stacks)

This will remove all the specified stacks, `myapp` and `vossibility`. Services, networks, and secrets associated with all the specified stacks will be removed.

```
$ docker stack rm myapp vossibility
Removing service myapp_redis
Removing service myapp_web
Removing service myapp_lb
Removing network myapp_default
Removing network myapp_frontend
Removing service vossibility_nsqd
Removing service vossibility_logstash
Removing service vossibility_elasticsearch
Removing service vossibility_kibana
Removing service vossibility_ghollector
Removing service vossibility_lookupd
Removing network vossibility_default
Removing network vossibility_vossibility
```