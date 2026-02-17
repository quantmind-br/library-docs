---
title: Phoenix
url: https://coolify.io/docs/applications/phoenix.md
source: llms
fetched_at: 2026-02-17T14:38:55.003481-03:00
rendered_js: false
word_count: 71
summary: This document outlines the specific configuration requirements and environment variables needed to deploy a Phoenix web framework application.
tags:
    - phoenix-framework
    - elixir
    - deployment-settings
    - configuration
    - environment-variables
    - nixpacks
category: configuration
---

# Phoenix

Phoenix is a productive web framework that does not compromise speed and maintainability written in Elixir/Erlang.

## Requirements

* Set `Build Pack` to `nixpacks`
* Set `MIX_ENV` to `prod`
  * It should be a `Build time` environment variable
* Set `SECRET_KEY_BASE` to a random string (https://hexdocs.pm/phoenix/deployment.html#handling-of-your-application-secrets)
  * It should be a `Build time` environment variable
* Set `DATABASE_URL` to your database connection string
  * It should be a `Build time` environment variable
* Set `Ports Exposes` to `4000` (default)