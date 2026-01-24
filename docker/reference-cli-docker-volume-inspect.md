---
title: docker volume inspect
url: https://docs.docker.com/reference/cli/docker/volume/inspect/
source: llms
fetched_at: 2026-01-24T14:41:50.664016428-03:00
rendered_js: false
word_count: 131
summary: This document explains how to use the docker volume inspect command to retrieve and format detailed configuration information for one or more Docker volumes.
tags:
    - docker
    - docker-volume
    - cli-reference
    - volume-management
    - json-formatting
    - go-templates
category: reference
---

DescriptionDisplay detailed information on one or more volumesUsage`docker volume inspect [OPTIONS] VOLUME [VOLUME...]`

## [Description](#description)

Returns information about a volume. By default, this command renders all results in a JSON array. You can specify an alternate format to execute a given template for each result. Go's [text/template](https://pkg.go.dev/text/template) package describes all the details of the format.

## [Options](#options)

OptionDefaultDescription[`-f, --format`](#format)Format output using a custom template:  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates

## [Examples](#examples)

```
$ docker volume create myvolume
myvolume
```

Use the `docker volume inspect` comment to inspect the configuration of the volume:

```
$ docker volume inspect myvolume
```

The output is in JSON format, for example:

```
[
  {
    "CreatedAt": "2020-04-19T11:00:21Z",
    "Driver": "local",
    "Labels": {},
    "Mountpoint": "/var/lib/docker/volumes/8140a838303144125b4f54653b47ede0486282c623c3551fbc7f390cdc3e9cf5/_data",
    "Name": "myvolume",
    "Options": {},
    "Scope": "local"
  }
]
```

### [Format the output (--format)](#format)

Use the `--format` flag to format the output using a Go template, for example, to print the `Mountpoint` property:

```
$ docker volume inspect --format '{{ .Mountpoint }}' myvolume
/var/lib/docker/volumes/myvolume/_data
```