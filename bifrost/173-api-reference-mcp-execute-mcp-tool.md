---
title: Execute MCP tool
url: https://docs.getbifrost.ai/api-reference/mcp/execute-mcp-tool.md
source: llms
fetched_at: 2026-01-21T19:39:55.195658017-03:00
rendered_js: false
word_count: 121
summary: This document defines the API endpoint for executing Model Context Protocol (MCP) tools and retrieving results using chat or response formats.
tags:
    - mcp
    - tool-execution
    - api-reference
    - model-context-protocol
    - bifrost-api
category: api
---

# Execute MCP tool

> Executes an MCP tool and returns the result.



## OpenAPI

````yaml openapi/openapi.json post /v1/mcp/tool/execute
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
  /v1/mcp/tool/execute:
    post:
      tags:
        - MCP
      summary: Execute MCP tool
      description: Executes an MCP tool and returns the result.
      operationId: executeMCPTool
      parameters:
        - name: format
          in: query
          required: false
          description: |
            Format of the tool execution request/response.
          schema:
            type: string
            enum:
              - chat
              - responses
            default: chat
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - type: object
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
                  title: Chat (Default)
                  description: Chat format - uses ChatAssistantMessageToolCall schema
                - type: object
                  description: Responses format - uses ResponsesToolMessage schema
                  required:
                    - name
                  properties:
                    call_id:
                      type: string
                      description: Common call ID for tool calls and outputs
                    name:
                      type: string
                      description: Tool function name (required for execution)
                    arguments:
                      type: string
                      description: Tool function arguments as JSON string
                    output:
                      type: object
                      description: Tool execution output
                      additionalProperties: true
                    action:
                      type: object
                      description: Tool action configuration
                      additionalProperties: true
                    error:
                      type: string
                      description: Error message if tool execution failed
                  title: Responses
              description: >
                MCP tool execution request. The schema depends on the `format`
                query parameter:

                - `format=chat` or empty (default): Use
                `ChatAssistantMessageToolCall` schema

                - `format=responses`: Use `ResponsesToolMessage` schema
            examples:
              chat:
                summary: Chat format example
                value:
                  id: call_123
                  type: function
                  function:
                    name: get_weather
                    arguments: '{"location": "San Francisco"}'
              responses:
                summary: Responses format example
                value:
                  call_id: call_123
                  name: get_weather
                  arguments: '{"location": "San Francisco"}'
      responses:
        '200':
          description: Tool executed successfully
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
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
                                  description: Cache control settings for content blocks
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - ephemeral
                                    ttl:
                                      type: string
                                      description: Time to live (e.g., "1m", "1h")
                        description: >-
                          Message content - can be a string or array of content
                          blocks
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
                    title: Chat (Default)
                    description: Chat format response
                  - type: object
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
                                  description: Cache control settings for content blocks
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
                    title: Responses
                    description: Responses format response
                description: |
                  MCP tool execution response.
              examples:
                chat:
                  summary: Chat format response
                  value:
                    name: get_weather
                    role: tool
                    tool_call_id: call_123
                    content: The weather in San Francisco is 72°F and sunny.
                responses:
                  summary: Responses format response
                  value:
                    id: msg_123
                    type: function_call_output
                    status: completed
                    role: assistant
                    call_id: call_123
                    name: get_weather
                    arguments: '{"location": "San Francisco"}'
                    content: The weather in San Francisco is 72°F and sunny.
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