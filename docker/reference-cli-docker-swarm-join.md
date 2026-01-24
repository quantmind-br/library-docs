---
title: docker swarm join
url: https://docs.docker.com/reference/cli/docker/swarm/join/
source: llms
fetched_at: 2026-01-24T14:41:20.987286729-03:00
rendered_js: false
word_count: 554
summary: This document explains the usage and configuration options for the docker swarm join command, which allows nodes to join a swarm as either managers or workers. It covers critical parameters such as security tokens, node availability, and network address advertising.
tags:
    - docker-swarm
    - cluster-management
    - node-configuration
    - container-orchestration
    - swarm-join
    - network-settings
category: reference
---

DescriptionJoin a swarm as a node and/or managerUsage`docker swarm join [OPTIONS] HOST:PORT`

Swarm This command works with the Swarm orchestrator.

Join a node to a swarm. The node joins as a manager node or worker node based upon the token you pass with the `--token` flag. If you pass a manager token, the node joins as a manager. If you pass a worker token, the node joins as a worker.

OptionDefaultDescription[`--advertise-addr`](#advertise-addr)Advertised address (format: `<ip|interface>[:port]`)[`--availability`](#availability)`active`Availability of the node (`active`, `pause`, `drain`)[`--data-path-addr`](#data-path-addr)API 1.31+ Address or interface to use for data path traffic (format: `<ip|interface>`)  
[`--listen-addr`](#listen-addr)`0.0.0.0:2377`Listen address (format: `<ip|interface>[:port]`)[`--token`](#token)Token for entry into the swarm

### [Join a node to swarm as a manager](#join-a-node-to-swarm-as-a-manager)

The example below demonstrates joining a manager node using a manager token.

A cluster should only have 3-7 managers at most, because a majority of managers must be available for the cluster to function. Nodes that aren't meant to participate in this management quorum should join as workers instead. Managers should be stable hosts that have static IP addresses.

### [Join a node to swarm as a worker](#join-a-node-to-swarm-as-a-worker)

The example below demonstrates joining a worker node using a worker token.

### [`--listen-addr value`](#listen-addr)

If the node is a manager, it will listen for inbound swarm manager traffic on this address. The default is to listen on 0.0.0.0:2377. It is also possible to specify a network interface to listen on that interface's address; for example `--listen-addr eth0:2377`.

Specifying a port is optional. If the value is a bare IP address, or interface name, the default port 2377 will be used.

This flag is generally not necessary when joining an existing swarm.

### [`--advertise-addr value`](#advertise-addr)

This flag specifies the address that will be advertised to other members of the swarm for API access. If unspecified, Docker will check if the system has a single IP address, and use that IP address with the listening port (see `--listen-addr`). If the system has multiple IP addresses, `--advertise-addr` must be specified so that the correct address is chosen for inter-manager communication and overlay networking.

It is also possible to specify a network interface to advertise that interface's address; for example `--advertise-addr eth0:2377`.

Specifying a port is optional. If the value is a bare IP address, or interface name, the default port 2377 will be used.

This flag is generally not necessary when joining an existing swarm. If you're joining new nodes through a load balancer, you should use this flag to ensure the node advertises its IP address and not the IP address of the load balancer.

### [`--data-path-addr`](#data-path-addr)

This flag specifies the address that global scope network drivers will publish towards other nodes in order to reach the containers running on this node. Using this parameter it is then possible to separate the container's data traffic from the management traffic of the cluster. If unspecified, Docker will use the same IP address or interface that is used for the advertise address.

### [`--token string`](#token)

Secret value required for nodes to join the swarm

### [`--availability`](#availability)

This flag specifies the availability of the node at the time the node joins a master. Possible availability values are `active`, `pause`, or `drain`.

This flag is useful in certain situations. For example, a cluster may want to have dedicated manager nodes that are not served as worker nodes. This could be achieved by passing `--availability=drain` to `docker swarm join`.