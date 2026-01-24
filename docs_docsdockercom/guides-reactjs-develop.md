---
title: Develop your app
url: https://docs.docker.com/guides/reactjs/develop/
source: llms
fetched_at: 2026-01-24T14:11:39.8998314-03:00
rendered_js: false
word_count: 615
summary: This guide explains how to set up containerized development and production environments for React.js applications using Docker Compose and Compose Watch. It covers configuring separate services, enabling automatic file synchronization for live-reloading, and optimizing Vite settings for container environments.
tags:
    - docker
    - react-js
    - docker-compose
    - compose-watch
    - development-workflow
    - vite
    - containerization
category: guide
---

## Use containers for React.js development

Complete [Containerize React.js application](https://docs.docker.com/guides/reactjs/containerize/).

* * *

In this section, you'll learn how to set up both production and development environments for your containerized React.js application using Docker Compose. This setup allows you to serve a static production build via Nginx and to develop efficiently inside containers using a live-reloading dev server with Compose Watch.

You’ll learn how to:

- Configure separate containers for production and development
- Enable automatic file syncing using Compose Watch in development
- Debug and live-preview your changes in real-time without manual rebuilds

* * *

Use Compose Watch to automatically sync source file changes into your containerized development environment. This provides a seamless, efficient development experience without needing to restart or rebuild containers manually.

Create a file named `Dockerfile.dev` in your project root with the following content:

This file sets up a lightweight development environment for your React app using the dev server.

### [Step 2: Update your `compose.yaml` file](#step-2-update-your-composeyaml-file)

Open your `compose.yaml` file and define two services: one for production (`react-prod`) and one for development (`react-dev`).

Here’s an example configuration for a React.js application:

- The `react-prod` service builds and serves your static production app using Nginx.
- The `react-dev` service runs your React development server with live reload and hot module replacement.
- `watch` triggers file sync with Compose Watch.

> For more details, see the official guide: [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

### [Step 3: Update vite.config.ts to ensure it works properly inside Docker](#step-3-update-viteconfigts-to-ensure-it-works-properly-inside-docker)

To make Vite’s development server work reliably inside Docker, you need to update your vite.config.ts with the correct settings.

Open the `vite.config.ts` file in your project root and update it as follows:

> The `server` options in `vite.config.ts` are essential for running Vite inside Docker:
> 
> - `host: true` allows the dev server to be accessible from outside the container.
> - `port: 5173` sets a consistent development port (must match the one exposed in Docker).
> - `strictPort: true` ensures Vite fails clearly if the port is unavailable, rather than switching silently.
> 
> For full details, refer to the [Vite server configuration docs](https://vitejs.dev/config/server-options.html).

After completing the previous steps, your project directory should now contain the following files:

### [Step 4: Start Compose Watch](#step-4-start-compose-watch)

Run the following command from your project root to start your container in watch mode:

### [Step 5: Test Compose Watch with React](#step-5-test-compose-watch-with-react)

To verify that Compose Watch is working correctly:

1. Open the `src/App.tsx` file in your text editor.
2. Locate the following line:
3. Change it to:
4. Save the file.
5. Open your browser at [http://localhost:5173](http://localhost:5173).

You should see the updated text appear instantly, without needing to rebuild the container manually. This confirms that file watching and automatic synchronization are working as expected.

* * *

In this section, you set up a complete development and production workflow for your React.js application using Docker and Docker Compose.

Here's what you achieved:

- Created a `Dockerfile.dev` to streamline local development with hot reloading
- Defined separate `react-dev` and `react-prod` services in your `compose.yaml` file
- Enabled real-time file syncing using Compose Watch for a smoother development experience
- Verified that live updates work seamlessly by modifying and previewing a component

With this setup, you're now equipped to build, run, and iterate on your React.js app entirely within containers—efficiently and consistently across environments.

* * *

Deepen your knowledge and improve your containerized development workflow with these guides:

- [Using Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/) – Automatically sync source changes during development
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) – Create efficient, production-ready Docker images
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) – Write clean, secure, and optimized Dockerfiles.
- [Compose file reference](https://docs.docker.com/compose/compose-file/) – Learn the full syntax and options available for configuring services in `compose.yaml`.
- [Docker volumes](https://docs.docker.com/storage/volumes/) – Persist and manage data between container runs

In the next section, you'll learn how to run unit tests for your React.js application inside Docker containers. This ensures consistent testing across all environments and removes dependencies on local machine setup.