---
title: docker compose exec
url: https://docs.docker.com/reference/cli/docker/compose/exec/
source: llms
fetched_at: 2026-01-24T14:34:06.835994903-03:00
rendered_js: false
word_count: 180
summary: This document describes the docker compose exec command, which allows users to run arbitrary commands within running service containers with support for interactive modes and TTY allocation.
tags:
    - docker-compose
    - container-management
    - cli-reference
    - command-execution
    - interactive-mode
category: reference
---

DescriptionExecute a command in a running containerUsage`docker compose exec [OPTIONS] SERVICE COMMAND [ARGS...]`

## [Description](#description)

This is the equivalent of `docker exec` targeting a Compose service.

With this subcommand, you can run arbitrary commands in your services. Commands allocate a TTY by default, so you can use a command such as `docker compose exec web sh` to get an interactive prompt.

By default, Compose will enter container in interactive mode and allocate a TTY, while the equivalent `docker exec` command requires passing `--interactive --tty` flags to get the same behavior. Compose also support those two flags to offer a smooth migration between commands, whenever they are no-op by default. Still, `interactive` can be used to force disabling interactive mode (`--interactive=false`), typically when `docker compose exec` command is used inside a script.

## [Options](#options)

OptionDefaultDescription`-d, --detach`Detached mode: Run command in the background`-e, --env`Set environment variables`--index`Index of the container if service has multiple replicas`-T, --no-tty``true`Disable pseudo-TTY allocation. By default 'docker compose exec' allocates a TTY.  
`--privileged`Give extended privileges to the process`-u, --user`Run the command as this user`-w, --workdir`Path to workdir directory for this command