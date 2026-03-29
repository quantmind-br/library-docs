---
title: Generate Auth Token
url: https://docs.perplexity.ai/api-reference/generate-auth-token-post.md
source: llms
fetched_at: 2026-02-04T07:20:41.124991686-03:00
rendered_js: false
word_count: 34
summary: This document specifies the API endpoint for generating new authentication tokens required for Perplexity AI API access.
tags:
    - authentication
    - api-token
    - security
    - token-generation
    - openapi-specification
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Auth Token

> Generates a new authentication token for API access.



## OpenAPI

````yaml post /generate_auth_token
openapi: 3.1.0
info:
  description: Perplexity AI API - Authentication Management
  title: Perplexity AI API - Authentication
  version: 1.0.0
servers:
  - url: https://api.perplexity.ai
    description: Perplexity AI API
security: []
paths:
  /generate_auth_token:
    post:
      summary: Generate Auth Token
      description: Generates a new authentication token for API access.
      operationId: generate_auth_token
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerateAuthTokenRequest'
      responses:
        '200':
          description: Successfully generated authentication token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateAuthTokenResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    GenerateAuthTokenRequest:
      type: object
      properties:
        token_name:
          type: string
          description: >-
            Optional name for the authentication token to help identify its
            purpose.
          example: Production API Key
    GenerateAuthTokenResponse:
      type: object
      required:
        - auth_token
        - created_at_epoch_seconds
      properties:
        auth_token:
          type: string
          description: >-
            The newly generated authentication token. Store this securely as it
            cannot be retrieved again.
          example: pplx-1234567890abcdef
        created_at_epoch_seconds:
          type: number
          description: Unix timestamp (in seconds) of when the token was created.
          example: 1735689600
        token_name:
          type: string
          description: The name associated with this token, if provided.
          example: Production API Key
  securitySchemes:
    BearerAuth:
      scheme: bearer
      type: http

````