---
title: Create transcription (Azure OpenAI)
url: https://docs.getbifrost.ai/api-reference/openai-integration/create-transcription-azure-openai.md
source: llms
fetched_at: 2026-01-21T19:40:13.486263749-03:00
rendered_js: false
word_count: 114
summary: This document defines the API endpoint for transcribing audio files using Azure OpenAI models through the Bifrost gateway, detailing the required parameters and response structure.
tags:
    - azure-openai
    - transcription
    - audio-processing
    - speech-to-text
    - api-endpoint
    - bifrost
category: api
---

# Create transcription (Azure OpenAI)



## OpenAPI

````yaml openapi/openapi.json post /openai/openai/deployments/{deployment-id}/audio/transcriptions
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
  /openai/openai/deployments/{deployment-id}/audio/transcriptions:
    post:
      tags:
        - OpenAI Integration
        - Azure Integration
      summary: Create transcription (Azure OpenAI)
      operationId: azureCreateTranscription
      parameters:
        - name: deployment-id
          in: path
          required: true
          schema:
            type: string
          description: Azure deployment ID
        - name: api-version
          in: query
          schema:
            type: string
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - model
                - file
              properties:
                model:
                  type: string
                  description: Model identifier (e.g., whisper-1)
                  example: whisper-1
                file:
                  type: string
                  format: binary
                  description: Audio file to transcribe
                language:
                  type: string
                  description: Language of the audio (ISO 639-1)
                prompt:
                  type: string
                  description: Prompt to guide transcription
                response_format:
                  type: string
                  enum:
                    - json
                    - text
                    - srt
                    - verbose_json
                    - vtt
                temperature:
                  type: number
                  minimum: 0
                  maximum: 1
                timestamp_granularities:
                  type: array
                  items:
                    type: string
                    enum:
                      - word
                      - segment
                stream:
                  type: boolean
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
                  duration:
                    type: number
                  language:
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
                  segments:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        seek:
                          type: integer
                        start:
                          type: number
                        end:
                          type: number
                        text:
                          type: string
                        tokens:
                          type: array
                          items:
                            type: integer
                        temperature:
                          type: number
                        avg_logprob:
                          type: number
                        compression_ratio:
                          type: number
                        no_speech_prob:
                          type: number
                  task:
                    type: string
                  text:
                    type: string
                  usage:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - tokens
                          - duration
                      input_tokens:
                        type: integer
                      input_token_details:
                        type: object
                        properties:
                          text_tokens:
                            type: integer
                          audio_tokens:
                            type: integer
                      output_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                      seconds:
                        type: integer
                  words:
                    type: array
                    items:
                      type: object
                      properties:
                        word:
                          type: string
                        start:
                          type: number
                        end:
                          type: number
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
                properties:
                  type:
                    type: string
                    enum:
                      - transcript.text.delta
                      - transcript.text.done
                  delta:
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
                  text:
                    type: string
                  usage:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - tokens
                          - duration
                      input_tokens:
                        type: integer
                      input_token_details:
                        type: object
                        properties:
                          text_tokens:
                            type: integer
                          audio_tokens:
                            type: integer
                      output_tokens:
                        type: integer
                      total_tokens:
                        type: integer
                      seconds:
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