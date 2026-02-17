---
title: Keycloak
url: https://coolify.io/docs/services/keycloak.md
source: llms
fetched_at: 2026-02-17T14:45:10.651293-03:00
rendered_js: false
word_count: 74
summary: This document outlines the deployment options for Keycloak within Coolify, detailing the differences between the development-focused H2 configuration and the production-ready PostgreSQL setup.
tags:
    - keycloak
    - identity-management
    - coolify-deployment
    - postgresql
    - h2-database
    - authentication
category: configuration
---

# Keycloak

## What is Keycloak

Keycloak is an open-source Identity and Access Management tool.

## Deployment Variants

Keycloak is available in two deployment configurations in Coolify:

### Keycloak (Default)

* **Database:** Embedded H2 (development)
* **Use case:** Development, testing, or evaluation purposes
* **Components:** Single Keycloak container with built-in H2 database

### Keycloak with PostgreSQL

* **Database:** PostgreSQL
* **Use case:** Production deployments requiring reliability, performance, and data persistence
* **Components:**
  * Keycloak container
  * PostgreSQL container
  * Automatic database configuration and health checks

## Links

* [Official Documentation](https://www.keycloak.org?utm_source=coolify.io)