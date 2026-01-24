---
title: Manage swarm service networks
url: https://docs.docker.com/engine/swarm/networking/
source: llms
fetched_at: 2026-01-24T14:26:01.323785633-03:00
rendered_js: false
word_count: 2201
summary: This document explains the networking architecture for Docker Swarm, detailing the differences between control and data plane traffic and how to configure overlay networks, ingress routing, and bridge networks.
tags:
    - docker-swarm
    - networking
    - overlay-network
    - ingress-network
    - container-orchestration
    - network-security
category: guide
---

This page describes networking for swarm services.

A Docker swarm generates two different kinds of traffic:

- Control and management plane traffic: This includes swarm management messages, such as requests to join or leave the swarm. This traffic is always encrypted.
- Application data plane traffic: This includes container traffic and traffic to and from external clients.

The following three network concepts are important to swarm services:

- Overlay networks manage communications among the Docker daemons participating in the swarm. You can create overlay networks, in the same way as user-defined networks for standalone containers. You can attach a service to one or more existing overlay networks as well, to enable service-to-service communication. Overlay networks are Docker networks that use the `overlay` network driver.
- The ingress network is a special overlay network that facilitates load balancing among a service's nodes. When any swarm node receives a request on a published port, it hands that request off to a module called `IPVS`. `IPVS` keeps track of all the IP addresses participating in that service, selects one of them, and routes the request to it, over the `ingress` network.
  
  The `ingress` network is created automatically when you initialize or join a swarm. Most users do not need to customize its configuration, but Docker allows you to do so.
- The docker\_gwbridge is a bridge network that connects the overlay networks (including the `ingress` network) to an individual Docker daemon's physical network. By default, each container a service is running is connected to its local Docker daemon host's `docker_gwbridge` network.
  
  The `docker_gwbridge` network is created automatically when you initialize or join a swarm. Most users do not need to customize its configuration, but Docker allows you to do so.

