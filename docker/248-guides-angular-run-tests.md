---
title: Run your tests
url: https://docs.docker.com/guides/angular/run-tests/
source: llms
fetched_at: 2026-01-24T14:08:31.337107687-03:00
rendered_js: false
word_count: 436
summary: This document provides instructions on how to configure and run Angular unit tests inside a Docker container using Docker Compose for consistent and isolated testing environments.
tags:
    - angular
    - docker
    - docker-compose
    - unit-testing
    - jasmine
    - containerization
    - dev-environment
category: guide
---

## Run Angular tests in a container

Table of contents

* * *

## [Prerequisites](#prerequisites)

Complete all the previous sections of this guide, starting with [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).

## [Overview](#overview)

Testing is a critical part of the development process. In this section, you'll learn how to:

- Run Jasmine unit tests using the Angular CLI inside a Docker container.
- Use Docker Compose to isolate your test environment.
- Ensure consistency between local and container-based testing.

The `docker-angular-sample` project comes pre-configured with Jasmine, so you can get started quickly without extra setup.

* * *

## [Run tests during development](#run-tests-during-development)

The `docker-angular-sample` application includes a sample test file at the following location:

```
$ src/app/app.component.spec.ts
```

This test uses Jasmine to validate the AppComponent logic.

### [Step 1: Update compose.yaml](#step-1-update-composeyaml)

Add a new service named `angular-test` to your `compose.yaml` file. This service allows you to run your test suite in an isolated, containerized environment.

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
services:angular-dev:build:context:.dockerfile:Dockerfile.devports:- "5173:5173"develop:watch:- action:syncpath:.target:/appangular-prod:build:context:.dockerfile:Dockerfileimage:docker-angular-sampleports:- "8080:8080"angular-test:build:context:.dockerfile:Dockerfile.devcommand:["npm","run","test"]
```

The angular-test service reuses the same `Dockerfile.dev` used for [development](https://docs.docker.com/guides/angular/develop/) and overrides the default command to run tests with `npm run test`. This setup ensures a consistent test environment that matches your local development configuration.

After completing the previous steps, your project directory should contain the following files:

```
├── docker-angular-sample/
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
$ docker compose run --rm angular-test
```

This command will:

- Start the `angular-test` service defined in your `compose.yaml` file.
- Execute the `npm run test` script using the same environment as development.
- Automatically removes the container after tests complete, using the [`docker compose run --rm`](https://docs.docker.com/engine/reference/commandline/compose_run) command.

You should see output similar to the following:

```
Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        1.529 s
```

> Note

* * *

## [Summary](#summary)

In this section, you learned how to run unit tests for your Angular application inside a Docker container using Jasmine and Docker Compose.

What you accomplished:

- Created a `angular-test` service in `compose.yaml` to isolate test execution.
- Reused the development `Dockerfile.dev` to ensure consistency between dev and test environments.
- Ran tests inside the container using `docker compose run --rm angular-test`.
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

Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions to automatically build and test your Angular application in a containerized environment. This ensures your code is validated on every push or pull request, maintaining consistency and reliability across your development workflow.