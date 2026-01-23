---
title: Get logs
url: https://docs.getbifrost.ai/api-reference/logging/get-logs.md
source: llms
fetched_at: 2026-01-21T19:39:49.575970849-03:00
rendered_js: false
word_count: 122
summary: This document describes the API endpoint for retrieving gateway logs with support for advanced filtering, search, and pagination. It details how to use query parameters to filter logs by provider, model, status, cost, and time range.
tags:
    - logging-api
    - bifrost-gateway
    - log-management
    - rest-api
    - api-monitoring
    - search-parameters
category: api
---

# Get logs

> Retrieves logs with filtering, search, and pagination via query parameters.




## OpenAPI

````yaml openapi/openapi.json get /api/logs
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
  /api/logs:
    get:
      tags:
        - Logging
      summary: Get logs
      description: >
        Retrieves logs with filtering, search, and pagination via query
        parameters.
      operationId: getLogs
      parameters:
        - name: providers
          in: query
          description: Comma-separated list of providers to filter by
          schema:
            type: string
        - name: models
          in: query
          description: Comma-separated list of models to filter by
          schema:
            type: string
        - name: status
          in: query
          description: Comma-separated list of statuses to filter by
          schema:
            type: string
        - name: objects
          in: query
          description: Comma-separated list of object types to filter by
          schema:
            type: string
        - name: selected_key_ids
          in: query
          description: Comma-separated list of selected key IDs to filter by
          schema:
            type: string
        - name: virtual_key_ids
          in: query
          description: Comma-separated list of virtual key IDs to filter by
          schema:
            type: string
        - name: start_time
          in: query
          description: Start time filter (RFC3339 format)
          schema:
            type: string
            format: date-time
        - name: end_time
          in: query
          description: End time filter (RFC3339 format)
          schema:
            type: string
            format: date-time
        - name: min_latency
          in: query
          description: Minimum latency filter
          schema:
            type: number
        - name: max_latency
          in: query
          description: Maximum latency filter
          schema:
            type: number
        - name: min_tokens
          in: query
          description: Minimum tokens filter
          schema:
            type: integer
        - name: max_tokens
          in: query
          description: Maximum tokens filter
          schema:
            type: integer
        - name: min_cost
          in: query
          description: Minimum cost filter
          schema:
            type: number
        - name: max_cost
          in: query
          description: Maximum cost filter
          schema:
            type: number
        - name: missing_cost_only
          in: query
          description: Only show logs with missing cost
          schema:
            type: boolean
        - name: content_search
          in: query
          description: Search in request/response content
          schema:
            type: string
        - name: limit
          in: query
          description: Number of logs to return (default 50, max 1000)
          schema:
            type: integer
            default: 50
            maximum: 1000
        - name: offset
          in: query
          description: Number of logs to skip
          schema:
            type: integer
            default: 0
        - name: sort_by
          in: query
          description: Field to sort by
          schema:
            type: string
            enum:
              - timestamp
              - latency
              - tokens
              - cost
            default: timestamp
        - name: order
          in: query
          description: Sort order
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                description: Search logs response
                properties:
                  logs:
                    type: array
                    items:
                      type: object
                      description: Log entry
                      properties:
                        id:
                          type: string
                        parent_request_id:
                          type: string
                        provider:
                          type: string
                        model:
                          type: string
                        status:
                          type: string
                          enum:
                            - processing
                            - success
                            - error
                        object:
                          type: string
                        timestamp:
                          type: string
                          format: date-time
                        number_of_retries:
                          type: integer
                        fallback_index:
                          type: integer
                        latency:
                          type: number
                        cost:
                          type: number
                        selected_key_id:
                          type: string
                        selected_key_name:
                          type: string
                        virtual_key_id:
                          type: string
                        virtual_key_name:
                          type: string
                          nullable: true
                        stream:
                          type: boolean
                        raw_request:
                          type: string
                        raw_response:
                          type: string
                        created_at:
                          type: string
                          format: date-time
                        token_usage:
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
                        error_details:
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
                        input_history:
                          type: array
                          items:
                            type: object
                            required:
                              - role
                            properties:
                              role:
                                type: string
                                enum:
                                  - assistant
                                  - user
                                  - system
                                  - tool
                                  - developer
                              name:
                                type: string
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
                                            - image_url
                                            - input_audio
                                            - file
                                            - refusal
                                        text:
                                          type: string
                                        refusal:
                                          type: string
                                        image_url:
                                          type: object
                                          required:
                                            - url
                                          properties:
                                            url:
                                              type: string
                                            detail:
                                              type: string
                                              enum:
                                                - low
                                                - high
                                                - auto
                                        input_audio:
                                          type: object
                                          required:
                                            - data
                                          properties:
                                            data:
                                              type: string
                                            format:
                                              type: string
                                        file:
                                          type: object
                                          properties:
                                            file_data:
                                              type: string
                                            file_id:
                                              type: string
                                            filename:
                                              type: string
                                            file_type:
                                              type: string
                                        cache_control:
                                          type: object
                                          description: >-
                                            Cache control settings for content
                                            blocks
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - ephemeral
                                            ttl:
                                              type: string
                                              description: Time to live (e.g., "1m", "1h")
                                description: >-
                                  Message content - can be a string or array of
                                  content blocks
                              tool_call_id:
                                type: string
                                description: For tool messages
                              refusal:
                                type: string
                              audio:
                                type: object
                                properties:
                                  id:
                                    type: string
                                  data:
                                    type: string
                                  expires_at:
                                    type: integer
                                  transcript:
                                    type: string
                              reasoning:
                                type: string
                              reasoning_details:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    id:
                                      type: string
                                    index:
                                      type: integer
                                    type:
                                      type: string
                                      enum:
                                        - reasoning.summary
                                        - reasoning.encrypted
                                        - reasoning.text
                                    summary:
                                      type: string
                                    text:
                                      type: string
                                    signature:
                                      type: string
                                    data:
                                      type: string
                              annotations:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                    url_citation:
                                      type: object
                                      properties:
                                        start_index:
                                          type: integer
                                        end_index:
                                          type: integer
                                        title:
                                          type: string
                                        url:
                                          type: string
                                        sources:
                                          type: object
                                        type:
                                          type: string
                              tool_calls:
                                type: array
                                items:
                                  type: object
                                  required:
                                    - function
                                  properties:
                                    index:
                                      type: integer
                                    type:
                                      type: string
                                    id:
                                      type: string
                                    function:
                                      type: object
                                      properties:
                                        name:
                                          type: string
                                        arguments:
                                          type: string
                        responses_input_history:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: string
                              type:
                                type: string
                                enum:
                                  - message
                                  - file_search_call
                                  - computer_call
                                  - computer_call_output
                                  - web_search_call
                                  - function_call
                                  - function_call_output
                                  - code_interpreter_call
                                  - local_shell_call
                                  - local_shell_call_output
                                  - mcp_call
                                  - custom_tool_call
                                  - custom_tool_call_output
                                  - image_generation_call
                                  - mcp_list_tools
                                  - mcp_approval_request
                                  - mcp_approval_responses
                                  - reasoning
                                  - item_reference
                                  - refusal
                              status:
                                type: string
                                enum:
                                  - in_progress
                                  - completed
                                  - incomplete
                                  - interpreting
                                  - failed
                              role:
                                type: string
                                enum:
                                  - assistant
                                  - user
                                  - system
                                  - developer
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
                                            - input_text
                                            - input_image
                                            - input_file
                                            - input_audio
                                            - output_text
                                            - refusal
                                            - reasoning_text
                                        file_id:
                                          type: string
                                        text:
                                          type: string
                                        signature:
                                          type: string
                                        image_url:
                                          type: string
                                        detail:
                                          type: string
                                        file_data:
                                          type: string
                                        file_url:
                                          type: string
                                        filename:
                                          type: string
                                        file_type:
                                          type: string
                                        input_audio:
                                          type: object
                                          required:
                                            - format
                                            - data
                                          properties:
                                            format:
                                              type: string
                                              enum:
                                                - mp3
                                                - wav
                                            data:
                                              type: string
                                        annotations:
                                          type: array
                                          items:
                                            type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - file_citation
                                                  - url_citation
                                                  - container_file_citation
                                                  - file_path
                                              index:
                                                type: integer
                                              file_id:
                                                type: string
                                              text:
                                                type: string
                                              start_index:
                                                type: integer
                                              end_index:
                                                type: integer
                                              filename:
                                                type: string
                                              title:
                                                type: string
                                              url:
                                                type: string
                                              container_id:
                                                type: string
                                        logprobs:
                                          type: array
                                          items:
                                            type: object
                                            properties:
                                              bytes:
                                                type: array
                                                items:
                                                  type: integer
                                              logprob:
                                                type: number
                                              token:
                                                type: string
                                              top_logprobs:
                                                type: array
                                                items:
                                                  type: object
                                                  properties:
                                                    bytes:
                                                      type: array
                                                      items:
                                                        type: integer
                                                    logprob:
                                                      type: number
                                                    token:
                                                      type: string
                                        refusal:
                                          type: string
                                        cache_control:
                                          type: object
                                          description: >-
                                            Cache control settings for content
                                            blocks
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - ephemeral
                                            ttl:
                                              type: string
                                              description: Time to live (e.g., "1m", "1h")
                              call_id:
                                type: string
                              name:
                                type: string
                              arguments:
                                type: string
                              output:
                                type: object
                              action:
                                type: object
                              error:
                                type: string
                              queries:
                                type: array
                                items:
                                  type: string
                              results:
                                type: array
                                items:
                                  type: object
                              summary:
                                type: array
                                items:
                                  type: object
                                  required:
                                    - type
                                    - text
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - summary_text
                                    text:
                                      type: string
                              encrypted_content:
                                type: string
                        output_message:
                          type: object
                          required:
                            - role
                          properties:
                            role:
                              type: string
                              enum:
                                - assistant
                                - user
                                - system
                                - tool
                                - developer
                            name:
                              type: string
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
                                          - image_url
                                          - input_audio
                                          - file
                                          - refusal
                                      text:
                                        type: string
                                      refusal:
                                        type: string
                                      image_url:
                                        type: object
                                        required:
                                          - url
                                        properties:
                                          url:
                                            type: string
                                          detail:
                                            type: string
                                            enum:
                                              - low
                                              - high
                                              - auto
                                      input_audio:
                                        type: object
                                        required:
                                          - data
                                        properties:
                                          data:
                                            type: string
                                          format:
                                            type: string
                                      file:
                                        type: object
                                        properties:
                                          file_data:
                                            type: string
                                          file_id:
                                            type: string
                                          filename:
                                            type: string
                                          file_type:
                                            type: string
                                      cache_control:
                                        type: object
                                        description: >-
                                          Cache control settings for content
                                          blocks
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - ephemeral
                                          ttl:
                                            type: string
                                            description: Time to live (e.g., "1m", "1h")
                              description: >-
                                Message content - can be a string or array of
                                content blocks
                            tool_call_id:
                              type: string
                              description: For tool messages
                            refusal:
                              type: string
                            audio:
                              type: object
                              properties:
                                id:
                                  type: string
                                data:
                                  type: string
                                expires_at:
                                  type: integer
                                transcript:
                                  type: string
                            reasoning:
                              type: string
                            reasoning_details:
                              type: array
                              items:
                                type: object
                                properties:
                                  id:
                                    type: string
                                  index:
                                    type: integer
                                  type:
                                    type: string
                                    enum:
                                      - reasoning.summary
                                      - reasoning.encrypted
                                      - reasoning.text
                                  summary:
                                    type: string
                                  text:
                                    type: string
                                  signature:
                                    type: string
                                  data:
                                    type: string
                            annotations:
                              type: array
                              items:
                                type: object
                                properties:
                                  type:
                                    type: string
                                  url_citation:
                                    type: object
                                    properties:
                                      start_index:
                                        type: integer
                                      end_index:
                                        type: integer
                                      title:
                                        type: string
                                      url:
                                        type: string
                                      sources:
                                        type: object
                                      type:
                                        type: string
                            tool_calls:
                              type: array
                              items:
                                type: object
                                required:
                                  - function
                                properties:
                                  index:
                                    type: integer
                                  type:
                                    type: string
                                  id:
                                    type: string
                                  function:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                      arguments:
                                        type: string
                        responses_output:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: string
                              type:
                                type: string
                                enum:
                                  - message
                                  - file_search_call
                                  - computer_call
                                  - computer_call_output
                                  - web_search_call
                                  - function_call
                                  - function_call_output
                                  - code_interpreter_call
                                  - local_shell_call
                                  - local_shell_call_output
                                  - mcp_call
                                  - custom_tool_call
                                  - custom_tool_call_output
                                  - image_generation_call
                                  - mcp_list_tools
                                  - mcp_approval_request
                                  - mcp_approval_responses
                                  - reasoning
                                  - item_reference
                                  - refusal
                              status:
                                type: string
                                enum:
                                  - in_progress
                                  - completed
                                  - incomplete
                                  - interpreting
                                  - failed
                              role:
                                type: string
                                enum:
                                  - assistant
                                  - user
                                  - system
                                  - developer
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
                                            - input_text
                                            - input_image
                                            - input_file
                                            - input_audio
                                            - output_text
                                            - refusal
                                            - reasoning_text
                                        file_id:
                                          type: string
                                        text:
                                          type: string
                                        signature:
                                          type: string
                                        image_url:
                                          type: string
                                        detail:
                                          type: string
                                        file_data:
                                          type: string
                                        file_url:
                                          type: string
                                        filename:
                                          type: string
                                        file_type:
                                          type: string
                                        input_audio:
                                          type: object
                                          required:
                                            - format
                                            - data
                                          properties:
                                            format:
                                              type: string
                                              enum:
                                                - mp3
                                                - wav
                                            data:
                                              type: string
                                        annotations:
                                          type: array
                                          items:
                                            type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - file_citation
                                                  - url_citation
                                                  - container_file_citation
                                                  - file_path
                                              index:
                                                type: integer
                                              file_id:
                                                type: string
                                              text:
                                                type: string
                                              start_index:
                                                type: integer
                                              end_index:
                                                type: integer
                                              filename:
                                                type: string
                                              title:
                                                type: string
                                              url:
                                                type: string
                                              container_id:
                                                type: string
                                        logprobs:
                                          type: array
                                          items:
                                            type: object
                                            properties:
                                              bytes:
                                                type: array
                                                items:
                                                  type: integer
                                              logprob:
                                                type: number
                                              token:
                                                type: string
                                              top_logprobs:
                                                type: array
                                                items:
                                                  type: object
                                                  properties:
                                                    bytes:
                                                      type: array
                                                      items:
                                                        type: integer
                                                    logprob:
                                                      type: number
                                                    token:
                                                      type: string
                                        refusal:
                                          type: string
                                        cache_control:
                                          type: object
                                          description: >-
                                            Cache control settings for content
                                            blocks
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - ephemeral
                                            ttl:
                                              type: string
                                              description: Time to live (e.g., "1m", "1h")
                              call_id:
                                type: string
                              name:
                                type: string
                              arguments:
                                type: string
                              output:
                                type: object
                              action:
                                type: object
                              error:
                                type: string
                              queries:
                                type: array
                                items:
                                  type: string
                              results:
                                type: array
                                items:
                                  type: object
                              summary:
                                type: array
                                items:
                                  type: object
                                  required:
                                    - type
                                    - text
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - summary_text
                                    text:
                                      type: string
                              encrypted_content:
                                type: string
                        embedding_output:
                          type: array
                          items:
                            type: array
                            items:
                              type: number
                        params:
                          type: object
                          additionalProperties: true
                        tools:
                          type: array
                          items:
                            type: object
                            required:
                              - type
                            properties:
                              type:
                                type: string
                                enum:
                                  - function
                                  - custom
                              function:
                                type: object
                                required:
                                  - name
                                properties:
                                  name:
                                    type: string
                                  description:
                                    type: string
                                  parameters:
                                    type: object
                                    properties:
                                      type:
                                        type: string
                                      description:
                                        type: string
                                      required:
                                        type: array
                                        items:
                                          type: string
                                      properties:
                                        type: object
                                        additionalProperties: true
                                      enum:
                                        type: array
                                        items:
                                          type: string
                                      additionalProperties:
                                        type: boolean
                                  strict:
                                    type: boolean
                              custom:
                                type: object
                                properties:
                                  format:
                                    type: object
                                    required:
                                      - type
                                    properties:
                                      type:
                                        type: string
                                      grammar:
                                        type: object
                                        required:
                                          - definition
                                          - syntax
                                        properties:
                                          definition:
                                            type: string
                                          syntax:
                                            type: string
                                            enum:
                                              - lark
                                              - regex
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
                        tool_calls:
                          type: array
                          items:
                            type: object
                            required:
                              - function
                            properties:
                              index:
                                type: integer
                              type:
                                type: string
                              id:
                                type: string
                              function:
                                type: object
                                properties:
                                  name:
                                    type: string
                                  arguments:
                                    type: string
                        speech_input:
                          type: object
                          additionalProperties: true
                        transcription_input:
                          type: object
                          additionalProperties: true
                        image_generation_input:
                          type: object
                          additionalProperties: true
                        speech_output:
                          type: object
                          additionalProperties: true
                        transcription_output:
                          type: object
                          additionalProperties: true
                        image_generation_output:
                          type: object
                          additionalProperties: true
                        cache_debug:
                          type: object
                          additionalProperties: true
                        selected_key:
                          type: object
                          additionalProperties: true
                        virtual_key:
                          type: object
                          additionalProperties: true
                  total:
                    type: integer
                  offset:
                    type: integer
                  limit:
                    type: integer
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