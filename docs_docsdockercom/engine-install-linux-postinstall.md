---
title: Post-installation steps
url: https://docs.docker.com/engine/install/linux-postinstall/
source: llms
fetched_at: 2026-01-24T14:23:38.263661108-03:00
rendered_js: false
word_count: 552
summary: This document outlines essential post-installation configuration steps for Docker Engine on Linux, including managing user permissions, service auto-start, and logging driver optimization.
tags:
    - docker-engine
    - linux-setup
    - systemd
    - post-installation
    - logging-drivers
    - user-permissions
category: guide
---

## Linux post-installation steps for Docker Engine

These optional post-installation procedures describe how to configure your Linux host machine to work better with Docker.

The Docker daemon binds to a Unix socket, not a TCP port. By default it's the `root` user that owns the Unix socket, and other users can only access it using `sudo`. The Docker daemon always runs as the `root` user.

If you don't want to preface the `docker` command with `sudo`, create a Unix group called `docker` and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the `docker` group. On some Linux distributions, the system automatically creates this group when installing Docker Engine using a package manager. In that case, there is no need for you to manually create the group.

> The `docker` group grants root-level privileges to the user. For details on how this impacts security in your system, see [Docker Daemon Attack Surface](https://docs.docker.com/engine/security/#docker-daemon-attack-surface).

To create the `docker` group and add your user:

1. Create the `docker` group.
2. Add your user to the `docker` group.
3. Log out and log back in so that your group membership is re-evaluated.
   
   > If you're running Linux in a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.
   
   You can also run the following command to activate the changes to groups:
4. Verify that you can run `docker` commands without `sudo`.
   
   This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.
   
   If you initially ran Docker CLI commands using `sudo` before adding your user to the `docker` group, you may see the following error:
   
   This error indicates that the permission settings for the `~/.docker/` directory are incorrect, due to having used the `sudo` command earlier.
   
   To fix this problem, either remove the `~/.docker/` directory (it's recreated automatically, but any custom settings are lost), or change its ownership and permissions using the following commands:

Many modern Linux distributions use [systemd](https://systemd.io/) to manage which services start when the system boots. On Debian and Ubuntu, the Docker service starts on boot by default. To automatically start Docker and containerd on boot for other Linux distributions using systemd, run the following commands:

To stop this behavior, use `disable` instead.

You can use systemd unit files to configure the Docker service on startup, for example to add an HTTP proxy, set a different directory or partition for the Docker runtime files, or other customizations. For an example, see [Configure the daemon to use a proxy](https://docs.docker.com/engine/daemon/proxy/#systemd-unit-file).

Docker provides [logging drivers](https://docs.docker.com/engine/logging/) for collecting and viewing log data from all containers running on a host. The default logging driver, `json-file`, writes log data to JSON-formatted files on the host filesystem. Over time, these log files expand in size, leading to potential exhaustion of disk resources.

To avoid issues with overusing disk for log data, consider one of the following options:

- Configure the `json-file` logging driver to turn on [log rotation](https://docs.docker.com/engine/logging/drivers/json-file/).
- Use an [alternative logging driver](https://docs.docker.com/engine/logging/configure/#configure-the-default-logging-driver) such as the ["local" logging driver](https://docs.docker.com/engine/logging/drivers/local/) that performs log rotation by default.
- Use a logging driver that sends logs to a remote logging aggregator.

<!--THE END-->

- Take a look at the [Docker workshop](https://docs.docker.com/get-started/workshop/) to learn how to build an image and run it as a containerized application.