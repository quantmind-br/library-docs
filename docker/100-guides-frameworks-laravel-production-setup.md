---
title: Laravel Production Setup with Docker Compose
url: https://docs.docker.com/guides/frameworks/laravel/production-setup/
source: llms
fetched_at: 2026-01-24T14:09:49.932868176-03:00
rendered_js: false
word_count: 404
summary: This document explains how to configure and deploy a production-ready Laravel application using Docker and Docker Compose. It provides instructions for setting up optimized PHP-FPM, CLI, and Nginx containers using multi-stage builds.
tags:
    - laravel
    - docker
    - docker-compose
    - production-deployment
    - php-fpm
    - nginx
    - containerization
category: guide
---

This guide demonstrates how to set up a production-ready Laravel environment using Docker and Docker Compose. This configuration is designed for streamlined, scalable, and secure Laravel application deployments.

> To experiment with a ready-to-run configuration, download the [Laravel Docker Examples](https://github.com/dockersamples/laravel-docker-examples) repository. It contains pre-configured setups for both development and production.

This layout represents a typical Laravel project, with Docker configurations stored in a unified `docker` directory. You’ll find **two** Compose files — `compose.dev.yaml` (for development) and `compose.prod.yaml` (for production) — to keep your environments separate and manageable.

For production, the `php-fpm` Dockerfile creates an optimized image with only the PHP extensions and libraries your application needs. As demonstrated in the [GitHub example](https://github.com/dockersamples/laravel-docker-examples), a single Dockerfile with multi-stage builds maintains consistency and reduces duplication between development and production. The following snippet shows only the production-related stages:

For production, you often need a separate container to run Artisan commands, migrations, and other CLI tasks. In most cases you can run these commands by reusing existing PHP-FPM container:

If you need a separate CLI container with different extensions or strict separation of concerns, consider a php-cli Dockerfile:

This Dockerfile is similar to the PHP-FPM Dockerfile, but it uses the `php:8.4-cli` image as the base image and sets up the container for running CLI commands.

Nginx serves as the web server for the Laravel application. You can include static assets directly to the container. Here's an example of possible Dockerfile for Nginx:

This Dockerfile uses a multi-stage build to separate the asset building process from the final production image. The first stage installs Node.js and builds the assets, while the second stage sets up the Nginx production image with the optimized configuration and the built assets.

To bring all the services together, create a `compose.prod.yaml` file that defines the services, volumes, and networks for the production environment. Here's an example configuration:

> Ensure you have an `.env` file at the root of your Laravel project with the necessary configurations (e.g., database and Xdebug settings) to match the Docker Compose setup.

To start the production environment, run:

This command will build and start all the services in detached mode, providing a scalable and production-ready setup for your Laravel application.

By setting up a Docker Compose environment for Laravel in production, you ensure that your application is optimized for performance, scalable, and secure. This setup makes deployments consistent and easier to manage, reducing the likelihood of errors due to differences between environments.