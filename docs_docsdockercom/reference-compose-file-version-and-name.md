---
title: Version and name top-level elements
url: https://docs.docker.com/reference/compose-file/version-and-name/
source: llms
fetched_at: 2026-01-24T14:42:33.942393902-03:00
rendered_js: false
word_count: 181
summary: This document explains the role of the top-level version and name elements in a Compose file, including their validation behavior and project naming impact.
tags:
    - docker-compose
    - compose-file
    - project-name
    - schema-validation
    - backward-compatibility
category: reference
---

## [Version top-level element (obsolete)](#version-top-level-element-obsolete)

> Important
> 
> The top-level `version` property is defined by the Compose Specification for backward compatibility. It is only informative and you'll receive a warning message that it is obsolete if used.

Compose always uses the most recent schema to validate the Compose file, regardless of the `version` field.

Compose validates whether it can fully parse the Compose file. If some fields are unknown, typically because the Compose file was written with fields defined by a newer version of the Specification, you'll receive a warning message.

## [Name top-level element](#name-top-level-element)

The top-level `name` property is defined by the Compose Specification as the project name to be used if you don't set one explicitly.

Compose offers a way for you to override this name, and sets a default project name to be used if the top-level `name` element is not set.

Whenever a project name is defined by top-level `name` or by some custom mechanism, it is exposed for [interpolation](https://docs.docker.com/reference/compose-file/interpolation/) and environment variable resolution as `COMPOSE_PROJECT_NAME`

```
name:myappservices:foo:image:busyboxcommand:echo "I'm running ${COMPOSE_PROJECT_NAME}"
```

For more information on other ways to name Compose projects, see [Specify a project name](https://docs.docker.com/compose/how-tos/project-name/).