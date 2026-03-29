---
title: Invoke model with streaming (Bedrock format)
url: https://docs.getbifrost.ai/api-reference/bedrock-integration/invoke-model-with-streaming-bedrock-format.md
source: llms
fetched_at: 2026-01-21T19:38:15.861156526-03:00
rendered_js: false
word_count: 127
summary: This document defines the API endpoint for invoking AI models with streaming responses using the AWS Bedrock InvokeModelWithResponseStream format. It details the request body parameters for various model providers and the event stream response structure.
tags:
    - bedrock-integration
    - streaming-api
    - ai-inference
    - openapi-spec
    - aws-bedrock
    - model-invocation
category: api
---

# Invoke model with streaming (Bedrock format)

> Invokes a model with streaming using AWS Bedrock InvokeModelWithResponseStream API format.




## OpenAPI

````yaml openapi/openapi.json post /bedrock/model/{modelId}/invoke-with-response-stream
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
  /bedrock/model/{modelId}/invoke-with-response-stream:
    post:
      tags:
        - Bedrock Integration
      summary: Invoke model with streaming (Bedrock format)
      description: >
        Invokes a model with streaming using AWS Bedrock
        InvokeModelWithResponseStream API format.
      operationId: bedrockInvokeModelStream
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
              description: >
                Raw model invocation request. The body format depends on the
                model provider.

                For Anthropic models, use Anthropic format. For other models,
                use their native format.
              properties:
                prompt:
                  type: string
                  description: Text prompt to complete
                max_tokens:
                  type: integer
                max_tokens_to_sample:
                  type: integer
                  description: Anthropic-style max tokens
                temperature:
                  type: number
                top_p:
                  type: number
                top_k:
                  type: integer
                stop:
                  type: array
                  items:
                    type: string
                stop_sequences:
                  type: array
                  items:
                    type: string
                  description: Anthropic-style stop sequences
                messages:
                  type: array
                  items:
                    type: object
                  description: For Claude 3 models
                system:
                  description: System prompt (string or array of strings)
                  oneOf:
                    - type: string
                    - type: array
                      items:
                        type: string
                anthropic_version:
                  type: string
      responses:
        '200':
          description: Successful streaming response
          content:
            application/x-amz-eventstream:
              schema:
                type: object
                description: AWS event stream format
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt