---
title: Bridge network driver
url: https://docs.docker.com/engine/network/drivers/bridge/
source: llms
fetched_at: 2026-01-24T14:24:22.158770094-03:00
rendered_js: false
word_count: 2296
summary: This document explains the functionality and advantages of Docker bridge networks, focusing on the differences between default and user-defined bridge configurations for container communication and isolation.
tags:
    - docker-networking
    - bridge-networks
    - container-communication
    - network-isolation
    - dns-resolution
    - port-publishing
    - docker-engine
category: guide
---

A Docker bridge network has an IPv4 subnet and, optionally, an IPv6 subnet. Each container connected to the bridge network has a network interface with addresses in the network's subnets. By default, it:

- Allows unrestricted network access to containers in the network from the host, and from other containers connected to the same bridge network.
- Blocks access from containers in other networks and from outside the Docker host.
- Uses masquerading to give containers external network access. Devices on the host's external networks only see the IP address of the Docker host.
- Supports port publishing, where network traffic is forwarded between container ports and ports on host IP addresses. The published ports can be accessed from outside the Docker host, on its IP addresses.

In terms of Docker, a bridge network uses a software bridge which lets containers connected to the same bridge network communicate, while providing isolation from containers that aren't connected to that bridge network. By default, the Docker bridge driver automatically installs rules in the host machine so that containers connected to different bridge networks can only communicate with each other using published ports.

Bridge networks apply to containers running on the same Docker daemon host. For communication among containers running on different Docker daemon hosts, you can either manage routing at the OS level, or you can use an [overlay network](https://docs.docker.com/engine/network/drivers/overlay/).

When you start Docker, a [default bridge network](#use-the-default-bridge-network) (also called `bridge`) is created automatically, and newly-started containers connect to it unless otherwise specified. You can also create user-defined custom bridge networks. **User-defined bridge networks are superior to the default `bridge` network.**

- **User-defined bridges provide automatic DNS resolution between containers**.
  
  Containers on the default bridge network can only access each other by IP addresses, unless you use the [`--link` option](https://docs.docker.com/engine/network/links/), which is considered legacy. On a user-defined bridge network, containers can resolve each other by name or alias.
  
  Imagine an application with a web front-end and a database back-end. If you call your containers `web` and `db`, the web container can connect to the db container at `db`, no matter which Docker host the application stack is running on.
  
  If you run the same application stack on the default bridge network, you need to manually create links between the containers (using the legacy `--link` flag). These links need to be created in both directions, so you can see this gets complex with more than two containers which need to communicate. Alternatively, you can manipulate the `/etc/hosts` files within the containers, but this creates problems that are difficult to debug.
- **User-defined bridges provide better isolation**.
  
  All containers without a `--network` specified, are attached to the default bridge network. This can be a risk, as unrelated stacks/services/containers are then able to communicate.
  
  Using a user-defined network provides a scoped network in which only containers attached to that network are able to communicate.
- **Containers can be attached and detached from user-defined networks on the fly**.
  
  During a container's lifetime, you can connect or disconnect it from user-defined networks on the fly. To remove a container from the default bridge network, you need to stop the container and recreate it with different network options.
- **Each user-defined network creates a configurable bridge**.
  
  If your containers use the default bridge network, you can configure it, but all the containers use the same settings, such as MTU and `iptables` rules. In addition, configuring the default bridge network happens outside of Docker itself, and requires a restart of Docker.
  
  User-defined bridge networks are created and configured using `docker network create`. If different groups of applications have different network requirements, you can configure each user-defined bridge separately, as you create it.
- **Linked containers on the default bridge network share environment variables**.
  
  Originally, the only way to share environment variables between two containers was to link them using the [`--link` flag](https://docs.docker.com/engine/network/links/). This type of variable sharing isn't possible with user-defined networks. However, there are superior ways to share environment variables. A few ideas:
  
  - Multiple containers can mount a file or directory containing the shared information, using a Docker volume.
  - Multiple containers can be started together using `docker-compose` and the compose file can define the shared variables.
  - You can use swarm services instead of standalone containers, and take advantage of shared [secrets](https://docs.docker.com/engine/swarm/secrets/) and [configs](https://docs.docker.com/engine/swarm/configs/).

Containers connected to the same user-defined bridge network effectively expose all ports to each other. For a port to be accessible to containers or non-Docker hosts on different networks, that port must be *published* using the `-p` or `--publish` flag.

The following table describes the driver-specific options that you can pass to `--opt` when creating a custom network using the `bridge` driver.

OptionDefaultDescription`com.docker.network.bridge.name`Interface name to use when creating the Linux bridge.`com.docker.network.bridge.enable_ip_masquerade``true`Enable IP masquerading.`com.docker.network.host_ipv4`  
`com.docker.network.host_ipv6`Address to use for source NAT. See [Packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/).`com.docker.network.bridge.gateway_mode_ipv4`  
`com.docker.network.bridge.gateway_mode_ipv6``nat`Control external connectivity. See [Packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/).`com.docker.network.bridge.enable_icc``true`Enable or Disable inter-container connectivity.`com.docker.network.bridge.host_binding_ipv4`all IPv4 and IPv6 addressesDefault IP when binding container ports.`com.docker.network.driver.mtu``0` (no limit)Set the containers network Maximum Transmission Unit (MTU).`com.docker.network.container_iface_prefix``eth`Set a custom prefix for container interfaces.`com.docker.network.bridge.inhibit_ipv4``false`Prevent Docker from [assigning an IP address](#skip-bridge-ip-address-configuration) to the bridge.

Some of these options are also available as flags to the `dockerd` CLI, and you can use them to configure the default `docker0` bridge when starting the Docker daemon. The following table shows which options have equivalent flags in the `dockerd` CLI.

OptionFlag`com.docker.network.bridge.name`-`com.docker.network.bridge.enable_ip_masquerade``--ip-masq``com.docker.network.bridge.enable_icc``--icc``com.docker.network.bridge.host_binding_ipv4``--ip``com.docker.network.driver.mtu``--mtu``com.docker.network.container_iface_prefix`-

The Docker daemon supports a `--bridge` flag, which you can use to define your own `docker0` bridge. Use this option if you want to run multiple daemon instances on the same host. For details, see [Run multiple daemons](https://docs.docker.com/reference/cli/dockerd/#run-multiple-daemons).

### [Default host binding address](#default-host-binding-address)

When no host address is given in port publishing options like `-p 80` or `-p 8080:80`, the default is to make the container's port 80 available on all host addresses, IPv4 and IPv6.

The bridge network driver option `com.docker.network.bridge.host_binding_ipv4` can be used to modify the default address for published ports.

Despite the option's name, it is possible to specify an IPv6 address.

When the default binding address is an address assigned to a specific interface, the container's port will only be accessible via that address.

Setting the default binding address to `::` means published ports will only be available on the host's IPv6 addresses. However, setting it to `0.0.0.0` means it will be available on the host's IPv4 and IPv6 addresses.

To restrict a published port to IPv4 only, the address must be included in the container's publishing options. For example, `-p 0.0.0.0:8080:80`.

Use the `docker network create` command to create a user-defined bridge network.

You can specify the subnet, the IP address range, the gateway, and other options. See the [docker network create](https://docs.docker.com/reference/cli/docker/network/create/#specify-advanced-options) reference or the output of `docker network create --help` for details.

Use the `docker network rm` command to remove a user-defined bridge network. If containers are currently connected to the network, [disconnect them](#disconnect-a-container-from-a-user-defined-bridge) first.

> **What's really happening?**
> 
> When you create or remove a user-defined bridge or connect or disconnect a container from a user-defined bridge, Docker uses tools specific to the operating system to manage the underlying network infrastructure (such as adding or removing bridge devices or configuring `iptables` rules on Linux). These details should be considered implementation details. Let Docker manage your user-defined networks for you.

When you create a new container, you can specify one or more `--network` flags. This example connects an Nginx container to the `my-net` network. It also publishes port 80 in the container to port 8080 on the Docker host, so external clients can access that port. Any other container connected to the `my-net` network has access to all ports on the `my-nginx` container, and vice versa.

To connect a **running** container to an existing user-defined bridge, use the `docker network connect` command. The following command connects an already-running `my-nginx` container to an already-existing `my-net` network:

To disconnect a running container from a user-defined bridge, use the `docker network disconnect` command. The following command disconnects the `my-nginx` container from the `my-net` network.

When you create your network, you can specify the `--ipv6` flag to enable IPv6.

If you do not provide a `--subnet` option, a Unique Local Address (ULA) prefix will be chosen automatically.

To skip IPv4 address configuration on the bridge and in its containers, create the network with option `--ipv4=false`, and enable IPv6 using `--ipv6`.

IPv4 address configuration cannot be disabled in the default bridge network.

The default `bridge` network is considered a legacy detail of Docker and is not recommended for production use. Configuring it is a manual operation, and it has [technical shortcomings](#differences-between-user-defined-bridges-and-the-default-bridge).

### [Connect a container to the default bridge network](#connect-a-container-to-the-default-bridge-network)

If you do not specify a network using the `--network` flag, and you do specify a network driver, your container is connected to the default `bridge` network by default. Containers connected to the default `bridge` network can communicate, but only by IP address, unless they're linked using the [legacy `--link` flag](https://docs.docker.com/engine/network/links/).

### [Configure the default bridge network](#configure-the-default-bridge-network)

To configure the default `bridge` network, you specify options in `daemon.json`. Here is an example `daemon.json` with several options specified. Only specify the settings you need to customize.

In this example:

- The bridge's address is "192.168.1.1/24" (from `bip`).
- The bridge network's subnet is "192.168.1.0/24" (from `bip`).
- Container addresses will be allocated from "192.168.1.0/25" (from `fixed-cidr`).

### [Use IPv6 with the default bridge network](#use-ipv6-with-the-default-bridge-network)

IPv6 can be enabled for the default bridge using the following options in `daemon.json`, or their command line equivalents.

These three options only affect the default bridge, they are not used by user-defined networks. The addresses in below are examples from the IPv6 documentation range.

- Option `ipv6` is required.
- Option `bip6` is optional, it specifies the address of the default bridge, which will be used as the default gateway by containers. It also specifies the subnet for the bridge network.
- Option `fixed-cidr-v6` is optional, it specifies the address range Docker may automatically allocate to containers.
  
  - The prefix should normally be `/64` or shorter.
  - For experimentation on a local network, it is better to use a Unique Local Address (ULA) prefix (matching `fd00::/8`) than a Link Local prefix (matching `fe80::/10`).
- Option `default-gateway-v6` is optional. If unspecified, the default is the first address in the `fixed-cidr-v6` subnet.

If no `bip6` is specified, `fixed-cidr-v6` defines the subnet for the bridge network. If no `bip6` or `fixed-cidr-v6` is specified, a ULA prefix will be chosen.

Restart Docker for changes to take effect.

Due to limitations set by the Linux kernel, bridge networks become unstable and inter-container communications may break when 1000 containers or more connect to a single network.

For more information about this limitation, see [moby/moby#44973](https://github.com/moby/moby/issues/44973#issuecomment-1543747718).

The bridge is normally assigned the network's `--gateway` address, which is used as the default route from the bridge network to other networks.

The `com.docker.network.bridge.inhibit_ipv4` option lets you create a network without the IPv4 gateway address being assigned to the bridge. This is useful if you want to configure the gateway IP address for the bridge manually. For instance if you add a physical interface to your bridge, and need it to have the gateway address.

With this configuration, north-south traffic (to and from the bridge network) won't work unless you've manually configured the gateway address on the bridge, or a device attached to it.

This option can only be used with user-defined bridge networks.

This section provides hands-on examples for working with bridge networks.

### [Use the default bridge network](#use-the-default-bridge-network-1)

This example shows how the default `bridge` network works. You start two `alpine` containers on the default bridge and test how they communicate.

> The default `bridge` network is not recommended for production. Use user-defined bridge networks instead.

1. List current networks:
   
   The default `bridge` network is listed, along with `host` and `none`.
2. Start two `alpine` containers running `ash`. The `-dit` flags mean detached, interactive, and with a TTY. Since you haven't specified a `--network` flag, the containers connect to the default `bridge` network.
   
   Verify both containers are running:
3. Inspect the `bridge` network to see connected containers:
   
   The output shows both containers connected, with their assigned IP addresses (`172.17.0.2` for `alpine1` and `172.17.0.3` for `alpine2`).
4. Connect to `alpine1`:
   
   Show the network interfaces for `alpine1` from within the container:
   
   In this example, the `eth0` interface has the IP address `172.17.0.2`.
5. From within `alpine1`, verify you can connect to the internet:
6. Ping the second container by its IP address:
   
   This succeeds. Now try pinging by container name:
   
   On the default bridge network, containers can't resolve each other by name.
7. Detach from `alpine1` without stopping it using `CTRL+p CTRL+q`.
8. Clean up: stop the containers and remove them.
   
   Stopped containers lose their IP addresses.

### [Use user-defined bridge networks](#use-user-defined-bridge-networks)

This example shows how user-defined bridge networks provide better isolation and automatic DNS resolution between containers.

1. Create the `alpine-net` network:
2. List Docker's networks:
   
   Inspect the `alpine-net` network:
   
   This shows the network's gateway (for example, `172.18.0.1`) and that no containers are connected yet.
3. Create four containers. Three connect to `alpine-net`, and one connects to the default `bridge`. Then connect one container to both networks:
   
   Verify all containers are running:
4. Inspect both networks again to see which containers are connected:
   
   Containers `alpine3` and `alpine4` are connected to the `bridge` network.
   
   Containers `alpine1`, `alpine2`, and `alpine4` are connected to `alpine-net`.
5. On user-defined networks, containers can resolve each other by name. Connect to `alpine1` and test:
   
   > Automatic service discovery only resolves custom container names, not default automatically generated names.
6. From `alpine1`, you can't connect to `alpine3` because it's on a different network:
   
   You also can't connect by IP address. If `alpine3`'s IP is `172.17.0.2`:
   
   Detach from `alpine1` using `CTRL+p CTRL+q`.
7. Since `alpine4` is connected to both networks, it can reach all containers. However, you need to use `alpine3`'s IP address:
8. Verify all containers can connect to the internet:
   
   Detach with `CTRL+p CTRL+q` and repeat for `alpine3` and `alpine1` if desired.
9. Clean up:

<!--THE END-->

- Learn about [networking from the container's point of view](https://docs.docker.com/engine/network/)
- Learn about [overlay networks](https://docs.docker.com/engine/network/drivers/overlay/)
- Learn about [Macvlan networks](https://docs.docker.com/engine/network/drivers/macvlan/)