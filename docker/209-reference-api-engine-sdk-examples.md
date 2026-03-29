---
title: Examples
url: https://docs.docker.com/reference/api/engine/sdk/examples/
source: llms
fetched_at: 2026-01-24T14:30:31.749424016-03:00
rendered_js: false
word_count: 411
summary: This document provides practical examples for performing common Docker operations using the Docker Engine SDKs for Go and Python as well as the HTTP API.
tags:
    - docker-engine-sdk
    - docker-api
    - go-sdk
    - python-sdk
    - container-management
    - curl
category: tutorial
---

## Examples using the Docker Engine SDKs and Docker API

After you [install Docker](https://docs.docker.com/get-started/get-docker/), you can [install the Go or Python SDK](https://docs.docker.com/reference/api/engine/sdk/#install-the-sdks) and also try out the Docker Engine API.

Each of these examples show how to perform a given Docker operation using the Go and Python SDKs and the HTTP API using `curl`.

This first example shows how to run a container using the Docker API. On the command line, you would use the `docker run` command, but this is just as easy to do from your own apps too.

This is the equivalent of typing `docker run alpine echo hello world` at the command prompt:

When using cURL to connect over a Unix socket, the hostname isn't important. The previous examples use `localhost`, but any hostname would work.

> The previous examples assume you're using cURL 7.50.0 or above. Older versions of cURL used a [non-standard URL notation](https://github.com/moby/moby/issues/17960) when using a socket connection.
> 
> If you're' using an older version of cURL, use `http:/<API version>/` instead, for example: `http:/v1.52/containers/1c6594faf5/start`.

You can also run containers in the background, the equivalent of typing `docker run -d bfirsh/reticulate-splines`:

You can use the API to list containers that are running, just like using `docker ps`:

Now that you know what containers exist, you can perform operations on them. This example stops all running containers.

> Don't run this on a production server. Also, if you're' using swarm services, the containers stop, but Docker creates new ones to keep the service running in its configured state.

You can also perform actions on individual containers. This example prints the logs of a container given its ID. You need to modify the code before running it to change the hard-coded ID of the container to print the logs for.

List the images on your Engine, similar to `docker image ls`:

Pull an image, like `docker pull`:

Pull an image, like `docker pull`, with authentication:

> Credentials are sent in the clear. Docker's official registries use HTTPS. Private registries should also be configured to use HTTPS.

The Python SDK retrieves authentication information from the [credentials store](https://docs.docker.com/reference/cli/docker/login/#credential-stores) file and integrates with [credential helpers](https://github.com/docker/docker-credential-helpers). It's possible to override these credentials, but that's out of scope for this example guide. After using `docker login`, the Python SDK uses these credentials automatically.

This example leaves the credentials in your shell's history, so consider this a naive implementation. The credentials are passed as a Base-64-encoded JSON structure.

Commit a container to create an image from its contents: