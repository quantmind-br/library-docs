---
title: docker init
url: https://docs.docker.com/reference/cli/docker/init/
source: llms
fetched_at: 2026-01-24T14:36:36.049414652-03:00
rendered_js: false
word_count: 469
summary: This document explains the purpose and usage of the docker init CLI command, which automates the creation of essential Docker configuration files for various project types.
tags:
    - docker-init
    - containerization
    - scaffolding
    - docker-desktop
    - cli-reference
    - project-initialization
category: reference
---

DescriptionCreates Docker-related starter files for your projectUsage`docker init [OPTIONS]`

Requires: Docker Desktop [4.27](https://docs.docker.com/desktop/release-notes/#4270) and later

Initialize a project with the files necessary to run the project in a container.

Docker Desktop provides the `docker init` CLI command. Run `docker init` in your project directory to be walked through the creation of the following files with sensible defaults for your project:

- .dockerignore
- Dockerfile
- compose.yaml
- README.Docker.md

If any of the files already exist, a prompt appears and provides a warning as well as giving you the option to overwrite all the files. If `docker-compose.yaml` already exists instead of `compose.yaml`, `docker init` can overwrite it, using `docker-compose.yaml` as the name for the Compose file.

> You can't recover overwritten files. To back up an existing file before selecting to overwrite it, rename the file or copy it to another directory.

After running `docker init`, you can choose one of the following templates:

- ASP.NET Core: Suitable for an ASP.NET Core application.
- Go: Suitable for a Go server application.
- Java: suitable for a Java application that uses Maven and packages as an uber jar.
- Node: Suitable for a Node server application.
- PHP with Apache: Suitable for a PHP web application.
- Python: Suitable for a Python server application.
- Rust: Suitable for a Rust server application.
- Other: General purpose starting point for containerizing your application.

After `docker init` has completed, you may need to modify the created files and tailor them to your project. Visit the following topics to learn more about the files:

- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [compose.yaml](https://docs.docker.com/compose/intro/compose-application-model/)

OptionDefaultDescription`--version`Display version of the init plugin

### [Example of running `docker init`](#example-of-running-docker-init)

The following example shows the initial menu after running `docker init`. See the additional examples to view the options for each language or framework.

### [Example of selecting Go](#example-of-selecting-go)

The following example shows the prompts that appear after selecting `Go` and example input.

### [Example of selecting Node](#example-of-selecting-node)

The following example shows the prompts that appear after selecting `Node` and example input.

### [Example of selecting Python](#example-of-selecting-python)

The following example shows the prompts that appear after selecting `Python` and example input.

### [Example of selecting Rust](#example-of-selecting-rust)

The following example shows the prompts that appear after selecting `Rust` and example input.

### [Example of selecting ASP.NET Core](#example-of-selecting-aspnet-core)

The following example shows the prompts that appear after selecting `ASP.NET Core` and example input.

### [Example of selecting PHP with Apache](#example-of-selecting-php-with-apache)

The following example shows the prompts that appear after selecting `PHP with Apache` and example input. The PHP with Apache template is suitable for both pure PHP applications and applications using Composer as a dependency manager. After running `docker init`, you must manually add any PHP extensions that are required by your application to the Dockerfile.

### [Example of selecting Java](#example-of-selecting-java)

The following example shows the prompts that appear after selecting `Java` and example input.

### [Example of selecting Other](#example-of-selecting-other)

The following example shows the output after selecting `Other`.