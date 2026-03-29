---
title: Develop your app
url: https://docs.docker.com/guides/rust/develop/
source: llms
fetched_at: 2026-01-24T14:11:55.497463154-03:00
rendered_js: false
word_count: 881
summary: A comprehensive guide providing instructions and best practices for building and programming software applications.
tags:
    - software development
    - app building
    - programming
    - coding
category: guide
---

## Develop your Rust application

- You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
- You have completed the walkthroughs in the Docker Desktop [Learning Center](https://docs.docker.com/desktop/use-desktop/) to learn about Docker concepts.
- You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

In this section, you’ll learn how to use volumes and networking in Docker. You’ll also use Docker to build your images and Docker Compose to make everything a whole lot easier.

First, you’ll take a look at running a database in a container and how you can use volumes and networking to persist your data and let your application talk with the database. Then you’ll pull everything together into a Compose file which lets you set up and run a local development environment with one command.

Instead of downloading PostgreSQL, installing, configuring, and then running the PostgreSQL database as a service, you can use the Docker Official Image for PostgreSQL and run it in a container.

Before you run PostgreSQL in a container, create a volume that Docker can manage to store your persistent data and configuration. Use the named volumes feature that Docker provides instead of using bind mounts.

Run the following command to create your volume.

Now create a network that your application and database will use to talk to each other. The network is called a user-defined bridge network and gives you a nice DNS lookup service which you can use when creating your connection string.

Now you can run PostgreSQL in a container and attach to the volume and network that you created previously. Docker pulls the image from Hub and runs it for you locally. In the following command, option `--mount` is for starting the container with a volume. For more information, see [Docker volumes](https://docs.docker.com/engine/storage/volumes/).

Now, make sure that your PostgreSQL database is running and that you can connect to it. Connect to the running PostgreSQL database inside the container.

You should see output like the following.

In the previous command, you logged in to the PostgreSQL database by passing the `psql` command to the `db` container. Press ctrl-d to exit the PostgreSQL interactive terminal.

For the sample application, you'll use a variation of the backend from the react-rust-postgres application from [Awesome Compose](https://github.com/docker/awesome-compose/tree/master/react-rust-postgres).

1. Clone the sample application repository using the following command.
2. In the cloned repository's directory, run `docker init` to create the necessary Docker files. Refer to the following example to answer the prompts from `docker init`.
3. In the cloned repository's directory, open the `Dockerfile` in an IDE or text editor to update it.
   
   `docker init` handled creating most of the instructions in the Dockerfile, but you'll need to update it for your unique application. In addition to a `src` directory, this application includes a `migrations` directory to initialize the database. Add a bind mount for the `migrations` directory to the build stage in the Dockerfile. The following is the updated Dockerfile.
4. In the cloned repository's directory, run `docker build` to build the image.
5. Run `docker run` with the following options to run the image as a container on the same network as the database.
6. Curl the application to verify that it connects to the database.
   
   You should get a response like the following.

When you run `docker init`, in addition to a `Dockerfile`, it also creates a `compose.yaml` file.

This Compose file is super convenient as you don't have to type all the parameters to pass to the `docker run` command. You can declaratively do that using a Compose file.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor. `docker init` handled creating most of the instructions, but you'll need to update it for your unique application.

You need to update the following items in the `compose.yaml` file:

- Uncomment all of the database instructions.
- Add the environment variables under the server service.

The following is the updated `compose.yaml` file.

Note that the file doesn't specify a network for those 2 services. When you use Compose, it automatically creates a network and connects the services to it. For more information see [Networking in Compose](https://docs.docker.com/compose/how-tos/networking/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.

If you have any other containers running from the previous sections, [stop](https://docs.docker.com/guides/rust/run-containers/#stop-start-and-name-containers) them now.

Now, run the following `docker compose up` command to start your application.

The command passes the `--build` flag so Docker will compile your image and then start the containers.

Now test your API endpoint. Open a new terminal then make a request to the server using the curl commands:

You should receive the following response:

In this section, you took a look at setting up your Compose file to run your Rust application and database with a single command.

Related information:

- [Docker volumes](https://docs.docker.com/engine/storage/volumes/)
- [Compose overview](https://docs.docker.com/compose/)

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.