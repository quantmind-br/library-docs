---
title: Generate image
url: https://docs.getbifrost.ai/api-reference/image-generations/generate-image.md
source: llms
fetched_at: 2026-01-21T19:39:11.355113253-03:00
rendered_js: false
word_count: 121
summary: This document specifies the API endpoint for generating images from text prompts using various AI providers via the Bifrost unified interface. It details the request parameters for controlling image size, quality, style, and output format.
tags:
    - image-generation
    - text-to-image
    - bifrost-api
    - api-endpoint
    - multi-provider
    - ai-inference
category: api
---

# Generate image

> Generates images from text prompts using the specified model.




## OpenAPI

````yaml openapi/openapi.json post /v1/images/generations
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
  /v1/images/generations:
    post:
      tags:
        - Image Generations
      summary: Generate image
      description: |
        Generates images from text prompts using the specified model.
      operationId: imageGeneration
      requestBody:
        required: true
        content:
          application/json:
            schema:
              allOf:
                - type: object
                  required:
                    - model
                    - prompt
                  properties:
                    model:
                      type: string
                      description: Model identifier in format `provider/model`
                    prompt:
                      type: string
                      description: Text prompt to generate image
                    'n':
                      type: integer
                      minimum: 1
                      maximum: 10
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
                        - auto
                        - high
                        - medium
                        - low
                        - hd
                        - standard
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
                      description: |
                        Format of the response.
                    background:
                      type: string
                      enum:
                        - transparent
                        - opaque
                        - auto
                      description: Background type for the image
                    moderation:
                      type: string
                      enum:
                        - low
                        - auto
                      description: Content moderation level
                    partial_images:
                      type: integer
                      minimum: 0
                      maximum: 3
                      description: Number of partial images to generate
                    output_compression:
                      type: integer
                      minimum: 0
                      maximum: 100
                      description: Compression level (0-100%)
                    output_format:
                      type: string
                      enum:
                        - png
                        - webp
                        - jpeg
                      description: Output image format
                    user:
                      type: string
                      description: User identifier for tracking
                    seed:
                      type: integer
                      description: Seed for reproducible image generation
                    negative_prompt:
                      type: string
                      description: Negative prompt to guide what to avoid in generation
                    num_inference_steps:
                      type: integer
                      description: Number of inference steps for generation
                    stream:
                      type: boolean
                      default: false
                      description: >
                        Whether to stream the response. When true, images are
                        sent as SSE.

                        When streaming, providers may return base64 chunks
                        (`b64_json`) and/or URLs (`url`) depending on provider
                        and configuration.
                    fallbacks:
                      type: array
                      items:
                        type: object
                        description: Fallback model configuration
                        required:
                          - provider
                          - model
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
                          model:
                            type: string
                            description: Model name
                      description: Fallback models to try if primary model fails
      responses:
        '200':
          description: >
            Successful response. Returns JSON for non-streaming requests, or
            Server-Sent Events (SSE) stream when `stream=true`.

            When streaming, events are sent with the following event types:

            - `image_generation.partial_image`: Intermediate image chunks with
            base64-encoded image data

            - `image_generation.completed`: Final event for each image with
            usage information

            - `error`: Error events with error details
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: Unique identifier for the generation request
                  created:
                    type: integer
                    format: int64
                    description: Unix timestamp when the image was created
                  model:
                    type: string
                    description: Model used for generation
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
                    description: Background type for the image
                  output_format:
                    type: string
                    enum:
                      - png
                      - webp
                      - jpeg
                    description: Output image format
                  quality:
                    type: string
                    description: Quality of the generated image
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
            text/event-stream:
              schema:
                type: object
                description: >
                  Streaming response chunk for image generation.

                  Sent via Server-Sent Events (SSE).

                  Providers may return either b64_json (base64-encoded image
                  data) or url (public URL to the image).
                properties:
                  id:
                    type: string
                    description: Request identifier
                  type:
                    type: string
                    enum:
                      - image_generation.partial_image
                      - image_generation.completed
                      - error
                    description: Type of stream event
                  partial_image_index:
                    type: integer
                    description: Index of the partial image chunk
                  sequence_number:
                    type: integer
                    description: Sequence number for event ordering within the stream
                  b64_json:
                    type: string
                    description: |
                      Base64-encoded chunk of image data.
                      Optional; either b64_json or url may be present.
                  url:
                    type: string
                    format: uri
                    description: >
                      Optional public URL to the generated image chunk.

                      Used by HuggingFace and other providers that return image
                      URLs instead of base64 data.
                  created_at:
                    type: integer
                    format: int64
                    description: Timestamp when chunk was created
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
                    description: Quality setting used
                  background:
                    type: string
                    description: Background type used
                  output_format:
                    type: string
                    enum:
                      - png
                      - webp
                      - jpeg
                    description: Output format used
                  revised_prompt:
                    type: string
                    description: Revised prompt
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
                    description: Token usage
                  error:
                    type: object
                    description: Error information if generation failed
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