---
title: Containerize your app
url: https://docs.docker.com/guides/bun/containerize/
source: llms
fetched_at: 2026-01-24T14:08:36.448888328-03:00
rendered_js: false
word_count: 565
summary: This document provides instructions on how to containerize a Bun application using Docker, covering base image selection, Dockerfile configuration, and running containers.
tags:
    - bun
    - docker
    - containerization
    - dockerfile
    - javascript-runtime
    - deployment
category: guide
---

## Containerize a Bun application

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

For a long time, Node.js has been the de-facto runtime for server-side JavaScript applications. Recent years have seen a rise in new alternative runtimes in the ecosystem, including [Bun website](https://bun.sh/). Like Node.js, Bun is a JavaScript runtime. Bun is a comparatively lightweight runtime that is designed to be fast and efficient.

Why develop Bun applications with Docker? Having multiple runtimes to choose from is great. But as the number of runtimes increases, it becomes challenging to manage the different runtimes and their dependencies consistently across environments. This is where Docker comes in. Creating and destroying containers on demand is a great way to manage the different runtimes and their dependencies. Also, as it's fairly a new runtime, getting a consistent development environment for Bun can be challenging. Docker can help you set up a consistent development environment for Bun.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

You should now have the following contents in your `bun-docker` directory.

Before creating a Dockerfile, you need to choose a base image. You can either use the [Bun Docker Official Image](https://hub.docker.com/r/oven/bun) or a Docker Hardened Image (DHI) from the [Hardened Image catalog](https://hub.docker.com/hardened-images/catalog).

Choosing DHI offers the advantage of a production-ready image that is lightweight and secure. For more information, see [Docker Hardened Images](https://docs.docker.com/dhi/).

Docker Hardened Images (DHIs) are available for Bun in the [Docker Hardened Images catalog](https://hub.docker.com/hardened-images/catalog/dhi/bun). You can pull DHIs directly from the `dhi.io` registry.

1. Sign in to the DHI registry:
2. Pull the Bun DHI as `dhi.io/bun:1`. The tag (`1`) in this example refers to the version to the latest 1.x version of Bun.

For other available versions, refer to the [catalog](https://hub.docker.com/hardened-images/catalog/dhi/bun).

Using the Docker Official Image is straightforward. In the following Dockerfile, you'll notice that the `FROM` instruction uses `oven/bun` as the base image.

You can find the image on [Docker Hub](https://hub.docker.com/r/oven/bun). This is the Docker Official Image for Bun created by Oven, the company behind Bun, and it's available on Docker Hub.

In addition to specifying the base image, the Dockerfile also:

- Sets the working directory in the container to `/app`.
- Copies the content of the current directory to the `/app` directory in the container.
- Exposes port 3000, where the API is listening for requests.
- And finally, starts the server when the container launches with the command `bun server.js`.

Inside the `bun-docker` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:3000](http://localhost:3000). You will see a message `{"Status" : "OK"}` in the browser.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `bun-docker` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:3000](http://localhost:3000).

In the terminal, run the following command to stop the application.

In this section, you learned how you can containerize and run your Bun application using Docker.

Related information:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore file](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [Docker Compose overview](https://docs.docker.com/compose/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Docker Hardened Images](https://docs.docker.com/dhi/)

In the next section, you'll learn how you can develop your application using containers.