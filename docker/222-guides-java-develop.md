---
title: Develop your app
url: https://docs.docker.com/guides/java/develop/
source: llms
fetched_at: 2026-01-24T14:10:35.160805889-03:00
rendered_js: false
word_count: 1066
summary: This guide explains how to set up a local Java development environment using Docker, covering database integration, remote debugging, and automatic code reloading with Compose Watch.
tags:
    - java
    - docker
    - docker-compose
    - debugging
    - development-environment
    - compose-watch
    - multi-stage-build
category: tutorial
---

## Use containers for Java development

Work through the steps to containerize your application in [Containerize your app](https://docs.docker.com/guides/java/containerize/).

In this section, you’ll walk through setting up a local development environment for the application you containerized in the previous section. This includes:

- Adding a local database and persisting data
- Creating a development container to connect a debugger
- Configuring Compose to automatically update your running Compose services as you edit and save your code

You can use containers to set up local services, like a database. In this section, you'll update the `docker-compose.yaml` file to define a database service and a volume to persist data. Also, this particular application uses a system property to define the database type, so you'll need to update the `Dockerfile` to pass in the system property when starting the app.

In the cloned repository's directory, open the `docker-compose.yaml` file in an IDE or text editor. Your Compose file has an example database service, but it'll require a few changes for your unique app.

In the `docker-compose.yaml` file, you need to do the following:

- Uncomment all of the database instructions. You'll now use a database service instead of local storage for the data.
- Remove the top-level `secrets` element as well as the element inside the `db` service. This example uses the environment variable for the password rather than secrets.
- Remove the `user` element from the `db` service. This example specifies the user in the environment variable.
- Update the database environment variables. These are defined by the Postgres image. For more details, see the [Postgres Official Docker Image](https://hub.docker.com/_/postgres).
- Update the healthcheck test for the `db` service and specify the user. By default, the healthcheck uses the root user instead of the `petclinic` user you defined.
- Add the database URL as an environment variable in the `server` service. This overrides the default value defined in `spring-petclinic/src/main/resources/application-postgres.properties`.

The following is the updated `docker-compose.yaml` file. All comments have been removed.

Open the `Dockerfile` in an IDE or text editor. In the `ENTRYPOINT` instruction, update the instruction to pass in the system property as specified in the `spring-petclinic/src/resources/db/postgres/petclinic_db_setup_postgres.txt` file.

Save and close all the files.

Now, run the following `docker compose up` command to start your application.

Open a browser and view the application at [http://localhost:8080](http://localhost:8080). You should see a simple app for a pet clinic. Browse around the application. Navigate to **Veterinarians** and verify that the application is connected to the database by being able to list veterinarians.

In the terminal, press `ctrl`+`c` to stop the application.

The Dockerfile you have now is great for a small, secure production image with only the components necessary to run the application. When developing, you may want a different image that has a different environment.

For example, in the development image you may want to set up the image to start the application so that you can connect a debugger to the running Java process.

Rather than managing multiple Dockerfiles, you can add a new stage. Your Dockerfile can then produce a final image which is ready for production as well as a development image.

Replace the contents of your Dockerfile with the following.

Save and close the `Dockerfile`.

In the `Dockerfile` you added a new stage labeled `development` based on the `extract` stage. In this stage, you copy the extracted files to a common directory, then run a command to start the application. In the command, you expose port 8000 and declare the debug configuration for the JVM so that you can attach a debugger.

The current Compose file doesn't start your development container. To do that, you must update your Compose file to target the development stage. Also, update the port mapping of the server service to provide access for the debugger.

Open the `docker-compose.yaml` and add the following instructions into the file.

Now, start your application and to confirm that it's running.

Finally, test your API endpoint. Run the following curl command:

You should receive the following response:

You’ll use the debugger that comes with the IntelliJ IDEA. You can use the community version of this IDE. Open your project in IntelliJ IDEA, go to the **Run** menu, and then **Edit Configuration**. Add a new Remote JVM Debug configuration similar to the following:

![Java Connect a Debugger](https://docs.docker.com/guides/java/images/connect-debugger.webp)

![Java Connect a Debugger](https://docs.docker.com/guides/java/images/connect-debugger.webp)

Set a breakpoint.

Open `src/main/java/org/springframework/samples/petclinic/vet/VetController.java` and add a breakpoint inside the `showResourcesVetList` function.

To start your debug session, select the **Run** menu and then **Debug *NameOfYourConfiguration***.

![Debug menu](https://docs.docker.com/guides/java/images/debug-menu.webp)

![Debug menu](https://docs.docker.com/guides/java/images/debug-menu.webp)

You should now see the connection in the logs of your Compose application.

![Compose log file ](https://docs.docker.com/guides/java/images/compose-logs.webp)

![Compose log file ](https://docs.docker.com/guides/java/images/compose-logs.webp)

You can now call the server endpoint.

You should have seen the code break on the marked line and now you are able to use the debugger just like you would normally. You can also inspect and watch variables, set conditional breakpoints, view stack traces and a do bunch of other stuff.

![Debugger code breakpoint](https://docs.docker.com/guides/java/images/debugger-breakpoint.webp)

![Debugger code breakpoint](https://docs.docker.com/guides/java/images/debugger-breakpoint.webp)

Press `ctrl+c` in the terminal to stop your application.

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `docker-compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `docker-compose.yaml` file.

Run the following command to run your application with Compose Watch.

Open a web browser and view the application at [http://localhost:8080](http://localhost:8080). You should see the Spring Pet Clinic home page.

Any changes to the application's source files on your local machine will now be automatically reflected in the running container.

Open `spring-petclinic/src/main/resources/templates/fragments/layout.html` in an IDE or text editor and update the `Home` navigation string by adding an exclamation mark.

Save the changes to `layout.html` and then you can continue developing while the container automatically rebuilds.

After the container is rebuilt and running, refresh [http://localhost:8080](http://localhost:8080) and then verify that **Home!** now appears in the menu.

Press `ctrl+c` in the terminal to stop Compose Watch.

In this section, you took a look at running a database locally and persisting the data. You also created a development image that contains the JDK and lets you attach a debugger. Finally, you set up your Compose file to expose the debugging port and configured Compose Watch to live reload your changes.

Related information:

- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

In the next section, you’ll take a look at how to run unit tests in Docker.