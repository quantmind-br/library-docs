---
title: Update a machine template - Factory Documentation
url: https://docs.factory.ai/api-reference/machine-templates/update-a-machine-template
source: sitemap
fetched_at: 2026-01-13T19:03:17.842969424-03:00
rendered_js: false
word_count: 58
summary: Documentation for the API endpoint used to update machine templates, including authentication, body parameters, and response fields.
tags:
    - api
    - machine-templates
    - http-request
    - update-operation
    - configuration
category: api
---

Update a machine template

#### Authorizations

Factory API key for authentication

#### Path Parameters

#### Body

Shared environment variables for all machine users

User-specific environment variables

Setup script to run after cloning

Maximum string length: `10000`

#### Response

Human-readable template name

Last update timestamp (ms)

Shared environment variables

userEnvironmentVariablesByUser

User-specific environment variables

Setup script to run after cloning

[Delete a machine template](https://docs.factory.ai/api-reference/machine-templates/delete-a-machine-template)