---
title: Get Docker Desktop
url: https://docs.docker.com/get-started/introduction/get-docker-desktop/
source: llms
fetched_at: 2026-01-24T14:02:44.254151998-03:00
rendered_js: false
word_count: 352
summary: This document provides a walk-through for installing Docker Desktop and running an initial container to introduce users to container management. It covers basic CLI commands for starting containers and explores the Docker Desktop interface for monitoring and inspecting active services.
tags:
    - docker-desktop
    - container-management
    - installation-guide
    - docker-cli
    - getting-started
category: tutorial
---

## [Explanation](#explanation)

Docker Desktop is the all-in-one package to build images, run containers, and so much more. This guide will walk you through the installation process, enabling you to experience Docker Desktop firsthand.

> **Docker Desktop terms**
> 
> Commercial use of Docker Desktop in larger enterprises (more than 250 employees OR more than $10 million USD in annual revenue) requires a [paid subscription](https://www.docker.com/pricing/?_gl=1%2A1nyypal%2A_ga%2AMTYxMTUxMzkzOS4xNjgzNTM0MTcw%2A_ga_XJWPQMJYHQ%2AMTcxNjk4MzU4Mi4xMjE2LjEuMTcxNjk4MzkzNS4xNy4wLjA.).

### Docker Desktop for Mac

### Docker Desktop for Windows

### Docker Desktop for Linux

Once it's installed, complete the setup process and you're all set to run a Docker container.

## [Try it out](#try-it-out)

In this hands-on guide, you will see how to run a Docker container using Docker Desktop.

Follow the instructions to run a container using the CLI.

## [Run your first container](#run-your-first-container)

Open your CLI terminal and start a container by running the `docker run` command:

```
$ docker run -d -p 8080:80 docker/welcome-to-docker
```

## [Access the frontend](#access-the-frontend)

For this container, the frontend is accessible on port `8080`. To open the website, visit [http://localhost:8080](http://localhost:8080) in your browser.

![Screenshot of the landing page of the Nginx web server, coming from the running container](https://docs.docker.com/get-started/docker-concepts/the-basics/images/access-the-frontend.webp)

![Screenshot of the landing page of the Nginx web server, coming from the running container](https://docs.docker.com/get-started/docker-concepts/the-basics/images/access-the-frontend.webp)

## [Manage containers using Docker Desktop](#manage-containers-using-docker-desktop)

1. Open Docker Desktop and select the **Containers** field on the left sidebar.
2. You can view information about your container including logs, and files, and even access the shell by selecting the **Exec** tab.
   
   ![Screenshot of exec into the running container in Docker Desktop](https://docs.docker.com/get-started/introduction/images/exec-into-docker-container.webp)
   
   ![Screenshot of exec into the running container in Docker Desktop](https://docs.docker.com/get-started/introduction/images/exec-into-docker-container.webp)
3. Select the **Inspect** field to obtain detailed information about the container. You can perform various actions such as pause, resume, start or stop containers, or explore the **Logs**, **Bind mounts**, **Exec**, **Files**, and **Stats** tabs.

![Screenshot of inspecting the running container in Docker Desktop](https://docs.docker.com/get-started/introduction/images/inspecting-container.webp)

![Screenshot of inspecting the running container in Docker Desktop](https://docs.docker.com/get-started/introduction/images/inspecting-container.webp)

Docker Desktop simplifies container management for developers by streamlining the setup, configuration, and compatibility of applications across different environments, thereby addressing the pain points of environment inconsistencies and deployment challenges.

## [What's next?](#whats-next)

Now that you have Docker Desktop installed and ran your first container, it's time to start developing with containers.

[Develop with containers](https://docs.docker.com/get-started/introduction/develop-with-containers/)