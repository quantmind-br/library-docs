---
title: Tips
url: https://docs.docker.com/engine/security/rootless/tips/
source: llms
fetched_at: 2026-01-24T14:25:22.510334711-03:00
rendered_js: false
word_count: 599
summary: This document explains how to configure and manage Docker in rootless mode, covering daemon setup, client configuration, networking adjustments, and resource limitations.
tags:
    - docker-rootless
    - systemd
    - container-security
    - linux-administration
    - resource-management
    - networking
category: guide
---

### [Daemon](#daemon)

The systemd unit file is installed as `~/.config/systemd/user/docker.service`.

Use `systemctl --user` to manage the lifecycle of the daemon:

To launch the daemon on system startup, enable the systemd service and lingering:

Starting Rootless Docker as a systemd-wide service (`/etc/systemd/system/docker.service`) is not supported, even with the `User=` directive.

To run the daemon directly without systemd, you need to run `dockerd-rootless.sh` instead of `dockerd`.

The following environment variables must be set:

- `$HOME`: the home directory
- `$XDG_RUNTIME_DIR`: an ephemeral directory that is only accessible by the expected user, e,g, `~/.docker/run`. The directory should be removed on every host shutdown. The directory can be on tmpfs, however, should not be under `/tmp`. Locating this directory under `/tmp` might be vulnerable to TOCTOU attack.

It's important to note that with directory paths:

- The socket path is set to `$XDG_RUNTIME_DIR/docker.sock` by default. `$XDG_RUNTIME_DIR` is typically set to `/run/user/$UID`.
- The data dir is set to `~/.local/share/docker` by default. The data dir should not be on NFS.
- The daemon config dir is set to `~/.config/docker` by default. This directory is different from `~/.docker` that is used by the client.

### [Client](#client)

Since Docker Engine v23.0, `dockerd-rootless-setuptool.sh install` automatically configures the `docker` CLI to use the `rootless` context.

Prior to Docker Engine v23.0, a user had to specify either the socket path or the CLI context explicitly.

To specify the socket path using `$DOCKER_HOST`:

To specify the CLI context using `docker context`:

### [Rootless Docker in Docker](#rootless-docker-in-docker)

To run Rootless Docker inside "rootful" Docker, use the `docker:<version>-dind-rootless` image instead of `docker:<version>-dind`.

The `docker:<version>-dind-rootless` image runs as a non-root user (UID 1000). However, `--privileged` is required for disabling seccomp, AppArmor, and mount masks.

### [Expose Docker API socket through TCP](#expose-docker-api-socket-through-tcp)

To expose the Docker API socket through TCP, you need to launch `dockerd-rootless.sh` with `DOCKERD_ROOTLESS_ROOTLESSKIT_FLAGS="-p 0.0.0.0:2376:2376/tcp"`.

### [Expose Docker API socket through SSH](#expose-docker-api-socket-through-ssh)

To expose the Docker API socket through SSH, you need to make sure `$DOCKER_HOST` is set on the remote host.

### [Routing ping packets](#routing-ping-packets)

On some distributions, `ping` does not work by default.

Add `net.ipv4.ping_group_range = 0 2147483647` to `/etc/sysctl.conf` (or `/etc/sysctl.d`) and run `sudo sysctl --system` to allow using `ping`.

### [Exposing privileged ports](#exposing-privileged-ports)

To expose privileged ports (&lt; 1024), set `CAP_NET_BIND_SERVICE` on `rootlesskit` binary and restart the daemon.

Or add `net.ipv4.ip_unprivileged_port_start=0` to `/etc/sysctl.conf` (or `/etc/sysctl.d`) and run `sudo sysctl --system`.

### [Limiting resources](#limiting-resources)

Limiting resources with cgroup-related `docker run` flags such as `--cpus`, `--memory`, `--pids-limit` is supported only when running with cgroup v2 and systemd. See [Changing cgroup version](https://docs.docker.com/engine/containers/runmetrics/) to enable cgroup v2.

If `docker info` shows `none` as `Cgroup Driver`, the conditions are not satisfied. When these conditions are not satisfied, rootless mode ignores the cgroup-related `docker run` flags. See [Limiting resources without cgroup](#limiting-resources-without-cgroup) for workarounds.

If `docker info` shows `systemd` as `Cgroup Driver`, the conditions are satisfied. However, typically, only `memory` and `pids` controllers are delegated to non-root users by default.

To allow delegation of all controllers, you need to change the systemd configuration as follows:

> Delegating `cpuset` requires systemd 244 or later.

#### [Limiting resources without cgroup](#limiting-resources-without-cgroup)

Even when cgroup is not available, you can still use the traditional `ulimit` and [`cpulimit`](https://github.com/opsengine/cpulimit), though they work in process-granularity rather than in container-granularity, and can be arbitrarily disabled by the container process.

For example:

- To limit CPU usage to 0.5 cores (similar to `docker run --cpus 0.5`): `docker run <IMAGE> cpulimit --limit=50 --include-children <COMMAND>`
- To limit max VSZ to 64MiB (similar to `docker run --memory 64m`): `docker run <IMAGE> sh -c "ulimit -v 65536; <COMMAND>"`
- To limit max number of processes to 100 per namespaced UID 2000 (similar to `docker run --pids-limit=100`): `docker run --user 2000 --ulimit nproc=100 <IMAGE> <COMMAND>`