---
title: Containerize your app
url: https://docs.docker.com/guides/php/containerize/
source: llms
fetched_at: 2026-01-24T14:11:06.462458054-03:00
rendered_js: false
word_count: 367
summary: This document provides a step-by-step walkthrough for containerizing a PHP application using the docker init command and running it with Docker Compose.
tags:
    - php
    - docker
    - containerization
    - docker-compose
    - docker-init
    - apache
category: tutorial
---

## Containerize a PHP application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

This section walks you through containerizing and running a PHP application.

In this guide, you will use a pre-built PHP application. The application uses Composer for library dependency management. You'll serve the application via an Apache web server.

Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository.

The sample application is a basic hello world application and an application that increments a counter in a database. In addition, the application uses PHPUnit for testing.

Now that you have an application, you can use `docker init` to create the necessary Docker assets to containerize your application. Inside the `docker-php-sample` directory, run the `docker init` command in a terminal. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. For example, this application uses PHP version 8.2. Refer to the following `docker init` example and use the same answers for your prompts.

You should now have the following contents in your `docker-php-sample` directory.

To learn more about the files that `docker init` added, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [compose.yaml](https://docs.docker.com/reference/compose-file/)

Inside the `docker-php-sample` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:9000/hello.php](http://localhost:9000/hello.php). You should see a simple hello world application.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-php-sample` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:9000/hello.php](http://localhost:9000/hello.php). You should see a simple hello world application.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

In this section, you learned how you can containerize and run a simple PHP application using Docker.

Related information:

- [docker init reference](https://docs.docker.com/reference/cli/docker/init/)

In the next section, you'll learn how you can develop your application using Docker containers.