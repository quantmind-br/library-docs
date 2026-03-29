---
title: Update a provider
url: https://docs.getbifrost.ai/api-reference/providers/update-a-provider.md
source: llms
fetched_at: 2026-01-21T19:40:36.693216812-03:00
rendered_js: false
word_count: 134
summary: This document describes the API endpoint for updating a provider's configuration in the Bifrost gateway, requiring a full replacement of all configuration fields.
tags:
    - bifrost-api
    - provider-management
    - api-reference
    - configuration-update
    - ai-gateway
category: api
---

# Update a provider

> Updates a provider's configuration. Expects ALL fields to be provided,
including both edited and non-edited fields. Partial updates are not supported.




## OpenAPI

````yaml openapi/openapi.json put /api/providers/{provider}
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
  /api/providers/{provider}:
    put:
      tags:
        - Providers
      summary: Update a provider
      description: >
        Updates a provider's configuration. Expects ALL fields to be provided,

        including both edited and non-edited fields. Partial updates are not
        supported.
      operationId: updateProvider
      parameters:
        - name: provider
          in: path
          required: true
          description: Provider name
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: Update provider request
              properties:
                keys:
                  type: array
                  items:
                    type: object
                    description: API key configuration
                    properties:
                      id:
                        type: string
                        description: Unique identifier for the key
                      name:
                        type: string
                        description: Name of the key
                      value:
                        type: object
                        description: API key value (redacted in responses)
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
                        description: List of models this key can access
                      weight:
                        type: number
                        description: Weight for load balancing
                      azure_key_config:
                        type: object
                        description: Azure-specific key configuration
                        properties:
                          endpoint:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          deployments:
                            type: object
                            additionalProperties:
                              type: string
                          api_version:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          client_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          client_secret:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          tenant_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                      vertex_key_config:
                        type: object
                        description: Vertex-specific key configuration
                        properties:
                          project_id:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          project_number:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          region:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          auth_credentials:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          deployments:
                            type: object
                            additionalProperties:
                              type: string
                      bedrock_key_config:
                        type: object
                        description: AWS Bedrock-specific key configuration
                        properties:
                          access_key:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          secret_key:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          session_token:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          region:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          arn:
                            type: object
                            description: Environment variable configuration
                            properties:
                              value:
                                type: string
                              env_var:
                                type: string
                              from_env:
                                type: boolean
                          deployments:
                            type: object
                            additionalProperties:
                              type: string
                          batch_s3_config:
                            type: object
                            properties:
                              buckets:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    bucket_name:
                                      type: string
                                    prefix:
                                      type: string
                                    is_default:
                                      type: boolean
                      huggingface_key_config:
                        type: object
                        description: Hugging Face-specific key configuration
                        properties:
                          deployments:
                            type: object
                            additionalProperties:
                              type: string
                      enabled:
                        type: boolean
                      use_for_batch_api:
                        type: boolean
                network_config:
                  type: object
                  description: Network configuration for provider connections
                  properties:
                    base_url:
                      type: string
                      description: Base URL for the provider (optional)
                    extra_headers:
                      type: object
                      additionalProperties:
                        type: string
                      description: Additional headers to include in requests
                    default_request_timeout_in_seconds:
                      type: integer
                      description: Default timeout for requests
                    max_retries:
                      type: integer
                      description: Maximum number of retries
                    retry_backoff_initial:
                      type: integer
                      format: int64
                      description: Initial backoff duration in milliseconds
                    retry_backoff_max:
                      type: integer
                      format: int64
                      description: Maximum backoff duration in milliseconds
                concurrency_and_buffer_size:
                  type: object
                  description: Concurrency settings
                  properties:
                    concurrency:
                      type: integer
                      description: Number of concurrent operations
                    buffer_size:
                      type: integer
                      description: Size of the buffer
                proxy_config:
                  type: object
                  description: Proxy configuration
                  properties:
                    type:
                      type: string
                      enum:
                        - none
                        - http
                        - socks5
                        - environment
                    url:
                      type: string
                    username:
                      type: string
                    password:
                      type: string
                    ca_cert_pem:
                      type: string
                send_back_raw_request:
                  type: boolean
                send_back_raw_response:
                  type: boolean
                custom_provider_config:
                  type: object
                  description: Custom provider configuration
                  properties:
                    is_key_less:
                      type: boolean
                    base_provider_type:
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
                    allowed_requests:
                      type: object
                      description: Allowed request types for custom providers
                      properties:
                        list_models:
                          type: boolean
                        text_completion:
                          type: boolean
                        text_completion_stream:
                          type: boolean
                        chat_completion:
                          type: boolean
                        chat_completion_stream:
                          type: boolean
                        responses:
                          type: boolean
                        responses_stream:
                          type: boolean
                        count_tokens:
                          type: boolean
                        embedding:
                          type: boolean
                        speech:
                          type: boolean
                        speech_stream:
                          type: boolean
                        transcription:
                          type: boolean
                        transcription_stream:
                          type: boolean
                        image_generation:
                          type: boolean
                        image_generation_stream:
                          type: boolean
                        batch_create:
                          type: boolean
                        batch_list:
                          type: boolean
                        batch_retrieve:
                          type: boolean
                        batch_cancel:
                          type: boolean
                        batch_results:
                          type: boolean
                        file_upload:
                          type: boolean
                        file_list:
                          type: boolean
                        file_retrieve:
                          type: boolean
                        file_delete:
                          type: boolean
                        file_content:
                          type: boolean
                    request_path_overrides:
                      type: object
                      additionalProperties:
                        type: string
      responses:
        '200':
          description: Provider updated successfully
          content:
            application/json:
              schema:
                type: object
                description: Provider configuration response
                properties:
                  name:
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
                  keys:
                    type: array
                    items:
                      type: object
                      description: API key configuration
                      properties:
                        id:
                          type: string
                          description: Unique identifier for the key
                        name:
                          type: string
                          description: Name of the key
                        value:
                          type: object
                          description: API key value (redacted in responses)
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
                          description: List of models this key can access
                        weight:
                          type: number
                          description: Weight for load balancing
                        azure_key_config:
                          type: object
                          description: Azure-specific key configuration
                          properties:
                            endpoint:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            deployments:
                              type: object
                              additionalProperties:
                                type: string
                            api_version:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            client_id:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            client_secret:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            tenant_id:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                        vertex_key_config:
                          type: object
                          description: Vertex-specific key configuration
                          properties:
                            project_id:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            project_number:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            region:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            auth_credentials:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            deployments:
                              type: object
                              additionalProperties:
                                type: string
                        bedrock_key_config:
                          type: object
                          description: AWS Bedrock-specific key configuration
                          properties:
                            access_key:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            secret_key:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            session_token:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            region:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            arn:
                              type: object
                              description: Environment variable configuration
                              properties:
                                value:
                                  type: string
                                env_var:
                                  type: string
                                from_env:
                                  type: boolean
                            deployments:
                              type: object
                              additionalProperties:
                                type: string
                            batch_s3_config:
                              type: object
                              properties:
                                buckets:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      bucket_name:
                                        type: string
                                      prefix:
                                        type: string
                                      is_default:
                                        type: boolean
                        huggingface_key_config:
                          type: object
                          description: Hugging Face-specific key configuration
                          properties:
                            deployments:
                              type: object
                              additionalProperties:
                                type: string
                        enabled:
                          type: boolean
                        use_for_batch_api:
                          type: boolean
                  network_config:
                    type: object
                    description: Network configuration for provider connections
                    properties:
                      base_url:
                        type: string
                        description: Base URL for the provider (optional)
                      extra_headers:
                        type: object
                        additionalProperties:
                          type: string
                        description: Additional headers to include in requests
                      default_request_timeout_in_seconds:
                        type: integer
                        description: Default timeout for requests
                      max_retries:
                        type: integer
                        description: Maximum number of retries
                      retry_backoff_initial:
                        type: integer
                        format: int64
                        description: Initial backoff duration in milliseconds
                      retry_backoff_max:
                        type: integer
                        format: int64
                        description: Maximum backoff duration in milliseconds
                  concurrency_and_buffer_size:
                    type: object
                    description: Concurrency settings
                    properties:
                      concurrency:
                        type: integer
                        description: Number of concurrent operations
                      buffer_size:
                        type: integer
                        description: Size of the buffer
                  proxy_config:
                    type: object
                    description: Proxy configuration
                    properties:
                      type:
                        type: string
                        enum:
                          - none
                          - http
                          - socks5
                          - environment
                      url:
                        type: string
                      username:
                        type: string
                      password:
                        type: string
                      ca_cert_pem:
                        type: string
                  send_back_raw_request:
                    type: boolean
                  send_back_raw_response:
                    type: boolean
                  custom_provider_config:
                    type: object
                    description: Custom provider configuration
                    properties:
                      is_key_less:
                        type: boolean
                      base_provider_type:
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
                      allowed_requests:
                        type: object
                        description: Allowed request types for custom providers
                        properties:
                          list_models:
                            type: boolean
                          text_completion:
                            type: boolean
                          text_completion_stream:
                            type: boolean
                          chat_completion:
                            type: boolean
                          chat_completion_stream:
                            type: boolean
                          responses:
                            type: boolean
                          responses_stream:
                            type: boolean
                          count_tokens:
                            type: boolean
                          embedding:
                            type: boolean
                          speech:
                            type: boolean
                          speech_stream:
                            type: boolean
                          transcription:
                            type: boolean
                          transcription_stream:
                            type: boolean
                          image_generation:
                            type: boolean
                          image_generation_stream:
                            type: boolean
                          batch_create:
                            type: boolean
                          batch_list:
                            type: boolean
                          batch_retrieve:
                            type: boolean
                          batch_cancel:
                            type: boolean
                          batch_results:
                            type: boolean
                          file_upload:
                            type: boolean
                          file_list:
                            type: boolean
                          file_retrieve:
                            type: boolean
                          file_delete:
                            type: boolean
                          file_content:
                            type: boolean
                      request_path_overrides:
                        type: object
                        additionalProperties:
                          type: string
                  status:
                    type: string
                    enum:
                      - active
                      - error
                      - deleted
                    description: Status of the provider
                  config_hash:
                    type: string
                    description: Hash of config.json version, used for change detection
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