---
title: 'Part 6: Multi-container apps'
url: https://docs.docker.com/get-started/workshop/07_multi_container/
source: llms
fetched_at: 2026-01-24T14:08:03.042549238-03:00
rendered_js: false
word_count: 1144
summary: This document explains how to architecture and connect a multi-container application by running a MySQL database separately and establishing communication via Docker networking.
tags:
    - docker
    - container-networking
    - multi-container
    - mysql
    - service-discovery
    - environment-variables
category: tutorial
---

Up to this point, you've been working with single container apps. But, now you will add MySQL to the application stack. The following question often arises - "Where will MySQL run? Install it in the same container or run it separately?" In general, each container should do one thing and do it well. The following are a few reasons to run the container separately:

- There's a good chance you'd have to scale APIs and front-ends differently than databases.
- Separate containers let you version and update versions in isolation.
- While you may use a container for the database locally, you may want to use a managed service for the database in production. You don't want to ship your database engine with your app then.
- Running multiple processes will require a process manager (the container only starts one process), which adds complexity to container startup/shutdown.

And there are more reasons. So, like the following diagram, it's best to run your app in multiple containers.

![Todo App connected to MySQL container](https://docs.docker.com/get-started/workshop/images/multi-container.webp)

![Todo App connected to MySQL container](https://docs.docker.com/get-started/workshop/images/multi-container.webp)

Remember that containers, by default, run in isolation and don't know anything about other processes or containers on the same machine. So, how do you allow one container to talk to another? The answer is networking. If you place the two containers on the same network, they can talk to each other.

There are two ways to put a container on a network:

- Assign the network when starting the container.
- Connect an already running container to a network.

In the following steps, you'll create the network first and then attach the MySQL container at startup.

1. Create the network.
2. Start a MySQL container and attach it to the network. You're also going to define a few environment variables that the database will use to initialize the database. To learn more about the MySQL environment variables, see the "Environment Variables" section in the [MySQL Docker Hub listing](https://hub.docker.com/_/mysql/).
   
   In the previous command, you can see the `--network-alias` flag. In a later section, you'll learn more about this flag.
   
   > You'll notice a volume named `todo-mysql-data` in the above command that is mounted at `/var/lib/mysql`, which is where MySQL stores its data. However, you never ran a `docker volume create` command. Docker recognizes you want to use a named volume and creates one automatically for you.
3. To confirm you have the database up and running, connect to the database and verify that it connects.
   
   When the password prompt comes up, type in `secret`. In the MySQL shell, list the databases and verify you see the `todos` database.
   
   You should see output that looks like this:
4. Exit the MySQL shell to return to the shell on your machine.
   
   You now have a `todos` database and it's ready for you to use.

Now that you know MySQL is up and running, you can use it. But, how do you use it? If you run another container on the same network, how do you find the container? Remember that each container has its own IP address.

To answer the questions above and better understand container networking, you're going to make use of the [nicolaka/netshoot](https://github.com/nicolaka/netshoot) container, which ships with a lot of tools that are useful for troubleshooting or debugging networking issues.

1. Start a new container using the nicolaka/netshoot image. Make sure to connect it to the same network.
2. Inside the container, you're going to use the `dig` command, which is a useful DNS tool. You're going to look up the IP address for the hostname `mysql`.
   
   You should get output like the following.
   
   In the "ANSWER SECTION", you will see an `A` record for `mysql` that resolves to `172.23.0.2` (your IP address will most likely have a different value). While `mysql` isn't normally a valid hostname, Docker was able to resolve it to the IP address of the container that had that network alias. Remember, you used the `--network-alias` earlier.
   
   What this means is that your app only simply needs to connect to a host named `mysql` and it'll talk to the database.

The todo app supports the setting of a few environment variables to specify MySQL connection settings. They are:

- `MYSQL_HOST` - the hostname for the running MySQL server
- `MYSQL_USER` - the username to use for the connection
- `MYSQL_PASSWORD` - the password to use for the connection
- `MYSQL_DB` - the database to use once connected

> While using env vars to set connection settings is generally accepted for development, it's highly discouraged when running applications in production. Diogo Monica, a former lead of security at Docker, [wrote a fantastic blog post](https://blog.diogomonica.com/2017/03/27/why-you-shouldnt-use-env-variables-for-secret-data/) explaining why.
> 
> A more secure mechanism is to use the secret support provided by your container orchestration framework. In most cases, these secrets are mounted as files in the running container. You'll see many apps (including the MySQL image and the todo app) also support env vars with a `_FILE` suffix to point to a file containing the variable.
> 
> As an example, setting the `MYSQL_PASSWORD_FILE` var will cause the app to use the contents of the referenced file as the connection password. Docker doesn't do anything to support these env vars. Your app will need to know to look for the variable and get the file contents.

You can now start your dev-ready container.

1. Specify each of the previous environment variables, as well as connect the container to your app network. Make sure that you are in the `getting-started-app` directory when you run this command.
   
   In Windows, run this command in PowerShell.
   
   In Windows, run this command in Command Prompt.
2. If you look at the logs for the container (`docker logs -f <container-id>`), you should see a message similar to the following, which indicates it's using the mysql database.
3. Open the app in your browser and add a few items to your todo list.
4. Connect to the mysql database and prove that the items are being written to the database. Remember, the password is `secret`.
   
   And in the mysql shell, run the following:
   
   Your table will look different because it has your items. But, you should see them stored there.

At this point, you have an application that now stores its data in an external database running in a separate container. You learned a little bit about container networking and service discovery using DNS.

Related information:

- [docker CLI reference](https://docs.docker.com/reference/cli/docker/)
- [Networking overview](https://docs.docker.com/engine/network/)

There's a good chance you are starting to feel a little overwhelmed with everything you need to do to start up this application. You have to create a network, start containers, specify all of the environment variables, expose ports, and more. That's a lot to remember and it's certainly making things harder to pass along to someone else.

In the next section, you'll learn about Docker Compose. With Docker Compose, you can share your application stacks in a much easier way and let others spin them up with a single, simple command.

[Use Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/)