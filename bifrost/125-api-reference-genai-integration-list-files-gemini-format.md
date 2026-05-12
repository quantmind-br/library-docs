---
title: List files (Gemini format)
url: https://docs.getbifrost.ai/api-reference/genai-integration/list-files-gemini-format.md
source: llms
fetched_at: 2026-01-21T19:38:46.763072947-03:00
rendered_js: false
word_count: 122
summary: This document provides the API specification for listing uploaded files in the Google Gemini compatible format through the Bifrost gateway.
tags:
    - gemini-api
    - file-management
    - google-genai
    - bifrost-gateway
    - api-integration
category: api
---

# List files (Gemini format)

> Lists uploaded files in Google Gemini API format.




## OpenAPI

````yaml openapi/openapi.json get /genai/v1beta/files
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
  /genai/v1beta/files:
    get:
      tags:
        - GenAI Integration
      summary: List files (Gemini format)
      description: |
        Lists uploaded files in Google Gemini API format.
      operationId: geminiListFiles
      parameters:
        - name: pageSize
          in: query
          schema:
            type: integer
          description: Maximum number of files to return
        - name: pageToken
          in: query
          schema:
            type: string
          description: Page token for pagination
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  files:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          description: File resource name (e.g., files/abc123)
                        displayName:
                          type: string
                        mimeType:
                          type: string
                        sizeBytes:
                          type: string
                          description: Size in bytes (returned as string by Gemini API)
                        createTime:
                          type: string
                          format: date-time
                        updateTime:
                          type: string
                          format: date-time
                        expirationTime:
                          type: string
                          format: date-time
                        sha256Hash:
                          type: string
                        uri:
                          type: string
                          description: URI for accessing the file content
                        state:
                          type: string
                          enum:
                            - STATE_UNSPECIFIED
                            - PROCESSING
                            - ACTIVE
                            - FAILED
                        error:
                          type: object
                          properties:
                            code:
                              type: integer
                            message:
                              type: string
                        videoMetadata:
                          type: object
                          properties:
                            videoDuration:
                              type: string
                  nextPageToken:
                    type: string
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
                      status:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            '@type':
                              type: string
                              description: Type identifier for the error details
                            fieldViolations:
                              type: array
                              items:
                                type: object
                                properties:
                                  description:
                                    type: string
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
                      status:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            '@type':
                              type: string
                              description: Type identifier for the error details
                            fieldViolations:
                              type: array
                              items:
                                type: object
                                properties:
                                  description:
                                    type: string

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt