---
title: Specify a project name
url: https://docs.docker.com/compose/how-tos/project-name/
source: llms
fetched_at: 2026-01-24T14:18:00.594906588-03:00
rendered_js: false
word_count: 321
summary: This document explains how to define and customize project names in Docker Compose to isolate environments, covering use cases and the order of precedence for configuration methods.
tags:
    - docker-compose
    - project-management
    - environment-isolation
    - configuration-precedence
    - cli-options
    - environment-variables
category: guide
---

By default, Compose assigns the project name based on the name of the directory that contains the Compose file. You can override this with several methods.

This page offers examples of scenarios where custom project names can be helpful, outlines the various methods to set a project name, and provides the order of precedence for each approach.

> Note
> 
> The default project directory is the base directory of the Compose file. A custom value can also be set for it using the [`--project-directory` command line option](https://docs.docker.com/reference/cli/docker/compose/#options).

## [Example use cases](#example-use-cases)

Compose uses a project name to isolate environments from each other. There are multiple contexts where a project name is useful:

- On a development host: Create multiple copies of a single environment, useful for running stable copies for each feature branch of a project.
- On a CI server: Prevent interference between builds by setting the project name to a unique build number.
- On a shared or development host: Avoid interference between different projects that might share the same service names.

## [Set a project name](#set-a-project-name)

Project names must contain only lowercase letters, decimal digits, dashes, and underscores, and must begin with a lowercase letter or decimal digit. If the base name of the project directory or current directory violates this constraint, alternative mechanisms are available.

The precedence order for each method, from highest to lowest, is as follows:

1. The `-p` command line flag.
2. The [COMPOSE\_PROJECT\_NAME environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/).
3. The [top-level `name:` attribute](https://docs.docker.com/reference/compose-file/version-and-name/) in your Compose file. Or the last `name:` if you [specify multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) in the command line with the `-f` flag.
4. The base name of the project directory containing your Compose file. Or the base name of the first Compose file if you [specify multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) in the command line with the `-f` flag.
5. The base name of the current directory if no Compose file is specified.

## [What's next?](#whats-next)

- Read up on [working with multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/).
- Explore some [sample apps](https://github.com/docker/awesome-compose).