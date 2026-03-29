---
title: Docker driver
url: https://docs.docker.com/build/builders/drivers/docker/
source: llms
fetched_at: 2026-01-24T14:15:28.283431503-03:00
rendered_js: false
word_count: 127
summary: This document explains the features and limitations of the default Buildx Docker driver, which utilizes the BuildKit components integrated into the Docker Engine.
tags:
    - docker-buildx
    - buildkit
    - docker-driver
    - container-images
    - docker-engine
category: reference
---

Table of contents

* * *

The Buildx Docker driver is the default driver. It uses the BuildKit server components built directly into the Docker Engine. The Docker driver requires no configuration.

Unlike the other drivers, builders using the Docker driver can't be manually created. They're only created automatically from the Docker context.

Images built with the Docker driver are automatically loaded to the local image store.

## [Synopsis](#synopsis)

```
# The Docker driver is used by buildx by default
docker buildx build .
```

It's not possible to configure which BuildKit version to use, or to pass any additional BuildKit parameters to a builder using the Docker driver. The BuildKit version and parameters are preset by the Docker Engine internally.

If you need additional configuration and flexibility, consider using the [Docker container driver](https://docs.docker.com/build/builders/drivers/docker-container/).

## [Further reading](#further-reading)

For more information on the Docker driver, see the [buildx reference](https://docs.docker.com/reference/cli/docker/buildx/create/#driver).