---
title: List Async Chat Completions
url: https://docs.perplexity.ai/api-reference/async-chat-completions-get.md
source: llms
fetched_at: 2026-02-04T07:20:30.884063469-03:00
rendered_js: false
word_count: 40
summary: This document provides the API specification for retrieving a list of all asynchronous chat completion requests and their processing statuses for a user.
tags:
    - perplexity-ai
    - api-endpoint
    - async-chat
    - chat-completions
    - request-listing
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Async Chat Completions

> Retrieve a list of all asynchronous chat completion requests for a given user.



## OpenAPI

````yaml get /async/chat/completions
openapi: 3.1.0
info:
  title: Perplexity AI API
  description: Perplexity AI API
  version: 0.1.0
servers: []
security: []
paths:
  /async/chat/completions:
    get:
      summary: List Async Chat Completions
      description: >-
        Retrieve a list of all asynchronous chat completion requests for a given
        user.
      operationId: list_async_chat_completions_async_chat_completions_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAsyncApiChatCompletionsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    ListAsyncApiChatCompletionsResponse:
      properties:
        next_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Next Token
        requests:
          items:
            $ref: '#/components/schemas/AsyncApiChatCompletionsResponseSummary'
          type: array
          title: Requests
      type: object
      required:
        - requests
      title: ListAsyncApiChatCompletionsResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AsyncApiChatCompletionsResponseSummary:
      properties:
        id:
          type: string
          title: Id
        created_at:
          type: integer
          title: Created At
        started_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Started At
        completed_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completed At
        failed_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Failed At
        model:
          type: string
          title: Model
        status:
          $ref: '#/components/schemas/AsyncProcessingStatus'
      type: object
      required:
        - id
        - created_at
        - model
        - status
      title: AsyncApiChatCompletionsResponseSummary
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    AsyncProcessingStatus:
      type: string
      enum:
        - CREATED
        - IN_PROGRESS
        - COMPLETED
        - FAILED
      title: AsyncProcessingStatus
      description: Status enum for async processing.
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````