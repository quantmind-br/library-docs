---
title: Embed content (Gemini format)
url: https://docs.getbifrost.ai/api-reference/genai-integration/embed-content-gemini-format.md
source: llms
fetched_at: 2026-01-21T19:38:42.85284441-03:00
rendered_js: false
word_count: 121
summary: This document provides the OpenAPI specification for the Google Gemini-compatible embedding endpoint within the Bifrost API gateway, detailing how to generate embeddings using the GenAI format.
tags:
    - gemini-api
    - embeddings
    - bifrost-gateway
    - google-genai
    - openapi-spec
    - vector-embeddings
category: api
---

# Embed content (Gemini format)

> Creates embeddings using Google Gemini API format.




## OpenAPI

````yaml openapi/openapi.json post /genai/v1beta/models/{model}:embedContent
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
  /genai/v1beta/models/{model}:embedContent:
    post:
      tags:
        - GenAI Integration
      summary: Embed content (Gemini format)
      description: |
        Creates embeddings using Google Gemini API format.
      operationId: geminiEmbedContent
      parameters:
        - name: model
          in: path
          required: true
          schema:
            type: string
          description: Model name with action (e.g., embedding-001:embedContent)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                content:
                  type: object
                  properties:
                    role:
                      type: string
                      enum:
                        - user
                        - model
                      description: >-
                        The producer of the content. Must be either 'user' or
                        'model'
                    parts:
                      type: array
                      items:
                        type: object
                        properties:
                          text:
                            type: string
                            description: Text part (can be code)
                          thought:
                            type: boolean
                            description: Indicates if the part is thought from the model
                          thoughtSignature:
                            type: string
                            format: byte
                            description: >-
                              Opaque signature for thought that can be reused in
                              subsequent requests
                          inlineData:
                            type: object
                            properties:
                              mimeType:
                                type: string
                                description: The IANA standard MIME type of the source data
                              data:
                                type: string
                                format: byte
                                description: Base64-encoded raw bytes
                              displayName:
                                type: string
                                description: >-
                                  Display name of the blob (not currently used
                                  in GenerateContent calls)
                          fileData:
                            type: object
                            properties:
                              mimeType:
                                type: string
                                description: The IANA standard MIME type of the source data
                              fileUri:
                                type: string
                                description: URI of the file
                              displayName:
                                type: string
                                description: Display name of the file data
                          functionCall:
                            type: object
                            properties:
                              id:
                                type: string
                                description: >-
                                  Unique ID of the function call. If populated,
                                  client should return response with matching id
                              name:
                                type: string
                                description: >-
                                  The name of the function to call. Matches
                                  FunctionDeclaration.name
                              args:
                                type: object
                                description: >-
                                  Function parameters and values in JSON object
                                  format
                          functionResponse:
                            type: object
                            properties:
                              id:
                                type: string
                                description: >-
                                  ID of the function call this response is for.
                                  Matches FunctionCall.id
                              name:
                                type: string
                                description: >-
                                  The name of the function. Matches
                                  FunctionDeclaration.name and FunctionCall.name
                              response:
                                type: object
                                description: >-
                                  Function response in JSON object format. Use
                                  "output" key for output and "error" key for
                                  error details
                              willContinue:
                                type: boolean
                                description: >-
                                  Signals that function call continues
                                  (NON_BLOCKING only). If false, future
                                  responses will not be considered
                              scheduling:
                                type: string
                                description: >-
                                  How the response should be scheduled
                                  (NON_BLOCKING only). Defaults to WHEN_IDLE
                          executableCode:
                            type: object
                            properties:
                              language:
                                type: string
                                description: Programming language of the code
                              code:
                                type: string
                                description: The code to be executed
                          codeExecutionResult:
                            type: object
                            properties:
                              outcome:
                                type: string
                                enum:
                                  - OUTCOME_UNSPECIFIED
                                  - OUTCOME_OK
                                  - OUTCOME_FAILED
                                  - OUTCOME_DEADLINE_EXCEEDED
                                description: Outcome of the code execution
                              output:
                                type: string
                                description: >-
                                  Contains stdout when successful, stderr or
                                  other description otherwise
                          videoMetadata:
                            type: object
                            properties:
                              fps:
                                type: number
                                description: Frame rate of the video. Range is (0.0, 24.0]
                              startOffset:
                                type: string
                                description: Start offset of the video
                              endOffset:
                                type: string
                                description: End offset of the video
                      description: List of parts that constitute a single message
                taskType:
                  type: string
                title:
                  type: string
                outputDimensionality:
                  type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  embeddings:
                    type: array
                    items:
                      type: object
                      properties:
                        values:
                          type: array
                          items:
                            type: number
                        statistics:
                          type: object
                          properties:
                            tokenCount:
                              type: integer
                  metadata:
                    type: object
                    properties:
                      billableCharacterCount:
                        type: integer
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
                      status:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            '@type':
                              type: string
                              description: Type identifier for the error details
                            fieldViolations:
                              type: array
                              items:
                                type: object
                                properties:
                                  description:
                                    type: string
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
                      status:
                        type: string
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            '@type':
                              type: string
                              description: Type identifier for the error details
                            fieldViolations:
                              type: array
                              items:
                                type: object
                                properties:
                                  description:
                                    type: string

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt