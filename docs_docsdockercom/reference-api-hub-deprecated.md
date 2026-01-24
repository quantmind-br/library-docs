---
title: Deprecated
url: https://docs.docker.com/reference/api/hub/deprecated/
source: llms
fetched_at: 2026-01-24T14:31:43.251880338-03:00
rendered_js: false
word_count: 241
summary: This document lists deprecated and removed Docker Hub API endpoints, explaining the deprecation policy and providing modern alternatives for legacy routes.
tags:
    - docker-hub
    - api-deprecation
    - api-migration
    - endpoint-reference
    - breaking-changes
category: reference
---

## Deprecated Docker Hub API endpoints

Table of contents

* * *

This page provides an overview of endpoints that are deprecated in Docker Hub API.

## [Endpoint deprecation policy](#endpoint-deprecation-policy)

As changes are made to Docker there may be times when existing endpoints need to be removed or replaced with newer endpoints. Before an existing endpoint is removed it is labeled as "deprecated" within the documentation. After some time it may be removed.

## [Deprecated endpoints](#deprecated-endpoints)

The following table provides an overview of the current status of deprecated endpoints:

**Deprecated**: the endpoint is marked "deprecated" and should no longer be used.

The endpoint may be removed, disabled, or change behavior in a future release.

**Removed**: the endpoint was removed, disabled, or hidden.

* * *

StatusFeatureDateDeprecated[Deprecate undocumented create/get repository](#deprecate-legacy-createrepository-and-getrepository)2025-09-19Deprecated[Deprecate /v2/repositories/{namespace}](#deprecate-legacy-listnamespacerepositories)2025-06-27[Create deprecation log table](#create-deprecation-log-table)2025-06-27Removed[Docker Hub API v1 deprecation](#docker-hub-api-v1-deprecation)2022-08-23

* * *

### [Deprecate legacy CreateRepository and GetRepository](#deprecate-legacy-createrepository-and-getrepository)

Deprecate undocumented endpoints :

- `POST /v2/repositories` and `POST /v2/repositories/{namespace}` replaced by [Create repository](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/CreateRepository).
- `GET /v2/repositories/{namespace}/{repository}` replaced by [Get repository](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/GetRepository).
- `HEAD /v2/repositories/{namespace}/{repository}` replaced by [Check repository](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/CheckRepository).

* * *

### [Deprecate legacy ListNamespaceRepositories](#deprecate-legacy-listnamespacerepositories)

Deprecate undocumented endpoint `GET /v2/repositories/{namespace}` replaced by [List repositories](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/listNamespaceRepositories).

* * *

### [Create deprecation log table](#create-deprecation-log-table)

Reformat page

* * *

### [Docker Hub API v1 deprecation](#docker-hub-api-v1-deprecation)

Docker Hub API v1 has been deprecated. Use Docker Hub API v2 instead.

The following API routes within the v1 path will no longer work and will return a 410 status code:

- `/v1/repositories/{name}/images`
- `/v1/repositories/{name}/tags`
- `/v1/repositories/{name}/tags/{tag_name}`
- `/v1/repositories/{namespace}/{name}/images`
- `/v1/repositories/{namespace}/{name}/tags`
- `/v1/repositories/{namespace}/{name}/tags/{tag_name}`

If you want to continue using the Docker Hub API in your current applications, update your clients to use v2 endpoints.

* * *