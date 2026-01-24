---
title: Containerize your app
url: https://docs.docker.com/guides/r/containerize/
source: llms
fetched_at: 2026-01-24T14:11:23.382287274-03:00
rendered_js: false
word_count: 258
summary: This tutorial provides a step-by-step guide on how to containerize and run an R application using the Shiny framework and Docker Compose.
tags:
    - r-language
    - docker
    - shiny
    - containerization
    - docker-compose
    - devops
category: tutorial
---

## Containerize a R application

Table of contents

* * *

## [Prerequisites](#prerequisites)

- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## [Overview](#overview)

This section walks you through containerizing and running a R application.

## [Get the sample application](#get-the-sample-application)

The sample application uses the popular [Shiny](https://shiny.posit.co/) framework.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

```
$ git clone https://github.com/mfranzon/r-docker-dev.git && cd r-docker-dev
```

You should now have the following contents in your `r-docker-dev` directory.

```
├── r-docker-dev/
│ ├── src/
│ │ └── app.R
│ ├── src_db/
│ │ └── app_db.R
│ ├── compose.yaml
│ ├── Dockerfile
│ └── README.md
```

To learn more about the files in the repository, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [compose.yaml](https://docs.docker.com/reference/compose-file/)

## [Run the application](#run-the-application)

Inside the `r-docker-dev` directory, run the following command in a terminal.

```
$ docker compose up --build
```

Open a browser and view the application at [http://localhost:3838](http://localhost:3838). You should see a simple Shiny application.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `r-docker-dev` directory, run the following command in a terminal.

```
$ docker compose up --build -d
```

Open a browser and view the application at [http://localhost:3838](http://localhost:3838).

You should see a simple Shiny application.

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## [Summary](#summary)

In this section, you learned how you can containerize and run your R application using Docker.

Related information:

- [Docker Compose overview](https://docs.docker.com/compose/)

## [Next steps](#next-steps)

In the next section, you'll learn how you can develop your application using containers.