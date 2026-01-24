---
title: docker compose down
url: https://docs.docker.com/reference/cli/docker/compose/down/
source: llms
fetched_at: 2026-01-24T14:34:03.746184303-03:00
rendered_js: false
word_count: 155
summary: This document provides a technical reference for the docker compose down command, detailing how to stop and remove resources like containers, networks, and volumes.
tags:
    - docker-compose
    - container-management
    - docker-cli
    - resource-cleanup
    - command-reference
category: reference
---

DescriptionStop and remove containers, networksUsage`docker compose down [OPTIONS] [SERVICES]`

## [Description](#description)

Stops containers and removes containers, networks, volumes, and images created by `up`.

By default, the only things removed are:

- Containers for services defined in the Compose file.
- Networks defined in the networks section of the Compose file.
- The default network, if one is used.

Networks and volumes defined as external are never removed.

Anonymous volumes are not removed by default. However, as they don’t have a stable name, they are not automatically mounted by a subsequent `up`. For data that needs to persist between updates, use explicit paths as bind mounts or named volumes.

## [Options](#options)

OptionDefaultDescription`--remove-orphans`Remove containers for services not defined in the Compose file`--rmi`Remove images used by services. "local" remove only images that don't have a custom tag ("local"|"all")  
`-t, --timeout`Specify a shutdown timeout in seconds`-v, --volumes`Remove named volumes declared in the "volumes" section of the Compose file and anonymous volumes attached to containers