---
title: docker stack config
url: https://docs.docker.com/reference/cli/docker/stack/config/
source: llms
fetched_at: 2026-01-24T14:41:05.049734571-03:00
rendered_js: false
word_count: 202
summary: This document explains the usage and options for the docker stack config command, which generates a merged and interpolated Compose file for Docker Swarm deployments.
tags:
    - docker-swarm
    - stack-config
    - compose-file
    - cli-reference
    - orchestration
category: reference
---

DescriptionOutputs the final config file, after doing merges and interpolationsUsage`docker stack config [OPTIONS]`

Swarm This command works with the Swarm orchestrator.

## [Description](#description)

Outputs the final Compose file, after doing the merges and interpolations of the input Compose files.

## [Options](#options)

OptionDefaultDescription`-c, --compose-file`Path to a Compose file, or `-` to read from stdin`--skip-interpolation`Skip interpolation and output only merged config

## [Examples](#examples)

The following command outputs the result of the merge and interpolation of two Compose files.

```
$ docker stack config --compose-file docker-compose.yml --compose-file docker-compose.prod.yml
```

The Compose file can also be provided as standard input with `--compose-file -`:

```
$ cat docker-compose.yml | docker stack config --compose-file -
```

### [Skipping interpolation](#skipping-interpolation)

In some cases, it might be useful to skip interpolation of environment variables. For example, when you want to pipe the output of this command back to `stack deploy`.

If you have a regex for a redirect route in an environment variable for your webserver you would use two `$` signs to prevent `stack deploy` from interpolating `${1}`.

```
service:webserverenvironment:REDIRECT_REGEX=http://host/redirect/$${1}
```

With interpolation, the `stack config` command will replace the environment variable in the Compose file with `REDIRECT_REGEX=http://host/redirect/${1}`, but then when piping it back to the `stack deploy` command it will be interpolated again and result in undefined behavior. That is why, when piping the output back to `stack deploy` one should always prefer the `--skip-interpolation` option.

```
$ docker stack config --compose-file web.yml --compose-file web.prod.yml --skip-interpolation | docker stack deploy --compose-file -
```