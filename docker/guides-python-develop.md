---
title: Develop your app
url: https://docs.docker.com/guides/python/develop/
source: llms
fetched_at: 2026-01-24T14:11:21.746104495-03:00
rendered_js: false
word_count: 719
summary: This tutorial explains how to set up a robust Python development environment using Docker Compose, including database integration and automatic service updates via Compose Watch.
tags:
    - python
    - docker-compose
    - development-environment
    - compose-watch
    - data-persistence
    - containerization
category: tutorial
---

## Use containers for Python development

Complete [Containerize a Python application](https://docs.docker.com/guides/python/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring Compose to automatically update your running Compose services as you edit and save your code

You'll need to clone a new repository to get a sample application that includes logic to connect to the database.

1. Change to a directory where you want to clone the repository and run the following command.
2. In the cloned repository's directory, manually create the Docker assets or run `docker init` to create the necessary Docker assets.
   
   In the cloned repository's directory, run `docker init`. Refer to the following example to answer the prompts from `docker init`.
   
   Create a file named `.gitignore` with the following contents.
   
   If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.
   
   Create a file named `Dockerfile` with the following contents.
   
   Create a file named `compose.yaml` with the following contents.
   
   Create a file named `.dockerignore` with the following contents.
   
   Create a file named `.gitignore` with the following contents.

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor. `docker init` handled creating most of the instructions, but you'll need to update it for your unique application.

In the `compose.yaml` file, you need to uncomment all of the database instructions. In addition, you need to add the database password file as an environment variable to the server service and specify the secret file to use .

The following is the updated `compose.yaml` file.

> To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.

Save and close the `password.txt` file.

You should now have the following contents in your `python-docker-dev-example` directory.

Now, run the following `docker compose up` command to start your application.

Now test your API endpoint. Open a new terminal then make a request to the server using the curl commands:

Let's create an object with a post method

You should receive the following response:

Let's make a get request with the next curl command:

You should receive the same response as above because it's the only one object we have in database.

Press `ctrl+c` in the terminal to stop your application.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.

Run the following command to run your application with Compose Watch.

In a terminal, curl the application to get a response.

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `python-docker-dev-example/app.py` in an IDE or text editor and update the `Hello, Docker!` string by adding a few more exclamation marks.

Save the changes to `app.py` and then wait a few seconds for the application to rebuild. Curl the application again and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop your application.

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

In the next section, you'll learn how you can set up linting, formatting and type checking to follow the best practices in python apps.