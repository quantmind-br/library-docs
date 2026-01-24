---
title: Develop your app
url: https://docs.docker.com/guides/deno/develop/
source: llms
fetched_at: 2026-01-24T14:03:57.590635941-03:00
rendered_js: false
word_count: 275
summary: This guide explains how to use Docker Compose Watch to create a streamlined Deno development environment that automatically updates running services when source code is modified.
tags:
    - deno
    - docker
    - docker-compose
    - compose-watch
    - development-workflow
    - containerization
category: tutorial
---

## Use containers for Deno development

## [Prerequisites](#prerequisites)

Complete [Containerize a Deno application](https://docs.docker.com/guides/deno/containerize/).

## [Overview](#overview)

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Configuring Compose to automatically update your running Compose services as you edit and save your code

## [Get the sample application](#get-the-sample-application)

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

```
$ git clone https://github.com/dockersamples/docker-deno.git && cd docker-deno
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
services:server:image:deno-serverbuild:context:.dockerfile:Dockerfileports:- "8000:8000"develop:watch:- action:rebuildpath:.
```

Run the following command to run your application with Compose Watch.

Now, if you modify your `server.ts` you will see the changes in real time without re-building the image.

To test it out, open the `server.ts` file in your favorite text editor and change the message from `{"Status" : "OK"}` to `{"Status" : "Updated"}`. Save the file and refresh your browser at `http://localhost:8000`. You should see the updated message.

Press `ctrl+c` in the terminal to stop your application.

## [Summary](#summary)

In this section, you also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## [Next steps](#next-steps)

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.