---
title: Visualizing your PostgreSQL databases with pgAdmin
url: https://docs.docker.com/guides/pgadmin/
source: llms
fetched_at: 2026-01-24T14:11:04.115466592-03:00
rendered_js: false
word_count: 528
summary: This guide explains how to integrate pgAdmin into a Docker Compose application stack and configure it to automatically connect to a PostgreSQL database for easier administration.
tags:
    - docker-compose
    - postgresql
    - pgadmin
    - database-administration
    - containerization
    - local-development
category: guide
---

Many applications use PostgreSQL databases in the application stack. However, not all developers are knowledgeable about navigating and working with PostgreSQL databases.

Fortunately, when you use containers in development, it is easy to add additional services to help with troubleshooting and debugging.

The [pgAdmin](https://www.pgadmin.org/) tool is a popular open-source tool designed to help administer and visualize PostgreSQL databases.

In this guide you will learn how to:

1. Add pgAdmin to your application stack
2. Configure pgAdmin to automatically connect to the development database

<!--THE END-->

1. In your `compose.yaml` file, add the `pgadmin` service next to your existing `postgres` service:
2. Start the Compose stack with the following command:
   
   After the image is downloaded the container starts, you will see output that looks similar to the following indicating pgAdmin is ready:
3. Open pgAdmin by going to http://localhost:5050.
4. Once in the admin panel, select the **Add New Server** link to define a new server. Enter the following details:
   
   - **General** tab:
     
     - **Name**: `postgres`
   - **Connection** tab:
     
     - **Host name/address**: `postgres`
     - **Username**: `postgres`
     - **Password**: `secret`
     - Enable the **Save password?** field
   
   > These connection details assume you are using the previous Compose file snippet. If you are using an existing Compose file, adjust the connection details as required. The **Host name/address** field should match the name of your postgres service.
5. Select the **Save** button to create the new database.

You now have pgAdmin setup and connected to your containerized database. Feel free to navigate around, view the tables, and explore your database.

Although you have pgAdmin running, it would be nice if you could simply open the app without needing to configure the database connection. Reducing the setup steps would be a great way to make it easier for teammates to get value from this tool.

Fortunately, there is an ability to auto-connect to the database.

> In order to auto-connect, the database credentials are shared using plaintext files. During local development, this is often acceptable as local data is not real customer data. However, if you are using production or sensitive data, this practice is strongly discouraged.

1. First, you need to define the server itself, which pgAdmin does using a `servers.json` file.
   
   Add the following to your `compose.yaml` file to define a config file for the `servers.json` file:
2. The `servers.json` file defines a `PassFile` field, which is a reference to a [postgreSQL password files](https://www.postgresql.org/docs/current/libpq-pgpass.html). These are often referred to as a pgpass file.
   
   Add the following config to your `compose.yaml` file to define a pgpass file:
   
   This will indicate any connection requests to `postgres:5432` using the username `postgres` should provide a password of `secret`.
3. In your `compose.yaml`, update the `pgadmin` service to inject the config files:
4. Update the application stack by running `docker compose up` again:
5. Once the application is restarted, open your browser to http://localhost:5050. You should be able to access the database without any logging in or configuration.

Using containers makes it easy to not only run your application's dependencies, but also additional tools to help with troubleshooting and debugging.

When you add tools, think about the experience and possible friction your teammates might experience and how you might be able to remove it. In this case, you were able to take an extra step to add configuration to automatically configure and connect the databases, saving your teammates valuable time.