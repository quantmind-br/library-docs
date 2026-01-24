---
title: docker buildx history logs
url: https://docs.docker.com/reference/cli/docker/buildx/history/logs/
source: llms
fetched_at: 2026-01-24T14:33:11.510589929-03:00
rendered_js: false
word_count: 137
summary: This document explains how to use the docker buildx history logs command to retrieve and view logs from previous build records using IDs or relative offsets.
tags:
    - docker
    - buildx
    - logging
    - cli-reference
    - build-history
category: reference
---

DescriptionPrint the logs of a build recordUsage`docker buildx history logs [OPTIONS] [REF]`

## [Description](#description)

Print the logs for a completed build. The output appears in the same format as `--progress=plain`, showing the full logs for each step.

By default, this shows logs for the most recent build on the current builder.

You can also specify an earlier build using an offset. For example:

- `^1` shows logs for the build before the most recent
- `^2` shows logs for the build two steps back

## [Options](#options)

OptionDefaultDescription[`--progress`](#progress)`plain`Set type of progress output (plain, rawjson, tty)

## [Examples](#examples)

### [Print logs for the most recent build](#print-logs-for-the-most-recent-build)

```
$ docker buildx history logs
#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 31B done
#1 DONE 0.0s
#2 [internal] load .dockerignore
#2 transferring context: 2B done
#2 DONE 0.0s
...
```

By default, this shows logs for the most recent build on the current builder.

### [Print logs for a specific build](#print-logs-for-a-specific-build)

To print logs for a specific build, use a build ID or offset:

```
# Using a build ID
docker buildx history logs qu2gsuo8ejqrwdfii23xkkckt
# Or using a relative offset
docker buildx history logs ^1
```

### [Set type of progress output (--progress)](#progress)

```
$ docker buildx history logs ^1 --progress rawjson
{"id":"buildx_step_1","status":"START","timestamp":"2024-05-01T12:34:56.789Z","detail":"[internal] load build definition from Dockerfile"}
{"id":"buildx_step_1","status":"COMPLETE","timestamp":"2024-05-01T12:34:57.001Z","duration":212000000}
...
```