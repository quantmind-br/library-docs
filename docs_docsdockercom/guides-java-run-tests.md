---
title: Run your tests
url: https://docs.docker.com/guides/java/run-tests/
source: llms
fetched_at: 2026-01-24T14:10:36.639436983-03:00
rendered_js: false
word_count: 305
summary: This document explains how to integrate unit testing into a Java application's Docker build process using multi-stage Dockerfiles to ensure builds fail if tests do not pass.
tags:
    - docker
    - java
    - unit-testing
    - multi-stage-build
    - dockerfile
    - maven
    - containerization
category: guide
---

Complete all the previous sections of this guide, starting with [Containerize a Java application](https://docs.docker.com/guides/java/containerize/).

Testing is an essential part of modern software development. Testing can mean a lot of things to different development teams. There are unit tests, integration tests and end-to-end testing. In this guide you'll take a look at running your unit tests in Docker.

### [Multi-stage Dockerfile for testing](#multi-stage-dockerfile-for-testing)

In the following example, you'll pull the testing commands into your Dockerfile. Replace the contents of your Dockerfile with the following.

First, you added a new base stage. In the base stage, you added common instructions that both the test and deps stage will need.

Next, you added a new test stage labeled `test` based on the base stage. In this stage you copied in the necessary source files and then specified `RUN` to run `./mvnw test`. Instead of using `CMD`, you used `RUN` to run the tests. The reason is that the `CMD` instruction runs when the container runs, and the `RUN` instruction runs when the image is being built. When using `RUN`, the build will fail if the tests fail.

Finally, you updated the deps stage to be based on the base stage and removed the instructions that are now in the base stage.

Run the following command to build a new image using the test stage as the target and view the test results. Include `--progress=plain` to view the build output, `--no-cache` to ensure the tests always run, and `--target test` to target the test stage.

Now, build your image and run your tests. You'll run the `docker build` command and add the `--target test` flag so that you specifically run the test build stage.

You should see output containing the following

In the next section, you’ll take a look at how to set up a CI/CD pipeline using GitHub Actions.