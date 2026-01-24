---
title: Configure remote access for Docker daemon
url: https://docs.docker.com/engine/daemon/remote-access/
source: llms
fetched_at: 2026-01-24T14:23:05.132746948-03:00
rendered_js: false
word_count: 305
summary: This document explains how to configure the Docker daemon to accept remote client connections using systemd or configuration files, emphasizing security considerations and firewall setup.
tags:
    - docker-daemon
    - remote-access
    - network-security
    - systemd
    - configuration
    - tls-encryption
category: guide
---

By default, the Docker daemon listens for connections on a Unix socket to accept requests from local clients. You can configure Docker to accept requests from remote clients by configuring it to listen on an IP address and port as well as the Unix socket.

Configuring Docker to accept connections from remote clients can leave you vulnerable to unauthorized access to the host and other attacks.

It's critically important that you understand the security implications of opening Docker to the network. If steps aren't taken to secure the connection, it's possible for remote non-root users to gain root access on the host.

Remote access without TLS is **not recommended**, and will require explicit opt-in in a future release. For more information on how to use TLS certificates to secure this connection, see [Protect the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/).

You can enable remote access to the daemon either using a `docker.service` systemd unit file for Linux distributions using systemd. Or you can use the `daemon.json` file, if your distribution doesn't use systemd.

Configuring Docker to listen for connections using both the systemd unit file and the `daemon.json` file causes a conflict that prevents Docker from starting.

If you run a firewall on the same host as you run Docker, and you want to access the Docker Remote API from another remote host, you must configure your firewall to allow incoming connections on the Docker port. The default port is `2376` if you're using TLS encrypted transport, or `2375` otherwise.

Consult the documentation for your OS and firewall. The following information might help you get started. The settings used in this instruction are permissive, and you may want to use a different configuration that locks your system down more.

For more detailed information on configuration options for remote access to the daemon, refer to the [dockerd CLI reference](https://docs.docker.com/reference/cli/dockerd/#bind-docker-to-another-hostport-or-a-unix-socket).