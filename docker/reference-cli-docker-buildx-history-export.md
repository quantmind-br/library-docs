---
title: docker buildx history export
url: https://docs.docker.com/reference/cli/docker/buildx/history/export/
source: llms
fetched_at: 2026-01-24T14:33:06.928807926-03:00
rendered_js: false
word_count: 159
summary: This document explains how to use the docker buildx history export command to save build records, including metadata and logs, into .dockerbuild archive files.
tags:
    - docker-buildx
    - history-export
    - build-records
    - cli-reference
    - docker-desktop
    - metadata-export
category: reference
---

DescriptionExport build records into Docker Desktop bundleUsage`docker buildx history export [OPTIONS] [REF...]`

## [Description](#description)

Export one or more build records to `.dockerbuild` archive files. These archives contain metadata, logs, and build outputs, and can be imported into Docker Desktop or shared across environments.

## [Options](#options)

OptionDefaultDescription[`--all`](#all)Export all build records for the builder[`--finalize`](#finalize)Ensure build records are finalized before exporting[`-o, --output`](#output)Output file path

## [Examples](#examples)

### [Export all build records to a file (--all)](#all)

Use the `--all` flag and redirect the output:

```
docker buildx history export --all > all-builds.dockerbuild
```

Or use the `--output` flag:

```
docker buildx history export --all -o all-builds.dockerbuild
```

### [Use a specific builder instance (--builder)](#builder)

```
docker buildx history export --builder builder0 ^1 -o builder0-build.dockerbuild
```

### [Enable debug logging (--debug)](#debug)

```
docker buildx history export --debug qu2gsuo8ejqrwdfii23xkkckt -o debug-build.dockerbuild
```

### [Ensure build records are finalized before exporting (--finalize)](#finalize)

Clients can report their own traces concurrently, and not all traces may be saved yet by the time of the export. Use the `--finalize` flag to ensure all traces are finalized before exporting.

```
docker buildx history export --finalize qu2gsuo8ejqrwdfii23xkkckt -o finalized-build.dockerbuild
```

### [Export a single build to a custom file (--output)](#output)

```
docker buildx history export qu2gsuo8ejqrwdfii23xkkckt --output mybuild.dockerbuild
```

You can find build IDs by running:

To export two builds to separate files:

```
# Using build IDs
docker buildx history export qu2gsuo8ejqrwdfii23xkkckt qsiifiuf1ad9pa9qvppc0z1l3 -o multi.dockerbuild
# Or using relative offsets
docker buildx history export ^1 ^2 -o multi.dockerbuild
```

Or use shell redirection:

```
docker buildx history export ^1 > mybuild.dockerbuild
docker buildx history export ^2 > backend-build.dockerbuild
```