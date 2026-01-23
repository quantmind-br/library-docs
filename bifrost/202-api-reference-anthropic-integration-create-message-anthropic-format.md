---
title: Create message (Anthropic format)
url: https://docs.getbifrost.ai/api-reference/anthropic-integration/create-message-anthropic-format.md
source: llms
fetched_at: 2026-01-21T19:37:52.483652313-03:00
rendered_js: false
word_count: 128
summary: This document defines the Bifrost API endpoint for creating messages using the Anthropic Messages API format, including support for streaming via Server-Sent Events (SSE). It details the request schema for model parameters, message structures, and various content types like text, images, and tool usage.
tags:
    - anthropic-api
    - message-creation
    - ai-inference
    - streaming-sse
    - api-integration
    - bifrost-gateway
category: api
---

# Create message (Anthropic format)

> Creates a message using Anthropic Messages API format.
Supports streaming via SSE.




## OpenAPI

````yaml openapi/openapi.json post /anthropic/v1/messages
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
  /anthropic/v1/messages:
    post:
      tags:
        - Anthropic Integration
      summary: Create message (Anthropic format)
      description: |
        Creates a message using Anthropic Messages API format.
        Supports streaming via SSE.
      operationId: anthropicCreateMessage
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - max_tokens
                - messages
              properties:
                model:
                  type: string
                  description: Model identifier (e.g., claude-3-opus-20240229)
                  example: claude-3-opus-20240229
                max_tokens:
                  type: integer
                  description: Maximum tokens to generate
                messages:
                  type: array
                  items:
                    type: object
                    required:
                      - role
                      - content
                    properties:
                      role:
                        type: string
                        enum:
                          - user
                          - assistant
                      content:
                        oneOf:
                          - type: string
                          - type: array
                            items:
                              type: object
                              required:
                                - type
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - text
                                    - image
                                    - document
                                    - tool_use
                                    - server_tool_use
                                    - tool_result
                                    - web_search_result
                                    - mcp_tool_use
                                    - mcp_tool_result
                                    - thinking
                                    - redacted_thinking
                                text:
                                  type: string
                                  description: For text content
                                thinking:
                                  type: string
                                  description: For thinking content
                                signature:
                                  type: string
                                  description: For signature content
                                data:
                                  type: string
                                  description: >-
                                    For data content (encrypted data for
                                    redacted thinking)
                                tool_use_id:
                                  type: string
                                  description: For tool_result content
                                id:
                                  type: string
                                  description: For tool_use content
                                name:
                                  type: string
                                  description: For tool_use content
                                input:
                                  type: object
                                  description: For tool_use content
                                server_name:
                                  type: string
                                  description: For mcp_tool_use content
                                content:
                                  $ref: '#/components/schemas/AnthropicContent'
                                  description: For tool_result content
                                source:
                                  type: object
                                  required:
                                    - type
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - base64
                                        - url
                                        - text
                                        - content_block
                                    media_type:
                                      type: string
                                      description: >-
                                        MIME type (e.g., image/jpeg,
                                        application/pdf)
                                    data:
                                      type: string
                                      description: Base64-encoded data (for base64 type)
                                    url:
                                      type: string
                                      description: URL (for url type)
                                  description: For image/document content
                                cache_control:
                                  type: object
                                  description: Cache control settings for content blocks
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - ephemeral
                                    ttl:
                                      type: string
                                      description: Time to live (e.g., "1m", "1h")
                                citations:
                                  type: object
                                  properties:
                                    enabled:
                                      type: boolean
                                  description: For document content
                                context:
                                  type: string
                                  description: For document content
                                title:
                                  type: string
                                  description: For document content
                        description: Content - can be a string or array of content blocks
                  description: List of messages in the conversation
                system:
                  oneOf:
                    - type: string
                    - type: array
                      items:
                        type: object
                        required:
                          - type
                        properties:
                          type:
                            type: string
                            enum:
                              - text
                              - image
                              - document
                              - tool_use
                              - server_tool_use
                              - tool_result
                              - web_search_result
                              - mcp_tool_use
                              - mcp_tool_result
                              - thinking
                              - redacted_thinking
                          text:
                            type: string
                            description: For text content
                          thinking:
                            type: string
                            description: For thinking content
                          signature:
                            type: string
                            description: For signature content
                          data:
                            type: string
                            description: >-
                              For data content (encrypted data for redacted
                              thinking)
                          tool_use_id:
                            type: string
                            description: For tool_result content
                          id:
                            type: string
                            description: For tool_use content
                          name:
                            type: string
                            description: For tool_use content
                          input:
                            type: object
                            description: For tool_use content
                          server_name:
                            type: string
                            description: For mcp_tool_use content
                          content:
                            $ref: '#/components/schemas/AnthropicContent'
                            description: For tool_result content
                          source:
                            type: object
                            required:
                              - type
                            properties:
                              type:
                                type: string
                                enum:
                                  - base64
                                  - url
                                  - text
                                  - content_block
                              media_type:
                                type: string
                                description: MIME type (e.g., image/jpeg, application/pdf)
                              data:
                                type: string
                                description: Base64-encoded data (for base64 type)
                              url:
                                type: string
                                description: URL (for url type)
                            description: For image/document content
                          cache_control:
                            type: object
                            description: Cache control settings for content blocks
                            properties:
                              type:
                                type: string
                                enum:
                                  - ephemeral
                              ttl:
                                type: string
                                description: Time to live (e.g., "1m", "1h")
                          citations:
                            type: object
                            properties:
                              enabled:
                                type: boolean
                            description: For document content
                          context:
                            type: string
                            description: For document content
                          title:
                            type: string
                            description: For document content
                  description: System prompt
                metadata:
                  type: object
                  properties:
                    user_id:
                      type: string
                stream:
                  type: boolean
                  description: Whether to stream the response
                temperature:
                  type: number
                  minimum: 0
                  maximum: 1
                top_p:
                  type: number
                top_k:
                  type: integer
                stop_sequences:
                  type: array
                  items:
                    type: string
                tools:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - custom
                          - bash_20250124
                          - computer_20250124
                          - computer_20251124
                          - code_execution_20250825
                          - text_editor_20250124
                          - text_editor_20250429
                          - text_editor_20250728
                          - web_search_20250305
                      name:
                        type: string
                        description: Tool name (for custom tools)
                      description:
                        type: string
                      input_schema:
                        type: object
                        description: JSON Schema for tool input
                      cache_control:
                        type: object
                        description: Cache control settings for content blocks
                        properties:
                          type:
                            type: string
                            enum:
                              - ephemeral
                          ttl:
                            type: string
                            description: Time to live (e.g., "1m", "1h")
                      display_width_px:
                        type: integer
                      display_height_px:
                        type: integer
                      display_number:
                        type: integer
                      enable_zoom:
                        type: boolean
                      max_uses:
                        type: integer
                      allowed_domains:
                        type: array
                        items:
                          type: string
                      blocked_domains:
                        type: array
                        items:
                          type: string
                      user_location:
                        type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - approximate
                          city:
                            type: string
                          country:
                            type: string
                          timezone:
                            type: string
                tool_choice:
                  oneOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - auto
                            - any
                            - tool
                            - none
                        name:
                          type: string
                          description: Required when type is 'tool'
                        disable_parallel_tool_use:
                          type: boolean
                mcp_servers:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                      name:
                        type: string
                      url:
                        type: string
                      authorization_token:
                        type: string
                        description: Authorization token for the MCP server
                      tool_configuration:
                        type: object
                        properties:
                          enabled:
                            type: boolean
                          allowed_tools:
                            type: array
                            items:
                              type: string
                  description: MCP servers configuration (requires beta header)
                thinking:
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - enabled
                        - disabled
                    budget_tokens:
                      type: integer
                output_format:
                  type: object
                  description: Structured output format (requires beta header)
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
                  id:
                    type: string
                  type:
                    type: string
                    default: message
                  role:
                    type: string
                    default: assistant
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
                            - image
                            - document
                            - tool_use
                            - server_tool_use
                            - tool_result
                            - web_search_result
                            - mcp_tool_use
                            - mcp_tool_result
                            - thinking
                            - redacted_thinking
                        text:
                          type: string
                          description: For text content
                        thinking:
                          type: string
                          description: For thinking content
                        signature:
                          type: string
                          description: For signature content
                        data:
                          type: string
                          description: >-
                            For data content (encrypted data for redacted
                            thinking)
                        tool_use_id:
                          type: string
                          description: For tool_result content
                        id:
                          type: string
                          description: For tool_use content
                        name:
                          type: string
                          description: For tool_use content
                        input:
                          type: object
                          description: For tool_use content
                        server_name:
                          type: string
                          description: For mcp_tool_use content
                        content:
                          $ref: '#/components/schemas/AnthropicContent'
                          description: For tool_result content
                        source:
                          type: object
                          required:
                            - type
                          properties:
                            type:
                              type: string
                              enum:
                                - base64
                                - url
                                - text
                                - content_block
                            media_type:
                              type: string
                              description: MIME type (e.g., image/jpeg, application/pdf)
                            data:
                              type: string
                              description: Base64-encoded data (for base64 type)
                            url:
                              type: string
                              description: URL (for url type)
                          description: For image/document content
                        cache_control:
                          type: object
                          description: Cache control settings for content blocks
                          properties:
                            type:
                              type: string
                              enum:
                                - ephemeral
                            ttl:
                              type: string
                              description: Time to live (e.g., "1m", "1h")
                        citations:
                          type: object
                          properties:
                            enabled:
                              type: boolean
                          description: For document content
                        context:
                          type: string
                          description: For document content
                        title:
                          type: string
                          description: For document content
                  model:
                    type: string
                  stop_reason:
                    type: string
                    enum:
                      - end_turn
                      - max_tokens
                      - stop_sequence
                      - tool_use
                      - pause_turn
                      - refusal
                      - model_context_window_exceeded
                      - null
                  stop_sequence:
                    type: string
                    nullable: true
                  usage:
                    type: object
                    properties:
                      input_tokens:
                        type: integer
                      output_tokens:
                        type: integer
                      cache_creation_input_tokens:
                        type: integer
                      cache_read_input_tokens:
                        type: integer
                      cache_creation:
                        type: object
                        properties:
                          ephemeral_5m_input_tokens:
                            type: integer
                          ephemeral_1h_input_tokens:
                            type: integer
            text/event-stream:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  type:
                    type: string
                    enum:
                      - message_start
                      - content_block_start
                      - content_block_delta
                      - content_block_stop
                      - message_delta
                      - message_stop
                      - ping
                      - error
                  message:
                    type: object
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        default: message
                      role:
                        type: string
                        default: assistant
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
                                - image
                                - document
                                - tool_use
                                - server_tool_use
                                - tool_result
                                - web_search_result
                                - mcp_tool_use
                                - mcp_tool_result
                                - thinking
                                - redacted_thinking
                            text:
                              type: string
                              description: For text content
                            thinking:
                              type: string
                              description: For thinking content
                            signature:
                              type: string
                              description: For signature content
                            data:
                              type: string
                              description: >-
                                For data content (encrypted data for redacted
                                thinking)
                            tool_use_id:
                              type: string
                              description: For tool_result content
                            id:
                              type: string
                              description: For tool_use content
                            name:
                              type: string
                              description: For tool_use content
                            input:
                              type: object
                              description: For tool_use content
                            server_name:
                              type: string
                              description: For mcp_tool_use content
                            content:
                              $ref: '#/components/schemas/AnthropicContent'
                              description: For tool_result content
                            source:
                              type: object
                              required:
                                - type
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - base64
                                    - url
                                    - text
                                    - content_block
                                media_type:
                                  type: string
                                  description: >-
                                    MIME type (e.g., image/jpeg,
                                    application/pdf)
                                data:
                                  type: string
                                  description: Base64-encoded data (for base64 type)
                                url:
                                  type: string
                                  description: URL (for url type)
                              description: For image/document content
                            cache_control:
                              type: object
                              description: Cache control settings for content blocks
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - ephemeral
                                ttl:
                                  type: string
                                  description: Time to live (e.g., "1m", "1h")
                            citations:
                              type: object
                              properties:
                                enabled:
                                  type: boolean
                              description: For document content
                            context:
                              type: string
                              description: For document content
                            title:
                              type: string
                              description: For document content
                      model:
                        type: string
                      stop_reason:
                        type: string
                        enum:
                          - end_turn
                          - max_tokens
                          - stop_sequence
                          - tool_use
                          - pause_turn
                          - refusal
                          - model_context_window_exceeded
                          - null
                      stop_sequence:
                        type: string
                        nullable: true
                      usage:
                        type: object
                        properties:
                          input_tokens:
                            type: integer
                          output_tokens:
                            type: integer
                          cache_creation_input_tokens:
                            type: integer
                          cache_read_input_tokens:
                            type: integer
                          cache_creation:
                            type: object
                            properties:
                              ephemeral_5m_input_tokens:
                                type: integer
                              ephemeral_1h_input_tokens:
                                type: integer
                  index:
                    type: integer
                  content_block:
                    type: object
                    required:
                      - type
                    properties:
                      type:
                        type: string
                        enum:
                          - text
                          - image
                          - document
                          - tool_use
                          - server_tool_use
                          - tool_result
                          - web_search_result
                          - mcp_tool_use
                          - mcp_tool_result
                          - thinking
                          - redacted_thinking
                      text:
                        type: string
                        description: For text content
                      thinking:
                        type: string
                        description: For thinking content
                      signature:
                        type: string
                        description: For signature content
                      data:
                        type: string
                        description: >-
                          For data content (encrypted data for redacted
                          thinking)
                      tool_use_id:
                        type: string
                        description: For tool_result content
                      id:
                        type: string
                        description: For tool_use content
                      name:
                        type: string
                        description: For tool_use content
                      input:
                        type: object
                        description: For tool_use content
                      server_name:
                        type: string
                        description: For mcp_tool_use content
                      content:
                        $ref: '#/components/schemas/AnthropicContent'
                        description: For tool_result content
                      source:
                        type: object
                        required:
                          - type
                        properties:
                          type:
                            type: string
                            enum:
                              - base64
                              - url
                              - text
                              - content_block
                          media_type:
                            type: string
                            description: MIME type (e.g., image/jpeg, application/pdf)
                          data:
                            type: string
                            description: Base64-encoded data (for base64 type)
                          url:
                            type: string
                            description: URL (for url type)
                        description: For image/document content
                      cache_control:
                        type: object
                        description: Cache control settings for content blocks
                        properties:
                          type:
                            type: string
                            enum:
                              - ephemeral
                          ttl:
                            type: string
                            description: Time to live (e.g., "1m", "1h")
                      citations:
                        type: object
                        properties:
                          enabled:
                            type: boolean
                        description: For document content
                      context:
                        type: string
                        description: For document content
                      title:
                        type: string
                        description: For document content
                  delta:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - text_delta
                          - input_json_delta
                          - thinking_delta
                          - signature_delta
                      text:
                        type: string
                      partial_json:
                        type: string
                      thinking:
                        type: string
                      signature:
                        type: string
                      stop_reason:
                        type: string
                      stop_sequence:
                        type: string
                  usage:
                    type: object
                    properties:
                      input_tokens:
                        type: integer
                      output_tokens:
                        type: integer
                      cache_creation_input_tokens:
                        type: integer
                      cache_read_input_tokens:
                        type: integer
                      cache_creation:
                        type: object
                        properties:
                          ephemeral_5m_input_tokens:
                            type: integer
                          ephemeral_1h_input_tokens:
                            type: integer
                  error:
                    type: object
                    properties:
                      message:
                        type: string
                      type:
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
components:
  schemas:
    AnthropicContent:
      oneOf:
        - type: string
        - type: array
          items:
            type: object
            required:
              - type
            properties:
              type:
                type: string
                enum:
                  - text
                  - image
                  - document
                  - tool_use
                  - server_tool_use
                  - tool_result
                  - web_search_result
                  - mcp_tool_use
                  - mcp_tool_result
                  - thinking
                  - redacted_thinking
              text:
                type: string
                description: For text content
              thinking:
                type: string
                description: For thinking content
              signature:
                type: string
                description: For signature content
              data:
                type: string
                description: For data content (encrypted data for redacted thinking)
              tool_use_id:
                type: string
                description: For tool_result content
              id:
                type: string
                description: For tool_use content
              name:
                type: string
                description: For tool_use content
              input:
                type: object
                description: For tool_use content
              server_name:
                type: string
                description: For mcp_tool_use content
              content:
                $ref: '#/components/schemas/AnthropicContent'
                description: For tool_result content
              source:
                type: object
                required:
                  - type
                properties:
                  type:
                    type: string
                    enum:
                      - base64
                      - url
                      - text
                      - content_block
                  media_type:
                    type: string
                    description: MIME type (e.g., image/jpeg, application/pdf)
                  data:
                    type: string
                    description: Base64-encoded data (for base64 type)
                  url:
                    type: string
                    description: URL (for url type)
                description: For image/document content
              cache_control:
                type: object
                description: Cache control settings for content blocks
                properties:
                  type:
                    type: string
                    enum:
                      - ephemeral
                  ttl:
                    type: string
                    description: Time to live (e.g., "1m", "1h")
              citations:
                type: object
                properties:
                  enabled:
                    type: boolean
                description: For document content
              context:
                type: string
                description: For document content
              title:
                type: string
                description: For document content
      description: Content - can be a string or array of content blocks

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt