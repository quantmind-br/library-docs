---
title: docker compose config
url: https://docs.docker.com/reference/cli/docker/compose/config/
source: llms
fetched_at: 2026-01-24T14:33:54.931763919-03:00
rendered_js: false
word_count: 143
summary: This document provides a technical reference for the docker compose config command, detailing how it parses, merges, and validates Compose files and their associated options.
tags:
    - docker-compose
    - cli-reference
    - configuration-validation
    - yaml-processing
    - environment-interpolation
category: reference
---

`docker compose config` renders the actual data model to be applied on the Docker Engine. It merges the Compose files set by `-f` flags, resolves variables in the Compose file, and expands short-notation into the canonical format.

OptionDefaultDescription`--environment`Print environment used for interpolation.`--format`Format the output. Values: \[yaml | json]`--hash`Print the service config hash, one per line.`--images`Print the image names, one per line.`--lock-image-digests`Produces an override file with image digests`--models`Print the model names, one per line.`--networks`Print the network names, one per line.`--no-consistency`Don't check model consistency - warning: may produce invalid Compose output  
`--no-env-resolution`Don't resolve service env files`--no-interpolate`Don't interpolate environment variables`--no-normalize`Don't normalize compose model`--no-path-resolution`Don't resolve file paths`-o, --output`Save to file (default to stdout)`--profiles`Print the profile names, one per line.`-q, --quiet`Only validate the configuration, don't print anything`--resolve-image-digests`Pin image tags to digests`--services`Print the service names, one per line.`--variables`Print model variables and default values.`--volumes`Print the volume names, one per line.