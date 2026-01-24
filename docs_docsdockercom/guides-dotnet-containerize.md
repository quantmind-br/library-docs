---
title: Containerize your app
url: https://docs.docker.com/guides/dotnet/containerize/
source: llms
fetched_at: 2026-01-24T14:04:35.671635658-03:00
rendered_js: false
word_count: 343
summary: This guide provides step-by-step instructions on how to containerize and run a .NET application using the docker init command and Docker Compose.
tags:
    - dotnet
    - docker-init
    - containerization
    - docker-compose
    - net-core
    - devops
category: tutorial
---

## Containerize a .NET application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

This section walks you through containerizing and running a .NET application.

In this guide, you will use a pre-built .NET application. The application is similar to the application built in the Docker Blog article, [Building a Multi-Container .NET App Using Docker Desktop](https://www.docker.com/blog/building-multi-container-net-app-using-docker-desktop/).

Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository.

Now that you have an application, you can use `docker init` to create the necessary Docker assets to containerize your application. Inside the `docker-dotnet-sample` directory, run the `docker init` command in a terminal. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.

You should now have the following contents in your `docker-dotnet-sample` directory.

To learn more about the files that `docker init` added, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [compose.yaml](https://docs.docker.com/reference/compose-file/)

Inside the `docker-dotnet-sample` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple web application.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-dotnet-sample` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple web application.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

In this section, you learned how you can containerize and run your .NET application using Docker.

Related information:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore file reference](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [Docker Compose overview](https://docs.docker.com/compose/)

In the next section, you'll learn how you can develop your application using Docker containers.