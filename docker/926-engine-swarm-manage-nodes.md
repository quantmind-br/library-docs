---
title: Manage nodes in a swarm
url: https://docs.docker.com/engine/swarm/manage-nodes/
source: llms
fetched_at: 2026-01-24T14:25:59.503739478-03:00
rendered_js: false
word_count: 1004
summary: This document explains how to manage the lifecycle of nodes in a Docker Swarm, including procedures for inspecting, updating, promoting, and removing nodes from the cluster.
tags:
    - docker-swarm
    - node-management
    - container-orchestration
    - swarm-mode
    - node-labels
    - cluster-administration
category: guide
---

As part of the swarm management lifecycle, you may need to:

- [List nodes in the swarm](#list-nodes)
- [Inspect an individual node](#inspect-an-individual-node)
- [Update a node](#update-a-node)
- [Leave the swarm](#leave-the-swarm)

To view a list of nodes in the swarm run `docker node ls` from a manager node:

The `AVAILABILITY` column shows whether or not the scheduler can assign tasks to the node:

- `Active` means that the scheduler can assign tasks to the node.
- `Pause` means the scheduler doesn't assign new tasks to the node, but existing tasks remain running.
- `Drain` means the scheduler doesn't assign new tasks to the node. The scheduler shuts down any existing tasks and schedules them on an available node.

The `MANAGER STATUS` column shows node participation in the Raft consensus:

- No value indicates a worker node that does not participate in swarm management.
- `Leader` means the node is the primary manager node that makes all swarm management and orchestration decisions for the swarm.
- `Reachable` means the node is a manager node participating in the Raft consensus quorum. If the leader node becomes unavailable, the node is eligible for election as the new leader.
- `Unavailable` means the node is a manager that can't communicate with other managers. If a manager node becomes unavailable, you should either join a new manager node to the swarm or promote a worker node to be a manager.

For more information on swarm administration refer to the [Swarm administration guide](https://docs.docker.com/engine/swarm/admin_guide/).

You can run `docker node inspect <NODE-ID>` on a manager node to view the details for an individual node. The output defaults to JSON format, but you can pass the `--pretty` flag to print the results in human-readable format. For example:

You can modify node attributes to:

- [Change node availability](#change-node-availability)
- [Add or remove label metadata](#add-or-remove-label-metadata)
- [Change a node role](#promote-or-demote-a-node)

### [Change node availability](#change-node-availability)

Changing node availability lets you:

- Drain a manager node so that it only performs swarm management tasks and is unavailable for task assignment.
- Drain a node so you can take it down for maintenance.
- Pause a node so it can't receive new tasks.
- Restore unavailable or paused nodes availability status.

For example, to change a manager node to `Drain` availability:

See [list nodes](#list-nodes) for descriptions of the different availability options.

### [Add or remove label metadata](#add-or-remove-label-metadata)

Node labels provide a flexible method of node organization. You can also use node labels in service constraints. Apply constraints when you create a service to limit the nodes where the scheduler assigns tasks for the service.

Run `docker node update --label-add` on a manager node to add label metadata to a node. The `--label-add` flag supports either a `<key>` or a `<key>=<value>` pair.

Pass the `--label-add` flag once for each node label you want to add:

The labels you set for nodes using `docker node update` apply only to the node entity within the swarm. Do not confuse them with the Docker daemon labels for [dockerd](https://docs.docker.com/engine/manage-resources/labels/).

Therefore, node labels can be used to limit critical tasks to nodes that meet certain requirements. For example, schedule only on machines where special workloads should be run, such as machines that meet [PCI-SS compliance](https://www.pcisecuritystandards.org/).

A compromised worker could not compromise these special workloads because it cannot change node labels.

Engine labels, however, are still useful because some features that do not affect secure orchestration of containers might be better off set in a decentralized manner. For instance, an engine could have a label to indicate that it has a certain type of disk device, which may not be relevant to security directly. These labels are more easily "trusted" by the swarm orchestrator.

Refer to the `docker service create` [CLI reference](https://docs.docker.com/reference/cli/docker/service/create/) for more information about service constraints.

### [Promote or demote a node](#promote-or-demote-a-node)

You can promote a worker node to the manager role. This is useful when a manager node becomes unavailable or if you want to take a manager offline for maintenance. Similarly, you can demote a manager node to the worker role.

> Regardless of your reason to promote or demote a node, you must always maintain a quorum of manager nodes in the swarm. For more information refer to the [Swarm administration guide](https://docs.docker.com/engine/swarm/admin_guide/).

To promote a node or set of nodes, run `docker node promote` from a manager node:

To demote a node or set of nodes, run `docker node demote` from a manager node:

`docker node promote` and `docker node demote` are convenience commands for `docker node update --role manager` and `docker node update --role worker` respectively.

If your swarm service relies on one or more [plugins](https://docs.docker.com/engine/extend/plugin_api/), these plugins need to be available on every node where the service could potentially be deployed. You can manually install the plugin on each node or script the installation. You can also deploy the plugin in a similar way as a global service using the Docker API, by specifying a `PluginSpec` instead of a `ContainerSpec`.

> There is currently no way to deploy a plugin to a swarm using the Docker CLI or Docker Compose. In addition, it is not possible to install plugins from a private repository.

The [`PluginSpec`](https://docs.docker.com/engine/extend/plugin_api/#json-specification) is defined by the plugin developer. To add the plugin to all Docker nodes, use the [`service/create`](https://docs.docker.com/reference/api/engine/v1.31/#operation/ServiceCreate) API, passing the `PluginSpec` JSON defined in the `TaskTemplate`.

Run the `docker swarm leave` command on a node to remove it from the swarm.

For example to leave the swarm on a worker node:

When a node leaves the swarm, Docker Engine stops running in Swarm mode. The orchestrator no longer schedules tasks to the node.

If the node is a manager node, you receive a warning about maintaining the quorum. To override the warning, pass the `--force` flag. If the last manager node leaves the swarm, the swarm becomes unavailable requiring you to take disaster recovery measures.

For information about maintaining a quorum and disaster recovery, refer to the [Swarm administration guide](https://docs.docker.com/engine/swarm/admin_guide/).

After a node leaves the swarm, you can run `docker node rm` on a manager node to remove the node from the node list.

For instance:

- [Swarm administration guide](https://docs.docker.com/engine/swarm/admin_guide/)
- [Docker Engine command line reference](https://docs.docker.com/reference/cli/docker/)
- [Swarm mode tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)