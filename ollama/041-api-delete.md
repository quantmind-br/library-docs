---
title: Delete a model
url: https://docs.ollama.com/api/delete.md
source: llms
fetched_at: 2026-02-04T11:33:13.272343983-03:00
rendered_js: false
word_count: 26
summary: This document specifies the Ollama API endpoint and request format for deleting a model from the local server.
tags:
    - ollama-api
    - model-management
    - delete-endpoint
    - openapi-spec
    - rest-api
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a model



## OpenAPI

````yaml openapi.yaml delete /api/delete
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
  /api/delete:
    delete:
      summary: Delete a model
      operationId: delete
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteRequest'
            example:
              model: gemma3
      responses:
        '200':
          description: Model successfully deleted
components:
  schemas:
    DeleteRequest:
      type: object
      required:
        - model
      properties:
        model:
          type: string
          description: Model name to delete

````