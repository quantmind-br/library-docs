---
title: Run your tests
url: https://docs.docker.com/guides/nodejs/run-tests/
source: llms
fetched_at: 2026-01-24T14:11:01.377839348-03:00
rendered_js: false
word_count: 518
summary: This guide explains how to configure and run Node.js tests within Docker containers using Docker Compose and multi-stage Dockerfiles. It covers executing unit, integration, and coverage tests in both local development and CI/CD environments.
tags:
    - node-js
    - docker-compose
    - multi-stage-build
    - unit-testing
    - vitest
    - continuous-integration
category: guide
---

## Run Node.js tests in a container

Complete all the previous sections of this guide, starting with [Containerize a Node.js application](https://docs.docker.com/guides/nodejs/containerize/).

Testing is a core part of building reliable software. Whether you're writing unit tests, integration tests, or end-to-end tests, running them consistently across environments matters. Docker makes this easy by giving you the same setup locally, in CI/CD, and during image builds.

The sample application uses Vitest for testing, and it already includes tests for React components, custom hooks, API routes, database operations, and utility functions.

### [Run tests locally (without Docker)](#run-tests-locally-without-docker)

### [Add test service to Docker Compose](#add-test-service-to-docker-compose)

To run tests in a containerized environment, you need to add a dedicated test service to your `compose.yml` file. Add the following service configuration:

This test service configuration:

- **Builds from test stage**: Uses the `test` target from your multi-stage Dockerfile
- **Isolated test database**: Uses a separate `todoapp_test` database for testing
- **Profile-based**: Uses the `test` profile so it only runs when explicitly requested
- **Health dependency**: Waits for the database to be healthy before starting tests

### [Run tests in a container](#run-tests-in-a-container)

You can run tests using the dedicated test service:

Or run tests against the development service:

For a one-off test run with coverage:

### [Run tests with coverage](#run-tests-with-coverage)

To generate a coverage report:

You should see output like the following:

### [Test structure](#test-structure)

The test suite covers:

- **Client Components** (`src/client/components/__tests__/`): React component testing with React Testing Library
- **Custom Hooks** (`src/client/hooks/__tests__/`): React hooks testing with proper mocking
- **Server Routes** (`src/server/__tests__/routes/`): API endpoint testing
- **Database Layer** (`src/server/database/__tests__/`): PostgreSQL database operations testing
- **Utility Functions** (`src/shared/utils/__tests__/`): Validation and helper function testing
- **Integration Tests** (`src/client/__tests__/`): Full application integration testing

To run tests during the Docker build process, you need to add a dedicated test stage to your Dockerfile. If you haven't already added this stage, add the following to your multi-stage Dockerfile:

This test stage:

- **Test environment**: Sets `NODE_ENV=test` and `CI=true` for proper test execution
- **Non-root user**: Runs tests as the `nodejs` user for security
- **Flexible execution**: Uses `CMD` instead of `RUN` to allow running tests during build or as a separate container
- **Coverage support**: Configured to run tests with coverage reporting

### [Build and run tests during image build](#build-and-run-tests-during-image-build)

To build an image that runs tests during the build process, you can create a custom Dockerfile or modify the existing one temporarily:

### [Run tests in a dedicated test container](#run-tests-in-a-dedicated-test-container)

The recommended approach is to use the test service defined in `compose.yml`:

Or run it as a one-off container:

### [Run tests with coverage in CI/CD](#run-tests-with-coverage-in-cicd)

For continuous integration, you can run tests with coverage:

You should see output containing the following:

In this section, you learned how to run tests when developing locally using Docker Compose and how to run tests when building your image.

Related information:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) – Understand all Dockerfile instructions and syntax.
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) – Write efficient, maintainable, and secure Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [`docker compose run` CLI reference](https://docs.docker.com/reference/cli/docker/compose/run/) – Run one-off commands in a service container.

Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions.