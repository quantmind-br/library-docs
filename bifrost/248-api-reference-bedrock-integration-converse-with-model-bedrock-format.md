---
title: Converse with model (Bedrock format)
url: https://docs.getbifrost.ai/api-reference/bedrock-integration/converse-with-model-bedrock-format.md
source: llms
fetched_at: 2026-01-21T19:38:15.415913938-03:00
rendered_js: false
word_count: 128
summary: This document defines the API specification for interacting with AI models through the Bifrost gateway using the AWS Bedrock Converse format.
tags:
    - bedrock-integration
    - aws-bedrock
    - converse-api
    - ai-inference
    - bifrost-api
    - api-endpoint
category: api
---

# Converse with model (Bedrock format)

> Sends messages to a model using AWS Bedrock Converse API format.




## OpenAPI

````yaml openapi/openapi.json post /bedrock/model/{modelId}/converse
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
  /bedrock/model/{modelId}/converse:
    post:
      tags:
        - Bedrock Integration
      summary: Converse with model (Bedrock format)
      description: |
        Sends messages to a model using AWS Bedrock Converse API format.
      operationId: bedrockConverse
      parameters:
        - name: modelId
          in: path
          required: true
          schema:
            type: string
          description: Model ID (e.g., anthropic.claude-3-sonnet-20240229-v1:0)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
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
                        type: array
                        items:
                          type: object
                          properties:
                            text:
                              type: string
                            image:
                              type: object
                              properties:
                                format:
                                  type: string
                                  enum:
                                    - jpeg
                                    - png
                                    - gif
                                    - webp
                                source:
                                  type: object
                                  properties:
                                    bytes:
                                      type: string
                                      format: byte
                            document:
                              type: object
                              properties:
                                format:
                                  type: string
                                  enum:
                                    - pdf
                                    - csv
                                    - doc
                                    - docx
                                    - xls
                                    - xlsx
                                    - html
                                    - txt
                                    - md
                                name:
                                  type: string
                                source:
                                  type: object
                                  properties:
                                    bytes:
                                      type: string
                                      format: byte
                                    text:
                                      type: string
                                      description: >-
                                        Plain text content (for text-based
                                        documents)
                            toolUse:
                              type: object
                              properties:
                                toolUseId:
                                  type: string
                                name:
                                  type: string
                                input:
                                  type: object
                            toolResult:
                              type: object
                              properties:
                                toolUseId:
                                  type: string
                                content:
                                  type: array
                                  items:
                                    $ref: '#/components/schemas/BedrockContentBlock'
                                status:
                                  type: string
                                  enum:
                                    - success
                                    - error
                            guardContent:
                              type: object
                              properties:
                                text:
                                  type: object
                                  properties:
                                    text:
                                      type: string
                                    qualifiers:
                                      type: array
                                      items:
                                        type: string
                            reasoningContent:
                              type: object
                              properties:
                                reasoningText:
                                  type: object
                                  properties:
                                    text:
                                      type: string
                                    signature:
                                      type: string
                            json:
                              type: object
                              description: JSON content for tool call results
                            cachePoint:
                              type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - default
                  description: Array of messages for the conversation
                system:
                  type: array
                  items:
                    type: object
                    properties:
                      text:
                        type: string
                      guardContent:
                        type: object
                        properties:
                          text:
                            type: object
                            properties:
                              text:
                                type: string
                              qualifiers:
                                type: array
                                items:
                                  type: string
                      cachePoint:
                        type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - default
                  description: System messages/prompts
                inferenceConfig:
                  type: object
                  properties:
                    maxTokens:
                      type: integer
                    temperature:
                      type: number
                    topP:
                      type: number
                    stopSequences:
                      type: array
                      items:
                        type: string
                toolConfig:
                  type: object
                  properties:
                    tools:
                      type: array
                      items:
                        type: object
                        properties:
                          toolSpec:
                            type: object
                            properties:
                              name:
                                type: string
                              description:
                                type: string
                              inputSchema:
                                type: object
                                properties:
                                  json:
                                    type: object
                          cachePoint:
                            type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - default
                    toolChoice:
                      type: object
                      properties:
                        auto:
                          type: object
                        any:
                          type: object
                        tool:
                          type: object
                          properties:
                            name:
                              type: string
                guardrailConfig:
                  type: object
                  properties:
                    guardrailIdentifier:
                      type: string
                    guardrailVersion:
                      type: string
                    trace:
                      type: string
                      enum:
                        - enabled
                        - disabled
                additionalModelRequestFields:
                  type: object
                  description: Model-specific parameters
                additionalModelResponseFieldPaths:
                  type: array
                  items:
                    type: string
                performanceConfig:
                  type: object
                  properties:
                    latency:
                      type: string
                      enum:
                        - standard
                        - optimized
                promptVariables:
                  type: object
                  additionalProperties:
                    type: object
                    properties:
                      text:
                        type: string
                requestMetadata:
                  type: object
                  additionalProperties:
                    type: string
                serviceTier:
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - reserved
                        - priority
                        - default
                        - flex
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
                  output:
                    type: object
                    properties:
                      message:
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
                            type: array
                            items:
                              type: object
                              properties:
                                text:
                                  type: string
                                image:
                                  type: object
                                  properties:
                                    format:
                                      type: string
                                      enum:
                                        - jpeg
                                        - png
                                        - gif
                                        - webp
                                    source:
                                      type: object
                                      properties:
                                        bytes:
                                          type: string
                                          format: byte
                                document:
                                  type: object
                                  properties:
                                    format:
                                      type: string
                                      enum:
                                        - pdf
                                        - csv
                                        - doc
                                        - docx
                                        - xls
                                        - xlsx
                                        - html
                                        - txt
                                        - md
                                    name:
                                      type: string
                                    source:
                                      type: object
                                      properties:
                                        bytes:
                                          type: string
                                          format: byte
                                        text:
                                          type: string
                                          description: >-
                                            Plain text content (for text-based
                                            documents)
                                toolUse:
                                  type: object
                                  properties:
                                    toolUseId:
                                      type: string
                                    name:
                                      type: string
                                    input:
                                      type: object
                                toolResult:
                                  type: object
                                  properties:
                                    toolUseId:
                                      type: string
                                    content:
                                      type: array
                                      items:
                                        $ref: '#/components/schemas/BedrockContentBlock'
                                    status:
                                      type: string
                                      enum:
                                        - success
                                        - error
                                guardContent:
                                  type: object
                                  properties:
                                    text:
                                      type: object
                                      properties:
                                        text:
                                          type: string
                                        qualifiers:
                                          type: array
                                          items:
                                            type: string
                                reasoningContent:
                                  type: object
                                  properties:
                                    reasoningText:
                                      type: object
                                      properties:
                                        text:
                                          type: string
                                        signature:
                                          type: string
                                json:
                                  type: object
                                  description: JSON content for tool call results
                                cachePoint:
                                  type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - default
                  stopReason:
                    type: string
                    enum:
                      - end_turn
                      - tool_use
                      - max_tokens
                      - stop_sequence
                      - guardrail_intervened
                      - content_filtered
                  usage:
                    type: object
                    properties:
                      inputTokens:
                        type: integer
                      outputTokens:
                        type: integer
                      totalTokens:
                        type: integer
                      cacheReadInputTokens:
                        type: integer
                      cacheWriteInputTokens:
                        type: integer
                  metrics:
                    type: object
                    properties:
                      latencyMs:
                        type: integer
                  additionalModelResponseFields:
                    type: object
                  trace:
                    type: object
                  performanceConfig:
                    type: object
                    properties:
                      latency:
                        type: string
                        enum:
                          - standard
                          - optimized
                  serviceTier:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - reserved
                          - priority
                          - default
                          - flex
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  type:
                    type: string
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  type:
                    type: string
