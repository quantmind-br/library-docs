---
title: Build and run a C++ application using Docker Compose
url: https://docs.docker.com/guides/cpp/containerize/
source: llms
fetched_at: 2026-01-24T14:08:42.769934055-03:00
rendered_js: false
word_count: 242
summary: This document provides a step-by-step tutorial on how to containerize and run a C++ application using Docker and Docker Compose.
tags:
    - docker
    - docker-compose
    - cpp
    - containerization
    - c-plus-plus
    - deployment
category: tutorial
---

## Containerize a C++ application

Table of contents

* * *

## [Prerequisites](#prerequisites)

- You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

## [Overview](#overview)

This section walks you through containerizing and running a C++ application, using Docker Compose.

## [Get the sample application](#get-the-sample-application)

We're using the same sample repository that you used in the previous sections of this guide. If you haven't already cloned the repository, clone it now:

```
$ git clone https://github.com/dockersamples/c-plus-plus-docker.git
```

You should now have the following contents in your `c-plus-plus-docker` (root) directory.

```
├── c-plus-plus-docker/
│ ├── compose.yml
│ ├── Dockerfile
│ ├── LICENSE
│ ├── ok_api.cpp
│ └── README.md
```

To learn more about the files in the repository, see the following:

- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
- [compose.yml](https://docs.docker.com/reference/compose-file/)

Inside the `c-plus-plus-docker` directory, run the following command in a terminal.

```
$ docker compose up --build
```

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You will see a message `{"Status" : "OK"}` in the browser.

In the terminal, press `ctrl`+`c` to stop the application.

### [Run the application in the background](#run-the-application-in-the-background)

You can run the application detached from the terminal by adding the `-d` option. Inside the `c-plus-plus-docker` directory, run the following command in a terminal.

```
$ docker compose up --build -d
```

Open a browser and view the application at [http://localhost:8080](http://localhost:8080).

In the terminal, run the following command to stop the application.

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## [Summary](#summary)

In this section, you learned how you can containerize and run your C++ application using Docker.

Related information:

- [Docker Compose overview](https://docs.docker.com/compose/)

## [Next steps](#next-steps)

In the next section, you'll learn how you can develop your application using containers.