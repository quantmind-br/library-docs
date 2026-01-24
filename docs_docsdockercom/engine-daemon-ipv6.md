---
title: Use IPv6 networking
url: https://docs.docker.com/engine/daemon/ipv6/
source: llms
fetched_at: 2026-01-24T14:22:50.950840046-03:00
rendered_js: false
word_count: 497
summary: This document explains how to enable and configure IPv6 networking for Docker on Linux hosts, covering both user-defined networks and the default bridge network.
tags:
    - docker-networking
    - ipv6
    - linux-host
    - docker-daemon
    - network-configuration
    - subnet-allocation
category: guide
---

IPv6 is only supported on Docker daemons running on Linux hosts.

- Using `docker network create`:
- Using `docker network create`, specifying an IPv6 subnet:
- Using a Docker Compose file:

You can now run containers that attach to the `ip6net` network.

This publishes port 80 on both IPv6 and IPv4. You can verify the IPv6 connection by running curl, connecting to port 80 on the IPv6 loopback address:

The following steps show you how to use IPv6 on the default bridge network.

1. Edit the Docker daemon configuration file, located at `/etc/docker/daemon.json`. Configure the following parameters:
   
   - `ipv6` enables IPv6 networking on the default network.
   - `fixed-cidr-v6` assigns a subnet to the default bridge network, enabling dynamic IPv6 address allocation.
   - `ip6tables` enables additional IPv6 packet filter rules, providing network isolation and port mapping. It is enabled by-default, but can be disabled.
2. Save the configuration file.
3. Restart the Docker daemon for your changes to take effect.

You can now run containers on the default bridge network.

This publishes port 80 on both IPv6 and IPv4. You can verify the IPv6 connection by making a request to port 80 on the IPv6 loopback address:

If you don't explicitly configure subnets for user-defined networks, using `docker network create --subnet=<your-subnet>`, those networks use the default address pools of the daemon as a fallback. This also applies to networks created from a Docker Compose file, with `enable_ipv6` set to `true`.

If no IPv6 pools are included in Docker Engine's `default-address-pools`, and no `--subnet` option is given, [Unique Local Addresses (ULAs)](https://en.wikipedia.org/wiki/Unique_local_address) will be used when IPv6 is enabled. These `/64` subnets include a 40-bit Global ID based on the Docker Engine's randomly generated ID, to give a high probability of uniqueness.

The built-in default address pool configuration is shown in [Subnet allocation](https://docs.docker.com/engine/network/#subnet-allocation). It does not include any IPv6 pools.

To use different pools of IPv6 subnets for dynamic address allocation, you must manually configure address pools of the daemon to include:

- The default IPv4 address pools
- One or more IPv6 pools of your own

The following example shows a valid configuration with IPv4 and IPv6 pools, both pools provide 256 subnets. IPv4 subnets with prefix length `/24` will be allocated from a `/16` pool. IPv6 subnets with prefix length `/64` will be allocated from a `/56` pool.

> The address `2001:db8::` in this example is [reserved for use in documentation](https://en.wikipedia.org/wiki/Reserved_IP_addresses#IPv6). Replace it with a valid IPv6 network.
> 
> The default IPv4 pools are from the private address range, similar to the default IPv6 [ULA](https://en.wikipedia.org/wiki/Unique_local_address) networks.

See [Subnet allocation](https://docs.docker.com/engine/network/#subnet-allocation) for more information about `default-address-pools`.

On a host using `xtables` (legacy `iptables`) instead of `nftables`, kernel module `ip6_tables` must be loaded before an IPv6 Docker network can be created, It is normally loaded automatically when Docker starts.

However, if you running Docker in Docker that is not based on a recent version of the [official `docker` image](https://hub.docker.com/_/docker), you may need to run `modprobe ip6_tables` on your host. Alternatively, use daemon option `--ip6tables=false` to disable `ip6tables` for the containerized Docker Engine.

- [Networking overview](https://docs.docker.com/engine/network/)