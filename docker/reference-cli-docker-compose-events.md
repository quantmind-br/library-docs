---
title: docker compose events
url: https://docs.docker.com/reference/cli/docker/compose/events/
source: llms
fetched_at: 2026-01-24T14:34:06.753094015-03:00
rendered_js: false
word_count: 65
summary: This document describes the usage and options for the docker compose events command, which allows users to stream real-time events from containers in a project.
tags:
    - docker-compose
    - container-events
    - real-time-monitoring
    - cli-command
    - json-output
category: reference
---

DescriptionReceive real time events from containersUsage`docker compose events [OPTIONS] [SERVICE...]`

## [Description](#description)

Stream container events for every container in the project.

With the `--json` flag, a json object is printed one per line with the format:

```
{
    "time": "2015-11-20T18:01:03.615550",
    "type": "container",
    "action": "create",
    "id": "213cf7...5fc39a",
    "service": "web",
    "attributes": {
      "name": "application_web_1",
      "image": "alpine:edge"
    }
}
```

The events that can be received using this can be seen [here](https://docs.docker.com/reference/cli/docker/system/events/#object-types).

## [Options](#options)

OptionDefaultDescription`--json`Output events as a stream of json objects`--since`Show all events created since timestamp`--until`Stream events until this timestamp