---
title: Troubleshooting
url: https://docs.docker.com/engine/security/rootless/troubleshoot/
source: llms
fetched_at: 2026-01-24T14:25:24.031247646-03:00
rendered_js: false
word_count: 1447
summary: This document provides troubleshooting guidance and configuration requirements for running Docker in rootless mode across various Linux distributions. It covers common error messages, systemd integration issues, and networking driver limitations.
tags:
    - docker-engine
    - rootless-mode
    - linux-containers
    - troubleshooting
    - user-namespaces
    - container-security
category: guide
---

### [Distribution-specific hint](#distribution-specific-hint)

- Ubuntu 24.04 and later enables restricted unprivileged user namespaces by default, which prevents unprivileged processes in creating user namespaces unless an AppArmor profile is configured to allow programs to use unprivileged user namespaces.
  
  If you install `docker-ce-rootless-extras` using the deb package (`apt-get install docker-ce-rootless-extras`), then the AppArmor profile for `rootlesskit` is already bundled with the `apparmor` deb package. With this installation method, you don't need to add any manual the AppArmor configuration. If you install the rootless extras using the [installation script](https://get.docker.com/rootless), however, you must add an AppArmor profile for `rootlesskit` manually:
  
  1. Create and install the currently logged-in user's AppArmor profile:
  2. Restart AppArmor.

<!--THE END-->

- Add `kernel.unprivileged_userns_clone=1` to `/etc/sysctl.conf` (or `/etc/sysctl.d`) and run `sudo sysctl --system`

<!--THE END-->

- `sudo modprobe ip_tables iptable_mangle iptable_nat iptable_filter` is required. This might be required on other distributions as well depending on the configuration.
- Known to work on openSUSE 15 and SLES 15.

<!--THE END-->

- For RHEL 8 and similar distributions, installing `fuse-overlayfs` is recommended. Run `sudo dnf install -y fuse-overlayfs`. This step is not required on RHEL 9 and similar distributions.
- You might need `sudo dnf install -y iptables`.

<!--THE END-->

- Only the following storage drivers are supported:
  
  - `overlay2` (only if running with kernel 5.11 or later)
  - `fuse-overlayfs` (only if running with kernel 4.18 or later, and `fuse-overlayfs` is installed)
  - `btrfs` (only if running with kernel 4.18 or later, or `~/.local/share/docker` is mounted with `user_subvol_rm_allowed` mount option)
  - `vfs`
- cgroup is supported only when running with cgroup v2 and systemd. See [Limiting resources](https://docs.docker.com/engine/security/rootless/tips/#limiting-resources).
- Following features are not supported:
  
  - AppArmor
  - Checkpoint
  - Overlay network
  - Exposing SCTP ports
- To use the `ping` command, see [Routing ping packets](https://docs.docker.com/engine/security/rootless/tips/#routing-ping-packets).
- To expose privileged TCP/UDP ports (&lt; 1024), see [Exposing privileged ports](https://docs.docker.com/engine/security/rootless/tips/#exposing-privileged-ports).
- `IPAddress` shown in `docker inspect` is namespaced inside RootlessKit's network namespace. This means the IP address is not reachable from the host without `nsenter`-ing into the network namespace.
- Host network (`docker run --net=host`) is also namespaced inside RootlessKit.
- NFS mounts as the docker "data-root" is not supported. This limitation is not specific to rootless mode.

### [Unable to install with systemd when systemd is present on the system](#unable-to-install-with-systemd-when-systemd-is-present-on-the-system)

`rootlesskit` cannot detect systemd properly if you switch to your user via `sudo su`. For users which cannot be logged-in, you must use the `machinectl` command which is part of the `systemd-container` package. After installing `systemd-container` switch to `myuser` with the following command:

Where `myuser@` is your desired username and @ signifies this machine.

### [Errors when starting the Docker daemon](#errors-when-starting-the-docker-daemon)

**\[rootlesskit:parent] error: failed to start the child: fork/exec /proc/self/exe: operation not permitted**

This error occurs mostly when the value of `/proc/sys/kernel/unprivileged_userns_clone` is set to 0:

To fix this issue, add `kernel.unprivileged_userns_clone=1` to `/etc/sysctl.conf` (or `/etc/sysctl.d`) and run `sudo sysctl --system`.

**\[rootlesskit:parent] error: failed to start the child: fork/exec /proc/self/exe: no space left on device**

This error occurs mostly when the value of `/proc/sys/user/max_user_namespaces` is too small:

To fix this issue, add `user.max_user_namespaces=28633` to `/etc/sysctl.conf` (or `/etc/sysctl.d`) and run `sudo sysctl --system`.

**\[rootlesskit:parent] error: failed to setup UID/GID map: failed to compute uid/gid map: No subuid ranges found for user 1001 ("testuser")**

This error occurs when `/etc/subuid` and `/etc/subgid` are not configured. See [Prerequisites](https://docs.docker.com/engine/security/rootless/#prerequisites).

**could not get XDG\_RUNTIME\_DIR**

This error occurs when `$XDG_RUNTIME_DIR` is not set.

On a non-systemd host, you need to create a directory and then set the path:

> You must remove the directory every time you log out.

On a systemd host, log into the host using `pam_systemd` (see below). The value is automatically set to `/run/user/$UID` and cleaned up on every logout.

**`systemctl --user` fails with "Failed to connect to bus: No such file or directory"**

This error occurs mostly when you switch from the root user to a non-root user with `sudo`:

Instead of `sudo -iu <USERNAME>`, you need to log in using `pam_systemd`. For example:

- Log in through the graphic console
- `ssh <USERNAME>@localhost`
- `machinectl shell <USERNAME>@`

**The daemon does not start up automatically**

You need `sudo loginctl enable-linger $(whoami)` to enable the daemon to start up automatically. See [Advanced Usage](https://docs.docker.com/engine/security/rootless/tips/#advanced-usage).

### [`docker pull` errors](#docker-pull-errors)

**docker: failed to register layer: Error processing tar file(exit status 1): lchown &lt;FILE&gt;: invalid argument**

This error occurs when the number of available entries in `/etc/subuid` or `/etc/subgid` is not sufficient. The number of entries required vary across images. However, 65,536 entries are sufficient for most images. See [Prerequisites](https://docs.docker.com/engine/security/rootless/#prerequisites).

**docker: failed to register layer: ApplyLayer exit status 1 stdout: stderr: lchown &lt;FILE&gt;: operation not permitted**

This error occurs mostly when `~/.local/share/docker` is located on NFS.

A workaround is to specify non-NFS `data-root` directory in `~/.config/docker/daemon.json` as follows:

### [`docker run` errors](#docker-run-errors)

**docker: Error response from daemon: OCI runtime create failed: ...: read unix @-&gt;/run/systemd/private: read: connection reset by peer: unknown.**

This error occurs on cgroup v2 hosts mostly when the dbus daemon is not running for the user.

To fix the issue, run `sudo apt-get install -y dbus-user-session` or `sudo dnf install -y dbus-daemon`, and then relogin.

If the error still occurs, try running `systemctl --user enable --now dbus` (without sudo).

**`--cpus`, `--memory`, and `--pids-limit` are ignored**

This is an expected behavior on cgroup v1 mode. To use these flags, the host needs to be configured for enabling cgroup v2. For more information, see [Limiting resources](https://docs.docker.com/engine/security/rootless/tips/#limiting-resources).

### [Networking errors](#networking-errors)

This section provides troubleshooting tips for networking in rootless mode.

Networking in rootless mode is supported via network and port drivers in RootlessKit. Network performance and characteristics depend on the combination of network and port driver you use. If you're experiencing unexpected behavior or performance related to networking, review the following table which shows the configurations supported by RootlessKit, and how they compare:

Network driverPort driverNet throughputPort throughputSource IP propagationNo SUIDNote`slirp4netns``builtin`SlowFast ✅❌✅Default in a typical setup`vpnkit``builtin`SlowFast ✅❌✅Default when `slirp4netns` isn't installed`slirp4netns``slirp4netns`SlowSlow✅✅`pasta``implicit`SlowFast ✅✅✅Experimental; Needs pasta version 2023\_12\_04 or later`lxc-user-nic``builtin`Fast ✅Fast ✅❌❌Experimental`bypass4netns``bypass4netns`Fast ✅Fast ✅✅✅**Note:** Not integrated to RootlessKit as it needs a custom seccomp profile

For information about troubleshooting specific networking issues, see:

- [`docker run -p` fails with `cannot expose privileged port`](#docker-run--p-fails-with-cannot-expose-privileged-port)
- [Ping doesn't work](#ping-doesnt-work)
- [`IPAddress` shown in `docker inspect` is unreachable](#ipaddress-shown-in-docker-inspect-is-unreachable)
- [`--net=host` doesn't listen ports on the host network namespace](#--nethost-doesnt-listen-ports-on-the-host-network-namespace)
- [Network is slow](#network-is-slow)
- [`docker run -p` does not propagate source IP addresses](#docker-run--p-does-not-propagate-source-ip-addresses)

#### [`docker run -p` fails with `cannot expose privileged port`](#docker-run--p-fails-with-cannot-expose-privileged-port)

`docker run -p` fails with this error when a privileged port (&lt; 1024) is specified as the host port.

When you experience this error, consider using an unprivileged port instead. For example, 8080 instead of 80.

To allow exposing privileged ports, see [Exposing privileged ports](https://docs.docker.com/engine/security/rootless/tips/#exposing-privileged-ports).

#### [Ping doesn't work](#ping-doesnt-work)

Ping does not work when `/proc/sys/net/ipv4/ping_group_range` is set to `1 0`:

For details, see [Routing ping packets](https://docs.docker.com/engine/security/rootless/tips/#routing-ping-packets).

#### [`IPAddress` shown in `docker inspect` is unreachable](#ipaddress-shown-in-docker-inspect-is-unreachable)

This is an expected behavior, as the daemon is namespaced inside RootlessKit's network namespace. Use `docker run -p` instead.

#### [`--net=host` doesn't listen ports on the host network namespace](#--nethost-doesnt-listen-ports-on-the-host-network-namespace)

This is an expected behavior, as the daemon is namespaced inside RootlessKit's network namespace. Use `docker run -p` instead.

#### [Network is slow](#network-is-slow)

Docker with rootless mode uses [slirp4netns](https://github.com/rootless-containers/slirp4netns) as the default network stack if slirp4netns v0.4.0 or later is installed. If slirp4netns is not installed, Docker falls back to [VPNKit](https://github.com/moby/vpnkit). Installing slirp4netns may improve the network throughput.

For more information about network drivers for RootlessKit, see [RootlessKit documentation](https://github.com/rootless-containers/rootlesskit/blob/v2.0.0/docs/network.md).

Also, changing MTU value may improve the throughput. The MTU value can be specified by creating `~/.config/systemd/user/docker.service.d/override.conf` with the following content:

And then restart the daemon:

#### [`docker run -p` does not propagate source IP addresses](#docker-run--p-does-not-propagate-source-ip-addresses)

This is because Docker in rootless mode uses RootlessKit's `builtin` port driver by default, which doesn't support source IP propagation. To enable source IP propagation, you can:

- Use the `slirp4netns` RootlessKit port driver
- Use the `pasta` RootlessKit network driver, with the `implicit` port driver

The `pasta` network driver is experimental, but provides improved throughput performance compared to the `slirp4netns` port driver. The `pasta` driver requires Docker Engine version 25.0 or later.

To change the RootlessKit networking configuration:

1. Create a file at `~/.config/systemd/user/docker.service.d/override.conf`.
2. Add the following contents, depending on which configuration you would like to use:
   
   - `slirp4netns`
   - `pasta` network driver with `implicit` port driver
3. Restart the daemon:

For more information about networking options for RootlessKit, see:

- [Network drivers](https://github.com/rootless-containers/rootlesskit/blob/v2.0.0/docs/network.md)
- [Port drivers](https://github.com/rootless-containers/rootlesskit/blob/v2.0.0/docs/port.md)

### [Tips for debugging](#tips-for-debugging)

**Entering into `dockerd` namespaces**

The `dockerd-rootless.sh` script executes `dockerd` in its own user, mount, and network namespaces.

For debugging, you can enter the namespaces by running `nsenter -U --preserve-credentials -n -m -t $(cat $XDG_RUNTIME_DIR/docker.pid)`.

To remove the systemd service of the Docker daemon, run `dockerd-rootless-setuptool.sh uninstall`:

Unset environment variables PATH and DOCKER\_HOST if you have added them to `~/.bashrc`.

To remove the data directory, run `rootlesskit rm -rf ~/.local/share/docker`.

To remove the binaries, remove `docker-ce-rootless-extras` package if you installed Docker with package managers. If you installed Docker with [https://get.docker.com/rootless](https://get.docker.com/rootless) ([Install without packages](https://docs.docker.com/engine/security/rootless/#install)), remove the binary files under `~/bin`: