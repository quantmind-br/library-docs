---
title: docker image prune
url: https://docs.docker.com/reference/cli/docker/image/prune/
source: llms
fetched_at: 2026-01-24T14:36:21.413831211-03:00
rendered_js: false
word_count: 350
summary: This document explains how to remove dangling or unreferenced images using filters like 'until' and 'label' while providing guidance on predicting which images will be deleted.
tags:
    - docker-prune
    - image-management
    - filtering-syntax
    - dangling-images
    - container-cleanup
category: reference
---

Remove all dangling images. If `-a` is specified, also remove all images not referenced by any container.

The filtering flag (`--filter`) format is of "key=value". If there is more than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`)

The `until` filter can be Unix timestamps, date formatted timestamps, or Go duration strings supported by [ParseDuration](https://pkg.go.dev/time#ParseDuration) (e.g. `10m`, `1h30m`) computed relative to the daemon machine’s time. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, `2006-01-02T15:04:05`, `2006-01-02T15:04:05.999999999`, `2006-01-02T07:00`, and `2006-01-02`. The local timezone on the daemon will be used if you do not provide either a `Z` or a `+-00:00` timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds\[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long.

The `label` filter accepts two formats. One is the `label=...` (`label=<key>` or `label=<key>=<value>`), which removes images with the specified labels. The other format is the `label!=...` (`label!=<key>` or `label!=<key>=<value>`), which removes images without the specified labels.

**Predicting what will be removed**

If you are using positive filtering (testing for the existence of a label or that a label has a specific value), you can use `docker image ls` with the same filtering syntax to see which images match your filter.

However, if you are using negative filtering (testing for the absence of a label or that a label doesn't have a specific value), this type of filter doesn't work with `docker image ls` so you cannot easily predict which images will be removed. In addition, the confirmation prompt for `docker image prune` always warns that all dangling images will be removed, even if you are using `--filter`.

You are prompted for confirmation before the `prune` removes anything, but you are not shown a list of what will potentially be removed. In addition, `docker image ls` doesn't support negative filtering, so it difficult to predict what images will actually be removed.