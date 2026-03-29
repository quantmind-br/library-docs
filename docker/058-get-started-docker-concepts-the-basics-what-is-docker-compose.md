---
title: What is Docker Compose?
url: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/
source: llms
fetched_at: 2026-01-24T14:07:31.791526956-03:00
rendered_js: false
word_count: 853
summary: This document introduces Docker Compose for managing multi-container applications and provides a hands-on walkthrough for starting and stopping a sample application using declarative YAML configuration.
tags:
    - docker-compose
    - multi-container
    - container-orchestration
    - yaml-configuration
    - docker-basics
    - devops
category: tutorial
---

If you've been following the guides so far, you've been working with single container applications. But, now you're wanting to do something more complicated - run databases, message queues, caches, or a variety of other services. Do you install everything in a single container? Run multiple containers? If you run multiple, how do you connect them all together?

One best practice for containers is that each container should do one thing and do it well. While there are exceptions to this rule, avoid the tendency to have one container do multiple things.

You can use multiple `docker run` commands to start multiple containers. But, you'll soon realize you'll need to manage networks, all of the flags needed to connect containers to those networks, and more. And when you're done, cleanup is a little more complicated.

With Docker Compose, you can define all of your containers and their configurations in a single YAML file. If you include this file in your code repository, anyone that clones your repository can get up and running with a single command.

It's important to understand that Compose is a declarative tool - you simply define it and go. You don't always need to recreate everything from scratch. If you make a change, run `docker compose up` again and Compose will reconcile the changes in your file and apply them intelligently.

> **Dockerfile versus Compose file**
> 
> A Dockerfile provides instructions to build a container image while a Compose file defines your running containers. Quite often, a Compose file references a Dockerfile to build an image to use for a particular service.

In this hands-on, you will learn how to use a Docker Compose to run a multi-container application. You'll use a simple to-do list app built with Node.js and MySQL as a database server.

### [Start the application](#start-the-application)

Follow the instructions to run the to-do list app on your system.

1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.
2. Open a terminal and [clone this sample application](https://github.com/dockersamples/todo-list-app).
3. Navigate into the `todo-list-app` directory:
   
   Inside this directory, you'll find a file named `compose.yaml`. This YAML file is where all the magic happens! It defines all the services that make up your application, along with their configurations. Each service specifies its image, ports, volumes, networks, and any other settings necessary for its functionality. Take some time to explore the YAML file and familiarize yourself with its structure.
4. Use the [`docker compose up`](https://docs.docker.com/reference/cli/docker/compose/up/) command to start the application:
   
   When you run this command, you should see an output like this:
   
   A lot happened here! A couple of things to call out:
   
   - Two container images were downloaded from Docker Hub - node and MySQL
   - A network was created for your application
   - A volume was created to persist the database files between container restarts
   - Two containers were started with all of their necessary config
   
   If this feels overwhelming, don't worry! You'll get there!
5. With everything now up and running, you can open [http://localhost:3000](http://localhost:3000) in your browser to see the site. Note that the application may take 10-15 seconds to fully start. If the page doesn't load right away, wait a moment and refresh. Feel free to add items to the list, check them off, and remove them.
   
   ![A screenshot of a webpage showing the todo-list application running on port 3000](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-app.webp)
   
   ![A screenshot of a webpage showing the todo-list application running on port 3000](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-app.webp)
6. If you look at the Docker Desktop GUI, you can see the containers and dive deeper into their configuration.
   
   ![A screenshot of Docker Desktop dashboard showing the list of containers running todo-list app](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-containers.webp)
   
   ![A screenshot of Docker Desktop dashboard showing the list of containers running todo-list app](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-containers.webp)

### [Tear it down](#tear-it-down)

Since this application was started using Docker Compose, it's easy to tear it all down when you're done.

1. In the CLI, use the [`docker compose down`](https://docs.docker.com/reference/cli/docker/compose/down/) command to remove everything:
   
   You'll see output similar to the following:
   
   > **Volume persistence**
   > 
   > By default, volumes *aren't* automatically removed when you tear down a Compose stack. The idea is that you might want the data back if you start the stack again.
   > 
   > If you do want to remove the volumes, add the `--volumes` flag when running the `docker compose down` command:
2. Alternatively, you can use the Docker Desktop GUI to remove the containers by selecting the application stack and selecting the **Delete** button.
   
   ![A screenshot of the Docker Desktop GUI showing the containers view with an arrow pointing to the "Delete" button](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-delete.webp)
   
   ![A screenshot of the Docker Desktop GUI showing the containers view with an arrow pointing to the "Delete" button](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-delete.webp)
   
   > **Using the GUI for Compose stacks**
   > 
   > Note that if you remove the containers for a Compose app in the GUI, it's removing only the containers. You'll have to manually remove the network and volumes if you want to do so.

In this walkthrough, you learned how to use Docker Compose to start and stop a multi-container application.

This page was a brief introduction to Compose. In the following resources, you can dive deeper into Compose and how to write Compose files.

- [Overview of Docker Compose](https://docs.docker.com/compose/)
- [Overview of Docker Compose CLI](https://docs.docker.com/compose/reference/)
- [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/)