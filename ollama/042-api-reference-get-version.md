---
title: Get version
url: https://docs.ollama.com/api-reference/get-version.md
source: llms
fetched_at: 2026-02-04T11:32:54.702284716-03:00
rendered_js: false
word_count: 31
summary: This document specifies the Ollama HTTP API endpoint used to retrieve the current version of the server.
tags:
    - ollama-api
    - api-version
    - http-get
    - openapi-spec
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get version

> Retrieve the version of the Ollama



## OpenAPI

````yaml openapi.yaml get /api/version
openapi: 3.1.0
info:
  title: Ollama API
  version: 0.1.0
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
  description: |
    OpenAPI specification for the Ollama HTTP API
servers:
  - url: http://localhost:11434
    description: Ollama
security: []
paths:
  /api/version:
    get:
      summary: Get version
      description: Retrieve the version of the Ollama
      operationId: version
      responses:
        '200':
          description: Version information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VersionResponse'
              example:
                version: 0.12.6
components:
  schemas:
    VersionResponse:
      type: object
      properties:
        version:
          type: string
          description: Version of Ollama

````