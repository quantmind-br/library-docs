---
title: How-tos
url: https://docs.docker.com/desktop/features/networking/networking-how-tos/
source: llms
fetched_at: 2026-01-24T14:18:28.650837384-03:00
rendered_js: false
word_count: 834
summary: This document provides instructions for configuring and managing network connectivity in Docker Desktop, covering host-container communication, proxy and VPN settings, and troubleshooting techniques.
tags:
    - docker-desktop
    - networking
    - container-connectivity
    - proxy-configuration
    - vpn-support
    - dns-resolution
    - port-forwarding
category: guide
---

## Explore networking how-tos on Docker Desktop

This page explains how to configure and use networking features, connect containers to host services, work behind proxies or VPNs, and troubleshoot common issues.

For details on how Docker Desktop routes network traffic and file I/O between containers, the VM, and the host, see [Network overview](https://docs.docker.com/desktop/features/networking/#overview).

### [Connect a container to a service on the host](#connect-a-container-to-a-service-on-the-host)

The host has a changing IP address, or none if you have no network access. To connect to services running on your host, use the special DNS name:

NameDescription`host.docker.internal`Resolves to the internal IP address of your host`gateway.docker.internal`Resolves to the gateway IP of the Docker VM

#### [Example](#example)

Run a simple HTTP server on port `8000`:

Then run a container, install `curl`, and try to connect to the host using the following commands:

### [Connect to a container from the host](#connect-to-a-container-from-the-host)

To access containerized services from your host or local network, publish ports with the `-p` or `--publish` flag. For example:

Docker Desktop makes whatever is running on port `80` in the container, in this case, `nginx`, available on port `80` of `localhost`.

> The syntax for `-p` is `HOST_PORT:CLIENT_PORT`.

To publish all ports, use the `-P` flag. For example, the following command starts a container (in detached mode) and the `-P` flag publishes all exposed ports of the container to random ports on the host.

Alternatively, you can also use [host networking](https://docs.docker.com/engine/network/drivers/host/#docker-desktop) to give the container direct access to the network stack of the host.

See the [run command](https://docs.docker.com/reference/cli/docker/container/run/) for more details on publish options used with `docker run`.

All inbound connections pass through the Docker Desktop backend process (`com.docker.backend` (Mac), `com.docker.backend` (Windows), or `qemu` (Linux), which handles port forwarding into the VM. For more details, see [How exposed ports work](https://docs.docker.com/desktop/features/networking/#how-exposed-ports-work)

### [Working with VPNs](#working-with-vpns)

Docker Desktop networking can work when attached to a VPN.

To do this, Docker Desktop intercepts traffic from the containers and injects it into the host as if it originated from the Docker application.

For details about how this traffic appears to host firewalls and endpoint detection systems, see [Firewalls and endpoint visibility](https://docs.docker.com/desktop/features/networking/#firewalls-and-endpoint-visibility.md).

### [Working with proxies](#working-with-proxies)

Docker Desktop can use your system proxy or a manual configuration. To configure proxies:

1. Navigate to the **Resources** tab in **Settings**.
2. From the dropdown menu select **Proxies**.
3. Switch on the **Manual proxy configuration** toggle.
4. Enter your HTTP, HTTPS or SOCKS5 proxy URLS.

For more details on proxies and proxy configurations, see the [Proxy settings documentation](https://docs.docker.com/desktop/settings-and-maintenance/settings/#proxies).

With Docker Desktop version 4.42 and later, you can control how Docker handles container networking and DNS resolution to better support a range of environments — from IPv4-only to dual-stack and IPv6-only systems. These settings help prevent timeouts and connectivity issues caused by incompatible or misconfigured host networks.

You can set the following settings on the **Network** tab in the Docker Desktop Dashboard settings, or if you're an admin, with Settings Management via the [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/#networking), or the [Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/)

> These settings can be overridden on a per-network basis using CLI flags or Compose file options.

### [Default networking mode](#default-networking-mode)

Choose the default IP protocol used when Docker creates new networks. This allows you to align Docker with your host’s network capabilities or organizational requirements, such as enforcing IPv6-only access.

ModeDescription**Dual IPv4/IPv6 (default)**Supports both IPv4 and IPv6. Most flexible.**IPv4 only**Uses only IPv4 addressing.**IPv6 only**Uses only IPv6 addressing.

### [DNS resolution behavior](#dns-resolution-behavior)

Control how Docker filters DNS records returned to containers, improving reliability in environments where only IPv4 or IPv6 is supported. This setting is especially useful for preventing apps from trying to connect using IP families that aren't actually available, which can cause avoidable delays or failures.

OptionDescription**Auto (recommended)**Automatically filters unsupported record types. (A for IPv4, AAAA for IPv6)**Filter IPv4 (A records)**Blocks IPv4 lookups. Only available in dual-stack mode.**Filter IPv6 (AAAA records)**Blocks IPv6 lookups. Only available in dual-stack mode.**No filtering**Returns both A and AAAA records.

> Switching the default networking mode resets the DNS filter to Auto.

### [SSH agent forwarding](#ssh-agent-forwarding)

Docker Desktop for Mac and Linux lets you use the host’s SSH agent inside a container. To do this:

1. Bind mount the SSH agent socket by adding the following parameter to your `docker run` command:
2. Add the `SSH_AUTH_SOCK` environment variable in your container:

To enable the SSH agent in Docker Compose, add the following flags to your service:

### [Changing internal IP addresses](#changing-internal-ip-addresses)

The internal IP addresses used by Docker can be changed from **Settings**. After changing IPs, you need to reset the Kubernetes cluster and to leave any active Swarm.

### [There is no `docker0` bridge on the host](#there-is-no-docker0-bridge-on-the-host)

Because of the way networking is implemented in Docker Desktop, you cannot see a `docker0` interface on the host. This interface is actually within the virtual machine.

### [I cannot ping my containers](#i-cannot-ping-my-containers)

Docker Desktop can't route traffic to Linux containers. However if you're a Windows user, you can ping the Windows containers.

### [Per-container IP addressing is not possible](#per-container-ip-addressing-is-not-possible)

This is because the Docker `bridge` network is not reachable from the host. However if you are a Windows user, per-container IP addressing is possible with Windows containers.