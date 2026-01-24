---
title: Quickstart
url: https://docs.docker.com/compose/gettingstarted/
source: llms
fetched_at: 2026-01-24T14:17:19.846621494-03:00
rendered_js: false
word_count: 1175
summary: This tutorial provides a practical introduction to Docker Compose by demonstrating how to define and orchestrate a multi-container application using a web service and a database. It covers core functionality including service configuration, automated development workflows with watch mode, and modularizing configurations with file includes.
tags:
    - docker-compose
    - container-orchestration
    - multi-container-apps
    - yaml-configuration
    - docker-watch
    - development-workflow
    - service-management
category: tutorial
---

## Docker Compose Quickstart

This tutorial aims to introduce fundamental concepts of Docker Compose by guiding you through the development of a basic Python web application.

Using the Flask framework, the application features a hit counter in Redis, providing a practical example of how Docker Compose can be applied in web development scenarios.

The concepts demonstrated here should be understandable even if you're not familiar with Python.

This is a non-normative example that demonstrates core Compose functionality.

Make sure you have:

- [Installed the latest version of Docker Compose](https://docs.docker.com/compose/install/)
- A basic understanding of Docker concepts and how Docker works

<!--THE END-->

1. Create a directory for the project:
2. Create a file called `app.py` in your project directory and paste the following code in:
   
   In this example, `redis` is the hostname of the redis container on the application's network and the default port, `6379` is used.
   
   > Note the way the `get_hit_count` function is written. This basic retry loop attempts the request multiple times if the Redis service is not available. This is useful at startup while the application comes online, but also makes the application more resilient if the Redis service needs to be restarted anytime during the app's lifetime. In a cluster, this also helps handling momentary connection drops between nodes.
3. Create another file called `requirements.txt` in your project directory and paste the following code in:
4. Create a `Dockerfile` and paste the following code in:
   
   This tells Docker to:
   
   - Build an image starting with the Python 3.10 image.
   - Set the working directory to `/code`.
   - Set environment variables used by the `flask` command.
   - Install gcc and other dependencies
   - Copy `requirements.txt` and install the Python dependencies.
   - Add metadata to the image to describe that the container is listening on port 5000
   - Copy the current directory `.` in the project to the workdir `.` in the image.
   - Set the default command for the container to `flask run --debug`.
   
   > Check that the `Dockerfile` has no file extension like `.txt`. Some editors may append this file extension automatically which results in an error when you run the application.
   
   For more information on how to write Dockerfiles, see the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

Compose simplifies the control of your entire application stack, making it easy to manage services, networks, and volumes in a single, comprehensible YAML configuration file.

Create a file called `compose.yaml` in your project directory and paste the following:

This Compose file defines two services: `web` and `redis`.

The `web` service uses an image that's built from the `Dockerfile` in the current directory. It then binds the container and the host machine to the exposed port, `8000`. This example service uses the default port for the Flask web server, `5000`.

The `redis` service uses a public [Redis](https://registry.hub.docker.com/_/redis/) image pulled from the Docker Hub registry.

For more information on the `compose.yaml` file, see [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/).

With a single command, you create and start all the services from your configuration file.

1. From your project directory, start up your application by running `docker compose up`.
   
   Compose pulls a Redis image, builds an image for your code, and starts the services you defined. In this case, the code is statically copied into the image at build time.
2. Enter `http://localhost:8000/` in a browser to see the application running.
   
   If this doesn't resolve, you can also try `http://127.0.0.1:8000`.
   
   You should see a message in your browser saying:
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-1.png)
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-1.png)
3. Refresh the page.
   
   The number should increment.
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-2.png)
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-2.png)
4. Switch to another terminal window, and type `docker image ls` to list local images.
   
   Listing images at this point should return `redis` and `web`.
   
   You can inspect images with `docker inspect <tag or id>`.
5. Stop the application, either by running `docker compose down` from within your project directory in the second terminal, or by hitting `CTRL+C` in the original terminal where you started the app.

Edit the `compose.yaml` file in your project directory to use `watch` so you can preview your running Compose services which are automatically updated as you edit and save your code:

Whenever a file is changed, Compose syncs the file to the corresponding location under `/code` inside the container. Once copied, the bundler updates the running application without a restart.

For more information on how Compose Watch works, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/). Alternatively, see [Manage data in containers](https://docs.docker.com/engine/storage/volumes/) for other options.

> For this example to work, the `--debug` option is added to the `Dockerfile`. The `--debug` option in Flask enables automatic code reload, making it possible to work on the backend API without the need to restart or rebuild the container. After changing the `.py` file, subsequent API calls will use the new code, but the browser UI will not automatically refresh in this small example. Most frontend development servers include native live reload support that works with Compose.

From your project directory, type `docker compose watch` or `docker compose up --watch` to build and launch the app and start the file watch mode.

Check the `Hello World` message in a web browser again, and refresh to see the count increment.

To see Compose Watch in action:

1. Change the greeting in `app.py` and save it. For example, change the `Hello World!` message to `Hello from Docker!`:
2. Refresh the app in your browser. The greeting should be updated, and the counter should still be incrementing.
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-3.png)
   
   ![hello world in browser](https://docs.docker.com/compose/images/quick-hello-world-3.png)
3. Once you're done, run `docker compose down`.

Using multiple Compose files lets you customize a Compose application for different environments or workflows. This is useful for large applications that may use dozens of containers, with ownership distributed across multiple teams.

1. In your project folder, create a new Compose file called `infra.yaml`.
2. Cut the Redis service from your `compose.yaml` file and paste it into your new `infra.yaml` file. Make sure you add the `services` top-level attribute at the top of your file. Your `infra.yaml` file should now look like this:
3. In your `compose.yaml` file, add the `include` top-level attribute along with the path to the `infra.yaml` file.
4. Run `docker compose up` to build the app with the updated Compose files, and run it. You should see the `Hello world` message in your browser.

This is a simplified example, but it demonstrates the basic principle of `include` and how it can make it easier to modularize complex applications into sub-Compose files. For more information on `include` and working with multiple Compose files, see [Working with multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/).

- If you want to run your services in the background, you can pass the `-d` flag (for "detached" mode) to `docker compose up` and use `docker compose ps` to see what is currently running:
- Run `docker compose --help` to see other available commands.
- If you started Compose with `docker compose up -d`, stop your services once you've finished with them:
- You can bring everything down, removing the containers entirely, with the `docker compose down` command.

<!--THE END-->

- Try the [Sample apps with Compose](https://github.com/docker/awesome-compose)
- [Explore the full list of Compose commands](https://docs.docker.com/reference/cli/docker/compose/)
- [Explore the Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Check out the Learning Docker Compose video on LinkedIn Learning](https://www.linkedin.com/learning/learning-docker-compose/)