---
title: Containerize your app
url: https://docs.docker.com/guides/ruby/containerize/
source: llms
fetched_at: 2026-01-24T14:11:43.439395945-03:00
rendered_js: false
word_count: 610
summary: This document provides a step-by-step guide for containerizing a Ruby on Rails application using Docker, covering Dockerfile configuration, multi-stage builds, and Docker Compose setup.
tags:
    - ruby-on-rails
    - docker
    - containerization
    - docker-compose
    - multi-stage-builds
    - dockerfile
category: tutorial
---

## Containerize a Ruby on Rails application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have a [Git client](https://git-scm.com/downloads). The examples in this section show the Git CLI, but you can use any client.

This section walks you through containerizing and running a [Ruby on Rails](https://rubyonrails.org/) application.

Starting from Rails 7.1 [Docker is supported out of the box](https://guides.rubyonrails.org/7_1_release_notes.html#generate-dockerfiles-for-new-rails-applications). This means that you will get a `Dockerfile`, `.dockerignore` and `bin/docker-entrypoint` files generated for you when you create a new Rails application.

If you have an existing Rails application, you will need to create the Docker assets manually. Unfortunately `docker init` command does not yet support Rails. This means that if you are working with Rails, you'll need to copy Dockerfile and other related configurations manually from the examples below.

Rails 7.1 and newer generates multistage Dockerfile out of the box. Following are two versions of such a file: one using Docker Hardened Images (DHIs) and another using the Docker Official Image (DOIs). Although the Dockerfile is generated automatically, understanding its purpose and functionality is important. Reviewing the following example is highly recommended.

[Docker Hardened Images (DHIs)](https://docs.docker.com/dhi/) are minimal, secure, and production-ready container base and application images maintained by Docker. DHIs are recommended whenever it is possible for better security. They are designed to reduce vulnerabilities and simplify compliance, freely available to everyone with no subscription required, no usage restrictions, and no vendor lock-in.

Multistage Dockerfiles help create smaller, more efficient images by separating build and runtime dependencies, ensuring only necessary components are included in the final image. Read more in the [Multi-stage builds guide](https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/).

You must authenticate to `dhi.io` before you can pull Docker Hardened Images. Run `docker login dhi.io` to authenticate.

The Dockerfile above assumes you are using Thruster together with Puma as an application server. In case you are using any other server, you can replace the last three lines with the following:

This Dockerfile uses a script at `./bin/docker-entrypoint` as the container's entrypoint. This script prepares the database and runs the application server. Below is an example of such a script.

Besides the two files above you will also need a `.dockerignore` file. This file is used to exclude files and directories from the context of the build. Below is an example of a `.dockerignore` file.

The last optional file that you may want is the `compose.yaml` file, which is used by Docker Compose to define the services that make up the application. Since SQLite is being used as the database, there is no need to define a separate service for the database. The only service required is the Rails application itself.

You should now have the following files in your application folder:

- `.dockerignore`
- `compose.yaml`
- `Dockerfile`
- `bin/docker-entrypoint`

To learn more about the files, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile)
- [.dockerignore](https://docs.docker.com/reference/dockerfile#dockerignore-file)
- [compose.yaml](https://docs.docker.com/reference/compose-file/)
- [docker-entrypoint](https://docs.docker.com/reference/dockerfile/#entrypoint)

To run the application, run the following command in a terminal inside the application's directory.

Open a browser and view the application at [http://localhost:3000](http://localhost:3000). You should see a simple Ruby on Rails application.

In the terminal, press `ctrl`+`c` to stop the application.

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-ruby-on-rails` directory, run the following command in a terminal.

Open a browser and view the application at [http://localhost:3000](http://localhost:3000).

You should see a simple Ruby on Rails application.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

In this section, you learned how you can containerize and run your Ruby application using Docker.

Related information:

- [Docker Compose overview](https://docs.docker.com/compose/)

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.