---
title: Authentik Forward Authentication Middleware
url: https://coolify.io/docs/knowledge-base/proxy/traefik/protect-services-with-authentik.md
source: llms
fetched_at: 2026-02-17T14:41:29.693457-03:00
rendered_js: false
word_count: 125
summary: This document explains how to secure web applications by integrating Authentik's forward authentication middleware with Traefik to enable single sign-on capabilities.
tags:
    - authentik
    - traefik
    - forward-auth
    - sso
    - middleware
    - security
    - docker-compose
category: guide
---

# Authentik Forward Authentication Middleware

Traefik enables you to secure your applications with authentication by using a [Proxy Provider](https://docs.goauthentik.io/docs/add-secure-apps/providers/proxy/).
This allows you to protect your services with Single Sign-On (SSO).

## Configure an Authentik Application and Proxy Provider

The first step is to deploy the [Authentik service](/services/authentik) and then configure the required components:

* Create a Proxy Provider with forward authentication.
* Create an application and assign the Proxy Provider you created.
* In the "Cookie Domain" field, add the domain of the services.

## Create the Traefik Configuration

The next step is to add the Traefik middleware configuration to your instance's dynamic configuration.

Replace `AUTHENTIK_SERVER_HOST` with your instance name, e.g., `authentik-server-ncoc0ooog0ckwc0gwgoocgs8`.

```yaml
http:
  middlewares:
    authentik-auth:
      forwardAuth:
        address: 'http://AUTHENTIK_SERVER_HOST:9000/outpost.goauthentik.io/auth/traefik'
        trustForwardHeader: true
        authResponseHeaders:
          - X-authentik-username
          - X-authentik-groups
          - X-authentik-entitlements
          - X-authentik-email
          - X-authentik-name
          - X-authentik-uid
          - X-authentik-jwt
          - X-authentik-meta-jwks
          - X-authentik-meta-outpost
          - X-authentik-meta-provider
          - X-authentik-meta-app
          - X-authentik-meta-version
```

## Protecting Services

To protect a service, the Traefik middleware label must be added to the container's Docker Compose configuration:

```yaml
services:
  privatebin:
    image: privatebin/nginx-fpm-alpine
    environment:
      - SERVICE_FQDN_PRIVATEBIN_8080
    volumes:
      - 'privatebin_data:/srv/data'
    healthcheck:
      test:
        - CMD-SHELL
        - 'wget -qO- http://127.0.0.1:8080/'
      interval: 5s
      timeout: 20s
      retries: 10
    labels:
      - traefik.http.middlewares.authentik-auth@file
```