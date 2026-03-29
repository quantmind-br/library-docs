---
title: Pull a model
url: https://docs.ollama.com/api/pull.md
source: llms
fetched_at: 2026-02-04T11:33:31.290824146-03:00
rendered_js: false
word_count: 26
summary: This document defines the OpenAPI specification for the Ollama API's model pull endpoint, detailing the request parameters and response formats for downloading models.
tags:
    - ollama
    - api-specification
    - model-management
    - openapi
    - http-api
    - rest-endpoint
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pull a model



## OpenAPI

````yaml openapi.yaml post /api/pull
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
  /api/pull:
    post:
      summary: Pull a model
      operationId: pull
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PullRequest'
            example:
              model: gemma3
      responses:
        '200':
          description: Pull status updates.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusResponse'
              example:
                status: success
            application/x-ndjson:
              schema:
                $ref: '#/components/schemas/StatusEvent'
              example:
                status: success
components:
  schemas:
    PullRequest:
      type: object
      required:
        - model
      properties:
        model:
          type: string
          description: Name of the model to download
        insecure:
          type: boolean
          description: Allow downloading over insecure connections
        stream:
          type: boolean
          default: true
          description: Stream progress updates
    StatusResponse:
      type: object
      properties:
        status:
          type: string
          description: Current status message
    StatusEvent:
      type: object
      properties:
        status:
          type: string
          description: Human-readable status message
        digest:
          type: string
          description: Content digest associated with the status, if applicable
        total:
          type: integer
          description: Total number of bytes expected for the operation
        completed:
          type: integer
          description: Number of bytes transferred so far

````