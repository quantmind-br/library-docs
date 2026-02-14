---
title: Environment Variables | Dokploy
url: https://docs.dokploy.com/docs/core/variables
source: crawler
fetched_at: 2026-02-14T14:12:41.477603-03:00
rendered_js: true
word_count: 321
summary: This document explains how to configure and manage environment variables at the project, environment, and service levels within Dokploy, including how to reference shared values across services.
tags:
    - dokploy
    - environment-variables
    - configuration-management
    - deployment-settings
    - devops-tools
category: guide
---

Dokploy allows you to create and manage shared and service-level environment variables for your projects and environments.

Environment variables in Dokploy allow you to:

- Define configuration once and reuse it
- Share values across multiple services
- Reference values from within the same service
- Centrally manage sensitive information

![Environment variables panel](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fshared-variables.png&w=3840&q=75)

You can declare environment variables either:

- **Project-level (shared)** — available across all services in the project
- **Environment-level** — specific to a single environment
- **Service-level** — specific to a single service

### [Practical Example](#practical-example)

Let's consider a common scenario where you have:

- A PostgreSQL database
- Two services that need to connect to this database

### [1. Define Shared Variable](#1-define-shared-variable)

In the project's shared variables section, define:

```
DATABASE_URL=postgresql://postgres:postgres@database:5432/postgres
```

### [2. Use the Variable in Services](#2-use-the-variable-in-services)

In each service's environment variables tab, reference the shared variable:

```
DATABASE_URL=${{project.DATABASE_URL}}
```

Dokploy will automatically replace `${{project.DATABASE_URL}}` with the value defined in the project's shared variables.

You can use shared environment variables in all the services available in dokploy.

### [Practical Example](#practical-example-1)

Let's consider a scenario where you have:

- A staging environment with different database credentials
- Multiple services that need environment-specific configurations

### [1. Define Environment Variable](#1-define-environment-variable)

In the environment's variables section, define:

```
DATABASE_PASSWORD=staging_secret_password
API_KEY=staging_api_key_12345
```

### [2. Use the Variable in Services](#2-use-the-variable-in-services-1)

In each service's environment variables tab, reference the environment variable:

```
DATABASE_URL=postgresql://postgres:${{environment.DATABASE_PASSWORD}}@staging-db:5432/postgres
EXTERNAL_API_KEY=${{environment.API_KEY}}
```

Dokploy will automatically replace `${{environment.VARIABLE_NAME}}` with the value defined in the environment's variables.

You can use environment variables in all the services available in that specific environment.

Service-level variables are specific to a single service and can be used to override shared variables or define service-specific configurations.

### [Practical Example](#practical-example-2)

Let's say you have a service that requires a different database user. You can define a service-level variable:

```
DATABASE_USER=service_user
DATABASE_PASSWORD=service_password
DATABASE_URL=postgresql://${{DATABASE_USER}}:${{DATABASE_PASSWORD}}@service-database:5432/postgres
```

Preview Deployments environments also include a service-level variable called `DOKPLOY_DEPLOY_URL`, which points to the deployment URL of the service. It can be used as `${{DOKPLOY_DEPLOY_URL}}` for variables like `APP_URL=https://${{DOKPLOY_DEPLOY_URL}}`.

### [Best Practices](#best-practices)

- Use shared variables for credentials and configurations that repeat across services
- Keep descriptive variable names
- Document the purpose of each variable for easier maintenance