> See also [Networking overview](https://docs.docker.com/engine/network/) for more details about Swarm networking in general.

Docker daemons participating in a swarm need the ability to communicate with each other over the following ports:

- Port `7946` TCP/UDP for container network discovery.
- Port `4789` UDP (configurable) for the overlay network (including ingress) data path.

When setting up networking in a Swarm, special care should be taken. Consult the [tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/#open-protocols-and-ports-between-the-hosts) for an overview.

When you initialize a swarm or join a Docker host to an existing swarm, two new networks are created on that Docker host:

- An overlay network called `ingress`, which handles the control and data traffic related to swarm services. When you create a swarm service and do not connect it to a user-defined overlay network, it connects to the `ingress` network by default.
- A bridge network called `docker_gwbridge`, which connects the individual Docker daemon to the other daemons participating in the swarm.

### [Create an overlay network](#create-an-overlay-network)

To create an overlay network, specify the `overlay` driver when using the `docker network create` command:

The above command doesn't specify any custom options, so Docker assigns a subnet and uses default options. You can see information about the network using `docker network inspect`.

When no containers are connected to the overlay network, its configuration is not very exciting:

In the above output, notice that the driver is `overlay` and that the scope is `swarm`, rather than `local`, `host`, or `global` scopes you might see in other types of Docker networks. This scope indicates that only hosts which are participating in the swarm can access this network.

The network's subnet and gateway are dynamically configured when a service connects to the network for the first time. The following example shows the same network as above, but with three containers of a `redis` service connected to it.

### [Customize an overlay network](#customize-an-overlay-network)

There may be situations where you don't want to use the default configuration for an overlay network. For a full list of configurable options, run the command `docker network create --help`. The following are some of the most common options to change.

#### [Configure the subnet and gateway](#configure-the-subnet-and-gateway)

By default, the network's subnet and gateway are configured automatically when the first service is connected to the network. You can configure these when creating a network using the `--subnet` and `--gateway` flags. The following example extends the previous one by configuring the subnet and gateway.

##### [Using custom default address pools](#using-custom-default-address-pools)

To customize subnet allocation for your Swarm networks, you can [optionally configure them](https://docs.docker.com/engine/swarm/swarm-mode/) during `swarm init`.

For example, the following command is used when initializing Swarm:

Whenever a user creates a network, but does not use the `--subnet` command line option, the subnet for this network will be allocated sequentially from the next available subnet from the pool. If the specified network is already allocated, that network will not be used for Swarm.

Multiple pools can be configured if discontiguous address space is required. However, allocation from specific pools is not supported. Network subnets will be allocated sequentially from the IP pool space and subnets will be reused as they are deallocated from networks that are deleted.

The default mask length can be configured and is the same for all networks. It is set to `/24` by default. To change the default subnet mask length, use the `--default-addr-pool-mask-length` command line option.

> Default address pools can only be configured on `swarm init` and cannot be altered after cluster creation.

##### [Overlay network size limitations](#overlay-network-size-limitations)

Docker recommends creating overlay networks with `/24` blocks. The `/24` overlay network blocks limit the network to 256 IP addresses.

This recommendation addresses [limitations with swarm mode](https://github.com/moby/moby/issues/30820). If you need more than 256 IP addresses, do not increase the IP block size. You can either use `dnsrr` endpoint mode with an external load balancer, or use multiple smaller overlay networks. See [Configure service discovery](#configure-service-discovery) for more information about different endpoint modes.

#### [Configure encryption of application data](#encryption)

Management and control plane data related to a swarm is always encrypted. For more details about the encryption mechanisms, see the [Docker swarm mode overlay network security model](https://docs.docker.com/engine/network/drivers/overlay/).

Application data among swarm nodes is not encrypted by default. To encrypt this traffic on a given overlay network, use the `--opt encrypted` flag on `docker network create`. This enables IPSEC encryption at the level of the vxlan. This encryption imposes a non-negligible performance penalty, so you should test this option before using it in production.

> You must [customize the automatically created ingress](#customize-ingress) to enable encryption. By default, all ingress traffic is unencrypted, as encryption is a network-level option.

To attach a service to an existing overlay network, pass the `--network` flag to `docker service create`, or the `--network-add` flag to `docker service update`.

Service containers connected to an overlay network can communicate with each other across it.

To see which networks a service is connected to, use `docker service ls` to find the name of the service, then `docker service ps <service-name>` to list the networks. Alternately, to see which services' containers are connected to a network, use `docker network inspect <network-name>`. You can run these commands from any swarm node which is joined to the swarm and is in a `running` state.

### [Configure service discovery](#configure-service-discovery)

Service discovery is the mechanism Docker uses to route a request from your service's external clients to an individual swarm node, without the client needing to know how many nodes are participating in the service or their IP addresses or ports. You don't need to publish ports which are used between services on the same network. For instance, if you have a [WordPress service that stores its data in a MySQL service](https://training.play-with-docker.com/swarm-service-discovery/), and they are connected to the same overlay network, you do not need to publish the MySQL port to the client, only the WordPress HTTP port.

Service discovery can work in two different ways: internal connection-based load-balancing at Layers 3 and 4 using the embedded DNS and a virtual IP (VIP), or external and customized request-based load-balancing at Layer 7 using DNS round robin (DNSRR). You can configure this per service.

- By default, when you attach a service to a network and that service publishes one or more ports, Docker assigns the service a virtual IP (VIP), which is the "front end" for clients to reach the service. Docker keeps a list of all worker nodes in the service, and routes requests between the client and one of the nodes. Each request from the client might be routed to a different node.
- If you configure a service to use DNS round-robin (DNSRR) service discovery, there is not a single virtual IP. Instead, Docker sets up DNS entries for the service such that a DNS query for the service name returns a list of IP addresses, and the client connects directly to one of these.
  
  DNS round-robin is useful in cases where you want to use your own load balancer, such as HAProxy. To configure a service to use DNSRR, use the flag `--endpoint-mode dnsrr` when creating a new service or updating an existing one.

Most users never need to configure the `ingress` network, but Docker allows you to do so. This can be useful if the automatically-chosen subnet conflicts with one that already exists on your network, or you need to customize other low-level network settings such as the MTU, or if you want to [enable encryption](#encryption).

Customizing the `ingress` network involves removing and recreating it. This is usually done before you create any services in the swarm. If you have existing services which publish ports, those services need to be removed before you can remove the `ingress` network.

During the time that no `ingress` network exists, existing services which do not publish ports continue to function but are not load-balanced. This affects services which publish ports, such as a WordPress service which publishes port 80.

1. Inspect the `ingress` network using `docker network inspect ingress`, and remove any services whose containers are connected to it. These are services that publish ports, such as a WordPress service which publishes port 80. If all such services are not stopped, the next step fails.
2. Remove the existing `ingress` network:
3. Create a new overlay network using the `--ingress` flag, along with the custom options you want to set. This example sets the MTU to 1200, sets the subnet to `10.11.0.0/16`, and sets the gateway to `10.11.0.2`.
   
   > You can name your `ingress` network something other than `ingress`, but you can only have one. An attempt to create a second one fails.
4. Restart the services that you stopped in the first step.

The `docker_gwbridge` is a virtual bridge that connects the overlay networks (including the `ingress` network) to an individual Docker daemon's physical network. Docker creates it automatically when you initialize a swarm or join a Docker host to a swarm, but it is not a Docker device. It exists in the kernel of the Docker host. If you need to customize its settings, you must do so before joining the Docker host to the swarm, or after temporarily removing the host from the swarm.

You need to have the `brctl` application installed on your operating system in order to delete an existing bridge. The package name is `bridge-utils`.

1. Stop Docker.
2. Use the `brctl show docker_gwbridge` command to check whether a bridge device exists called `docker_gwbridge`. If so, remove it using `brctl delbr docker_gwbridge`.
3. Start Docker. Do not join or initialize the swarm.
4. Create or re-create the `docker_gwbridge` bridge with your custom settings. This example uses the subnet `10.11.0.0/16`. For a full list of customizable options, see [Bridge driver options](https://docs.docker.com/reference/cli/docker/network/create/#bridge-driver-options).
5. Initialize or join the swarm.

By default, all swarm traffic is sent over the same interface, including control and management traffic for maintaining the swarm itself and data traffic to and from the service containers.

You can separate this traffic by passing the `--data-path-addr` flag when initializing or joining the swarm. If there are multiple interfaces, `--advertise-addr` must be specified explicitly, and `--data-path-addr` defaults to `--advertise-addr` if not specified. Traffic about joining, leaving, and managing the swarm is sent over the `--advertise-addr` interface, and traffic among a service's containers is sent over the `--data-path-addr` interface. These flags can take an IP address or a network device name, such as `eth0`.

This example initializes a swarm with a separate `--data-path-addr`. It assumes that your Docker host has two different network interfaces: 10.0.0.1 should be used for control and management traffic and 192.168.0.1 should be used for traffic relating to services.

This example joins the swarm managed by host `192.168.99.100:2377` and sets the `--advertise-addr` flag to `eth0` and the `--data-path-addr` flag to `eth1`.

Swarm services connected to the same overlay network effectively expose all ports to each other. For a port to be accessible outside of the service, that port must be *published* using the `-p` or `--publish` flag on `docker service create` or `docker service update`. Both the legacy colon-separated syntax and the newer comma-separated value syntax are supported. The longer syntax is preferred because it is somewhat self-documenting.

Flag valueDescription`-p 8080:80` or  
`-p published=8080,target=80`Map TCP port 80 on the service to port 8080 on the routing mesh.`-p 8080:80/udp` or  
`-p published=8080,target=80,protocol=udp`Map UDP port 80 on the service to port 8080 on the routing mesh.`-p 8080:80/tcp -p 8080:80/udp` or  
`-p published=8080,target=80,protocol=tcp -p published=8080,target=80,protocol=udp`Map TCP port 80 on the service to TCP port 8080 on the routing mesh, and map UDP port 80 on the service to UDP port 8080 on the routing mesh.

- [Deploy services to a swarm](https://docs.docker.com/engine/swarm/services/)
- [Swarm administration guide](https://docs.docker.com/engine/swarm/admin_guide/)
- [Swarm mode tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)
- [Networking overview](https://docs.docker.com/engine/network/)
- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/)