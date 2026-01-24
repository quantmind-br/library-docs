---
title: Run your tests
url: https://docs.docker.com/guides/reactjs/run-tests/
source: llms
fetched_at: 2026-01-24T14:11:40.827474084-03:00
rendered_js: false
word_count: 547
summary: This guide explains how to configure and run unit tests for a React.js application inside a Docker container using Vitest and Docker Compose. It covers installing testing tools, configuring the Vitest environment, and setting up a dedicated test service for isolated execution.
tags:
    - docker-compose
    - react-js
    - vitest
    - unit-testing
    - containerization
    - software-testing
category: tutorial
---

## Run React.js tests in a container

Table of contents

* * *

## [Prerequisites](#prerequisites)

Complete all the previous sections of this guide, starting with [Containerize React.js application](https://docs.docker.com/guides/reactjs/containerize/).

## [Overview](#overview)

Testing is a critical part of the development process. In this section, you'll learn how to:

- Run unit tests using Vitest inside a Docker container.
- Use Docker Compose to run tests in an isolated, reproducible environment.

You’ll use [Vitest](https://vitest.dev) — a blazing fast test runner designed for Vite — along with [Testing Library](https://testing-library.com/) for assertions.

* * *

## [Run tests during development](#run-tests-during-development)

`docker-reactjs-sample` application includes a sample test file at location:

This file uses Vitest and React Testing Library to verify the behavior of `App` component.

### [Step 1: Install Vitest and React Testing Library](#step-1-install-vitest-and-react-testing-library)

If you haven’t already added the necessary testing tools, install them by running:

```
$ npm install --save-dev vitest @testing-library/react @testing-library/jest-dom jsdom
```

Then, update the scripts section of your `package.json` file to include the following:

```
"scripts": {
  "test": "vitest run"
}
```

* * *

### [Step 2: Configure Vitest](#step-2-configure-vitest)

Update `vitest.config.ts` file in your project root with the following configuration:

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
```

```
/// <reference types="vitest" />
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({
  base: "/",
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
    strictPort: true,
  },
  test: {
    environment: "jsdom",
    setupFiles: "./src/setupTests.ts",
    globals: true,
  },
});
```

> Note
> 
> The `test` options in `vitest.config.ts` are essential for reliable testing inside Docker:
> 
> - `environment: "jsdom"` simulates a browser-like environment for rendering and DOM interactions.
> - `setupFiles: "./src/setupTests.ts"` loads global configuration or mocks before each test file (optional but recommended).
> - `globals: true` enables global test functions like `describe`, `it`, and `expect` without importing them.
> 
> For more details, see the official [Vitest configuration docs](https://vitest.dev/config/).

### [Step 3: Update compose.yaml](#step-3-update-composeyaml)

Add a new service named `react-test` to your `compose.yaml` file. This service allows you to run your test suite in an isolated containerized environment.

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
services:react-dev:build:context:.dockerfile:Dockerfile.devports:- "5173:5173"develop:watch:- action:syncpath:.target:/appreact-prod:build:context:.dockerfile:Dockerfileimage:docker-reactjs-sampleports:- "8080:8080"react-test:build:context:.dockerfile:Dockerfile.devcommand:["npm","run","test"]
```

The react-test service reuses the same `Dockerfile.dev` used for [development](https://docs.docker.com/guides/reactjs/develop/) and overrides the default command to run tests with `npm run test`. This setup ensures a consistent test environment that matches your local development configuration.

After completing the previous steps, your project directory should contain the following files:

```
├── docker-reactjs-sample/
│ ├── Dockerfile
│ ├── Dockerfile.dev
│ ├── .dockerignore
│ ├── compose.yaml
│ ├── nginx.conf
│ └── README.Docker.md
```

### [Step 4: Run the tests](#step-4-run-the-tests)

To execute your test suite inside the container, run the following command from your project root:

```
$ docker compose run --rm react-test
```

This command will:

- Start the `react-test` service defined in your `compose.yaml` file.
- Execute the `npm run test` script using the same environment as development.
- Automatically remove the container after the tests complete [`docker compose run --rm`](https://docs.docker.com/engine/reference/commandline/compose_run) command.

> Note

* * *

## [Summary](#summary)

In this section, you learned how to run unit tests for your React.js application inside a Docker container using Vitest and Docker Compose.

What you accomplished:

- Installed and configured Vitest and React Testing Library for testing React components.
- Created a `react-test` service in `compose.yaml` to isolate test execution.
- Reused the development `Dockerfile.dev` to ensure consistency between dev and test environments.
- Ran tests inside the container using `docker compose run --rm react-test`.
- Ensured reliable, repeatable testing across environments without relying on local machine setup.

* * *

## [Related resources](#related-resources)

Explore official references and best practices to sharpen your Docker testing workflow:

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) – Understand all Dockerfile instructions and syntax.
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) – Write efficient, maintainable, and secure Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [`docker compose run` CLI reference](https://docs.docker.com/reference/cli/docker/compose/run/) – Run one-off commands in a service container.

* * *

## [Next steps](#next-steps)

Next, you’ll learn how to set up a CI/CD pipeline using GitHub Actions to automatically build and test your React.js application in a containerized environment. This ensures your code is validated on every push or pull request, maintaining consistency and reliability across your development workflow.