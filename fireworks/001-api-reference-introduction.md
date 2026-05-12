---
title: Introduction - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/introduction
source: sitemap
fetched_at: 2026-04-27T20:14:01.050624992-03:00
rendered_js: false
word_count: 89
summary: This document explains how to interact with the Fireworks AI REST API, detailing the necessary authentication methods and providing references for managing account-scoped quotas.
tags:
    - rest-api
    - authentication
    - api-key
    - account-management
    - inference
    - deployment
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks AI REST API enables you to interact with language, image, and embedding models using an API key, and automate management of models, deployments, datasets, and more.

## Authentication

All requests must include an `Authorization` header with a valid `Bearer` token and the `Content-Type: application/json` header.

### Getting your API key

Obtain an API key via:

- [`firectl api-key create`]([[145-tools-sdks-firectl-commands-api-key-create]])
- [Fireworks AI dashboard](https://app.fireworks.ai/settings/users/api-keys)

Include in every request:

```bash
authorization: Bearer <API_KEY>
content-type: application/json
```

## Account management APIs

Fireworks exposes account-scoped quota endpoints:

- [[217-api-reference-list-quotas|List Quotas]]
- [[245-api-reference-get-quota|Get Quota]]
- [[270-api-reference-update-quota|Update Quota]]

#api-reference #authentication #rest-api
