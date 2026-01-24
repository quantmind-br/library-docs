---
title: Secrets
url: https://docs.docker.com/reference/compose-file/secrets/
source: llms
fetched_at: 2026-01-24T14:42:26.37811338-03:00
rendered_js: false
word_count: 153
summary: This document explains how to define and manage sensitive data in Docker Compose using the top-level secrets attribute with file or environment sources.
tags:
    - docker-compose
    - secrets-management
    - container-security
    - configuration
    - deployment
category: reference
---

Secrets are a flavor of [Configs](https://docs.docker.com/reference/compose-file/configs/) focusing on sensitive data, with specific constraint for this usage.

Services can only access secrets when explicitly granted by a [`secrets` attribute](https://docs.docker.com/reference/compose-file/services/#secrets) within the `services` top-level element.

The top-level `secrets` declaration defines or references sensitive data that is granted to the services in your Compose application. The source of the secret is either `file` or `environment`.

- `file`: The secret is created with the contents of the file at the specified path.
- `environment`: The secret is created with the value of an environment variable on the host.

## [Example 1](#example-1)

`server-certificate` secret is created as `<project_name>_server-certificate` when the application is deployed, by registering content of the `server.cert` as a platform secret.

```
secrets:server-certificate:file:./server.cert
```

## [Example 2](#example-2)

`token` secret is created as `<project_name>_token` when the application is deployed, by registering the content of the `OAUTH_TOKEN` environment variable as a platform secret.

```
secrets:token:environment:"OAUTH_TOKEN"
```

## [Additional resources](#additional-resources)

For more information, see [How to use secrets in Compose](https://docs.docker.com/compose/how-tos/use-secrets/).