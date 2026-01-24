---
title: 'Part 3: Share the application'
url: https://docs.docker.com/get-started/workshop/04_sharing_app/
source: llms
fetched_at: 2026-01-24T14:02:50.32178697-03:00
rendered_js: false
word_count: 95
summary: This document explains how to run a containerized application and describes the difference between binding ports to the loopback interface versus all host interfaces.
tags:
    - docker
    - port-binding
    - networking
    - containerization
    - deployment
category: tutorial
---

In the terminal, start your freshly pushed app.

You should see the image get pulled down and eventually start up.

You may have noticed that this command binds the port mapping to a different IP address. Previous `docker run` commands published ports to `127.0.0.1:3000` on the host. This time, you're using `0.0.0.0`.

Binding to `127.0.0.1` only exposes a container's ports to the loopback interface. Binding to `0.0.0.0`, however, exposes the container's port on all interfaces of the host, making it available to the outside world.

For more information about how port mapping works, see [Networking](https://docs.docker.com/engine/network/#published-ports).