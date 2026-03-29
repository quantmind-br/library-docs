---
title: Join nodes to a swarm
url: https://docs.docker.com/engine/swarm/join-nodes/
source: llms
fetched_at: 2026-01-24T14:25:56.556097516-03:00
rendered_js: false
word_count: 459
summary: This document explains how to add worker and manager nodes to a Docker Swarm to increase capacity and ensure high availability through fault tolerance. It describes the use of join tokens and the specific actions performed by the Docker Engine when joining a cluster.
tags:
    - docker-swarm
    - cluster-management
    - node-management
    - swarm-mode
    - high-availability
category: guide
---

When you first create a swarm, you place a single Docker Engine into Swarm mode. To take full advantage of Swarm mode you can add nodes to the swarm:

- Adding worker nodes increases capacity. When you deploy a service to a swarm, the engine schedules tasks on available nodes whether they are worker nodes or manager nodes. When you add workers to your swarm, you increase the scale of the swarm to handle tasks without affecting the manager raft consensus.
- Manager nodes increase fault-tolerance. Manager nodes perform the orchestration and cluster management functions for the swarm. Among manager nodes, a single leader node conducts orchestration tasks. If a leader node goes down, the remaining manager nodes elect a new leader and resume orchestration and maintenance of the swarm state. By default, manager nodes also run tasks.

Docker Engine joins the swarm depending on the **join-token** you provide to the `docker swarm join` command. The node only uses the token at join time. If you subsequently rotate the token, it doesn't affect existing swarm nodes. Refer to [Run Docker Engine in swarm mode](https://docs.docker.com/engine/swarm/swarm-mode/#view-the-join-command-or-update-a-swarm-join-token).

## [Join as a worker node](#join-as-a-worker-node)

To retrieve the join command including the join token for worker nodes, run the following command on a manager node:

```
$ docker swarm join-token worker
To add a worker to this swarm, run the following command:
    docker swarm join \
    --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
    192.168.99.100:2377
```

Run the command from the output on the worker to join the swarm:

```
$ docker swarm join \
  --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
  192.168.99.100:2377
This node joined a swarm as a worker.
```

The `docker swarm join` command does the following:

- Switches Docker Engine on the current node into Swarm mode.
- Requests a TLS certificate from the manager.
- Names the node with the machine hostname.
- Joins the current node to the swarm at the manager listen address based upon the swarm token.
- Sets the current node to `Active` availability, meaning it can receive tasks from the scheduler.
- Extends the `ingress` overlay network to the current node.

## [Join as a manager node](#join-as-a-manager-node)

When you run `docker swarm join` and pass the manager token, Docker Engine switches into Swarm mode the same as for workers. Manager nodes also participate in the raft consensus. The new nodes should be `Reachable`, but the existing manager remains the swarm `Leader`.

Docker recommends three or five manager nodes per cluster to implement high availability. Because Swarm-mode manager nodes share data using Raft, there must be an odd number of managers. The swarm can continue to function after as long as a quorum of more than half of the manager nodes are available.

For more detail about swarm managers and administering a swarm, see [Administer and maintain a swarm of Docker Engines](https://docs.docker.com/engine/swarm/admin_guide/).

To retrieve the join command including the join token for manager nodes, run the following command on a manager node:

```
$ docker swarm join-token manager
To add a manager to this swarm, run the following command:
    docker swarm join \
    --token SWMTKN-1-61ztec5kyafptydic6jfc1i33t37flcl4nuipzcusor96k7kby-5vy9t8u35tuqm7vh67lrz9xp6 \
    192.168.99.100:2377
```

Run the command from the output on the new manager node to join it to the swarm:

```
$ docker swarm join \
  --token SWMTKN-1-61ztec5kyafptydic6jfc1i33t37flcl4nuipzcusor96k7kby-5vy9t8u35tuqm7vh67lrz9xp6 \
  192.168.99.100:2377
This node joined a swarm as a manager.
```

## [Learn More](#learn-more)

- `swarm join` [command line reference](https://docs.docker.com/reference/cli/docker/swarm/join/)
- [Swarm mode tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)