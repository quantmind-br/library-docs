---
title: Develop your app
url: https://docs.docker.com/guides/nodejs/develop/
source: llms
fetched_at: 2026-01-24T14:10:58.201025432-03:00
rendered_js: false
word_count: 962
summary: This document explains how to configure a Node.js development environment using Docker, including database persistence, hot reloading with bind mounts, and remote debugging.
tags:
    - docker-compose
    - nodejs-development
    - hot-reloading
    - database-persistence
    - multi-stage-builds
    - debugging
category: guide
---

## Use containers for Node.js development

Complete [Containerize a Node.js application](https://docs.docker.com/guides/nodejs/containerize/).

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

- Adding a local database and persisting data
- Configuring your container to run a development environment
- Debugging your containerized application

The application uses PostgreSQL for data persistence. Add a database service to your Docker Compose configuration.

### [Add database service to Docker Compose](#add-database-service-to-docker-compose)

If you haven't already created a `compose.yml` file in the previous section, or if you need to add the database service, update your `compose.yml` file to include the PostgreSQL database service:

### [Update your application service](#update-your-application-service)

Make sure your application service in `compose.yml` is configured to connect to the database:

1. The PostgreSQL database configuration is handled automatically by the application. The database is created and initialized when the application starts, with data persisted using the `postgres_data` volume.
2. Configure your environment by copying the example file:
   
   Update the `.env` file with your preferred settings:
3. Run the following command to start your application in development mode:
4. Open a browser and verify that the application is running at [http://localhost:5173](http://localhost:5173) for the frontend or [http://localhost:3000](http://localhost:3000) for the API. The React frontend is served by Vite dev server on port 5173, with API calls proxied to the Express server on port 3000.
5. Add some items to the todo list to test data persistence.
6. After adding some items to the todo list, press `CTRL + C` in the terminal to stop your application.
7. Run the application again:
8. Refresh [http://localhost:5173](http://localhost:5173) in your browser and verify that the todo items persisted, even after the containers were removed and ran again.

You can use a bind mount to mount your source code into the container. The container can then see the changes you make to the code immediately, as soon as you save a file. This means that you can run processes, like nodemon, in the container that watch for filesystem changes and respond to them. To learn more about bind mounts, see [Storage overview](https://docs.docker.com/engine/storage/).

In addition to adding a bind mount, you can configure your Dockerfile and `compose.yaml` file to install development dependencies and run development tools.

### [Update your Dockerfile for development](#update-your-dockerfile-for-development)

Your Dockerfile should be configured as a multi-stage build with separate stages for development, production, and testing. If you followed the previous section, your Dockerfile already includes a development stage that has all development dependencies and runs the application with hot reload enabled.

Here's the development stage from your multi-stage Dockerfile:

The development stage:

- Installs all dependencies including dev dependencies
- Exposes ports for the API server (3000), Vite dev server (5173), and Node.js debugger (9229)
- Runs `npm run dev` which starts both the Express server and Vite dev server concurrently
- Includes health checks for monitoring container status

Next, you'll need to update your Compose file to use the new stage.

### [Update your Compose file for development](#update-your-compose-file-for-development)

Update your `compose.yml` file to run the development stage with bind mounts for hot reloading:

Key features of the development configuration:

- **Multi-port exposure**: API server (3000), Vite dev server (5173), and debugger (9229)
- **Comprehensive bind mounts**: Source code, configuration files, and package files for hot reloading
- **Environment variables**: Configurable through `.env` file or defaults
- **PostgreSQL database**: Production-ready database with persistent storage
- **Docker Compose watch**: Automatic file synchronization and container rebuilds
- **Health checks**: Database health monitoring with automatic dependency management

### [Run your development container and debug your application](#run-your-development-container-and-debug-your-application)

Run the following command to run your application with the development configuration:

Or with file watching for automatic updates:

For local development without Docker:

Or start services separately:

### [Using Task Runner (alternative)](#using-task-runner-alternative)

The project includes a Taskfile.yml for advanced workflows:

The application will start with both the Express API server and Vite development server:

- **API Server**: [http://localhost:3000](http://localhost:3000) - Express.js backend with REST API
- **Frontend**: [http://localhost:5173](http://localhost:5173) - Vite dev server with hot module replacement
- **Health Check**: [http://localhost:3000/health](http://localhost:3000/health) - Application health status

Any changes to the application's source files on your local machine will now be immediately reflected in the running container thanks to the bind mounts.

Try making a change to test hot reloading:

1. Open `src/client/components/TodoApp.tsx` in an IDE or text editor.
2. Update the main heading text:
3. Save the file and the Vite dev server will automatically reload the page with your changes.

**Debugging support:**

You can connect a debugger to your application on port 9229. The Node.js inspector is enabled with `--inspect=0.0.0.0:9230` in the development script (`dev:server`).

### [VS Code debugger setup](#vs-code-debugger-setup)

1. Create a launch configuration in `.vscode/launch.json`:
2. Start your development container:
3. Attach the debugger:
   
   - Open VS Code
   - From the Debug panel (Ctrl/Cmd + Shift + D), select **Attach to Docker Container** from the drop-down
   - Select the green play button or press F5

### [Chrome DevTools (alternative)](#chrome-devtools-alternative)

You can also use Chrome DevTools for debugging:

1. Start your container (if not already running):
2. Open Chrome and go to `chrome://inspect`.
3. From the **Configure** option, add:
4. When your Node.js target appears, select **inspect**.

### [Debugging configuration details](#debugging-configuration-details)

The debugger configuration:

- **Container port**: 9230 (internal debugger port)
- **Host port**: 9229 (mapped external port)
- **Script**: `tsx watch --inspect=0.0.0.0:9230 src/server/index.ts`

The debugger listens on all interfaces (`0.0.0.0`) inside the container on port 9230 and is accessible on port 9229 from your host machine.

### [Troubleshooting debugger connection](#troubleshooting-debugger-connection)

If the debugger doesn't connect:

1. Check if the container is running:
2. Check if the port is exposed:
3. Check container logs:
   
   You should see a message like:

Now you can set breakpoints in your TypeScript source files and debug your containerized Node.js application.

For more details about Node.js debugging, see the [Node.js documentation](https://nodejs.org/en/docs/guides/debugging-getting-started).

You've set up your Compose file with a PostgreSQL database and data persistence. You also created a multi-stage Dockerfile and configured bind mounts for development.

Related information:

- [Volumes top-level element](https://docs.docker.com/reference/compose-file/volumes/)
- [Services top-level element](https://docs.docker.com/reference/compose-file/services/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

In the next section, you'll learn how to run unit tests using Docker.