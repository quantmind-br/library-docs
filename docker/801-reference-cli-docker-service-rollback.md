---
title: docker service rollback
url: https://docs.docker.com/reference/cli/docker/service/rollback/
source: llms
fetched_at: 2026-01-24T14:41:00.006134024-03:00
rendered_js: false
word_count: 200
summary: This document explains how to use the docker service rollback command to revert a swarm service to its previous configuration version.
tags:
    - docker-swarm
    - service-rollback
    - container-orchestration
    - cli-command
    - cluster-management
category: reference
---

DescriptionRevert changes to a service's configurationUsage`docker service rollback [OPTIONS] SERVICE`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Roll back a specified service to its previous version from the swarm.

> Note
> 
> This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## [Options](#options)

OptionDefaultDescription`-d, --detach`API 1.29+ Exit immediately instead of waiting for the service to converge`-q, --quiet`Suppress progress output

## [Examples](#examples)

### [Roll back to the previous version of a service](#roll-back-to-the-previous-version-of-a-service)

Use the `docker service rollback` command to roll back to the previous version of a service. After executing this command, the service is reverted to the configuration that was in place before the most recent `docker service update` command.

The following example creates a service with a single replica, updates the service to use three replicas, and then rolls back the service to the previous version, having one replica.

Create a service with a single replica:

```
$ docker service create --name my-service -p 8080:80 nginx:alpine
```

Confirm that the service is running with a single replica:

```
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
xbw728mf6q0d        my-service          replicated          1/1                 nginx:alpine        *:8080->80/tcp
```

Update the service to use three replicas:

```
$ docker service update --replicas=3 my-service
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
xbw728mf6q0d        my-service          replicated          3/3                 nginx:alpine        *:8080->80/tcp
```

Now roll back the service to its previous version, and confirm it is running a single replica again:

```
$ docker service rollback my-service
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
xbw728mf6q0d        my-service          replicated          1/1                 nginx:alpine        *:8080->80/tcp
```