---
title: Edit MCP client
url: https://docs.getbifrost.ai/api-reference/mcp/edit-mcp-client.md
source: llms
fetched_at: 2026-01-21T19:39:54.827605284-03:00
rendered_js: false
word_count: 119
summary: This document provides the API specification for updating an existing Model Context Protocol (MCP) client configuration within the Bifrost gateway.
tags:
    - mcp
    - api-reference
    - model-context-protocol
    - client-configuration
    - bifrost-gateway
    - endpoint-update
category: api
---

# Edit MCP client

> Updates an existing MCP client's configuration.



## OpenAPI

````yaml openapi/openapi.json put /api/mcp/client/{id}
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
  /api/mcp/client/{id}:
    put:
      tags:
        - MCP
      summary: Edit MCP client
      description: Updates an existing MCP client's configuration.
      operationId: editMCPClient
      parameters:
        - name: id
          in: path
          required: true
          description: MCP client ID
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: MCP client configuration
              properties:
                id:
                  type: string
                name:
                  type: string
                is_code_mode_client:
                  type: boolean
                connection_type:
                  type: string
                  enum:
                    - http
                    - stdio
                    - sse
                    - inprocess
                  description: Connection type for MCP client
                connection_string:
                  type: string
                  description: HTTP or SSE URL (required for HTTP or SSE connections)
                stdio_config:
                  type: object
                  description: STDIO configuration for MCP client
                  properties:
                    command:
                      type: string
                      description: Executable command to run
                    args:
                      type: array
                      items:
                        type: string
                      description: Command line arguments
                    envs:
                      type: array
                      items:
                        type: string
                      description: Environment variables required
                headers:
                  type: object
                  additionalProperties:
                    type: string
                tools_to_execute:
                  type: array
                  items:
                    type: string
                  description: |
                    Include-only list for tools.
                    ["*"] => all tools are included
                    [] => no tools are included
                    ["tool1", "tool2"] => include only the specified tools
                tools_to_auto_execute:
                  type: array
                  items:
                    type: string
                  description: |
                    Auto-execute list for tools.
                    ["*"] => all tools are included
                    [] => no tools are included
                    ["tool1", "tool2"] => auto-execute only the specified tools
      responses:
        '200':
          description: MCP client updated successfully
          content:
            application/json:
              schema:
                type: object
                description: Generic success response
                properties:
                  status:
                    type: string
                    example: success
                  message:
                    type: string
                    example: Operation completed successfully
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