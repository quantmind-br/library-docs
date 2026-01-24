---
title: Develop your app
url: https://docs.docker.com/guides/ruby/develop/
source: llms
fetched_at: 2026-01-24T14:11:51.378910983-03:00
rendered_js: false
word_count: 564
summary: This document explains how to set up a containerized Ruby on Rails development environment using Docker Compose, focusing on database persistence and automatic code updates with Compose Watch.
tags:
    - ruby-on-rails
    - docker-compose
    - development-environment
    - database-persistence
    - compose-watch
category: guide
---

## Use containers for Ruby on Rails development

Complete [Containerize a Ruby on Rails application](https://docs.docker.com/guides/ruby/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring Compose to automatically update your running Compose services as you edit and save your code

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor. You need to add the database password file as an environment variable to the server service and specify the secret file to use.

The following is the updated `compose.yaml` file.

> To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.

Save and close the `password.txt` file. In addition, in the file `webapp.env` you can change the password to connect to the database.

You should now have the following contents in your `docker-ruby-on-rails` directory.

Now, run the following `docker compose up` command to start your application.

In Ruby on Rails, `db:migrate` is a Rake task that is used to run migrations on the database. Migrations are a way to alter the structure of your database schema over time in a consistent and easy way.

You will see a similar message like this:

`console == 20240710193146 CreateWhales: migrating ===================================== -- create_table(:whales) -> 0.0126s == 20240710193146 CreateWhales: migrated (0.0127s) ============================`

Refresh [http://localhost:3000](http://localhost:3000) in your browser and add the whales.

Press `ctrl+c` in the terminal to stop your application and run `docker compose up` again, the whales are being persisted.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.

Run the following command to run your application with Compose Watch.

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `docker-ruby-on-rails/app/views/whales/index.html.erb` in an IDE or text editor and update the `Whales` string by adding an exclamation mark.

Save the changes to `index.html.erb` and then wait a few seconds for the application to rebuild. Go to the application again and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop your application.

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

In the next section, you'll learn how you can locally test and debug your workloads on Kubernetes before deploying.