---
title: Engine v26.0
url: https://docs.docker.com/engine/release-notes/26.0/
source: llms
fetched_at: 2026-01-24T14:25:10.735639754-03:00
rendered_js: false
word_count: 131
summary: This document explains the default behavior of IPv6 on container loopback interfaces and provides instructions on how to manually disable it using sysctl settings.
tags:
    - docker
    - ipv6
    - networking
    - container-configuration
    - sysctl
    - moby
category: configuration
---

Always attempt to enable IPv6 on a container's loopback interface, and only include IPv6 in `/etc/hosts` if successful. [moby/moby#47062](https://github.com/moby/moby/pull/47062)

By default, IPv6 will remain enabled on a container's loopback interface when the container is not connected to an IPv6-enabled network. For example, containers that are only connected to an IPv4-only network now have the `::1` address on their loopback interface.

To disable IPv6 in a container, use option `--sysctl net.ipv6.conf.all.disable_ipv6=1` in the `create` or `run` command, or the equivalent `sysctls` option in the service configuration section of a Compose file.

If IPv6 is not available in a container because it has been explicitly disabled for the container, or the host's networking stack does not have IPv6 enabled (or for any other reason) the container's `/etc/hosts` file will not include IPv6 entries.