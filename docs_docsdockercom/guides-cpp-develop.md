---
title: Develop your app
url: https://docs.docker.com/guides/cpp/develop/
source: llms
fetched_at: 2026-01-24T14:08:46.249037588-03:00
rendered_js: false
word_count: 275
summary: This document explains how to set up a C++ development environment using Docker Compose Watch to automatically rebuild and update services when source code changes are detected.
tags:
    - docker
    - cpp
    - docker-compose
    - compose-watch
    - development-workflow
    - containerization
category: guide
---

## Use containers for C++ development

## [Prerequisites](#prerequisites)

Complete [Containerize a C++ application](https://docs.docker.com/guides/cpp/containerize/).

## [Overview](#overview)

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Configuring Compose to automatically update your running Compose services as you edit and save your code

## [Get the sample application](#get-the-sample-application)

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

```
$ git clone https://github.com/dockersamples/c-plus-plus-docker.git && cd c-plus-plus-docker
```

## [Automatically update services](#automatically-update-services)

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yml` file in an IDE or text editor and then add the Compose Watch instructions. The following example shows how to add Compose Watch to your `compose.yml` file.

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
```

```
services:ok-api:image:ok-apibuild:context:.dockerfile:Dockerfileports:- "8080:8080"develop:watch:- action:rebuildpath:.
```

Run the following command to run your application with Compose Watch.

Now, if you modify your `ok_api.cpp` you will see the changes in real time without re-building the image.

To test it out, open the `ok_api.cpp` file in your favorite text editor and change the message from `{"Status" : "OK"}` to `{"Status" : "Updated"}`. Save the file and refresh your browser at [http://localhost:8080](http://localhost:8080). You should see the updated message.

Press `ctrl+c` in the terminal to stop your application.

## [Summary](#summary)

In this section, you also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## [Next steps](#next-steps)

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.