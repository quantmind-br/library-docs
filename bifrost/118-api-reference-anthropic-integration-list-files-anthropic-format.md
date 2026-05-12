---
title: List files (Anthropic format)
url: https://docs.getbifrost.ai/api-reference/anthropic-integration/list-files-anthropic-format.md
source: llms
fetched_at: 2026-01-21T19:37:58.639004353-03:00
rendered_js: false
word_count: 117
summary: This document provides the API specification for listing uploaded files using the Anthropic-compatible format within the Bifrost gateway.
tags:
    - anthropic-integration
    - file-management
    - list-files
    - bifrost-api
    - rest-api
category: api
---

# List files (Anthropic format)

> Lists uploaded files.




## OpenAPI

````yaml openapi/openapi.json get /anthropic/v1/files
openapi: 3.1.0
info:
  title: Bifrost API
  description: >
    Bifrost HTTP Transport API for AI model inference and gateway management.


    This API provides a unified interface for interacting with multiple AI
    providers

    including OpenAI, Anthropic, Bedrock, Gemini, and more through a single API,

    along with comprehensive management APIs for configuring and monitoring the
    gateway.


    ## API Structure


    ### Unified Inference API (`/v1/*`)

    The primary API using Bifrost's unified format. Model parameters use the
    format

    `provider/model` (e.g., `openai/gpt-4`, `anthropic/claude-3-opus`).


    ### Provider Integration APIs

    Native provider-format APIs for drop-in compatibility:

    - `/openai/*` - OpenAI-compatible API

    - `/anthropic/*` - Anthropic-compatible API

    - `/genai/*` - Google GenAI (Gemini) compatible API

    - `/bedrock/*` - AWS Bedrock compatible API

    - `/cohere/*` - Cohere compatible API


    ### Framework Integration APIs

    Multi-provider proxy endpoints for AI frameworks:

    - `/litellm/*` - LiteLLM proxy with all provider formats

    - `/langchain/*` - LangChain compatible endpoints

    - `/pydanticai/*` - PydanticAI compatible endpoints


    ### Management APIs (`/api/*`)

    APIs for managing and monitoring the Bifrost gateway:

    - `/api/config` - Configuration management

    - `/api/providers` - Provider and API key management

    - `/api/plugins` - Plugin management

    - `/api/governance/*` - Virtual keys, teams, and customers

    - `/api/logs` - Log search and analytics

    - `/api/mcp/*` - MCP (Model Context Protocol) client management

    - `/api/session/*` - Authentication and session management

    - `/api/cache/*` - Cache management

    - `/health` - Health check endpoint


    ## Fallbacks

    Requests can include fallback models that will be tried if the primary model
    fails.
  version: 1.0.0
  contact:
    name: Contact Us
    url: https://getmaxim.ai/bifrost
  license:
    name: Apache 2.0
    url: https://opensource.org/licenses/Apache-2.0
servers:
  - url: http://localhost:8080
    description: Local development server
security: []
tags:
  - name: Models
    description: Model listing and information
  - name: Chat Completions
    description: Chat-based text generation
  - name: Text Completions
    description: Text completion generation
  - name: Responses
    description: OpenAI Responses API compatible endpoints
  - name: Embeddings
    description: Text embedding generation
  - name: Image Generations
    description: Image generation from text prompts
  - name: Audio
    description: Speech synthesis and transcription
  - name: Count Tokens
    description: Token counting utilities
  - name: Batch
    description: Batch processing operations
  - name: Files
    description: File management operations
  - name: OpenAI Integration
    description: OpenAI-compatible API endpoints (/openai/*)
  - name: Azure Integration
    description: Azure OpenAI integration endpoints
  - name: Anthropic Integration
    description: Anthropic-compatible API endpoints (/anthropic/*)
  - name: GenAI Integration
    description: Google GenAI (Gemini) compatible API endpoints (/genai/*)
  - name: Bedrock Integration
    description: AWS Bedrock compatible API endpoints (/bedrock/*)
  - name: Cohere Integration
    description: Cohere compatible API endpoints (/cohere/*)
  - name: LiteLLM Integration
    description: LiteLLM proxy endpoints with multi-provider support (/litellm/*)
  - name: LangChain Integration
    description: LangChain compatible endpoints with multi-provider support (/langchain/*)
  - name: PydanticAI Integration
    description: >-
      PydanticAI compatible endpoints with multi-provider support
      (/pydanticai/*)
  - name: Health
    description: Health check endpoints
  - name: Configuration
    description: Configuration management endpoints
  - name: Session
    description: Session and authentication endpoints
  - name: Providers
    description: Provider management endpoints
  - name: Plugins
    description: Plugin management endpoints
  - name: MCP
    description: Model Context Protocol endpoints
  - name: Governance
    description: Virtual keys, teams, and customers management
  - name: Logging
    description: Log search and management endpoints
  - name: Cache
    description: Cache management endpoints
paths:
  /anthropic/v1/files:
    get:
      tags:
        - Anthropic Integration
      summary: List files (Anthropic format)
      description: |
        Lists uploaded files.
      operationId: anthropicListFiles
      parameters:
        - name: x-model-provider
          in: header
          schema:
            type: string
          description: Provider to use (defaults to anthropic)
        - name: limit
          in: query
          schema:
            type: integer
            default: 30
          description: Maximum files to return
        - name: after_id
          in: query
          schema:
            type: string
          description: Cursor for pagination
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        type:
                          type: string
                          default: file
                        filename:
                          type: string
                        mime_type:
                          type: string
                          description: MIME type of the file
                        size_bytes:
                          type: integer
                          description: Size of the file in bytes
                        created_at:
                          type: string
                          format: date-time
                        downloadable:
                          type: boolean
                  has_more:
                    type: boolean
                  first_id:
                    type: string
                  last_id:
                    type: string
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    default: error
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        description: Error type (e.g., invalid_request_error, api_error)
                      message:
                        type: string
                        description: Error message
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    default: error
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                        description: Error type (e.g., invalid_request_error, api_error)
                      message:
                        type: string
                        description: Error message

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt