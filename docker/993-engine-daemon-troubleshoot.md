---
title: Troubleshooting the Docker daemon
url: https://docs.docker.com/engine/daemon/troubleshoot/
source: llms
fetched_at: 2026-01-24T14:23:11.896693619-03:00
rendered_js: false
word_count: 1966
summary: This document provides comprehensive instructions for troubleshooting and debugging the Docker daemon, covering issues ranging from connectivity errors and configuration conflicts to kernel compatibility and resource limitations.
tags:
    - docker-daemon
    - troubleshooting
    - debugging
    - configuration-conflicts
    - systemd
    - networking-issues
    - error-handling
category: guide
---

This page describes how to troubleshoot and debug the daemon if you run into issues.

You can turn on debugging on the daemon to learn about the runtime activity of the daemon and to aid in troubleshooting. If the daemon is unresponsive, you can also [force a full stack trace](https://docs.docker.com/engine/daemon/logs/#force-a-stack-trace-to-be-logged) of all threads to be added to the daemon log by sending the `SIGUSR` signal to the Docker daemon.

### [Unable to connect to the Docker daemon](#unable-to-connect-to-the-docker-daemon)

This error may indicate:

- The Docker daemon isn't running on your system. Start the daemon and try running the command again.
- Your Docker client is attempting to connect to a Docker daemon on a different host, and that host is unreachable.

### [Check whether Docker is running](#check-whether-docker-is-running)

The operating-system independent way to check whether Docker is running is to ask Docker, using the `docker info` command.

You can also use operating system utilities, such as `sudo systemctl is-active docker` or `sudo status docker` or `sudo service docker status`, or checking the service status using Windows utilities.

Finally, you can check in the process list for the `dockerd` process, using commands like `ps` or `top`.

#### [Check which host your client is connecting to](#check-which-host-your-client-is-connecting-to)

To see which host your client is connecting to, check the value of the `DOCKER_HOST` variable in your environment.

If this command returns a value, the Docker client is set to connect to a Docker daemon running on that host. If it's unset, the Docker client is set to connect to the Docker daemon running on the local host. If it's set in error, use the following command to unset it:

You may need to edit your environment in files such as `~/.bashrc` or `~/.profile` to prevent the `DOCKER_HOST` variable from being set erroneously.

If `DOCKER_HOST` is set as intended, verify that the Docker daemon is running on the remote host and that a firewall or network outage isn't preventing you from connecting.

### [Troubleshoot conflicts between the `daemon.json` and startup scripts](#troubleshoot-conflicts-between-the-daemonjson-and-startup-scripts)

If you use a `daemon.json` file and also pass options to the `dockerd` command manually or using start-up scripts, and these options conflict, Docker fails to start with an error such as:

If you see an error similar to this one and you are starting the daemon manually with flags, you may need to adjust your flags or the `daemon.json` to remove the conflict.

> If you see this specific error message about `hosts`, continue to the [next section](#configure-the-daemon-host-with-systemd) for a workaround.

If you are starting Docker using your operating system's init scripts, you may need to override the defaults in these scripts in ways that are specific to the operating system.

#### [Configure the daemon host with systemd](#configure-the-daemon-host-with-systemd)

One notable example of a configuration conflict that's difficult to troubleshoot is when you want to specify a different daemon address from the default. Docker listens on a socket by default. On Debian and Ubuntu systems using `systemd`, this means that a host flag `-H` is always used when starting `dockerd`. If you specify a `hosts` entry in the `daemon.json`, this causes a configuration conflict and results in the Docker daemon failing to start.

To work around this problem, create a new file `/etc/systemd/system/docker.service.d/docker.conf` with the following contents, to remove the `-H` argument that's used when starting the daemon by default.

There are other times when you might need to configure `systemd` with Docker, such as [configuring a HTTP or HTTPS proxy](https://docs.docker.com/engine/daemon/proxy/).

> If you override this option without specifying a `hosts` entry in the `daemon.json` or a `-H` flag when starting Docker manually, Docker fails to start.

Run `sudo systemctl daemon-reload` before attempting to start Docker. If Docker starts successfully, it's now listening on the IP address specified in the `hosts` key of the `daemon.json` instead of a socket.

> Setting `hosts` in the `daemon.json` isn't supported on Docker Desktop for Windows or Docker Desktop for Mac.

### [Out of memory issues](#out-of-memory-issues)

If your containers attempt to use more memory than the system has available, you may experience an Out of Memory (OOM) exception, and a container, or the Docker daemon, might be stopped by the kernel OOM killer. To prevent this from happening, ensure that your application runs on hosts with adequate memory and see [Understand the risks of running out of memory](https://docs.docker.com/engine/containers/resource_constraints/#understand-the-risks-of-running-out-of-memory).

### [Kernel compatibility](#kernel-compatibility)

Docker can't run correctly if your kernel is older than version 3.10, or if it's missing kernel modules. To check kernel compatibility, you can download and run the [`check-config.sh`](https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh) script.

The script only works on Linux.

### [Kernel cgroup swap limit capabilities](#kernel-cgroup-swap-limit-capabilities)

On Ubuntu or Debian hosts, you may see messages similar to the following when working with an image.

If you don't need these capabilities, you can ignore the warning.

You can turn on these capabilities on Ubuntu or Debian by following these instructions. Memory and swap accounting incur an overhead of about 1% of the total available memory and a 10% overall performance degradation, even when Docker isn't running.

1. Log into the Ubuntu or Debian host as a user with `sudo` privileges.
2. Edit the `/etc/default/grub` file. Add or edit the `GRUB_CMDLINE_LINUX` line to add the following two key-value pairs:
   
   Save and close the file.
3. Update the GRUB boot loader.
   
   An error occurs if your GRUB configuration file has incorrect syntax. In this case, repeat steps 2 and 3.
   
   The changes take effect when you reboot the system.

### [IP forwarding problems](#ip-forwarding-problems)

If you manually configure your network using `systemd-network` with systemd version 219 or later, Docker containers may not be able to access your network. Beginning with systemd version 220, the forwarding setting for a given network (`net.ipv4.conf.<interface>.forwarding`) defaults to off. This setting prevents IP forwarding. It also conflicts with Docker's behavior of enabling the `net.ipv4.conf.all.forwarding` setting within containers.

To work around this on RHEL, CentOS, or Fedora, edit the `<interface>.network` file in `/usr/lib/systemd/network/` on your Docker host, for example, `/usr/lib/systemd/network/80-container-host0.network`.

Add the following block within the `[Network]` section.

This configuration allows IP forwarding from the container as expected.

### [DNS resolver issues](#dns-resolver-issues)

Linux desktop environments often have a network manager program running, that uses `dnsmasq` to cache DNS requests by adding them to `/etc/resolv.conf`. The `dnsmasq` instance runs on a loopback address such as `127.0.0.1` or `127.0.1.1`. It speeds up DNS look-ups and provides DHCP services. Such a configuration doesn't work within a Docker container. The Docker container uses its own network namespace, and resolves loopback addresses such as `127.0.0.1` to itself, and it's unlikely to be running a DNS server on its own loopback address.

If Docker detects that no DNS server referenced in `/etc/resolv.conf` is a fully functional DNS server, the following warning occurs:

If you see this warning, first check to see if you use `dnsmasq`:

If your container needs to resolve hosts which are internal to your network, the public nameservers aren't adequate. You have two choices:

- Specify DNS servers for Docker to use.
- Turn off `dnsmasq`.
  
  Turning off `dnsmasq` adds the IP addresses of actual DNS nameservers to `/etc/resolv.conf`, and you lose the benefits of `dnsmasq`.

You only need to use one of these methods.

### [Specify DNS servers for Docker](#specify-dns-servers-for-docker)

The default location of the configuration file is `/etc/docker/daemon.json`. You can change the location of the configuration file using the `--config-file` daemon flag. The following instruction assumes that the location of the configuration file is `/etc/docker/daemon.json`.

1. Create or edit the Docker daemon configuration file, which defaults to `/etc/docker/daemon.json` file, which controls the Docker daemon configuration.
2. Add a `dns` key with one or more DNS server IP addresses as values.
   
   If the file has existing contents, you only need to add or edit the `dns` line. If your internal DNS server can't resolve public IP addresses, include at least one DNS server that can. Doing so allows you to connect to Docker Hub, and your containers to resolve internet domain names.
   
   Save and close the file.
3. Restart the Docker daemon.
4. Verify that Docker can resolve external IP addresses by trying to pull an image:
5. If necessary, verify that Docker containers can resolve an internal hostname by pinging it.

### [Turn off `dnsmasq`](#turn-off-dnsmasq)

If you prefer not to change the Docker daemon's configuration to use a specific IP address, follow these instructions to turn off `dnsmasq` in NetworkManager.

1. Edit the `/etc/NetworkManager/NetworkManager.conf` file.
2. Comment out the `dns=dnsmasq` line by adding a `#` character to the beginning of the line.
   
   Save and close the file.
3. Restart both NetworkManager and Docker. As an alternative, you can reboot your system.

To turn off `dnsmasq` on RHEL, CentOS, or Fedora:

1. Turn off the `dnsmasq` service:
2. Configure the DNS servers manually using the [Red Hat documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-the-order-of-dns-servers_configuring-and-managing-networking).

### [Docker networks disappearing](#docker-networks-disappearing)

If a Docker network, such as the `docker0` bridge or a custom network, randomly disappears or otherwise appears to be working incorrectly, it could be because another service is interfering with or modifying Docker interfaces. Tools that manage networking interfaces on the host are known to sometimes also inappropriately modify Docker interfaces.

Refer to the following sections for instructions on how to configure your network manager to set Docker interfaces as un-managed, depending on the network management tools that exist on the host:

- If `netscript` is installed, consider [uninstalling it](#uninstall-netscript)
- Configure the network manager to [treat Docker interfaces as un-managed](#un-manage-docker-interfaces)
- If you're using Netplan, you may need to [apply a custom Netplan configuration](#prevent-netplan-from-overriding-network-configuration)

#### [Uninstall `netscript`](#uninstall-netscript)

If `netscript` is installed on your system, you can likely fix this issue by uninstalling it. For example, on a Debian-based system:

#### [Un-manage Docker interfaces](#un-manage-docker-interfaces)

In some cases, the network manager will attempt to manage Docker interfaces by default. You can try to explicitly flag Docker networks as un-managed by editing your system's network configuration settings.

If you're using `NetworkManager`, edit your system network configuration under `/etc/network/interfaces`

1. Create a file at `/etc/network/interfaces.d/20-docker0` with the following contents:
   
   Note that this example configuration only "un-manages" the default `docker0` bridge, not custom networks.
2. Restart `NetworkManager` for the configuration change to take effect.
3. Verify that the `docker0` interface has the `unmanaged` state.

If you're running Docker on a system using `systemd-networkd` as a networking daemon, configure the Docker interfaces as un-managed by creating configuration files under `/etc/systemd/network`:

1. Create `/etc/systemd/network/docker.network` with the following contents:
2. Reload the configuration.
3. Restart the Docker daemon.
4. Verify that the Docker interfaces have the `unmanaged` state.

### [Prevent Netplan from overriding network configuration](#prevent-netplan-from-overriding-network-configuration)

On systems that use [Netplan](https://netplan.io/) through [`cloud-init`](https://cloudinit.readthedocs.io/en/latest/index.html), you may need to apply a custom configuration to prevent `netplan` from overriding the network manager configuration:

1. Follow the steps in [Un-manage Docker interfaces](#un-manage-docker-interfaces) for creating the network manager configuration.
2. Create a `netplan` configuration file under `/etc/netplan/50-cloud-init.yml`.
   
   The following example configuration file is a starting point. Adjust it to match the interfaces you want to un-manage. Incorrect configuration can lead to network connectivity issues.
3. Apply the new Netplan configuration.
4. Restart the Docker daemon:
5. Verify that the Docker interfaces have the `unmanaged` state.

### [Unable to remove filesystem](#unable-to-remove-filesystem)

Some container-based utilities, such as [Google cAdvisor](https://github.com/google/cadvisor), mount Docker system directories, such as `/var/lib/docker/`, into a container. For instance, the documentation for `cadvisor` instructs you to run the `cadvisor` container as follows:

When you bind-mount `/var/lib/docker/`, this effectively mounts all resources of all other running containers as filesystems within the container which mounts `/var/lib/docker/`. When you attempt to remove any of these containers, the removal attempt may fail with an error like the following:

The problem occurs if the container which bind-mounts `/var/lib/docker/` uses `statfs` or `fstatfs` on filesystem handles within `/var/lib/docker/` and does not close them.

Typically, we would advise against bind-mounting `/var/lib/docker` in this way. However, `cAdvisor` requires this bind-mount for core functionality.

If you are unsure which process is causing the path mentioned in the error to be busy and preventing it from being removed, you can use the `lsof` command to find its process. For instance, for the error above:

To work around this problem, stop the container which bind-mounts `/var/lib/docker` and try again to remove the other container.