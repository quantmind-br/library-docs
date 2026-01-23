---
title: Create embeddings (Azure OpenAI)
url: https://docs.getbifrost.ai/api-reference/openai-integration/create-embeddings-azure-openai.md
source: llms
fetched_at: 2026-01-21T19:40:04.767709986-03:00
rendered_js: false
word_count: 114
summary: This document provides the OpenAPI specification for the Azure OpenAI embedding endpoint within the Bifrost API gateway, detailing request parameters and response schemas.
tags:
    - azure-openai
    - embeddings
    - api-reference
    - bifrost-api
    - text-processing
category: api
---

# Create embeddings (Azure OpenAI)



## OpenAPI

````yaml openapi/openapi.json post /openai/openai/deployments/{deployment-id}/embeddings
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
  /openai/openai/deployments/{deployment-id}/embeddings:
    post:
      tags:
        - OpenAI Integration
        - Azure Integration
      summary: Create embeddings (Azure OpenAI)
      operationId: azureCreateEmbedding
      parameters:
        - name: deployment-id
          in: path
          required: true
          schema:
            type: string
          description: Azure deployment ID
        - name: api-version
          in: query
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - input
              properties:
                model:
                  type: string
                  description: Model identifier
                  example: text-embedding-3-small
                input:
                  oneOf:
                    - type: string
                    - type: array
                      items:
                        type: string
                  description: Input text to embed
                encoding_format:
                  type: string
                  enum:
                    - float
                    - base64
                dimensions:
                  type: integer
                  description: Number of dimensions for the embedding
                user:
                  type: string
                fallbacks:
                  type: array
                  items:
                    type: string
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
                        index:
                          type: integer
                        object:
                          type: string
                        embedding:
                          oneOf:
                            - type: string
                            - type: array
                              items:
                                type: number
                            - type: array
                              items:
                                type: array
                                items:
                                  type: number
                  model:
                    type: string
                  object:
                    type: string
                  usage:
                    type: object
                    description: Token usage information
                    properties:
                      prompt_tokens:
                        type: integer
                      prompt_tokens_details:
                        type: object
                        properties:
                          text_tokens:
                            type: integer
                          audio_tokens:
                            type: integer
                          image_tokens:
                            type: integer
                          cached_tokens:
                            type: integer
                      completion_tokens:
                        type: integer
                      completion_tokens_details:
                        type: object
                        properties:
                          text_tokens:
                            type: integer
                          accepted_prediction_tokens:
                            type: integer
                          audio_tokens:
                            type: integer
                          citation_tokens:
                            type: integer
                          num_search_queries:
                            type: integer
                          reasoning_tokens:
                            type: integer
                          image_tokens:
                            type: integer
                          rejected_prediction_tokens:
                            type: integer
                          cached_tokens:
                            type: integer
                      total_tokens:
                        type: integer
                      cost:
                        type: object
                        description: Cost breakdown for the request
                        properties:
                          input_tokens_cost:
                            type: number
                          output_tokens_cost:
                            type: number
                          request_cost:
                            type: number
                          total_cost:
                            type: number
                  extra_fields:
                    type: object
                    description: Additional fields included in responses
                    properties:
                      request_type:
                        type: string
                        description: Type of request that was made
                      provider:
                        type: string
                        description: AI model provider identifier
                        enum:
                          - openai
                          - azure
                          - anthropic
                          - bedrock
                          - cohere
                          - vertex
                          - mistral
                          - ollama
                          - groq
                          - sgl
                          - parasail
                          - perplexity
                          - cerebras
                          - gemini
                          - openrouter
                          - elevenlabs
                          - huggingface
                          - nebius
                          - xai
                      model_requested:
                        type: string
                        description: The model that was requested
                      model_deployment:
                        type: string
                        description: The actual model deployment used
                      latency:
                        type: integer
                        format: int64
                        description: Request latency in milliseconds
                      chunk_index:
                        type: integer
                        description: Index of the chunk for streaming responses
                      raw_request:
                        type: object
                        description: Raw request if enabled
                      raw_response:
                        type: object
                        description: Raw response if enabled
                      cache_debug:
                        type: object
                        properties:
                          cache_hit:
                            type: boolean
                          cache_id:
                            type: string
                          hit_type:
                            type: string
                          provider_used:
                            type: string
                          model_used:
                            type: string
                          input_tokens:
                            type: integer
                          threshold:
                            type: number
                          similarity:
                            type: number
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                description: Error response from Bifrost
                properties:
                  event_id:
                    type: string
                  type:
                    type: string
                  is_bifrost_error:
                    type: boolean
                  status_code:
                    type: integer
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                      code:
                        type: string
                      message:
                        type: string
                      param:
                        type: string
                      event_id:
                        type: string
                  extra_fields:
                    type: object
                    properties:
                      provider:
                        type: string
                        description: AI model provider identifier
                        enum:
                          - openai
                          - azure
                          - anthropic
                          - bedrock
                          - cohere
                          - vertex
                          - mistral
                          - ollama
                          - groq
                          - sgl
                          - parasail
                          - perplexity
                          - cerebras
                          - gemini
                          - openrouter
                          - elevenlabs
                          - huggingface
                          - nebius
                          - xai
                      model_requested:
                        type: string
                      request_type:
                        type: string
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                description: Error response from Bifrost
                properties:
                  event_id:
                    type: string
                  type:
                    type: string
                  is_bifrost_error:
                    type: boolean
                  status_code:
                    type: integer
                  error:
                    type: object
                    properties:
                      type:
                        type: string
                      code:
                        type: string
                      message:
                        type: string
                      param:
                        type: string
                      event_id:
                        type: string
                  extra_fields:
                    type: object
                    properties:
                      provider:
                        type: string
                        description: AI model provider identifier
                        enum:
                          - openai
                          - azure
                          - anthropic
                          - bedrock
                          - cohere
                          - vertex
                          - mistral
                          - ollama
                          - groq
                          - sgl
                          - parasail
                          - perplexity
                          - cerebras
                          - gemini
                          - openrouter
                          - elevenlabs
                          - huggingface
                          - nebius
                          - xai
                      model_requested:
                        type: string
                      request_type:
                        type: string

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt