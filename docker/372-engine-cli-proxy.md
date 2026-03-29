---
title: Proxy configuration
url: https://docs.docker.com/engine/cli/proxy/
source: llms
fetched_at: 2026-01-24T14:22:37.620544828-03:00
rendered_js: false
word_count: 686
summary: This document explains how to configure proxy settings for Docker containers and builds using the Docker CLI configuration file or command-line flags. It covers the setup of environment variables for various proxy types and discusses security implications of embedding proxy data.
tags:
    - docker-cli
    - proxy-server
    - container-configuration
    - environment-variables
    - docker-build
    - networking
category: configuration
---

## Use a proxy server with the Docker CLI

This page describes how to configure the Docker CLI to use proxies via environment variables in containers.

This page doesn't describe how to configure proxies for Docker Desktop. For instructions, see [configuring Docker Desktop to use HTTP/HTTPS proxies](https://docs.docker.com/desktop/settings-and-maintenance/settings/#proxies).

If you're running Docker Engine without Docker Desktop, refer to [Configure the Docker daemon to use a proxy](https://docs.docker.com/engine/daemon/proxy/) to learn how to configure a proxy server for the Docker daemon (`dockerd`) itself.

If your container needs to use an HTTP, HTTPS, or FTP proxy server, you can configure it in different ways:

- [Configure the Docker client](#configure-the-docker-client)
- [Set proxy using the CLI](#set-proxy-using-the-cli)

> Unfortunately, there's no standard that defines how web clients should handle proxy environment variables, or the format for defining them.
> 
> If you're interested in the history of these variables, check out this blog post on the subject, by the GitLab team: [We need to talk: Can we standardize NO\_PROXY?](https://about.gitlab.com/blog/2021/01/27/we-need-to-talk-no-proxy/).

You can add proxy configurations for the Docker client using a JSON configuration file, located in `~/.docker/config.json`. Builds and containers use the configuration specified in this file.

> Proxy settings may contain sensitive information. For example, some proxy servers require authentication information to be included in their URL, or their address may expose IP-addresses or hostnames of your company's environment.
> 
> Environment variables are stored as plain text in the container's configuration, and as such can be inspected through the remote API or committed to an image when using `docker commit`.

The configuration becomes active after saving the file, you don't need to restart Docker. However, the configuration only applies to new containers and builds, and doesn't affect existing containers.

The following table describes the available configuration parameters.

PropertyDescription`httpProxy`Sets the `HTTP_PROXY` and `http_proxy` environment variables and build arguments.`httpsProxy`Sets the `HTTPS_PROXY` and `https_proxy` environment variables and build arguments.`ftpProxy`Sets the `FTP_PROXY` and `ftp_proxy` environment variables and build arguments.`noProxy`Sets the `NO_PROXY` and `no_proxy` environment variables and build arguments.`allProxy`Sets the `ALL_PROXY` and `all_proxy` environment variables and build arguments.

These settings are used to configure proxy environment variables for containers only, and not used as proxy settings for the Docker CLI or the Docker Engine itself. Refer to the [environment variables](https://docs.docker.com/reference/cli/docker/#environment-variables) and [configure the Docker daemon to use a proxy server](https://docs.docker.com/engine/daemon/proxy/) sections for configuring proxy settings for the CLI and daemon.

### [Run containers with a proxy configuration](#run-containers-with-a-proxy-configuration)

When you start a container, its proxy-related environment variables are set to reflect your proxy configuration in `~/.docker/config.json`.

For example, assuming a proxy configuration like the example shown in the [earlier section](#configure-the-docker-client), environment variables for containers that you run are set as follows:

### [Build with a proxy configuration](#build-with-a-proxy-configuration)

When you invoke a build, proxy-related build arguments are pre-populated automatically, based on the proxy settings in your Docker client configuration file.

Assuming a proxy configuration like the example shown in the [earlier section](#configure-the-docker-client), environment are set as follows during builds:

### [Configure proxy settings per daemon](#configure-proxy-settings-per-daemon)

The `default` key under `proxies` in `~/.docker/config.json` configures the proxy settings for all daemons that the client connects to. To configure the proxies for individual daemons, use the address of the daemon instead of the `default` key.

The following example configures both a default proxy config, and a no-proxy override for the Docker daemon on address `tcp://docker-daemon1.example.com`:

Instead of [configuring the Docker client](#configure-the-docker-client), you can specify proxy configurations on the command-line when you invoke the `docker build` and `docker run` commands.

Proxy configuration on the command-line uses the `--build-arg` flag for builds, and the `--env` flag for when you want to run containers with a proxy.

For a list of all the proxy-related build arguments that you can use with the `docker build` command, see [Predefined ARGs](https://docs.docker.com/reference/dockerfile/#predefined-args). These proxy values are only available in the build container. They're not included in the build output.

Don't use the `ENV` Dockerfile instruction to specify proxy settings for builds. Use build arguments instead.

Using environment variables for proxies embeds the configuration into the image. If the proxy is an internal proxy, it might not be accessible for containers created from that image.

Embedding proxy settings in images also poses a security risk, as the values may include sensitive information.