---
title: Docker network driver plugins
url: https://docs.docker.com/engine/extend/plugins_network/
source: llms
fetched_at: 2026-01-24T14:23:22.431093844-03:00
rendered_js: false
word_count: 272
summary: This document explains how Docker Engine network driver plugins extend networking capabilities and how they are integrated via LibNetwork and the Docker plugin API.
tags:
    - docker-engine
    - network-plugins
    - libnetwork
    - swarm-mode
    - networking-drivers
category: concept
---

This document describes Docker Engine network driver plugins generally available in Docker Engine. To view information on plugins managed by Docker Engine, refer to [Docker Engine plugin system](https://docs.docker.com/engine/extend/).

Docker Engine network plugins enable Engine deployments to be extended to support a wide range of networking technologies, such as VXLAN, IPVLAN, MACVLAN or something completely different. Network driver plugins are supported via the LibNetwork project. Each plugin is implemented as a "remote driver" for LibNetwork, which shares plugin infrastructure with Engine. Effectively, network driver plugins are activated in the same way as other plugins, and use the same kind of protocol.

[Legacy plugins](https://docs.docker.com/engine/extend/legacy_plugins/) do not work in Swarm mode. However, plugins written using the [v2 plugin system](https://docs.docker.com/engine/extend/) do work in Swarm mode, as long as they are installed on each Swarm worker node.

The means of installing and running a network driver plugin depend on the particular plugin. So, be sure to install your plugin according to the instructions obtained from the plugin developer.

Once running however, network driver plugins are used just like the built-in network drivers: by being mentioned as a driver in network-oriented Docker commands. For example,

Some network driver plugins are listed in [plugins](https://docs.docker.com/engine/extend/legacy_plugins/)

The `mynet` network is now owned by `weave`, so subsequent commands referring to that network will be sent to the plugin,

Network plugins are written by third parties, and are published by those third parties, either on [Docker Hub](https://hub.docker.com/search?q=&type=plugin) or on the third party's site.

Network plugins implement the [Docker plugin API](https://docs.docker.com/engine/extend/plugin_api/) and the network plugin protocol

The network driver protocol, in addition to the plugin activation call, is documented as part of libnetwork: [https://github.com/moby/moby/blob/master/daemon/libnetwork/docs/remote.md](https://github.com/moby/moby/blob/master/daemon/libnetwork/docs/remote.md).