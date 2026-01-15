---
title: Create a machine template - Factory Documentation
url: https://docs.factory.ai/api-reference/machine-templates/create-a-machine-template
source: sitemap
fetched_at: 2026-01-13T19:03:19.166728185-03:00
rendered_js: false
word_count: 64
summary: Documentation for the API endpoint used to create a new machine template, specifying request body parameters and response structure.
tags:
    - api
    - factory-api
    - machine-templates
    - api-reference
    - environment-variables
    - authentication
category: api
---

Create a machine template

#### Authorizations

Factory API key for authentication

#### Body

Human-readable template name

Required string length: `1 - 100`

Environment variables to set in the machine

Setup script to run after cloning

Maximum string length: `10000`

#### Response

Human-readable template name

Last update timestamp (ms)

Shared environment variables

userEnvironmentVariablesByUser

User-specific environment variables

Setup script to run after cloning

[List machine templates](https://docs.factory.ai/api-reference/machine-templates/list-machine-templates)[Get a machine template](https://docs.factory.ai/api-reference/machine-templates/get-a-machine-template)