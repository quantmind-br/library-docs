---
title: Develop your app
url: https://docs.docker.com/guides/dotnet/develop/
source: llms
fetched_at: 2026-01-24T14:04:38.275302115-03:00
rendered_js: false
word_count: 1022
summary: This guide explains how to configure a .NET development environment using Docker, covering database integration, data persistence, automatic code updates with Compose Watch, and multi-stage Dockerfiles.
tags:
    - dotnet
    - docker-compose
    - compose-watch
    - multi-stage-build
    - data-persistence
    - development-workflow
category: tutorial
---

## Use containers for .NET development

Complete [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring Compose to automatically update your running Compose services as you edit and save your code
- Creating a development container that contains the .NET Core SDK tools and dependencies

This section uses a different branch of the `docker-dotnet-sample` repository that contains an updated .NET application. The updated application is on the `add-db` branch of the repository you cloned in [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/).

To get the updated code, you need to checkout the `add-db` branch. For the changes you made in [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/), for this section, you can stash them. In a terminal, run the following commands in the `docker-dotnet-sample` directory.

1. Stash any previous changes.
2. Check out the new branch with the updated application.

In the `add-db` branch, only the .NET application has been updated. None of the Docker assets have been updated yet.

You should now have the following in your `docker-dotnet-sample` directory.

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

Open the `compose.yaml` file in an IDE or text editor. You'll notice it already contains commented-out instructions for a PostgreSQL database and volume.

Open `docker-dotnet-sample/src/appsettings.json` in an IDE or text editor. You'll notice the connection string with all the database information. The `compose.yaml` already contains this information, but it's commented out. Uncomment the database instructions in the `compose.yaml` file.

The following is the updated `compose.yaml` file.

> To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file uses `secrets` and specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the `docker-dotnet-sample` directory, create a new directory named `db` and inside that directory create a file named `password.txt`. Open `password.txt` in an IDE or text editor and add the following password. The password must be on a single line, with no additional lines in the file.

Save and close the `password.txt` file.

You should now have the following in your `docker-dotnet-sample` directory.

Run the following command to start your application.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple web application with the text `Student name is`.

The application doesn't display a name because the database is empty. For this application, you need to access the database and then add records.

For the sample application, you must access the database directly to create sample records.

You can run commands inside the database container using the `docker exec` command. Before running that command, you must get the ID of the database container. Open a new terminal window and run the following command to list all your running containers.

You should see output like the following.

In the previous example, the container ID is `39fdcf0aff7b`. Run the following command to connect to the postgres database in the container. Replace the container ID with your own container ID.

And finally, insert a record into the database.

You should see output like the following.

Close the database connection and exit the container shell by running `exit`.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple web application with the text `Student name is Whale Moby`.

Press `ctrl+c` in the terminal to stop your application.

In the terminal, run `docker compose rm` to remove your containers and then run `docker compose up` to run your application again.

Refresh [http://localhost:8080](http://localhost:8080) in your browser and verify that the student name persisted, even after the containers were removed and ran again.

Press `ctrl+c` in the terminal to stop your application.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.

Run the following command to run your application with Compose Watch.

Open a browser and verify that the application is running at [http://localhost:8080](http://localhost:8080).

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `docker-dotnet-sample/src/Pages/Index.cshtml` in an IDE or text editor and update the student name text on line 13 from `Student name is` to `Student name:`.

Save the changes to `Index.cshmtl` and then wait a few seconds for the application to rebuild. Refresh [http://localhost:8080](http://localhost:8080) in your browser and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop your application.

At this point, when you run your containerized application, it's using the .NET runtime image. While this small image is good for production, it lacks the SDK tools and dependencies you may need when developing. Also, during development, you may not need to run `dotnet publish`. You can use multi-stage builds to build stages for both development and production in the same Dockerfile. For more details, see [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).

Add a new development stage to your Dockerfile and update your `compose.yaml` file to use this stage for local development.

The following is the updated Dockerfile.

The following is the updated `compose.yaml` file.

Your containerized application will now use the `mcr.microsoft.com/dotnet/sdk:8.0-alpine` image, which includes development tools like `dotnet test`. Continue to the next section to learn how you can run `dotnet test`.

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code. And finally, you learned how to create a development container that contains the SDK tools and dependencies needed for development.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

In the next section, you'll learn how to run unit tests using Docker.