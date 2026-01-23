---
title: Count input tokens (LiteLLM - OpenAI format)
url: https://docs.getbifrost.ai/api-reference/litellm-integration/count-input-tokens-litellm--openai-format.md
source: llms
fetched_at: 2026-01-21T19:39:34.263803229-03:00
rendered_js: false
word_count: 129
summary: This document defines an API endpoint for calculating the number of input tokens in a LiteLLM-compatible OpenAI request format within the Bifrost gateway. It specifies the request structure and supported model identifiers for token counting across multiple AI providers.
tags:
    - litellm
    - openai-format
    - token-counting
    - api-specification
    - bifrost-api
    - inference-gateway
category: api
---

# Count input tokens (LiteLLM - OpenAI format)

> Counts the number of tokens in a Responses API request via LiteLLM.




## OpenAPI

````yaml openapi/openapi.json post /litellm/v1/responses/input_tokens
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
  /litellm/v1/responses/input_tokens:
    post:
      tags:
        - LiteLLM Integration
      summary: Count input tokens (LiteLLM - OpenAI format)
      description: |
        Counts the number of tokens in a Responses API request via LiteLLM.
      operationId: litellmOpenAICountInputTokens
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
                  example: gpt-4
                input:
                  oneOf:
                    - type: string
                    - type: array
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
                  description: Input - can be a string or array of messages
                stream:
                  type: boolean
                instructions:
                  type: string
                  description: System instructions for the model
                max_output_tokens:
                  type: integer
                metadata:
                  type: object
                  additionalProperties: true
                parallel_tool_calls:
                  type: boolean
                previous_response_id:
                  type: string
                reasoning:
                  type: object
                  properties:
                    effort:
                      type: string
                      enum:
                        - none
                        - minimal
                        - low
                        - medium
                        - high
                        - xhigh
                    generate_summary:
                      type: string
                      enum:
                        - auto
                        - concise
                        - detailed
                    summary:
                      type: string
                      enum:
                        - auto
                        - concise
                        - detailed
                    max_tokens:
                      type: integer
                store:
                  type: boolean
                temperature:
                  type: number
                  minimum: 0
                  maximum: 2
                text:
                  type: object
                  properties:
                    format:
                      type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - text
                            - json_object
                            - json_schema
                        json_schema:
                          type: object
                          properties:
                            name:
                              type: string
                            schema:
                              type: object
                            strict:
                              type: boolean
                tool_choice:
                  oneOf:
                    - type: string
                      enum:
                        - none
                        - auto
                        - required
                    - type: object
                      required:
                        - type
                      properties:
                        type:
                          type: string
                          enum:
                            - none
                            - auto
                            - any
                            - required
                            - function
                            - allowed_tools
                            - file_search
                            - web_search_preview
                            - computer_use_preview
                            - code_interpreter
                            - image_generation
                            - mcp
                            - custom
                        mode:
                          type: string
                        name:
                          type: string
                        server_label:
                          type: string
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
                                  - mcp
                                  - image_generation
                              name:
                                type: string
                              server_label:
                                type: string
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
                          - file_search
                          - computer_use_preview
                          - web_search
                          - mcp
                          - code_interpreter
                          - image_generation
                          - local_shell
                          - custom
                          - web_search_preview
                      name:
                        type: string
                      description:
                        type: string
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
                      vector_store_ids:
                        type: array
                        items:
                          type: string
                      filters:
                        type: object
                      max_num_results:
                        type: integer
                      ranking_options:
                        type: object
                      display_height:
                        type: integer
                      display_width:
                        type: integer
                      environment:
                        type: string
                      enable_zoom:
                        type: boolean
                      search_context_size:
                        type: string
                      user_location:
                        type: object
                      server_label:
                        type: string
                      server_url:
                        type: string
                      allowed_tools:
                        type: object
                      authorization:
                        type: string
                      connector_id:
                        type: string
                      headers:
                        type: object
                        additionalProperties:
                          type: string
                      require_approval:
                        type: object
                      server_description:
                        type: string
                      container:
                        type: object
                      background:
                        type: string
                      input_fidelity:
                        type: string
                      input_image_mask:
                        type: object
                      moderation:
                        type: string
                      output_compression:
                        type: integer
                      output_format:
                        type: string
                      partial_images:
                        type: integer
                      quality:
                        type: string
                      size:
                        type: string
                      format:
                        type: object
                top_p:
                  type: number
                truncation:
                  type: string
                  enum:
                    - auto
                    - disabled
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
                  object:
                    type: string
                  model:
                    type: string
                  input_tokens:
                    type: integer
                  input_tokens_details:
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
                  tokens:
                    type: array
                    items:
                      type: integer
                  token_strings:
                    type: array
                    items:
                      type: string
                  output_tokens:
                    type: integer
                  total_tokens:
                    type: integer
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