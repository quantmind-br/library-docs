---
title: Run your tests
url: https://docs.docker.com/guides/vuejs/run-tests/
source: llms
fetched_at: 2026-01-24T14:12:36.751101555-03:00
rendered_js: false
word_count: 466
summary: This guide explains how to configure and execute Vue.js unit tests using Vitest and Docker Compose within a containerized environment. It demonstrates how to isolate test execution to ensure consistency between development and testing workflows.
tags:
    - docker
    - vuejs
    - vitest
    - docker-compose
    - unit-testing
    - containerization
category: guide
---

## Run vue.js tests in a container

Table of contents

* * *

## [Prerequisites](#prerequisites)

Complete all the previous sections of this guide, starting with [Containerize Vue.js application](https://docs.docker.com/guides/vuejs/containerize/).

## [Overview](#overview)

Testing is a critical part of the development process. In this section, you'll learn how to:

- Run unit tests using Vitest inside a Docker container.
- Use Docker Compose to run tests in an isolated, reproducible environment.

You’ll use [Vitest](https://vitest.dev) — a blazing fast test runner designed for Vite — together with [@vue/test-utils](https://test-utils.vuejs.org/) to write unit tests that validate your component logic, props, events, and reactive behavior.

This setup ensures your Vue.js components are tested in an environment that mirrors how users actually interact with your application.

* * *

## [Run tests during development](#run-tests-during-development)

`docker-vuejs-sample` application includes a sample test file at location:

```
$ src/components/__tests__/HelloWorld.spec.ts
```

This test uses Vitest and Vue Test Utils to verify the behavior of the HelloWorld component.

* * *

### [Step 1: Update compose.yaml](#step-1-update-composeyaml)

Add a new service named `vuejs-test` to your `compose.yaml` file. This service allows you to run your test suite in an isolated containerized environment.

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
```

```
services:vuejs-prod:build:context:.dockerfile:Dockerfileimage:docker-vuejs-sampleports:- "8080:8080"vuejs-dev:build:context:.dockerfile:Dockerfile.devports:- "5173:5173"develop:watch:- action:syncpath:.target:/appvuejs-test:build:context:.dockerfile:Dockerfile.devcommand:["npm","run","test:unit"]
```

The vuejs-test service reuses the same `Dockerfile.dev` used for [development](https://docs.docker.com/guides/vuejs/develop/) and overrides the default command to run tests with `npm run test`. This setup ensures a consistent test environment that matches your local development configuration.

After completing the previous steps, your project directory should contain the following files:

```
├── docker-vuejs-sample/
│ ├── Dockerfile
│ ├── Dockerfile.dev
│ ├── .dockerignore
│ ├── compose.yaml
│ ├── nginx.conf
│ └── README.Docker.md
```

### [Step 2: Run the tests](#step-2-run-the-tests)

To execute your test suite inside the container, run the following command from your project root:

```
$ docker compose run --rm vuejs-test
```

This command will:

- Start the `vuejs-test` service defined in your `compose.yaml` file.
- Execute the `npm run test` script using the same environment as development.
- Automatically remove the container after the tests complete [`docker compose run --rm`](https://docs.docker.com/engine/reference/commandline/compose_run) command.

You should see output similar to the following:

```
Test Files: 1 passed (1)
Tests:      1 passed (1)
Start at:   16:50:55
Duration:   718ms
```

> Note

* * *

## [Summary](#summary)

In this section, you learned how to run unit tests for your Vue.js application inside a Docker container using Vitest and Docker Compose.

What you accomplished:

- Created a `vuejs-test` service in `compose.yaml` to isolate test execution.
- Reused the development `Dockerfile.dev` to ensure consistency between dev and test environments.
- Ran tests inside the container using `docker compose run --rm vuejs-test`.
- Ensured reliable, repeatable testing across environments without depending on your local machine setup.

* * *

## [Related resources](#related-resources)

Explore official references and best practices to sharpen your Docker testing workflow:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) – Understand all Dockerfile instructions and syntax.
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) – Write efficient, maintainable, and secure Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [`docker compose run` CLI reference](https://docs.docker.com/reference/cli/docker/compose/run/) – Run one-off commands in a service container.

* * *

## [Next steps](#next-steps)

Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions to automatically build and test your Vue.js application in a containerized environment. This ensures your code is validated on every push or pull request, maintaining consistency and reliability across your development workflow.