---
title: Update configuration
url: https://docs.getbifrost.ai/api-reference/configuration/update-configuration.md
source: llms
fetched_at: 2026-01-21T19:38:31.866596156-03:00
rendered_js: false
word_count: 132
summary: This document details the API endpoint for updating the Bifrost gateway configuration, supporting both hot-reloadable and restart-required settings for the AI inference gateway.
tags:
    - bifrost
    - api-configuration
    - gateway-management
    - hot-reloading
    - inference-gateway
    - configuration-management
category: api
---

# Update configuration

> Updates the Bifrost configuration. Supports hot-reloading of certain settings
like drop_excess_requests. Some settings may require a restart to take effect.




## OpenAPI

````yaml openapi/openapi.json put /api/config
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
  /api/config:
    put:
      tags:
        - Configuration
      summary: Update configuration
      description: >
        Updates the Bifrost configuration. Supports hot-reloading of certain
        settings

        like drop_excess_requests. Some settings may require a restart to take
        effect.
      operationId: updateConfig
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: Update configuration request
              properties:
                client_config:
                  type: object
                  description: Client configuration
                  properties:
                    drop_excess_requests:
                      type: boolean
                      description: Whether to drop excess requests when rate limited
                    prometheus_labels:
                      type: array
                      items:
                        type: string
                      description: Custom Prometheus labels
                    allowed_origins:
                      type: array
                      items:
                        type: string
                      description: Allowed CORS origins
                    initial_pool_size:
                      type: integer
                      description: Initial connection pool size
                    enable_logging:
                      type: boolean
                      description: Whether logging is enabled
                    disable_content_logging:
                      type: boolean
                      description: Whether content logging is disabled
                    enable_governance:
                      type: boolean
                      description: Whether governance is enabled
                    enforce_governance_header:
                      type: boolean
                      description: Whether to enforce governance header
                    allow_direct_keys:
                      type: boolean
                      description: Whether to allow direct API keys
                    max_request_body_size_mb:
                      type: integer
                      description: Maximum request body size in MB
                    enable_litellm_fallbacks:
                      type: boolean
                      description: Whether LiteLLM fallbacks are enabled
                    log_retention_days:
                      type: integer
                      description: Number of days to retain logs
                    header_filter_config:
                      type: object
                      description: Header filter configuration
                      properties:
                        allowlist:
                          type: array
                          items:
                            type: string
                        denylist:
                          type: array
                          items:
                            type: string
                    mcp_agent_depth:
                      type: integer
                      description: Depth of MCP agent
                    mcp_tool_execution_timeout:
                      type: integer
                      description: Timeout for MCP tool execution in seconds
                    mcp_code_mode_binding_level:
                      type: string
                      description: Binding level for MCP code mode
                framework_config:
                  type: object
                  description: Framework configuration
                  properties:
                    id:
                      type: integer
                      description: Unique identifier for the framework config
                    pricing_url:
                      type: string
                      description: URL for pricing data
                    pricing_sync_interval:
                      type: integer
                      format: int64
                      description: Pricing sync interval in seconds
                auth_config:
                  type: object
                  description: Authentication configuration
                  properties:
                    admin_username:
                      type: string
                    admin_password:
                      type: string
                      description: Password (redacted as <redacted> in responses)
                    is_enabled:
                      type: boolean
                    disable_auth_on_inference:
                      type: boolean
      responses:
        '200':
          description: Configuration updated successfully
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