---
title: Develop your app
url: https://docs.docker.com/guides/r/develop/
source: llms
fetched_at: 2026-01-24T14:11:26.458441653-03:00
rendered_js: false
word_count: 508
summary: This tutorial explains how to set up a containerized R development environment using Docker Compose to integrate a local database and utilize Compose Watch for real-time code updates.
tags:
    - docker-compose
    - r-language
    - shiny-app
    - database-persistence
    - compose-watch
    - containerization
    - development-environment
category: tutorial
---

## Use containers for R development

Complete [Containerize a R application](https://docs.docker.com/guides/r/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring Compose to automatically update your running Compose services as you edit and save your code

You'll need to clone a new repository to get a sample application that includes logic to connect to the database.

Change to a directory where you want to clone the repository and run the following command.

To try the connection between the Shiny application and the local database you have to modify the `Dockerfile` changing the `COPY` instruction:

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor.

In the `compose.yaml` file, you need to un-comment the properties for configuring the database. You must also mount the database password file and set an environment variable on the `shiny-app` service pointing to the location of the file in the container.

The following is the updated `compose.yaml` file.

> To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.

Save and close the `password.txt` file.

You should now have the following contents in your `r-docker-dev` directory.

Now, run the following `docker compose up` command to start your application.

Now test your DB connection opening a browser at:

You should see a pop-up message:

Press `ctrl+c` in the terminal to stop your application.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Lines 15 to 18 in the `compose.yaml` file contain properties that trigger Docker to rebuild the image when a file in the current working directory is changed:

Run the following command to run your application with Compose Watch.

Now, if you modify your `app.R` you will see the changes in real time without re-building the image!

Press `ctrl+c` in the terminal to stop your application.

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.