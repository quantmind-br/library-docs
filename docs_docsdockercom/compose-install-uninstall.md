---
title: Uninstall
url: https://docs.docker.com/compose/install/uninstall/
source: llms
fetched_at: 2026-01-24T14:18:16.858384028-03:00
rendered_js: false
word_count: 196
summary: This document provides step-by-step instructions for uninstalling Docker Compose based on its installation method, including Docker Desktop, package managers, and manual binary removal.
tags:
    - docker-compose
    - uninstallation
    - docker-desktop
    - cli-plugin
    - linux
    - package-manager
category: guide
---

## Uninstall Docker Compose

Table of contents

* * *

How you uninstall Docker Compose depends on how it was installed. This guide covers uninstallation instructions for:

- Docker Compose installed via Docker Desktop
- Docker Compose installed as a CLI plugin

## [Uninstalling Docker Compose with Docker Desktop](#uninstalling-docker-compose-with-docker-desktop)

If you want to uninstall Docker Compose and you have installed Docker Desktop, see [Uninstall Docker Desktop](https://docs.docker.com/desktop/uninstall/).

> Warning
> 
> Unless you have other Docker instances installed on that specific environment, uninstalling Docker Desktop removes all Docker components, including Docker Engine, Docker CLI, and Docker Compose.

## [Uninstalling the Docker Compose CLI plugin](#uninstalling-the-docker-compose-cli-plugin)

If you installed Docker Compose via a package manager, run:

On Ubuntu or Debian:

```
$ sudo apt-get remove docker-compose-plugin
```

On RPM-based distributions:

```
$ sudo yum remove docker-compose-plugin
```

### [Manually installed](#manually-installed)

If you installed Docker Compose manually (using curl), remove it by deleting the binary:

```
$ rm $DOCKER_CONFIG/cli-plugins/docker-compose
```

### [Remove for all users](#remove-for-all-users)

If installed for all users, remove it from the system directory:

```
$ rm /usr/local/lib/docker/cli-plugins/docker-compose
```

> Note
> 
> If you get a **Permission denied** error using either of the previous methods, you do not have the permissions needed to remove Docker Compose. To force the removal, prepend `sudo` to either of the previous instructions and run it again.

### [Inspect the location of the Compose CLI plugin](#inspect-the-location-of-the-compose-cli-plugin)

To check where Compose is installed, use:

```
$ docker info --format '{{range .ClientInfo.Plugins}}{{if eq .Name "compose"}}{{.Path}}{{end}}{{end}}'
```