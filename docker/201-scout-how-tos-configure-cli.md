---
title: Docker Scout environment variables
url: https://docs.docker.com/scout/how-tos/configure-cli/
source: llms
fetched_at: 2026-01-24T14:28:44.488918106-03:00
rendered_js: false
word_count: 187
summary: This document lists and explains the environment variables available for configuring the Docker Scout CLI and container image, including settings for caching, authentication, and offline mode.
tags:
    - docker-scout
    - environment-variables
    - configuration
    - offline-mode
    - authentication
    - cli-tools
category: configuration
---

## Configure Docker Scout with environment variables

Table of contents

* * *

The following environment variables are available to configure the Docker Scout CLI commands, and the corresponding `docker/scout-cli` container image:

NameFormatDescriptionDOCKER\_SCOUT\_CACHE\_FORMATStringFormat of the local image cache; can be `oci` or `tar` (default: `oci`)DOCKER\_SCOUT\_CACHE\_DIRStringDirectory where the local SBOM cache is stored (default: `$HOME/.docker/scout`)DOCKER\_SCOUT\_NO\_CACHEBooleanWhen set to `true`, disables the use of local SBOM cacheDOCKER\_SCOUT\_OFFLINEBooleanUse [offline mode](#offline-mode) when indexing SBOMDOCKER\_SCOUT\_REGISTRY\_TOKENStringToken for authenticating to a registry when pulling imagesDOCKER\_SCOUT\_REGISTRY\_USERStringUsername for authenticating to a registry when pulling imagesDOCKER\_SCOUT\_REGISTRY\_PASSWORDStringPassword or personal access token for authenticating to a registry when pulling imagesDOCKER\_SCOUT\_HUB\_USERStringDocker Hub username for authenticating to the Docker Scout backendDOCKER\_SCOUT\_HUB\_PASSWORDStringDocker Hub password or personal access token for authenticating to the Docker Scout backendDOCKER\_SCOUT\_NEW\_VERSION\_WARNBooleanWarn about new versions of the Docker Scout CLIDOCKER\_SCOUT\_EXPERIMENTAL\_WARNBooleanWarn about experimental featuresDOCKER\_SCOUT\_EXPERIMENTAL\_POLICY\_OUTPUTBooleanDisable experimental output for policy evaluation

## [Offline mode](#offline-mode)

Under normal operation, Docker Scout cross-references external systems, such as npm, NuGet, or proxy.golang.org, to retrieve additional information about packages found in your image.

When `DOCKER_SCOUT_OFFLINE` is set to `true`, Docker Scout image analysis runs in offline mode. Offline mode means Docker Scout doesn't make outbound requests to external systems.

To use offline mode:

```
$ export DOCKER_SCOUT_OFFLINE=true
```