---
title: Develop your app
url: https://docs.docker.com/guides/php/develop/
source: llms
fetched_at: 2026-01-24T14:11:07.724282295-03:00
rendered_js: false
word_count: 1086
summary: This guide explains how to set up a containerized PHP development environment by integrating databases, persisting data, and using Compose Watch for real-time code updates. It also demonstrates how to use multi-stage Docker builds to manage development-specific dependencies separately from production environments.
tags:
    - php
    - docker-compose
    - local-development
    - multi-stage-build
    - data-persistence
    - compose-watch
category: tutorial
---

## Use containers for PHP development

Complete [Containerize a PHP application](https://docs.docker.com/guides/php/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Adding phpMyAdmin to interact with the database
- Configuring Compose to automatically update your running Compose services as you edit and save your code
- Creating a development container that contains the dev dependencies

You can use containers to set up local services, like a database. To do this for the sample application, you'll need to do the following:

- Update the `Dockerfile` to install extensions to connect to the database
- Update the `compose.yaml` file to add a database service and volume to persist data

### [Update the Dockerfile to install extensions](#update-the-dockerfile-to-install-extensions)

To install PHP extensions, you need to update the `Dockerfile`. Open your Dockerfile in an IDE or text editor and then update the contents. The following `Dockerfile` includes one new line that installs the `pdo` and `pdo_mysql` extensions. All comments have been removed.

For more details about installing PHP extensions, see the [Official Docker Image for PHP](https://hub.docker.com/_/php).

### [Update the compose.yaml file to add a db and persist data](#update-the-composeyaml-file-to-add-a-db-and-persist-data)

Open the `compose.yaml` file in an IDE or text editor. You'll notice it already contains commented-out instructions for a PostgreSQL database and volume. For this application, you'll use MariaDB. For more details about MariaDB, see the [MariaDB Official Docker image](https://hub.docker.com/_/mariadb).

Open the `src/database.php` file in an IDE or text editor. You'll notice that it reads environment variables in order to connect to the database.

In the `compose.yaml` file, you'll need to update the following:

1. Uncomment and update the database instructions for MariaDB.
2. Add a secret to the server service to pass in the database password.
3. Add the database connection environment variables to the server service.
4. Uncomment the volume instructions to persist data.

The following is the updated `compose.yaml` file. All comments have been removed.

> To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file uses `secrets` and specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the `docker-php-sample` directory, create a new directory named `db` and inside that directory create a file named `password.txt`. Open `password.txt` in an IDE or text editor and add the following password. The password must be on a single line, with no additional lines in the file.

Save and close the `password.txt` file.

You should now have the following in your `docker-php-sample` directory.

Run the following command to start your application.

Open a browser and view the application at [http://localhost:9000/database.php](http://localhost:9000/database.php). You should see a simple web application with text and a counter that increments every time you refresh.

Press `ctrl+c` in the terminal to stop your application.

In the terminal, run `docker compose rm` to remove your containers and then run `docker compose up` to run your application again.

Refresh [http://localhost:9000/database.php](http://localhost:9000/database.php) in your browser and verify that the previous count still exists. Without a volume, the database data wouldn't persist after you remove the container.

Press `ctrl+c` in the terminal to stop your application.

You can easily add services to your application stack by updating the `compose.yaml` file.

Update your `compose.yaml` to add a new service for phpMyAdmin. For more details, see the [phpMyAdmin Official Docker Image](https://hub.docker.com/_/phpmyadmin). The following is the updated `compose.yaml` file.

In the terminal, run `docker compose up` to run your application again.

Open [http://localhost:8080](http://localhost:8080) in your browser to access phpMyAdmin. Log in using `root` as the username and `example` as the password. You can now interact with the database through phpMyAdmin.

Press `ctrl+c` in the terminal to stop your application.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.

Run the following command to run your application with Compose Watch.

Open a browser and verify that the application is running at [http://localhost:9000/hello.php](http://localhost:9000/hello.php).

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `hello.php` in an IDE or text editor and update the string `Hello, world!` to `Hello, Docker!`.

Save the changes to `hello.php` and then wait a few seconds for the application to sync. Refresh [http://localhost:9000/hello.php](http://localhost:9000/hello.php) in your browser and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop Compose Watch. Run `docker compose down` in the terminal to stop the application.

At this point, when you run your containerized application, Composer isn't installing the dev dependencies. While this small image is good for production, it lacks the tools and dependencies you may need when developing and it doesn't include the `tests` directory. You can use multi-stage builds to build stages for both development and production in the same Dockerfile. For more details, see [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).

In the `Dockerfile`, you'll need to update the following:

1. Split the `deps` staged into two stages. One stage for production (`prod-deps`) and one stage (`dev-deps`) to install development dependencies.
2. Create a common `base` stage.
3. Create a new `development` stage for development.
4. Update the `final` stage to copy dependencies from the new `prod-deps` stage.

The following is the `Dockerfile` before and after the changes.

Update your `compose.yaml` file by adding an instruction to target the development stage.

The following is the updated section of the `compose.yaml` file.

Your containerized application will now install the dev dependencies.

Run the following command to start your application.

Open a browser and view the application at [http://localhost:9000/hello.php](http://localhost:9000/hello.php). You should still see the simple "Hello, Docker!" application.

Press `ctrl+c` in the terminal to stop your application.

While the application appears the same, you can now make use of the dev dependencies. Continue to the next section to learn how you can run tests using Docker.

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically sync your application when you update your code. And finally, you learned how to create a development container that contains the dependencies needed for development.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Official Docker Image for PHP](https://hub.docker.com/_/php)

In the next section, you'll learn how to run unit tests using Docker.