---
title: Chat with model (LangChain - Cohere format)
url: https://docs.getbifrost.ai/api-reference/langchain-integration/chat-with-model-langchain--cohere-format.md
source: llms
fetched_at: 2026-01-21T19:39:12.237636703-03:00
rendered_js: false
word_count: 126
summary: This document specifies the API endpoint for performing chat completions using the Cohere-compatible format via LangChain through the Bifrost gateway.
tags:
    - langchain
    - cohere
    - chat-completions
    - api-gateway
    - ai-inference
category: api
---

# Chat with model (LangChain - Cohere format)

> Sends a chat request using Cohere-compatible format via LangChain.




## OpenAPI

````yaml openapi/openapi.json post /langchain/cohere/v2/chat
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
  /langchain/cohere/v2/chat:
    post:
      tags:
        - LangChain Integration
      summary: Chat with model (LangChain - Cohere format)
      description: |
        Sends a chat request using Cohere-compatible format via LangChain.
      operationId: langchainCohereChat
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - messages
              properties:
                model:
                  type: string
                  description: Model to use for chat completion
                  example: command-r-plus
                messages:
                  type: array
                  items:
                    type: object
                    required:
                      - role
                    properties:
                      role:
                        type: string
                        enum:
                          - system
                          - user
                          - assistant
                          - tool
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
                        description: >-
                          Message content - can be a string or array of content
                          blocks
                      tool_calls:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            type:
                              type: string
                              enum:
                                - function
                            function:
                              type: object
                              properties:
                                name:
                                  type: string
                                arguments:
                                  type: string
                      tool_call_id:
                        type: string
                      tool_plan:
                        type: string
                        description: Chain-of-thought style reflection (assistant only)
                  description: Array of message objects
                tools:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - function
                      function:
                        type: object
                        properties:
                          name:
                            type: string
                          description:
                            type: string
                          parameters:
                            type: object
                tool_choice:
                  type: string
                  enum:
                    - AUTO
                    - NONE
                    - REQUIRED
                  description: >-
                    Tool choice mode - AUTO lets the model decide, NONE disables
                    tools, REQUIRED forces tool use
                temperature:
                  type: number
                  minimum: 0
                  maximum: 1
                p:
                  type: number
                  description: Top-p sampling
                k:
                  type: integer
                  description: Top-k sampling
                max_tokens:
                  type: integer
                stop_sequences:
                  type: array
                  items:
                    type: string
                frequency_penalty:
                  type: number
                presence_penalty:
                  type: number
                stream:
                  type: boolean
                safety_mode:
                  type: string
                  enum:
                    - CONTEXTUAL
                    - STRICT
                    - NONE
                log_probs:
                  type: boolean
                strict_tool_choice:
                  type: boolean
                thinking:
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - enabled
                        - disabled
                    token_budget:
                      type: integer
                      minimum: 1
                response_format:
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - text
                        - json_object
                      description: Response format type
                    schema:
                      type: object
                      description: >-
                        JSON schema for structured output (used with json_object
                        type)
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
                  finish_reason:
                    type: string
                    enum:
                      - COMPLETE
                      - STOP_SEQUENCE
                      - MAX_TOKENS
                      - TOOL_CALL
                      - ERROR
                      - TIMEOUT
                  message:
                    type: object
                    properties:
                      role:
                        type: string
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
                      tool_calls:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            type:
                              type: string
                              enum:
                                - function
                            function:
                              type: object
                              properties:
                                name:
                                  type: string
                                arguments:
                                  type: string
                      tool_plan:
                        type: string
                  usage:
                    type: object
                    properties:
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
                      cached_tokens:
                        type: integer
                        description: Cached tokens
                  logprobs:
                    type: array
                    items:
                      type: object
                      properties:
                        token_ids:
                          type: array
                          items:
                            type: integer
                          description: Token IDs of each token in text chunk
                        text:
                          type: string
                          description: Text chunk for log probabilities
                        logprobs:
                          type: array
                          items:
                            type: number
                          description: Log probability of each token
                    description: Log probabilities (if requested)
            text/event-stream:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - message-start
                      - content-start
                      - content-delta
                      - content-end
                      - tool-plan-delta
                      - tool-call-start
                      - tool-call-delta
                      - tool-call-end
                      - citation-start
                      - citation-end
                      - message-end
                      - debug
                    description: Type of streaming event
                  id:
                    type: string
                    description: Event ID (for message-start)
                  index:
                    type: integer
                    description: Index for indexed events
                  delta:
                    type: object
                    properties:
                      message:
                        type: object
                        properties:
                          role:
                            type: string
                            description: Message role (for message-start)
                          content:
                            oneOf:
                              - type: object
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
                                  thinking:
                                    type: string
                              - type: array
                                items:
                                  type: object
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
                                    thinking:
                                      type: string
                            description: Content for content events
                          tool_plan:
                            type: string
                            description: Tool plan content (for tool-plan-delta)
                          tool_calls:
                            oneOf:
                              - type: object
                                properties:
                                  id:
                                    type: string
                                  type:
                                    type: string
                                    enum:
                                      - function
                                  function:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                      arguments:
                                        type: string
                              - type: array
                                items:
                                  type: object
                                  properties:
                                    id:
                                      type: string
                                    type:
                                      type: string
                                      enum:
                                        - function
                                    function:
                                      type: object
                                      properties:
                                        name:
                                          type: string
                                        arguments:
                                          type: string
                            description: Tool calls (for tool-call events)
                          citations:
                            oneOf:
                              - type: object
                                properties:
                                  start:
                                    type: integer
                                    description: Start position of cited text
                                  end:
                                    type: integer
                                    description: End position of cited text
                                  text:
                                    type: string
                                    description: Cited text
                                  sources:
                                    type: array
                                    items:
                                      type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - tool
                                            - document
                                          description: Source type
                                        id:
                                          type: string
                                          description: Source ID (nullable)
                                        tool_output:
                                          type: object
                                          description: Tool output (for tool sources)
                                        document:
                                          type: object
                                          description: Document data (for document sources)
                                  content_index:
                                    type: integer
                                    description: Content index of the citation
                                  type:
                                    type: string
                                    enum:
                                      - TEXT_CONTENT
                                      - THINKING_CONTENT
                                      - PLAN
                                    description: Type of citation
                              - type: array
                                items:
                                  type: object
                                  properties:
                                    start:
                                      type: integer
                                      description: Start position of cited text
                                    end:
                                      type: integer
                                      description: End position of cited text
                                    text:
                                      type: string
                                      description: Cited text
                                    sources:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - tool
                                              - document
                                            description: Source type
                                          id:
                                            type: string
                                            description: Source ID (nullable)
                                          tool_output:
                                            type: object
                                            description: Tool output (for tool sources)
                                          document:
                                            type: object
                                            description: Document data (for document sources)
                                    content_index:
                                      type: integer
                                      description: Content index of the citation
                                    type:
                                      type: string
                                      enum:
                                        - TEXT_CONTENT
                                        - THINKING_CONTENT
                                        - PLAN
                                      description: Type of citation
                            description: Citations (for citation events)
                      finish_reason:
                        type: string
                        enum:
                          - COMPLETE
                          - STOP_SEQUENCE
                          - MAX_TOKENS
                          - TOOL_CALL
                          - ERROR
                          - TIMEOUT
                      usage:
                        type: object
                        properties:
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
                          cached_tokens:
                            type: integer
                            description: Cached tokens
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