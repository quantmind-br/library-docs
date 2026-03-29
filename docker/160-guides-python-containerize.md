---
title: Containerize your app
url: https://docs.docker.com/guides/python/containerize/
source: llms
fetched_at: 2026-01-24T14:11:19.297606058-03:00
rendered_js: false
word_count: 538
summary: This document provides a step-by-step guide on how to containerize and run a Python application using Docker, covering tool initialization, configuration files, and basic container management.
tags:
    - docker
    - python
    - fastapi
    - containerization
    - docker-compose
    - docker-init
    - deployment
category: tutorial
---

## Containerize a Python application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

This section walks you through containerizing and running a Python application.

The sample application uses the popular [FastAPI](https://fastapi.tiangolo.com) framework.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

Now that you have an application, you can create the necessary Docker assets to containerize your application. You can use Docker Desktop's built-in Docker Init feature to help streamline the process, or you can manually create the assets.

Inside the `python-docker-example` directory, run the `docker init` command. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. For example, this application uses FastAPI to run. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.

Before editing your Dockerfile, you need to choose a base image. You can use the [Python Docker Official Image](https://hub.docker.com/_/python),  
or a [Docker Hardened Image (DHI)](https://hub.docker.com/hardened-images/catalog/dhi/python).

Docker Hardened Images (DHIs) are minimal, secure, and production-ready base images maintained by Docker.  
They help reduce vulnerabilities and simplify compliance. For more details, see [Docker Hardened Images](https://docs.docker.com/dhi/).

Create a file named `.gitignore` with the following contents.

If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.

Create a file named `Dockerfile` with the following contents.

Create a file named `compose.yaml` with the following contents.

Create a file named `.dockerignore` with the following contents.

Create a file named `.gitignore` with the following contents.

If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.

Create a file named `Dockerfile` with the following contents.

Create a file named `compose.yaml` with the following contents.

Create a file named `.dockerignore` with the following contents.

Create a file named `.gitignore` with the following contents.

You should now have the following contents in your `python-docker-example` directory.

To learn more about the files, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [.gitignore](https://git-scm.com/docs/gitignore)
- [compose.yaml](https://docs.docker.com/reference/compose-file/)

Inside the `python-docker-example` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:8000](http://localhost:8000). You should see a simple FastAPI application.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `python-docker-example` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:8000](http://localhost:8000).

To see the OpenAPI docs you can go to [http://localhost:8000/docs](http://localhost:8000/docs).

You should see a simple FastAPI application.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

In this section, you learned how you can containerize and run your Python application using Docker.

Related information:

- [Docker Compose overview](https://docs.docker.com/compose/)

In the next section, you'll take a look at how to set up a local development environment using Docker containers.