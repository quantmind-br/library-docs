---
title: Develop your app
url: https://docs.docker.com/guides/angular/develop/
source: llms
fetched_at: 2026-01-24T14:03:20.420117605-03:00
rendered_js: false
word_count: 506
summary: This guide explains how to configure production and development environments for Angular applications using Docker Compose and Compose Watch for live-reloading.
tags:
    - angular
    - docker
    - docker-compose
    - compose-watch
    - containerization
    - web-development
    - live-reload
category: tutorial
---

## Use containers for Angular development

Complete [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).

* * *

In this section, you'll learn how to set up both production and development environments for your containerized Angular application using Docker Compose. This setup allows you to serve a static production build via Nginx and to develop efficiently inside containers using a live-reloading dev server with Compose Watch.

You’ll learn how to:

- Configure separate containers for production and development
- Enable automatic file syncing using Compose Watch in development
- Debug and live-preview your changes in real-time without manual rebuilds

* * *

Use Compose Watch to automatically sync source file changes into your containerized development environment. This provides a seamless, efficient development experience without restarting or rebuilding containers manually.

Create a file named `Dockerfile.dev` in your project root with the following content:

This file sets up a lightweight development environment for your Angular application using the dev server.

### [Step 2: Update your `compose.yaml` file](#step-2-update-your-composeyaml-file)

Open your `compose.yaml` file and define two services: one for production (`angular-prod`) and one for development (`angular-dev`).

Here’s an example configuration for an Angular application:

- The `angular-prod` service builds and serves your static production app using Nginx.
- The `angular-dev` service runs your Angular development server with live reload and hot module replacement.
- `watch` triggers file sync with Compose Watch.

> For more details, see the official guide: [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

After completing the previous steps, your project directory should now contain the following files:

### [Step 4: Start Compose Watch](#step-4-start-compose-watch)

Run the following command from the project root to start the container in watch mode

### [Step 5: Test Compose Watch with Angular](#step-5-test-compose-watch-with-angular)

To verify that Compose Watch is working correctly:

1. Open the `src/app/app.component.html` file in your text editor.
2. Locate the following line:
3. Change it to:
4. Save the file.
5. Open your browser at [http://localhost:4200](http://localhost:4200).

You should see the updated text appear instantly, without needing to rebuild the container manually. This confirms that file watching and automatic synchronization are working as expected.

* * *

In this section, you set up a complete development and production workflow for your Angular application using Docker and Docker Compose.

Here’s what you accomplished:

- Created a `Dockerfile.dev` to streamline local development with hot reloading
- Defined separate `angular-dev` and `angular-prod` services in your `compose.yaml` file
- Enabled real-time file syncing using Compose Watch for a smoother development experience
- Verified that live updates work seamlessly by modifying and previewing a component

With this setup, you're now equipped to build, run, and iterate on your Angular app entirely within containers—efficiently and consistently across environments.

* * *

Deepen your knowledge and improve your containerized development workflow with these guides:

- [Using Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/) – Automatically sync source changes during development
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) – Create efficient, production-ready Docker images
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) – Write clean, secure, and optimized Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [Docker volumes](https://docs.docker.com/storage/volumes/) – Persist and manage data between container runs

In the next section, you'll learn how to run unit tests for your Angular application inside Docker containers. This ensures consistent testing across all environments and removes dependencies on local machine setup.