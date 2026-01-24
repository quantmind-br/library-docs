---
title: docker system prune
url: https://docs.docker.com/reference/cli/docker/system/prune/
source: llms
fetched_at: 2026-01-24T14:41:36.089122581-03:00
rendered_js: false
word_count: 308
summary: This document provides instructions and parameter details for the 'docker system prune' command, which is used to remove unused containers, networks, images, and volumes.
tags:
    - docker
    - docker-cli
    - resource-management
    - system-maintenance
    - filtering
category: reference
---

DescriptionRemove unused dataUsage`docker system prune [OPTIONS]`

Remove all unused containers, networks, images (both dangling and unused), and optionally, volumes.

OptionDefaultDescription`-a, --all`Remove all unused images not just dangling ones[`--filter`](#filter)API 1.28+ Provide filter values (e.g. `label=<key>=<value>`)`-f, --force`Do not prompt for confirmation`--volumes`Prune anonymous volumes

By default, volumes aren't removed to prevent important data from being deleted if there is currently no container using the volume. Use the `--volumes` flag when running the command to prune anonymous volumes as well:

### [Filtering (--filter)](#filter)

The filtering flag (`--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`)

The currently supported filters are:

- until (`<timestamp>`) - only remove containers, images, and networks created before given timestamp
- label (`label=<key>`, `label=<key>=<value>`, `label!=<key>`, or `label!=<key>=<value>`) - only remove containers, images, networks, and volumes with (or without, in case `label!=...` is used) the specified labels.

The `until` filter can be Unix timestamps, date formatted timestamps, or Go duration strings supported by [ParseDuration](https://pkg.go.dev/time#ParseDuration) (e.g. `10m`, `1h30m`) computed relative to the daemon machine’s time. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, `2006-01-02T15:04:05`, `2006-01-02T15:04:05.999999999`, `2006-01-02T07:00`, and `2006-01-02`. The local timezone on the daemon will be used if you do not provide either a `Z` or a `+-00:00` timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds\[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long.

The `label` filter accepts two formats. One is the `label=...` (`label=<key>` or `label=<key>=<value>`), which removes containers, images, networks, and volumes with the specified labels. The other format is the `label!=...` (`label!=<key>` or `label!=<key>=<value>`), which removes containers, images, networks, and volumes without the specified labels.