components:
  schemas:
    BedrockContentBlock:
      type: object
      properties:
        text:
          type: string
        image:
          type: object
          properties:
            format:
              type: string
              enum:
                - jpeg
                - png
                - gif
                - webp
            source:
              type: object
              properties:
                bytes:
                  type: string
                  format: byte
        document:
          type: object
          properties:
            format:
              type: string
              enum:
                - pdf
                - csv
                - doc
                - docx
                - xls
                - xlsx
                - html
                - txt
                - md
            name:
              type: string
            source:
              type: object
              properties:
                bytes:
                  type: string
                  format: byte
                text:
                  type: string
                  description: Plain text content (for text-based documents)
        toolUse:
          type: object
          properties:
            toolUseId:
              type: string
            name:
              type: string
            input:
              type: object
        toolResult:
          type: object
          properties:
            toolUseId:
              type: string
            content:
              type: array
              items:
                $ref: '#/components/schemas/BedrockContentBlock'
            status:
              type: string
              enum:
                - success
                - error
        guardContent:
          type: object
          properties:
            text:
              type: object
              properties:
                text:
                  type: string
                qualifiers:
                  type: array
                  items:
                    type: string
        reasoningContent:
          type: object
          properties:
            reasoningText:
              type: object
              properties:
                text:
                  type: string
                signature:
                  type: string
        json:
          type: object
          description: JSON content for tool call results
        cachePoint:
          type: object
          properties:
            type:
              type: string
              enum:
                - default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt