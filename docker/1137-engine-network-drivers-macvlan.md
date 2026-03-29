---
title: Macvlan network driver
url: https://docs.docker.com/engine/network/drivers/macvlan/
source: llms
fetched_at: 2026-01-24T14:24:26.410506254-03:00
rendered_js: false
word_count: 942
summary: This document explains how to use the Docker macvlan network driver to connect containers directly to a physical network by assigning them unique MAC addresses. It covers configuration options, technical requirements, and usage examples for both standard bridge and 802.1Q trunked modes.
tags:
    - docker-networking
    - macvlan
    - network-drivers
    - linux-kernel
    - 8021q
    - container-networking
category: guide
---

Some applications, especially legacy applications or applications which monitor network traffic, expect to be directly connected to the physical network. In this type of situation, you can use the `macvlan` network driver to assign a MAC address to each container's virtual network interface, making it appear to be a physical network interface directly connected to the physical network. In this case, you need to designate a physical interface on your Docker host to use for the Macvlan, as well as the subnet and gateway of the network. You can even isolate your Macvlan networks using different physical network interfaces.

- The macvlan driver only works on Linux hosts. It is not supported on Docker Desktop for Mac or Windows, or Docker Engine on Windows.
- Most cloud providers block macvlan networking. You may need physical access to your networking equipment.
- Requires at least Linux kernel version 3.9 (version 4.0 or later is recommended).
- The macvlan driver is not supported in rootless mode.

<!--THE END-->

- You may unintentionally degrade your network due to IP address exhaustion or to "VLAN spread", a situation that occurs when you have an inappropriately large number of unique MAC addresses in your network.
- Your networking equipment needs to be able to handle "promiscuous mode", where one physical interface can be assigned multiple MAC addresses.
- If your application can work using a bridge (on a single Docker host) or overlay (to communicate across multiple Docker hosts), these solutions may be better in the long term.
- Containers attached to a macvlan network cannot communicate with the host directly, this is a restriction in the Linux kernel. If you need communication between the host and the containers, you can connect the containers to a bridge network as well as the macvlan. It is also possible to create a macvlan interface on the host with the same parent interface, and assign it an IP address in the Docker network's subnet.

The following table describes the driver-specific options that you can pass to `--opt` when creating a network using the `macvlan` driver.

OptionDefaultDescription`macvlan_mode``bridge`Sets the Macvlan mode. Can be one of: `bridge`, `vepa`, `passthru`, `private``parent`Specifies the parent interface to use.

When you create a Macvlan network, it can either be in bridge mode or 802.1Q trunk bridge mode.

- In bridge mode, Macvlan traffic goes through a physical device on the host.
- In 802.1Q trunk bridge mode, traffic goes through an 802.1Q sub-interface which Docker creates on the fly. This allows you to control routing and filtering at a more granular level.

### [Bridge mode](#bridge-mode)

To create a `macvlan` network which bridges with a given physical network interface, use `--driver macvlan` with the `docker network create` command. You also need to specify the `parent`, which is the interface the traffic will physically go through on the Docker host.

If you need to exclude IP addresses from being used in the `macvlan` network, such as when a given IP address is already in use, use `--aux-addresses`:

### [802.1Q trunk bridge mode](#8021q-trunk-bridge-mode)

If you specify a `parent` interface name with a dot included, such as `eth0.50`, Docker interprets that as a sub-interface of `eth0` and creates the sub-interface automatically.

### [Use an IPvlan instead of Macvlan](#use-an-ipvlan-instead-of-macvlan)

An `ipvlan` network created with option `-o ipvlan_mode=l2` is similar to a macvlan network. The main difference is that the `ipvlan` driver doesn't assign a MAC address to each container, the layer-2 network stack is shared by devices in the ipvlan network. So, containers use the parent interface's MAC address.

The network will see fewer MAC addresses, and the host's MAC address will be associated with the IP address of each container.

The choice of network type depends on your environment and requirements. There are some notes about the trade-offs in the [Linux kernel documentation](https://docs.kernel.org/networking/ipvlan.html#what-to-choose-macvlan-vs-ipvlan).

If you have [configured the Docker daemon to allow IPv6](https://docs.docker.com/engine/daemon/ipv6/), you can use dual-stack IPv4/IPv6 `macvlan` networks.

This section provides hands-on examples for working with macvlan networks, including bridge mode and 802.1Q trunk bridge mode.

> These examples assume your ethernet interface is `eth0`. If your device has a different name, use that instead.

### [Bridge mode example](#bridge-mode-example)

In bridge mode, your traffic flows through `eth0` and Docker routes traffic to your container using its MAC address. To network devices on your network, your container appears to be physically attached to the network.

1. Create a macvlan network called `my-macvlan-net`. Modify the `subnet`, `gateway`, and `parent` values to match your environment:
   
   Verify the network was created:
2. Start an `alpine` container and attach it to the `my-macvlan-net` network. The `-dit` flags start the container in the background. The `--rm` flag removes the container when it stops:
3. Inspect the container and notice the `MacAddress` key within the `Networks` section:
   
   Look for output similar to:
4. Check how the container sees its own network interfaces:
   
   Check the routing table:
5. Stop the container (Docker removes it automatically) and remove the network:

### [802.1Q trunked bridge mode example](#8021q-trunked-bridge-mode-example)

In 802.1Q trunk bridge mode, your traffic flows through a sub-interface of `eth0` (called `eth0.10`) and Docker routes traffic to your container using its MAC address. To network devices on your network, your container appears to be physically attached to the network.

1. Create a macvlan network called `my-8021q-macvlan-net`. Modify the `subnet`, `gateway`, and `parent` values to match your environment:
   
   Verify the network was created and has parent `eth0.10`. You can use `ip addr show` on the Docker host to verify that the interface `eth0.10` exists:
2. Start an `alpine` container and attach it to the `my-8021q-macvlan-net` network:
3. Inspect the container and notice the `MacAddress` key:
   
   Look for the `Networks` section with the MAC address.
4. Check how the container sees its own network interfaces:
   
   Check the routing table:
5. Stop the container and remove the network: