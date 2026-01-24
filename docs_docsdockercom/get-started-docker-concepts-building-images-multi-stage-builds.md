---
title: Multi-stage builds
url: https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/
source: llms
fetched_at: 2026-01-24T14:07:06.087759608-03:00
rendered_js: false
word_count: 1332
summary: This document explains the concept and implementation of Docker multi-stage builds to create optimized, smaller, and more secure container images. It provides a step-by-step approach to separating build-time dependencies from the final runtime environment.
tags:
    - docker
    - multi-stage-builds
    - container-optimization
    - dockerfile
    - image-security
    - java-development
category: guide
---

In a traditional build, all build instructions are executed in sequence, and in a single build container: downloading dependencies, compiling code, and packaging the application. All those layers end up in your final image. This approach works, but it leads to bulky images carrying unnecessary weight and increasing your security risks. This is where multi-stage builds come in.

Multi-stage builds introduce multiple stages in your Dockerfile, each with a specific purpose. Think of it like the ability to run different parts of a build in multiple different environments, concurrently. By separating the build environment from the final runtime environment, you can significantly reduce the image size and attack surface. This is especially beneficial for applications with large build dependencies.

Multi-stage builds are recommended for all types of applications.

- For interpreted languages, like JavaScript or Ruby or Python, you can build and minify your code in one stage, and copy the production-ready files to a smaller runtime image. This optimizes your image for deployment.
- For compiled languages, like C or Go or Rust, multi-stage builds let you compile in one stage and copy the compiled binaries into a final runtime image. No need to bundle the entire compiler in your final image.

Here's a simplified example of a multi-stage build structure using pseudo-code. Notice there are multiple `FROM` statements and a new `AS <stage-name>`. In addition, the `COPY` statement in the second stage is copying `--from` the previous stage.

This Dockerfile uses two stages:

- The build stage uses a base image containing build tools needed to compile your application. It includes commands to install build tools, copy source code, and execute build commands.
- The final stage uses a smaller base image suitable for running your application. It copies the compiled artifacts (a JAR file, for example) from the build stage. Finally, it defines the runtime configuration (using `CMD` or `ENTRYPOINT`) for starting your application.

In this hands-on guide, you'll unlock the power of multi-stage builds to create lean and efficient Docker images for a sample Java application. You'll use a simple “Hello World” Spring Boot-based application built with Maven as your example.

1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.
2. Open this [pre-initialized project](https://start.spring.io/#!type=maven-project&language=java&platformVersion=4.0.1&packaging=jar&configurationFileFormat=properties&jvmVersion=21&groupId=com.example&artifactId=spring-boot-docker&name=spring-boot-docker&description=Demo%20project%20for%20Spring%20Boot&packageName=com.example.spring-boot-docker&dependencies=web) to generate a ZIP file. Here’s how that looks:
   
   ![A screenshot of Spring Initializr tool selected with Java 21, Spring Web and Spring Boot 3.4.0](https://docs.docker.com/get-started/docker-concepts/building-images/images/multi-stage-builds-spring-initializer.webp)
   
   ![A screenshot of Spring Initializr tool selected with Java 21, Spring Web and Spring Boot 3.4.0](https://docs.docker.com/get-started/docker-concepts/building-images/images/multi-stage-builds-spring-initializer.webp)
   
   [Spring Initializr](https://start.spring.io/) is a quickstart generator for Spring projects. It provides an extensible API to generate JVM-based projects with implementations for several common concepts — like basic language generation for Java, Kotlin, Groovy, and Maven.
   
   Select **Generate** to create and download the zip file for this project.
   
   For this demonstration, you’ve paired Maven build automation with Java, a Spring Web dependency, and Java 21 for your metadata.
3. Navigate the project directory. Once you unzip the file, you'll see the following project directory structure:
   
   The `src/main/java` directory contains your project's source code, the `src/test/java` directory  
   contains the test source, and the `pom.xml` file is your project’s Project Object Model (POM).
   
   The `pom.xml` file is the core of a Maven project's configuration. It's a single configuration file that  
   contains most of the information needed to build a customized project. The POM is huge and can seem  
   daunting. Thankfully, you don't yet need to understand every intricacy to use it effectively.
4. Create a RESTful web service that displays "Hello World!".
   
   Under the `src/main/java/com/example/spring_boot_docker/` directory, you can modify your  
   `SpringBootDockerApplication.java` file with the following content:
   
   The `SpringbootDockerApplication.java` file starts by declaring your `com.example.spring_boot_docker` package and importing necessary Spring frameworks. This Java file creates a simple Spring Boot web application that responds with "Hello World" when a user visits its homepage.

### [Create the Dockerfile](#create-the-dockerfile)

Now that you have the project, you’re ready to create the `Dockerfile`.

1. Create a file named `Dockerfile` in the same folder that contains all the other folders and files (like src, pom.xml, etc.).
2. In the `Dockerfile`, define your base image by adding the following line:
3. Now, define the working directory by using the `WORKDIR` instruction. This will specify where future commands will run and the directory files will be copied inside the container image.
4. Copy both the Maven wrapper script and your project's `pom.xml` file into the current working directory `/app` within the Docker container.
5. Execute a command within the container. It runs the `./mvnw dependency:go-offline` command, which uses the Maven wrapper (`./mvnw`) to download all dependencies for your project without building the final JAR file (useful for faster builds).
6. Copy the `src` directory from your project on the host machine to the `/app` directory within the container.
7. Set the default command to be executed when the container starts. This command instructs the container to run the Maven wrapper (`./mvnw`) with the `spring-boot:run` goal, which will build and execute your Spring Boot application.
   
   And with that, you should have the following Dockerfile:

### [Build the container image](#build-the-container-image)

1. Execute the following command to build the Docker image:
2. Check the size of the Docker image by using the `docker images` command:
   
   Doing so will produce output like the following:
   
   This output shows that your image is 880MB in size. It contains the full JDK, Maven toolchain, and more. In production, you don’t need that in your final image.

### [Run the Spring Boot application](#run-the-spring-boot-application)

1. Now that you have an image built, it's time to run the container.
   
   You'll then see output similar to the following in the container log:
2. Access your “Hello World” page through your web browser at [http://localhost:8080](http://localhost:8080), or via this curl command:

### [Use multi-stage builds](#use-multi-stage-builds)

1. Consider the following Dockerfile:
   
   Notice that this Dockerfile has been split into two stages.
   
   - The first stage remains the same as the previous Dockerfile, providing a Java Development Kit (JDK) environment for building the application. This stage is given the name of builder.
   - The second stage is a new stage named `final`. It uses a slimmer `eclipse-temurin:21.0.2_13-jre-jammy` image, containing just the Java Runtime Environment (JRE) needed to run the application. This image provides a Java Runtime Environment (JRE) which is enough for running the compiled application (JAR file).
   
   > For production use, it's highly recommended that you produce a custom JRE-like runtime using jlink. JRE images are available for all versions of Eclipse Temurin, but `jlink` allows you to create a minimal runtime containing only the necessary Java modules for your application. This can significantly reduce the size and improve the security of your final image. [Refer to this page](https://hub.docker.com/_/eclipse-temurin) for more information.
   
   With multi-stage builds, a Docker build uses one base image for compilation, packaging, and unit tests and then a separate image for the application runtime. As a result, the final image is smaller in size since it doesn’t contain any development or debugging tools. By separating the build environment from the final runtime environment, you can significantly reduce the image size and increase the security of your final images.
2. Now, rebuild your image and run your ready-to-use production build.
   
   This command builds a Docker image named `spring-helloworld-builder` using the final stage from your `Dockerfile` file located in the current directory.
   
   > In your multi-stage Dockerfile, the final stage (final) is the default target for building. This means that if you don't explicitly specify a target stage using the `--target` flag in the `docker build` command, Docker will automatically build the last stage by default. You could use `docker build -t spring-helloworld-builder --target builder .` to build only the builder stage with the JDK environment.
3. Look at the image size difference by using the `docker images` command:
   
   You'll get output similar to the following:
   
   Your final image is just 428 MB, compared to the original build size of 880 MB.
   
   By optimizing each stage and only including what's necessary, you were able to significantly reduce the overall image size while still achieving the same functionality. This not only improves performance but also makes your Docker images more lightweight, more secure, and easier to manage.

<!--THE END-->

- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Base images](https://docs.docker.com/build/building/base-images/)
- [Spring Boot Docker](https://spring.io/guides/topicals/spring-boot-docker)