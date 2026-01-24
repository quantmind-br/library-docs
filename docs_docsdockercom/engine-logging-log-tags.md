---
title: Customize log driver output
url: https://docs.docker.com/engine/logging/log_tags/
source: llms
fetched_at: 2026-01-24T14:24:09.862273366-03:00
rendered_js: false
word_count: 144
summary: This document explains how to use and customize the tag log option in Docker to identify container log messages using various template markup variables.
tags:
    - docker
    - logging
    - log-driver
    - container-configuration
    - template-markup
category: configuration
---

The `tag` log option specifies how to format a tag that identifies the container's log messages. By default, the system uses the first 12 characters of the container ID. To override this behavior, specify a `tag` option:

```
$ docker run --log-driver=fluentd --log-opt fluentd-address=myhost.local:24224 --log-opt tag="mailer"
```

Docker supports some special template markup you can use when specifying a tag's value:

MarkupDescription`{{.ID}}`The first 12 characters of the container ID.`{{.FullID}}`The full container ID.`{{.Name}}`The container name.`{{.ImageID}}`The first 12 characters of the container's image ID.`{{.ImageFullID}}`The container's full image ID.`{{.ImageName}}`The name of the image used by the container.`{{.DaemonName}}`The name of the Docker program (`docker`).

For example, specifying a `--log-opt tag="{{.ImageName}}/{{.Name}}/{{.ID}}"` value yields `syslog` log lines like:

```
Aug  7 18:33:19 HOSTNAME hello-world/foobar/5790672ab6a0[9103]: Hello from Docker.
```

At startup time, the system sets the `container_name` field and `{{.Name}}` in the tags. If you use `docker rename` to rename a container, the new name isn't reflected in the log messages. Instead, these messages continue to use the original container name.