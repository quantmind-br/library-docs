---
title: Create image
url: https://docs.getbifrost.ai/api-reference/openai-integration/create-image.md
source: llms
fetched_at: 2026-01-21T19:40:07.04732839-03:00
rendered_js: false
word_count: 143
summary: This document provides the API specification for generating images from text prompts using an OpenAI-compatible endpoint, including details on request parameters and streaming options.
tags:
    - openai-api
    - image-generation
    - text-to-image
    - ai-inference
    - api-reference
    - bifrost
category: api
---

# Create image

> Generates images from text prompts using OpenAI-compatible format.

**Note:** Azure OpenAI deployments are also supported via the Azure integration endpoint.

**Note:** This endpoint also works without the `/v1` prefix (e.g., `/openai/images/generations`).




## OpenAPI

````yaml openapi/openapi.json post /openai/v1/images/generations
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
  /openai/v1/images/generations:
    post:
      tags:
        - OpenAI Integration
      summary: Create image
      description: >
        Generates images from text prompts using OpenAI-compatible format.


        **Note:** Azure OpenAI deployments are also supported via the Azure
        integration endpoint.


        **Note:** This endpoint also works without the `/v1` prefix (e.g.,
        `/openai/images/generations`).
      operationId: openaiCreateImage
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - prompt
              properties:
                model:
                  type: string
                  description: Model identifier
                prompt:
                  type: string
                  description: Text prompt to generate image
                'n':
                  type: integer
                  minimum: 1
                  maximum: 10
                  default: 1
                  description: Number of images to generate
                size:
                  type: string
                  enum:
                    - 256x256
                    - 512x512
                    - 1024x1024
                    - 1792x1024
                    - 1024x1792
                    - 1536x1024
                    - 1024x1536
                    - auto
                  description: Size of the generated image
                quality:
                  type: string
                  enum:
                    - standard
                    - hd
                  description: Quality of the generated image
                style:
                  type: string
                  enum:
                    - natural
                    - vivid
                  description: Style of the generated image
                response_format:
                  type: string
                  enum:
                    - url
                    - b64_json
                  default: url
                  description: >-
                    Format of the response. This parameter is not supported for
                    streaming requests.
                user:
                  type: string
                  description: User identifier for tracking
                stream:
                  type: boolean
                  default: false
                  description: >
                    Whether to stream the response. When true, images are sent
                    as base64 chunks via SSE.
                fallbacks:
                  type: array
                  items:
                    type: string
                  description: Fallback models to try if primary model fails
      responses:
        '200':
          description: >
            Successful response. Returns JSON for non-streaming requests, or
            Server-Sent Events (SSE) stream when `stream=true`.

            When streaming, each event contains a chunk of the image as base64
            data, with the final event having type `image_generation.completed`.
          content:
            application/json:
              schema:
                type: object
                properties:
                  created:
                    type: integer
                    format: int64
                    description: Unix timestamp when the image was created
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          format: uri
                          description: URL of the generated image
                        b64_json:
                          type: string
                          description: Base64-encoded image data
                        revised_prompt:
                          type: string
                          description: Revised prompt used for generation
                        index:
                          type: integer
                          description: Index of this image
                    description: Array of generated images
                  background:
                    type: string
                    description: Background type used
                  output_format:
                    type: string
                    description: Output format used
                  quality:
                    type: string
                    description: Quality setting used
                  size:
                    type: string
                    description: Size setting used
                  usage:
                    type: object
                    properties:
                      input_tokens:
                        type: integer
                        description: Number of input tokens
                      input_tokens_details:
                        type: object
                        properties:
                          image_tokens:
                            type: integer
                            description: Tokens used for images
                          text_tokens:
                            type: integer
                            description: Tokens used for text
                      total_tokens:
                        type: integer
                        description: Total tokens used
                      output_tokens:
                        type: integer
                        description: Number of output tokens
                      output_tokens_details:
                        type: object
                        properties:
                          image_tokens:
                            type: integer
                            description: Tokens used for images
                          text_tokens:
                            type: integer
                            description: Tokens used for text
            text/event-stream:
              schema:
                type: object
                description: |
                  Streaming response chunk for image generation (OpenAI format).
                  Sent via Server-Sent Events (SSE) when stream=true.
                properties:
                  type:
                    type: string
                    enum:
                      - image_generation.partial_image
                      - image_generation.completed
                      - error
                    description: Type of stream event
                  b64_json:
                    type: string
                    description: Base64-encoded chunk of image data
                  partial_image_index:
                    type: integer
                    description: Index of the partial image chunk
                  sequence_number:
                    type: integer
                    description: Ordering index for stream chunks
                  created_at:
                    type: integer
                    format: int64
                    description: Timestamp when chunk was created
                  size:
                    type: string
                    description: Size of the generated image
                  quality:
                    type: string
                    description: Quality setting used
                  background:
                    type: string
                    description: Background type used
                  output_format:
                    type: string
                    description: Output format used
                  usage:
                    type: object
                    properties:
                      input_tokens:
                        type: integer
                        description: Number of input tokens
                      input_tokens_details:
                        type: object
                        properties:
                          image_tokens:
                            type: integer
                            description: Tokens used for images
                          text_tokens:
                            type: integer
                            description: Tokens used for text
                      total_tokens:
                        type: integer
                        description: Total tokens used
                      output_tokens:
                        type: integer
                        description: Number of output tokens
                      output_tokens_details:
                        type: object
                        properties:
                          image_tokens:
                            type: integer
                            description: Tokens used for images
                          text_tokens:
                            type: integer
                            description: Tokens used for text
                    description: Token usage (usually in final chunk)
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