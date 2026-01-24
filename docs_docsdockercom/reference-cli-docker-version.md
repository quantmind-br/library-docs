---
title: docker version
url: https://docs.docker.com/reference/cli/docker/version/
source: llms
fetched_at: 2026-01-24T14:41:49.164876121-03:00
rendered_js: false
word_count: 484
summary: This document provides a detailed reference for the docker version command, explaining how to retrieve and format version information for Docker client and server components.
tags:
    - docker-cli
    - command-reference
    - version-management
    - api-negotiation
    - go-templates
    - docker-engine
category: reference
---

DescriptionShow the Docker version informationUsage`docker version [OPTIONS]`

The version command prints the current version number for all independently versioned Docker components. Use the [`--format`](#format) option to customize the output.

The version command (`docker version`) outputs the version numbers of Docker components, while the `--version` flag (`docker --version`) outputs the version number of the Docker CLI you are using.

### [Default output](#default-output)

The default output renders all version information divided into two sections; the `Client` section contains information about the Docker CLI and client components, and the `Server` section contains information about the Docker Engine and components used by the Docker Engine, such as the containerd and runc OCI Runtimes.

The information shown may differ depending on how you installed Docker and what components are in use. The following example shows the output on a macOS machine running Docker Desktop:

### [Client and server versions](#client-and-server-versions)

Docker uses a client/server architecture, which allows you to use the Docker CLI on your local machine to control a Docker Engine running on a remote machine, which can be (for example) a machine running in the cloud or inside a virtual machine.

The following example switches the Docker CLI to use a [context](https://docs.docker.com/reference/cli/docker/context/) named `remote-test-server`, which runs an older version of the Docker Engine on a Linux server:

### [API version and version negotiation](#api-version-and-version-negotiation)

The API version used by the client depends on the Docker Engine that the Docker CLI is connecting with. When connecting with the Docker Engine, the Docker CLI and Docker Engine perform API version negotiation, and select the highest API version that is supported by both the Docker CLI and the Docker Engine.

For example, if the CLI is connecting with Docker Engine version 27.5, it downgrades to API version 1.47 (refer to the [API version matrix](https://docs.docker.com/reference/api/engine/#api-version-matrix) to learn about the supported API versions for Docker Engine):

Be aware that API version can also be overridden using the `DOCKER_API_VERSION` environment variable, which can be useful for debugging purposes, and disables API version negotiation. The following example illustrates an environment where the `DOCKER_API_VERSION` environment variable is set. Unsetting the environment variable removes the override, and re-enables API version negotiation:

OptionDefaultDescription[`-f, --format`](#format)Format output using a custom template:  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates

### [Format the output (--format)](#format)

The formatting option (`--format`) pretty-prints the output using a Go template, which allows you to customize the output format, or to obtain specific information from the output. Refer to the [format command and log output](https://docs.docker.com/config/formatting/) page for details of the format.

### [Get the server version](#get-the-server-version)

### [Get the client API version](#get-the-client-api-version)

The following example prints the API version that is used by the client:

The version shown is the API version that is negotiated between the client and the Docker Engine. Refer to [API version and version negotiation](#api-version-and-version-negotiation) above for more information.

### [Dump raw JSON data](#dump-raw-json-data)