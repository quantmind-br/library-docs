---
title: Run containers
url: https://docs.docker.com/guides/golang/run-containers/
source: llms
fetched_at: 2026-01-24T14:10:30.143613783-03:00
rendered_js: false
word_count: 1120
summary: This document explains how to run and manage Go applications within Docker containers, covering essential commands for port publishing, detached execution, and container lifecycle management.
tags:
    - docker
    - container-management
    - golang
    - devops
    - port-publishing
    - docker-cli
category: tutorial
---

## Run your Go image as a container

Work through the steps to containerize a Go application in [Build your Go image](https://docs.docker.com/guides/golang/build-images/).

In the previous module you created a `Dockerfile` for your example application and then you created your Docker image using the command `docker build`. Now that you have the image, you can run that image and see if your application is running correctly.

A container is a normal operating system process except that this process is isolated and has its own file system, its own networking, and its own isolated process tree separate from the host.

To run an image inside of a container, you use the `docker run` command. It requires one parameter and that's the image name. Start your image and make sure it's running correctly. Run the following command in your terminal.

When you run this command, you’ll notice that you weren't returned to the command prompt. This is because your application is a REST server and will run in a loop waiting for incoming requests without returning control back to the OS until you stop the container.

Make a GET request to the server using the curl command.

Your curl command failed because the connection to your server was refused. Meaning that you weren't able to connect to localhost on port 8080. This is expected because your container is running in isolation which includes networking. Stop the container and restart with port 8080 published on your local network.

To stop the container, press ctrl-c. This will return you to the terminal prompt.

To publish a port for your container, you’ll use the `--publish` flag (`-p` for short) on the `docker run` command. The format of the `--publish` command is `[host_port]:[container_port]`. So if you wanted to expose port `8080` inside the container to port `3000` outside the container, you would pass `3000:8080` to the `--publish` flag.

Start the container and expose port `8080` to port `8080` on the host.

Now, rerun the curl command.

Success! You were able to connect to the application running inside of your container on port 8080. Switch back to the terminal where your container is running and you should see the `GET` request logged to the console.

Press `ctrl-c` to stop the container.

This is great so far, but your sample application is a web server and you shouldn't have to have your terminal connected to the container. Docker can run your container in detached mode in the background. To do this, you can use the `--detach` or `-d` for short. Docker will start your container the same as before but this time will detach from the container and return you to the terminal prompt.

Docker started your container in the background and printed the container ID on the terminal.

Again, make sure that your container is running. Run the same `curl` command:

Since you ran your container in the background, how do you know if your container is running or what other containers are running on your machine? Well, to see a list of containers running on your machine, run `docker ps`. This is similar to how the ps command is used to see a list of processes on a Linux machine.

The `ps` command tells you a bunch of stuff about your running containers. You can see the container ID, the image running inside the container, the command that was used to start the container, when it was created, the status, ports that are exposed, and the names of the container.

You are probably wondering where the name of your container is coming from. Since you didn’t provide a name for the container when you started it, Docker generated a random name. You'll fix this in a minute but first you need to stop the container. To stop the container, run the `docker stop` command, passing the container's name or ID.

Now rerun the `docker ps` command to see a list of running containers.

Docker containers can be started, stopped and restarted. When you stop a container, it's not removed but the status is changed to stopped and the process inside of the container is stopped. When you ran the `docker ps` command, the default output is to only show running containers. If you pass the `--all` or `-a` for short, you will see all containers on your system, including stopped containers and running containers.

If you’ve been following along, you should see several containers listed. These are containers that you started and stopped but haven't removed yet.

Restart the container that you have just stopped. Locate the name of the container and replace the name of the container in the following `restart` command:

Now, list all the containers again using the `ps` command:

Notice that the container you just restarted has been started in detached mode and has port `8080` exposed. Also, note that the status of the container is `Up X seconds`. When you restart a container, it will be started with the same flags or commands that it was originally started with.

Stop and remove all of your containers and take a look at fixing the random naming issue.

Stop the container you just started. Find the name of your running container and replace the name in the following command with the name of the container on your system:

Now that all of your containers are stopped, remove them. When a container is removed, it's no longer running nor is it in the stopped state. Instead, the process inside the container is terminated and the metadata for the container is removed.

To remove a container, run the `docker rm` command passing the container name. You can pass multiple container names to the command in one command.

Again, make sure you replace the containers names in the following command with the container names from your system:

Run the `docker ps --all` command again to verify that all containers are gone.

Now, address the pesky random name issue. Standard practice is to name your containers for the simple reason that it's easier to identify what's running in the container and what application or service it's associated with. Just like good naming conventions for variables in your code makes it simpler to read. So goes naming your containers.

To name a container, you must pass the `--name` flag to the `run` command:

Now, you can easily identify your container based on the name.

In this module, you learned how to run containers and publish ports. You also learned to manage the lifecycle of containers. You then learned the importance of naming your containers so that they're more easily identifiable. In the next module, you’ll learn how to run a database in a container and connect it to your application.