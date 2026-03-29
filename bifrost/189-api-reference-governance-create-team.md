---
title: Create team
url: https://docs.getbifrost.ai/api-reference/governance/create-team.md
source: llms
fetched_at: 2026-01-21T19:38:52.161919114-03:00
rendered_js: false
word_count: 118
summary: This document defines the API specification for creating a new team in the Bifrost gateway, including parameters for team naming, customer association, and budget constraints.
tags:
    - bifrost-api
    - governance
    - team-management
    - api-endpoint
    - budget-configuration
    - ai-gateway
category: api
---

# Create team

> Creates a new team.



## OpenAPI

````yaml openapi/openapi.json post /api/governance/teams
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
  /api/governance/teams:
    post:
      tags:
        - Governance
      summary: Create team
      description: Creates a new team.
      operationId: createTeam
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: Create team request
              required:
                - name
              properties:
                name:
                  type: string
                customer_id:
                  type: string
                budget:
                  type: object
                  description: Create budget request
                  required:
                    - max_limit
                    - reset_duration
                  properties:
                    max_limit:
                      type: number
                    reset_duration:
                      type: string
      responses:
        '200':
          description: Team created successfully
          content:
            application/json:
              schema:
                type: object
                description: Team operation response
                properties:
                  message:
                    type: string
                  team:
                    type: object
                    description: Team configuration
                    properties:
                      id:
                        type: string
                      name:
                        type: string
                      customer_id:
                        type: string
                      budget_id:
                        type: string
                      customer:
                        type: object
                        description: Customer configuration
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          budget_id:
                            type: string
                          budget:
                            type: object
                            description: Budget configuration
                            properties:
                              id:
                                type: string
                              max_limit:
                                type: number
                                description: Maximum budget in dollars
                              reset_duration:
                                type: string
                                description: >-
                                  Reset duration (e.g., "30s", "5m", "1h", "1d",
                                  "1w", "1M")
                              last_reset:
                                type: string
                                format: date-time
                              current_usage:
                                type: number
                              config_hash:
                                type: string
                                nullable: true
                              created_at:
                                type: string
                                format: date-time
                              updated_at:
                                type: string
                                format: date-time
                          teams:
                            type: array
                            items:
                              $ref: '#/components/schemas/Team'
                          virtual_keys:
                            type: array
                            items:
                              type: object
                              description: Virtual key configuration
                              properties:
                                id:
                                  type: string
                                name:
                                  type: string
                                value:
                                  type: string
                                description:
                                  type: string
                                is_active:
                                  type: boolean
                                provider_configs:
                                  type: array
                                  items:
                                    type: object
                                    description: Provider configuration for a virtual key
                                    properties:
                                      id:
                                        type: integer
                                      virtual_key_id:
                                        type: string
                                      provider:
                                        type: string
                                      weight:
                                        type: number
                                      allowed_models:
                                        type: array
                                        items:
                                          type: string
                                      budget_id:
                                        type: string
                                      rate_limit_id:
                                        type: string
                                      budget:
                                        type: object
                                        description: Budget configuration
                                        properties:
                                          id:
                                            type: string
                                          max_limit:
                                            type: number
                                            description: Maximum budget in dollars
                                          reset_duration:
                                            type: string
                                            description: >-
                                              Reset duration (e.g., "30s", "5m", "1h",
                                              "1d", "1w", "1M")
                                          last_reset:
                                            type: string
                                            format: date-time
                                          current_usage:
                                            type: number
                                          config_hash:
                                            type: string
                                            nullable: true
                                          created_at:
                                            type: string
                                            format: date-time
                                          updated_at:
                                            type: string
                                            format: date-time
                                      rate_limit:
                                        type: object
                                        description: Rate limit configuration
                                        properties:
                                          id:
                                            type: string
                                          token_max_limit:
                                            type: integer
                                            format: int64
                                          token_reset_duration:
                                            type: string
                                          token_current_usage:
                                            type: integer
                                            format: int64
                                          token_last_reset:
                                            type: string
                                            format: date-time
                                          request_max_limit:
                                            type: integer
                                            format: int64
                                            nullable: true
                                          request_reset_duration:
                                            type: string
                                            nullable: true
                                          request_current_usage:
                                            type: integer
                                            format: int64
                                          request_last_reset:
                                            type: string
                                            format: date-time
                                          config_hash:
                                            type: string
                                            nullable: true
                                          created_at:
                                            type: string
                                            format: date-time
                                          updated_at:
                                            type: string
                                            format: date-time
                                      keys:
                                        type: array
                                        items:
                                          type: object
                                          description: Table key configuration
                                          properties:
                                            id:
                                              type: integer
                                            name:
                                              type: string
                                            provider_id:
                                              type: integer
                                            provider:
                                              type: string
                                            key_id:
                                              type: string
                                            value:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                            models:
                                              type: array
                                              items:
                                                type: string
                                            weight:
                                              type: number
                                              nullable: true
                                            enabled:
                                              type: boolean
                                              default: true
                                              nullable: true
                                            use_for_batch_api:
                                              type: boolean
                                              default: false
                                              nullable: true
                                            created_at:
                                              type: string
                                              format: date-time
                                            updated_at:
                                              type: string
                                              format: date-time
                                            config_hash:
                                              type: string
                                              nullable: true
                                            azure_endpoint:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            azure_api_version:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            azure_client_id:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            azure_client_secret:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            azure_tenant_id:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            vertex_project_id:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            vertex_project_number:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            vertex_region:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            vertex_auth_credentials:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            bedrock_access_key:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            bedrock_secret_key:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            bedrock_session_token:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            bedrock_region:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                            bedrock_arn:
                                              type: object
                                              description: Environment variable configuration
                                              properties:
                                                value:
                                                  type: string
                                                env_var:
                                                  type: string
                                                from_env:
                                                  type: boolean
                                              nullable: true
                                mcp_configs:
                                  type: array
                                  items:
                                    type: object
                                    description: MCP configuration for a virtual key
                                    properties:
                                      id:
                                        type: integer
                                      mcp_client_name:
                                        type: string
                                      tools_to_execute:
                                        type: array
                                        items:
                                          type: string
                          config_hash:
                            type: string
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
                      budget:
                        type: object
                        description: Budget configuration
                        properties:
                          id:
                            type: string
                          max_limit:
                            type: number
                            description: Maximum budget in dollars
                          reset_duration:
                            type: string
                            description: >-
                              Reset duration (e.g., "30s", "5m", "1h", "1d",
                              "1w", "1M")
                          last_reset:
                            type: string
                            format: date-time
                          current_usage:
                            type: number
                          config_hash:
                            type: string
                            nullable: true
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
                      virtual_keys:
                        type: array
                        items:
                          type: object
                          description: Virtual key configuration
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            value:
                              type: string
                            description:
                              type: string
                            is_active:
                              type: boolean
                            provider_configs:
                              type: array
                              items:
                                type: object
                                description: Provider configuration for a virtual key
                                properties:
                                  id:
                                    type: integer
                                  virtual_key_id:
                                    type: string
                                  provider:
                                    type: string
                                  weight:
                                    type: number
                                  allowed_models:
                                    type: array
                                    items:
                                      type: string
                                  budget_id:
                                    type: string
                                  rate_limit_id:
                                    type: string
                                  budget:
                                    type: object
                                    description: Budget configuration
                                    properties:
                                      id:
                                        type: string
                                      max_limit:
                                        type: number
                                        description: Maximum budget in dollars
                                      reset_duration:
                                        type: string
                                        description: >-
                                          Reset duration (e.g., "30s", "5m", "1h",
                                          "1d", "1w", "1M")
                                      last_reset:
                                        type: string
                                        format: date-time
                                      current_usage:
                                        type: number
                                      config_hash:
                                        type: string
                                        nullable: true
                                      created_at:
                                        type: string
                                        format: date-time
                                      updated_at:
                                        type: string
                                        format: date-time
                                  rate_limit:
                                    type: object
                                    description: Rate limit configuration
                                    properties:
                                      id:
                                        type: string
                                      token_max_limit:
                                        type: integer
                                        format: int64
                                      token_reset_duration:
                                        type: string
                                      token_current_usage:
                                        type: integer
                                        format: int64
                                      token_last_reset:
                                        type: string
                                        format: date-time
                                      request_max_limit:
                                        type: integer
                                        format: int64
                                        nullable: true
                                      request_reset_duration:
                                        type: string
                                        nullable: true
                                      request_current_usage:
                                        type: integer
                                        format: int64
                                      request_last_reset:
                                        type: string
                                        format: date-time
                                      config_hash:
                                        type: string
                                        nullable: true
                                      created_at:
                                        type: string
                                        format: date-time
                                      updated_at:
                                        type: string
                                        format: date-time
                                  keys:
                                    type: array
                                    items:
                                      type: object
                                      description: Table key configuration
                                      properties:
                                        id:
                                          type: integer
                                        name:
                                          type: string
                                        provider_id:
                                          type: integer
                                        provider:
                                          type: string
                                        key_id:
                                          type: string
                                        value:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                        models:
                                          type: array
                                          items:
                                            type: string
                                        weight:
                                          type: number
                                          nullable: true
                                        enabled:
                                          type: boolean
                                          default: true
                                          nullable: true
                                        use_for_batch_api:
                                          type: boolean
                                          default: false
                                          nullable: true
                                        created_at:
                                          type: string
                                          format: date-time
                                        updated_at:
                                          type: string
                                          format: date-time
                                        config_hash:
                                          type: string
                                          nullable: true
                                        azure_endpoint:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        azure_api_version:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        azure_client_id:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        azure_client_secret:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        azure_tenant_id:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        vertex_project_id:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        vertex_project_number:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        vertex_region:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        vertex_auth_credentials:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        bedrock_access_key:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        bedrock_secret_key:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        bedrock_session_token:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        bedrock_region:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                                        bedrock_arn:
                                          type: object
                                          description: Environment variable configuration
                                          properties:
                                            value:
                                              type: string
                                            env_var:
                                              type: string
                                            from_env:
                                              type: boolean
                                          nullable: true
                            mcp_configs:
                              type: array
                              items:
                                type: object
                                description: MCP configuration for a virtual key
                                properties:
                                  id:
                                    type: integer
                                  mcp_client_name:
                                    type: string
                                  tools_to_execute:
                                    type: array
                                    items:
                                      type: string
                      profile:
                        type: object
                        additionalProperties: true
                      config:
                        type: object
                        additionalProperties: true
                      claims:
                        type: object
                        additionalProperties: true
                      config_hash:
                        type: string
                        nullable: true
                      created_at:
                        type: string
                        format: date-time
                      updated_at:
                        type: string
                        format: date-time
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
components:
  schemas:
    Team:
      type: object
      description: Team configuration
      properties:
        id:
          type: string
        name:
          type: string
        customer_id:
          type: string
        budget_id:
          type: string
        customer:
          type: object
          description: Customer configuration
          properties:
            id:
              type: string
            name:
              type: string
            budget_id:
              type: string
            budget:
              type: object
              description: Budget configuration
              properties:
                id:
                  type: string
                max_limit:
                  type: number
                  description: Maximum budget in dollars
                reset_duration:
                  type: string
                  description: Reset duration (e.g., "30s", "5m", "1h", "1d", "1w", "1M")
                last_reset:
                  type: string
                  format: date-time
                current_usage:
                  type: number
                config_hash:
                  type: string
                  nullable: true
                created_at:
                  type: string
                  format: date-time
                updated_at:
                  type: string
                  format: date-time
            teams:
              type: array
              items:
                $ref: '#/components/schemas/Team'
            virtual_keys:
              type: array
              items:
                type: object
                description: Virtual key configuration
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  value:
                    type: string
                  description:
                    type: string
                  is_active:
                    type: boolean
                  provider_configs:
                    type: array
                    items:
                      type: object
                      description: Provider configuration for a virtual key
                      properties:
                        id:
                          type: integer
                        virtual_key_id:
                          type: string
                        provider:
                          type: string
                        weight:
                          type: number
                        allowed_models:
                          type: array
                          items:
                            type: string
                        budget_id:
                          type: string
                        rate_limit_id:
                          type: string
                        budget:
                          type: object
                          description: Budget configuration
                          properties:
                            id:
                              type: string
                            max_limit:
                              type: number
                              description: Maximum budget in dollars
                            reset_duration:
                              type: string
                              description: >-
                                Reset duration (e.g., "30s", "5m", "1h", "1d",
                                "1w", "1M")
                            last_reset:
                              type: string
                              format: date-time
                            current_usage:
                              type: number
                            config_hash:
                              type: string
                              nullable: true
                            created_at:
                              type: string
                              format: date-time
                            updated_at:
                              type: string
                              format: date-time
                        rate_limit:
                          type: object
                          description: Rate limit configuration
                          properties:
                            id:
                              type: string
                            token_max_limit:
                              type: integer
                              format: int64
                            token_reset_duration:
                              type: string
                            token_current_usage:
                              type: integer
                              format: int64
                            token_last_reset:
                              type: string
                              format: date-time
                            request_max_limit:
                              type: integer
                              format: int64
                              nullable: true
                            request_reset_duration:
                              type: string
                              nullable: true
                            request_current_usage:
                              type: integer
                              format: int64
                            request_last_reset:
                              type: string
                              format: date-time
                            config_hash:
                              type: string
                              nullable: true
                            created_at:
                              type: string
                              format: date-time
                            updated_at:
                              type: string
                              format: date-time
                        keys:
                          type: array
                          items:
                            type: object
                            description: Table key configuration
                            properties:
                              id:
                                type: integer
                              name:
                                type: string
                              provider_id:
                                type: integer
                              provider:
                                type: string
                              key_id:
                                type: string
                              value:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                              models:
                                type: array
                                items:
                                  type: string
                              weight:
                                type: number
                                nullable: true
                              enabled:
                                type: boolean
                                default: true
                                nullable: true
                              use_for_batch_api:
                                type: boolean
                                default: false
                                nullable: true
                              created_at:
                                type: string
                                format: date-time
                              updated_at:
                                type: string
                                format: date-time
                              config_hash:
                                type: string
                                nullable: true
                              azure_endpoint:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              azure_api_version:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              azure_client_id:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              azure_client_secret:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              azure_tenant_id:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              vertex_project_id:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              vertex_project_number:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              vertex_region:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              vertex_auth_credentials:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              bedrock_access_key:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              bedrock_secret_key:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              bedrock_session_token:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              bedrock_region:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                              bedrock_arn:
                                type: object
                                description: Environment variable configuration
                                properties:
                                  value:
                                    type: string
                                  env_var:
                                    type: string
                                  from_env:
                                    type: boolean
                                nullable: true
                  mcp_configs:
                    type: array
                    items:
                      type: object
                      description: MCP configuration for a virtual key
                      properties:
                        id:
                          type: integer
                        mcp_client_name:
                          type: string
                        tools_to_execute:
                          type: array
                          items:
                            type: string
            config_hash:
              type: string
            created_at:
              type: string
              format: date-time
            updated_at:
              type: string
              format: date-time
        budget:
          type: object
          description: Budget configuration
          properties:
            id:
              type: string
            max_limit:
              type: number
              description: Maximum budget in dollars
            reset_duration:
              type: string
              description: Reset duration (e.g., "30s", "5m", "1h", "1d", "1w", "1M")
            last_reset:
              type: string
              format: date-time
            current_usage:
              type: number
            config_hash:
              type: string
              nullable: true
            created_at:
              type: string
              format: date-time
            updated_at:
              type: string
              format: date-time
        virtual_keys:
          type: array
          items:
            type: object
            description: Virtual key configuration
            properties:
              id:
                type: string
              name:
                type: string
              value:
                type: string
              description:
                type: string
              is_active:
                type: boolean
              provider_configs:
                type: array
                items:
                  type: object
                  description: Provider configuration for a virtual key
                  properties:
                    id:
                      type: integer
                    virtual_key_id:
                      type: string
                    provider:
                      type: string
                    weight:
                      type: number
                    allowed_models:
                      type: array
                      items:
                        type: string
                    budget_id:
                      type: string
                    rate_limit_id:
                      type: string
                    budget:
                      type: object
                      description: Budget configuration
                      properties:
                        id:
                          type: string
                        max_limit:
                          type: number
                          description: Maximum budget in dollars
                        reset_duration:
                          type: string
                          description: >-
                            Reset duration (e.g., "30s", "5m", "1h", "1d", "1w",
                            "1M")
                        last_reset:
                          type: string
                          format: date-time
                        current_usage:
                          type: number
                        config_hash:
                          type: string
                          nullable: true
                        created_at:
                          type: string
                          format: date-time
                        updated_at:
                          type: string
                          format: date-time
                    rate_limit:
                      type: object
                      description: Rate limit configuration
                      properties:
                        id:
                          type: string
                        token_max_limit:
                          type: integer
                          format: int64
                        token_reset_duration:
                          type: string
                        token_current_usage:
                          type: integer
                          format: int64
                        token_last_reset:
                          type: string
                          format: date-time
                        request_max_limit:
                          type: integer
                          format: int64
                          nullable: true
                        request_reset_duration:
                          type: string
                          nullable: true
                        request_current_usage:
                          type: integer
                          format: int64
                        request_last_reset:
                          type: string
                          format: date-time
                        config_hash:
                          type: string
                          nullable: true
                        created_at:
                          type: string
                          format: date-time
                        updated_at:
                          type: string
                          format: date-time
                    keys:
                      type: array
                      items:
                        type: object
                        description: Table key configuration
                        properties:
                          id:
                            type: integer
                          name:
                            type: string
                          provider_id:
                            type: integer
                          provider:
                            type: string
                          key_id:
                            type: string
                          value:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          models:
                            type: array
                            items:
                              type: string
                          weight:
                            type: number
                            nullable: true
                          enabled:
                            type: boolean
                            default: true
                            nullable: true
                          use_for_batch_api:
                            type: boolean
                            default: false
                            nullable: true
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
                          config_hash:
                            type: string
                            nullable: true
                          azure_endpoint:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          azure_api_version:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          azure_client_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          azure_client_secret:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          azure_tenant_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          vertex_project_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          vertex_project_number:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          vertex_region:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          vertex_auth_credentials:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          bedrock_access_key:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          bedrock_secret_key:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          bedrock_session_token:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          bedrock_region:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
                          bedrock_arn:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                            nullable: true
              mcp_configs:
                type: array
                items:
                  type: object
                  description: MCP configuration for a virtual key
                  properties:
                    id:
                      type: integer
                    mcp_client_name:
                      type: string
                    tools_to_execute:
                      type: array
                      items:
                        type: string
        profile:
          type: object
          additionalProperties: true
        config:
          type: object
          additionalProperties: true
        claims:
          type: object
          additionalProperties: true
        config_hash:
          type: string
          nullable: true
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt