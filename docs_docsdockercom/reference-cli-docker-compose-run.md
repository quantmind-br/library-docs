---
title: docker compose run
url: https://docs.docker.com/reference/cli/docker/compose/run/
source: llms
fetched_at: 2026-01-24T14:34:26.411507954-03:00
rendered_js: false
word_count: 419
summary: This document explains the usage and options of the docker compose run command for executing one-off tasks within a service's environment. It details how the command interacts with service configurations, overrides, and dependencies.
tags:
    - docker-compose
    - cli-reference
    - container-management
    - one-off-commands
    - devops
category: reference
---

DescriptionRun a one-off command on a serviceUsage`docker compose run [OPTIONS] SERVICE [COMMAND] [ARGS...]`

Runs a one-time command against a service.

The following command starts the `web` service and runs `bash` as its command:

Commands you use with run start in new containers with configuration defined by that of the service, including volumes, links, and other details. However, there are two important differences:

First, the command passed by `run` overrides the command defined in the service configuration. For example, if the `web` service configuration is started with `bash`, then `docker compose run web python app.py` overrides it with `python app.py`.

The second difference is that the `docker compose run` command does not create any of the ports specified in the service configuration. This prevents port collisions with already-open ports. If you do want the service’s ports to be created and mapped to the host, specify the `--service-ports`

Alternatively, manual port mapping can be specified with the `--publish` or `-p` options, just as when using docker run:

If you start a service configured with links, the run command first checks to see if the linked service is running and starts the service if it is stopped. Once all the linked services are running, the run executes the command you passed it. For example, you could run:

This opens an interactive PostgreSQL shell for the linked `db` container.

If you do not want the run command to start linked containers, use the `--no-deps` flag:

If you want to remove the container after running while overriding the container’s restart policy, use the `--rm` flag:

This runs a database upgrade script, and removes the container when finished running, even if a restart policy is specified in the service configuration.

OptionDefaultDescription`--build`Build image before starting container`--cap-add`Add Linux capabilities`--cap-drop`Drop Linux capabilities`-d, --detach`Run container in background and print container ID`--entrypoint`Override the entrypoint of the image`-e, --env`Set environment variables`--env-from-file`Set environment variables from file`-i, --interactive``true`Keep STDIN open even if not attached`-l, --label`Add or override a label`--name`Assign a name to the container`-T, --no-TTY``true`Disable pseudo-TTY allocation (default: auto-detected)`--no-deps`Don't start linked services`-p, --publish`Publish a container's port(s) to the host`--pull``policy`Pull image before running ("always"|"missing"|"never")`-q, --quiet`Don't print anything to STDOUT`--quiet-build`Suppress progress output from the build process`--quiet-pull`Pull without printing progress information`--remove-orphans`Remove containers for services not defined in the Compose file`--rm`Automatically remove the container when it exits`-P, --service-ports`Run command with all service's ports enabled and mapped to the host  
`--use-aliases`Use the service's network useAliases in the network(s) the container connects to  
`-u, --user`Run as specified username or uid`-v, --volume`Bind mount a volume`-w, --workdir`Working directory inside the container