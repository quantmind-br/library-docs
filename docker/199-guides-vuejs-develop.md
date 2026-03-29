---
title: Develop your app
url: https://docs.docker.com/guides/vuejs/develop/
source: llms
fetched_at: 2026-01-24T14:12:34.785336271-03:00
rendered_js: false
word_count: 559
summary: This document explains how to set up production and development environments for Vue.js applications using Docker Compose and Compose Watch for real-time file synchronization.
tags:
    - docker
    - vuejs
    - docker-compose
    - compose-watch
    - containerization
    - frontend-development
    - live-reload
category: tutorial
---

## Use containers for Vue.js development

Complete [Containerize Vue.js application](https://docs.docker.com/guides/vuejs/containerize/).

* * *

In this section, you'll set up both production and development environments for your Vue.js application using Docker Compose. This approach streamlines your workflow—delivering a lightweight, static site via Nginx in production, and providing a fast, live-reloading dev server with Compose Watch for efficient local development.

You’ll learn how to:

- Configure isolated environments: Set up separate containers optimized for production and development use cases.
- Live-reload in development: Use Compose Watch to automatically sync file changes, enabling real-time updates without manual intervention.
- Preview and debug with ease: Develop inside containers with a seamless preview and debug experience—no rebuilds required after every change.

* * *

Leverage Compose Watch to enable real-time file synchronization between your local machine and the containerized Vue.js development environment. This powerful feature eliminates the need to manually rebuild or restart containers, providing a fast, seamless, and efficient development workflow.

With Compose Watch, your code updates are instantly reflected inside the container—perfect for rapid testing, debugging, and live previewing changes.

Create a file named `Dockerfile.dev` in your project root with the following content:

This file sets up a lightweight development environment for your Vue.js application using the dev server.

### [Step 2: Update your `compose.yaml` file](#step-2-update-your-composeyaml-file)

Open your `compose.yaml` file and define two services: one for production (`vuejs-prod`) and one for development (`vuejs-dev`).

Here’s an example configuration for an Vue.js application:

- The `vuejs-prod` service builds and serves your static production app using Nginx.
- The `vuejs-dev` service runs your Vue.js development server with live reload and hot module replacement.
- `watch` triggers file sync with Compose Watch.

> For more details, see the official guide: [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

After completing the previous steps, your project directory should now contain the following files:

### [Step 4: Start Compose Watch](#step-4-start-compose-watch)

Run the following command from the project root to start the container in watch mode

### [Step 5: Test Compose Watch with Vue.js](#step-5-test-compose-watch-with-vuejs)

To confirm that Compose Watch is functioning correctly:

1. Open the `src/App.vue` file in your text editor.
2. Locate the following line:
3. Change it to:
4. Save the file.
5. Open your browser at [http://localhost:5173](http://localhost:5173).

You should see the updated text appear instantly, without needing to rebuild the container manually. This confirms that file watching and automatic synchronization are working as expected.

* * *

In this section, you set up a complete development and production workflow for your Vue.js application using Docker and Docker Compose.

Here’s what you accomplished:

- Created a `Dockerfile.dev` to streamline local development with hot reloading
- Defined separate `vuejs-dev` and `vuejs-prod` services in your `compose.yaml` file
- Enabled real-time file syncing using Compose Watch for a smoother development experience
- Verified that live updates work seamlessly by modifying and previewing a component

With this setup, you're now equipped to build, run, and iterate on your Vue.js app entirely within containers—efficiently and consistently across environments.

* * *

Deepen your knowledge and improve your containerized development workflow with these guides:

- [Using Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/) – Automatically sync source changes during development
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) – Create efficient, production-ready Docker images
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) – Write clean, secure, and optimized Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [Docker volumes](https://docs.docker.com/storage/volumes/) – Persist and manage data between container runs

In the next section, you'll learn how to run unit tests for your Vue.js application inside Docker containers. This ensures consistent testing across all environments and removes dependencies on local machine setup.