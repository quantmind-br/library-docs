---
title: Create embeddings (Cohere v2 format)
url: https://docs.getbifrost.ai/api-reference/cohere-integration/create-embeddings-cohere-v2-format.md
source: llms
fetched_at: 2026-01-21T19:38:25.203391563-03:00
rendered_js: false
word_count: 122
summary: This document provides the API specification for generating text and multimodal embeddings using the Cohere v2 compatible endpoint via the Bifrost gateway.
tags:
    - cohere-v2
    - embeddings
    - api-reference
    - bifrost-gateway
    - multimodal-ai
category: api
---

# Create embeddings (Cohere v2 format)

> Creates embeddings using Cohere v2 API format.




## OpenAPI

````yaml openapi/openapi.json post /cohere/v2/embed
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
  /cohere/v2/embed:
    post:
      tags:
        - Cohere Integration
      summary: Create embeddings (Cohere v2 format)
      description: |
        Creates embeddings using Cohere v2 API format.
      operationId: cohereEmbedV2
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - input_type
              properties:
                model:
                  type: string
                  description: ID of an available embedding model
                  example: embed-english-v3.0
                input_type:
                  type: string
                  description: >-
                    Specifies the type of input passed to the model. Required
                    for embedding models v3 and higher.
                texts:
                  type: array
                  items:
                    type: string
                  description: >-
                    Array of strings to embed. Maximum 96 texts per call. At
                    least one of texts, images, or inputs is required.
                  maxItems: 96
                images:
                  type: array
                  items:
                    type: string
                  description: >-
                    Array of image data URIs for multimodal embedding. Maximum 1
                    image per call. Supports JPEG, PNG, WebP, GIF up to 5MB.
                  maxItems: 1
                inputs:
                  type: array
                  items:
                    type: object
                    properties:
                      content:
                        type: array
                        items:
                          type: object
                          required:
                            - type
                          properties:
                            type:
                              type: string
                              enum:
                                - text
                                - image_url
                                - thinking
                                - document
                            text:
                              type: string
                            image_url:
                              type: object
                              properties:
                                url:
                                  type: string
                            thinking:
                              type: string
                            document:
                              type: object
                              properties:
                                data:
                                  type: object
                                id:
                                  type: string
                        description: Array of content blocks (reuses chat content blocks)
                  description: >-
                    Array of mixed text/image components for embedding. Maximum
                    96 per call.
                  maxItems: 96
                embedding_types:
                  type: array
                  items:
                    type: string
                  description: >-
                    Specifies the return format types (float, int8, uint8,
                    binary, ubinary, base64). Defaults to float if unspecified.
                output_dimension:
                  type: integer
                  description: >-
                    Number of dimensions for output embeddings (256, 512, 1024,
                    1536). Available only for embed-v4 and newer models.
                max_tokens:
                  type: integer
                  description: Maximum tokens to embed per input before truncation.
                truncate:
                  type: string
                  description: Handling for inputs exceeding token limits. Defaults to END.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: Response ID
                  embeddings:
                    type: object
                    description: Embedding data object with different types
                    properties:
                      float:
                        type: array
                        items:
                          type: array
                          items:
                            type: number
                        description: Float embeddings
                      int8:
                        type: array
                        items:
                          type: array
                          items:
                            type: integer
                        description: Int8 embeddings
                      uint8:
                        type: array
                        items:
                          type: array
                          items:
                            type: integer
                        description: Uint8 embeddings
                      binary:
                        type: array
                        items:
                          type: array
                          items:
                            type: integer
                        description: Binary embeddings
                      ubinary:
                        type: array
                        items:
                          type: array
                          items:
                            type: integer
                        description: Unsigned binary embeddings
                      base64:
                        type: array
                        items:
                          type: string
                        description: Base64-encoded embeddings
                  response_type:
                    type: string
                    description: Response type (embeddings_floats, embeddings_by_type)
                  texts:
                    type: array
                    items:
                      type: string
                    description: Original text entries
                  images:
                    type: array
                    items:
                      type: object
                      description: Image information in the response
                      properties:
                        width:
                          type: integer
                          description: Width in pixels
                        height:
                          type: integer
                          description: Height in pixels
                        format:
                          type: string
                          description: Image format
                        bit_depth:
                          type: integer
                          description: Bit depth
                    description: Original image entries
                  meta:
                    type: object
                    description: Metadata in embedding response
                    properties:
                      api_version:
                        type: object
                        description: API version information
                        properties:
                          version:
                            type: string
                            description: API version
                          is_deprecated:
                            type: boolean
                            description: Deprecation status
                          is_experimental:
                            type: boolean
                            description: Experimental status
                      billed_units:
                        type: object
                        properties:
                          input_tokens:
                            type: integer
                            description: Number of billed input tokens
                          output_tokens:
                            type: integer
                            description: Number of billed output tokens
                          search_units:
                            type: integer
                            description: Number of billed search units
                          classifications:
                            type: integer
                            description: Number of billed classification units
                      tokens:
                        type: object
                        properties:
                          input_tokens:
                            type: integer
                            description: Number of input tokens used
                          output_tokens:
                            type: integer
                            description: Number of output tokens produced
                      warnings:
                        type: array
                        items:
                          type: string
                        description: Any warnings
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    description: Error type
                  message:
                    type: string
                    description: Error message
                  code:
                    type: string
                    description: Optional error code
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    description: Error type
                  message:
                    type: string
                    description: Error message
                  code:
                    type: string
                    description: Optional error code

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt