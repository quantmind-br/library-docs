---
title: OCI artifact applications
url: https://docs.docker.com/compose/how-tos/oci-artifact/
source: llms
fetched_at: 2026-01-24T14:17:47.59297249-03:00
rendered_js: false
word_count: 518
summary: This document explains how to package, publish, and deploy Docker Compose applications as OCI artifacts using the Docker CLI. It covers the publishing process, advanced configuration options, and specific limitations when using container registries for Compose file distribution.
tags:
    - docker-compose
    - oci-artifacts
    - container-registry
    - deployment-workflow
    - docker-hub
    - software-distribution
category: guide
---

## Package and deploy Docker Compose applications as OCI artifacts

Requires: Docker Compose [2.34.0](https://github.com/docker/compose/releases/tag/v2.34.0) and later

Docker Compose supports working with [OCI artifacts](https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts/), allowing you to package and distribute your Compose applications through container registries. This means you can store your Compose files alongside your container images, making it easier to version, share, and deploy your multi-container applications.

To distribute your Compose application as an OCI artifact, you can use the `docker compose publish` command, to publish it to an OCI-compliant registry. This allows others to then deploy your application directly from the registry.

The publish function supports most of the composition capabilities of Compose, like overrides, extends or include, [with some limitations](#limitations).

### [General steps](#general-steps)

1. Navigate to your Compose application's directory.  
   Ensure you're in the directory containing your `compose.yml` file or that you are specifying your Compose file with the `-f` flag.
2. In your terminal, sign in to your Docker account so you're authenticated with Docker Hub.
3. Use the `docker compose publish` command to push your application as an OCI artifact:
   
   If you have multiple Compose files, run:

### [Advanced publishing options](#advanced-publishing-options)

When publishing, you can pass additional options:

- `--oci-version`: Specify the OCI version (default is automatically determined).
- `--resolve-image-digests`: Pin image tags to digests.
- `--with-env`: Include environment variables in the published OCI artifact.

Compose checks to make sure there isn't any sensitive data in your configuration and displays your environment variables to confirm you want to publish them.

If you decline, the publish process stops without sending anything to the registry.

There are limitations to publishing Compose applications as OCI artifacts. You can't publish a Compose configuration:

- With service(s) containing bind mounts
- With service(s) containing only a `build` section
- That includes local files with the `include` attribute. To publish successfully, ensure that any included local files are also published. You can then use `include` to reference these files as remote `include` is supported.

To start a Docker Compose application that uses an OCI artifact, you can use the `-f` (or `--file`) flag followed by the OCI artifact reference. This allows you to specify a Compose file stored as an OCI artifact in a registry.

The `oci://` prefix indicates that the Compose file should be pulled from an OCI-compliant registry rather than loaded from the local filesystem.

To then run the Compose application, use the `docker compose up` command with the `-f` flag pointing to your OCI artifact:

### [Troubleshooting](#troubleshooting)

When you run an application from an OCI artifact, Compose may display warning messages that require you to confirm the following so as to limit the risk of running a malicious application:

- A list of the interpolation variables used along with their values
- A list of all environment variables used by the application
- If your OCI artifact application is using another remote resources, for example via [`include`](https://docs.docker.com/reference/compose-file/include/).

If you agree to start the application, Compose displays the directory where all the resources from the OCI artifact have been downloaded:

The `docker compose publish` command supports non-interactive execution, letting you skip the confirmation prompt by including the `-y` (or `--yes`) flag:

- [Learn about OCI artifacts in Docker Hub](https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts/)
- [Compose publish command](https://docs.docker.com/reference/cli/docker/compose/publish/)
- [Understand `include`](https://docs.docker.com/reference/compose-file/include/)