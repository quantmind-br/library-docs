---
title: Networks
url: https://docs.docker.com/reference/compose-file/networks/
source: llms
fetched_at: 2026-01-24T14:42:22.382648595-03:00
rendered_js: false
word_count: 670
summary: This document provides a detailed reference for defining and configuring networks within Docker Compose files to enable service communication and isolation. It explains top-level network attributes such as drivers, IPAM settings, and external network integration.
tags:
    - docker-compose
    - container-networking
    - network-configuration
    - orchestration
    - ipam
    - network-drivers
category: reference
---

## Define and manage networks in Docker Compose

Networks let services communicate with each other. By default Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by the service's name. The top-level `networks` element lets you configure named networks that can be reused across multiple services.

To use a network across multiple services, you must explicitly grant each service access by using the [networks](https://docs.docker.com/reference/compose-file/services/) attribute within the `services` top-level element. The `networks` top-level element has additional syntax that provides more granular control.

### [Basic example](#basic-example)

In the following example, at runtime, networks `front-tier` and `back-tier` are created and the `frontend` service is connected to `front-tier` and `back-tier` networks.

### [Advanced example](#advanced-example)

This example shows a Compose file which defines two custom networks. The `proxy` service is isolated from the `db` service, because they do not share a network in common. Only `app` can talk to both.

When a Compose file doesn't declare explicit networks, Compose uses an implicit `default` network. Services without an explicit [`networks`](https://docs.docker.com/reference/compose-file/services/#networks) declaration are connected by Compose to this `default` network:

This example is actually equivalent to:

You can customize the `default` network with an explicit declaration:

For options, see the [Docker Engine docs](https://docs.docker.com/engine/network/drivers/bridge/#options).

### [`attachable`](#attachable)

If `attachable` is set to `true`, then standalone containers should be able to attach to this network, in addition to services. If a standalone container attaches to the network, it can communicate with services and other standalone containers that are also attached to the network.

### [`driver`](#driver)

`driver` specifies which driver should be used for this network. Compose returns an error if the driver is not available on the platform.

For more information on drivers and available options, see [Network drivers](https://docs.docker.com/engine/network/drivers/).

### [`driver_opts`](#driver_opts)

`driver_opts` specifies a list of options as key-value pairs to pass to the driver. These options are driver-dependent.

Consult the [network drivers documentation](https://docs.docker.com/engine/network/) for more information.

### [`enable_ipv4`](#enable_ipv4)

Requires: Docker Compose [2.33.1](https://github.com/docker/compose/releases/tag/v2.33.1) and later

`enable_ipv4` can be used to disable IPv4 address assignment.

### [`enable_ipv6`](#enable_ipv6)

`enable_ipv6` enables IPv6 address assignment.

### [`external`](#external)

If set to `true`:

- `external` specifies that this network’s lifecycle is maintained outside of that of the application. Compose doesn't attempt to create these networks, and returns an error if one doesn't exist.
- All other attributes apart from name are irrelevant. If Compose detects any other attribute, it rejects the Compose file as invalid.

In the following example, `proxy` is the gateway to the outside world. Instead of attempting to create a network, Compose queries the platform for an existing network called `outside` and connects the `proxy` service's containers to it.

### [`ipam`](#ipam)

`ipam` specifies a custom IPAM configuration. This is an object with several properties, each of which is optional:

- `driver`: Custom IPAM driver, instead of the default.
- `config`: A list with zero or more configuration elements, each containing a:
  
  - `subnet`: Subnet in CIDR format that represents a network segment
  - `ip_range`: Range of IPs from which to allocate container IPs
  - `gateway`: IPv4 or IPv6 gateway for the master subnet
  - `aux_addresses`: Auxiliary IPv4 or IPv6 addresses used by Network driver, as a mapping from hostname to IP
- `options`: Driver-specific options as a key-value mapping.

### [`internal`](#internal)

By default, Compose provides external connectivity to networks. `internal`, when set to `true`, lets you create an externally isolated network.

### [`labels`](#labels)

Add metadata to containers using `labels`. You can use either an array or a dictionary.

It is recommended that you use reverse-DNS notation to prevent labels from conflicting with those used by other software.

Compose sets `com.docker.compose.project` and `com.docker.compose.network` labels.

### [`name`](#name)

`name` sets a custom name for the network. The name field can be used to reference networks which contain special characters. The name is used as is and is not scoped with the project name.

It can also be used in conjunction with the `external` property to define the platform network that Compose should retrieve, typically by using a parameter so the Compose file doesn't need to hard-code runtime specific values:

For more examples, see [Networking in Compose](https://docs.docker.com/compose/how-tos/networking/).