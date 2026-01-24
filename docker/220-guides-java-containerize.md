---
title: Containerize your app
url: https://docs.docker.com/guides/java/containerize/
source: llms
fetched_at: 2026-01-24T14:10:32.922489187-03:00
rendered_js: false
word_count: 515
summary: This guide provides instructions on how to containerize and run a Java Spring Boot application using Docker, covering automated asset generation with docker init and manual configuration.
tags:
    - java
    - docker
    - containerization
    - spring-boot
    - dockerfile
    - docker-compose
    - docker-init
category: tutorial
---

## Containerize a Java application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/). Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.

<!--THE END-->

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

This section walks you through containerizing and running a Java application.

Clone the sample application that you'll be using to your local development machine. Run the following command in a terminal to clone the repository.

The sample application is a Spring Boot application built using Maven. For more details, see `readme.md` in the repository.

Now that you have an application, you can create the necessary Docker assets to containerize your application. You can use Docker Desktop's built-in Docker Init feature to help streamline the process, or you can manually create the assets.

Inside the `spring-petclinic` directory, run the `docker init` command. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.

The sample application already contains Docker assets. You'll be prompted to overwrite the existing Docker assets. To continue with this guide, select `y` to overwrite them.

In the previous example, notice the `WARNING`. `docker-compose.yaml` already exists, so `docker init` overwrites that file rather than creating a new `compose.yaml` file. This prevents having multiple Compose files in the directory. Both names are supported, but Compose prefers the canonical `compose.yaml`.

If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.

Create a file named `Dockerfile` with the following contents.

The sample already contains a Compose file. Overwrite this file to follow along with the guide. Update the`docker-compose.yaml` with the following contents.

Create a file named `.dockerignore` with the following contents.

You should now have the following three files in your `spring-petclinic` directory.

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [docker-compose.yaml](https://docs.docker.com/reference/compose-file/)

Inside the `spring-petclinic` directory, run the following command in a terminal.

The first time you build and run the app, Docker downloads dependencies and builds the app. It may take several minutes depending on your network connection.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple app for a pet clinic.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `spring-petclinic` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple app for a pet clinic.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

In this section, you learned how you can containerize and run a Java application using Docker.

Related information:

- [docker init reference](https://docs.docker.com/reference/cli/docker/init/)

In the next section, you'll learn how you can develop your application using Docker containers.