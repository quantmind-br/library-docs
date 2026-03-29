---
title: Stream generate content (PydanticAI - Gemini format)
url: https://docs.getbifrost.ai/api-reference/pydanticai-integration/stream-generate-content-pydanticai--gemini-format.md
source: llms
fetched_at: 2026-01-21T19:40:54.999385717-03:00
rendered_js: false
word_count: 128
summary: This document provides the OpenAPI specification for the PydanticAI integration endpoint that enables streaming content generation using the Google Gemini format.
tags:
    - openapi
    - pydanticai
    - gemini
    - streaming-api
    - ai-inference
    - content-generation
category: api
---

# Stream generate content (PydanticAI - Gemini format)

> Streams content generation using Google Gemini-compatible format via PydanticAI.




## OpenAPI

````yaml openapi/openapi.json post /pydanticai/genai/v1beta/models/{model}:streamGenerateContent
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
  /pydanticai/genai/v1beta/models/{model}:streamGenerateContent:
    post:
      tags:
        - PydanticAI Integration
      summary: Stream generate content (PydanticAI - Gemini format)
      description: >
        Streams content generation using Google Gemini-compatible format via
        PydanticAI.
      operationId: pydanticaiGeminiStreamGenerateContent
      parameters:
        - name: model
          in: path
          required: true
          schema:
            type: string
          description: Model name with action
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                  description: Model field for explicit model specification
                contents:
                  type: array
                  items:
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
                                Opaque signature for thought that can be reused
                                in subsequent requests
                            inlineData:
                              type: object
                              properties:
                                mimeType:
                                  type: string
                                  description: >-
                                    The IANA standard MIME type of the source
                                    data
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
                                  description: >-
                                    The IANA standard MIME type of the source
                                    data
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
                                    Unique ID of the function call. If
                                    populated, client should return response
                                    with matching id
                                name:
                                  type: string
                                  description: >-
                                    The name of the function to call. Matches
                                    FunctionDeclaration.name
                                args:
                                  type: object
                                  description: >-
                                    Function parameters and values in JSON
                                    object format
                            functionResponse:
                              type: object
                              properties:
                                id:
                                  type: string
                                  description: >-
                                    ID of the function call this response is
                                    for. Matches FunctionCall.id
                                name:
                                  type: string
                                  description: >-
                                    The name of the function. Matches
                                    FunctionDeclaration.name and
                                    FunctionCall.name
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
                                  description: >-
                                    Frame rate of the video. Range is (0.0,
                                    24.0]
                                startOffset:
                                  type: string
                                  description: Start offset of the video
                                endOffset:
                                  type: string
                                  description: End offset of the video
                        description: List of parts that constitute a single message
                  description: Content for the model to process
                systemInstruction:
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
                  description: System instruction for the model
                generationConfig:
                  type: object
                  properties:
                    temperature:
                      type: number
                      description: Controls the randomness of predictions
                    topP:
                      type: number
                      description: Nucleus sampling parameter
                    topK:
                      type: integer
                      description: Top-k sampling parameter
                    candidateCount:
                      type: integer
                      description: Number of candidates to generate. Defaults to 1
                    maxOutputTokens:
                      type: integer
                      description: Maximum number of output tokens to generate per message
                    stopSequences:
                      type: array
                      items:
                        type: string
                      description: Stop sequences
                    responseMimeType:
                      type: string
                      description: Output response mimetype (text/plain, application/json)
                    responseSchema:
                      type: object
                      description: Schema for JSON response (OpenAPI 3.0 subset)
                      properties:
                        type:
                          type: string
                          enum:
                            - TYPE_UNSPECIFIED
                            - STRING
                            - NUMBER
                            - INTEGER
                            - BOOLEAN
                            - ARRAY
                            - OBJECT
                            - 'NULL'
                          description: The type of the data
                        format:
                          type: string
                          description: >-
                            Format of the data (e.g., float, double, int32,
                            int64, email, byte)
                        title:
                          type: string
                          description: The title of the Schema
                        description:
                          type: string
                          description: The description of the data
                        nullable:
                          type: boolean
                          description: Indicates if the value may be null
                        enum:
                          type: array
                          items:
                            type: string
                          description: Possible values for primitive types with enum format
                        properties:
                          type: object
                          additionalProperties:
                            $ref: '#/components/schemas/GeminiSchema'
                          description: Properties of Type.OBJECT
                        required:
                          type: array
                          items:
                            type: string
                          description: Required properties of Type.OBJECT
                        items:
                          $ref: '#/components/schemas/GeminiSchema'
                          description: Schema of the elements of Type.ARRAY
                        minItems:
                          type: integer
                          description: Minimum number of elements for Type.ARRAY
                        maxItems:
                          type: integer
                          description: Maximum number of elements for Type.ARRAY
                        minLength:
                          type: integer
                          description: Minimum length of Type.STRING
                        maxLength:
                          type: integer
                          description: Maximum length of Type.STRING
                        minimum:
                          type: number
                          description: Minimum value of Type.INTEGER and Type.NUMBER
                        maximum:
                          type: number
                          description: Maximum value of Type.INTEGER and Type.NUMBER
                        pattern:
                          type: string
                          description: Pattern to restrict a string to a regular expression
                        default:
                          description: Default value of the data
                        example:
                          description: >-
                            Example of the object (only populated when object is
                            root)
                        anyOf:
                          type: array
                          items:
                            $ref: '#/components/schemas/GeminiSchema'
                          description: >-
                            Value should be validated against any of the
                            subschemas
                        propertyOrdering:
                          type: array
                          items:
                            type: string
                          description: Order of the properties (not standard OpenAPI)
                        minProperties:
                          type: integer
                          description: Minimum number of properties for Type.OBJECT
                        maxProperties:
                          type: integer
                          description: Maximum number of properties for Type.OBJECT
                    responseJsonSchema:
                      type: object
                      description: Alternative to responseSchema using JSON Schema format
                    responseModalities:
                      type: array
                      items:
                        type: string
                        enum:
                          - MODALITY_UNSPECIFIED
                          - TEXT
                          - IMAGE
                          - AUDIO
                      description: The modalities of the response
                    speechConfig:
                      type: object
                      properties:
                        voiceConfig:
                          type: object
                          properties:
                            prebuiltVoiceConfig:
                              type: object
                              properties:
                                voiceName:
                                  type: string
                                  description: The name of the prebuilt voice to use
                        multiSpeakerVoiceConfig:
                          type: object
                          properties:
                            speakerVoiceConfigs:
                              type: array
                              items:
                                type: object
                                properties:
                                  speaker:
                                    type: string
                                    description: >-
                                      The name of the speaker (should match
                                      prompt)
                                  voiceConfig:
                                    type: object
                                    properties:
                                      prebuiltVoiceConfig:
                                        type: object
                                        properties:
                                          voiceName:
                                            type: string
                                            description: The name of the prebuilt voice to use
                        languageCode:
                          type: string
                          description: >-
                            Language code (ISO 639) for speech synthesis. Only
                            available for Live API
                    thinkingConfig:
                      type: object
                      properties:
                        includeThoughts:
                          type: boolean
                          description: Whether to include thoughts in the response
                        thinkingBudget:
                          type: integer
                          description: Thinking budget in tokens
                        thinkingLevel:
                          type: string
                          enum:
                            - THINKING_LEVEL_UNSPECIFIED
                            - LOW
                            - HIGH
                          description: Thinking level preset
                    frequencyPenalty:
                      type: number
                      description: Frequency penalty for token generation
                    presencePenalty:
                      type: number
                      description: Presence penalty for token generation
                    seed:
                      type: integer
                      description: Seed for deterministic generation
                    logprobs:
                      type: integer
                      description: Number of log probabilities to return
                    responseLogprobs:
                      type: boolean
                      description: If true, export logprobs results in response
                    audioTimestamp:
                      type: boolean
                      description: If enabled, audio timestamp will be included in request
                    mediaResolution:
                      type: string
                      description: Media resolution specification
                    routingConfig:
                      type: object
                      properties:
                        autoMode:
                          type: object
                          properties:
                            modelRoutingPreference:
                              type: string
                              description: Model routing preference
                        manualMode:
                          type: object
                          properties:
                            modelName:
                              type: string
                              description: Model name to use
                    modelSelectionConfig:
                      type: object
                      properties:
                        featureSelectionPreference:
                          type: string
                          description: Options for feature selection preference
                    enableAffectiveDialog:
                      type: boolean
                      description: >-
                        If enabled, model will detect emotions and adapt
                        responses
                safetySettings:
                  type: array
                  items:
                    type: object
                    properties:
                      category:
                        type: string
                        description: Harm category
                      threshold:
                        type: string
                        description: The harm block threshold
                      method:
                        type: string
                        description: >-
                          Determines if harm block uses probability or
                          probability and severity scores
                tools:
                  type: array
                  items:
                    type: object
                    properties:
                      functionDeclarations:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: >-
                                Function name. Must start with
                                letter/underscore, a-z, A-Z, 0-9, underscores,
                                dots, dashes. Max 64 chars
                            description:
                              type: string
                              description: Description and purpose of the function
                            parameters:
                              type: object
                              description: >-
                                Schema object for defining input/output data
                                types (OpenAPI 3.0 subset)
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - TYPE_UNSPECIFIED
                                    - STRING
                                    - NUMBER
                                    - INTEGER
                                    - BOOLEAN
                                    - ARRAY
                                    - OBJECT
                                    - 'NULL'
                                  description: The type of the data
                                format:
                                  type: string
                                  description: >-
                                    Format of the data (e.g., float, double,
                                    int32, int64, email, byte)
                                title:
                                  type: string
                                  description: The title of the Schema
                                description:
                                  type: string
                                  description: The description of the data
                                nullable:
                                  type: boolean
                                  description: Indicates if the value may be null
                                enum:
                                  type: array
                                  items:
                                    type: string
                                  description: >-
                                    Possible values for primitive types with
                                    enum format
                                properties:
                                  type: object
                                  additionalProperties:
                                    $ref: '#/components/schemas/GeminiSchema'
                                  description: Properties of Type.OBJECT
                                required:
                                  type: array
                                  items:
                                    type: string
                                  description: Required properties of Type.OBJECT
                                items:
                                  $ref: '#/components/schemas/GeminiSchema'
                                  description: Schema of the elements of Type.ARRAY
                                minItems:
                                  type: integer
                                  description: Minimum number of elements for Type.ARRAY
                                maxItems:
                                  type: integer
                                  description: Maximum number of elements for Type.ARRAY
                                minLength:
                                  type: integer
                                  description: Minimum length of Type.STRING
                                maxLength:
                                  type: integer
                                  description: Maximum length of Type.STRING
                                minimum:
                                  type: number
                                  description: >-
                                    Minimum value of Type.INTEGER and
                                    Type.NUMBER
                                maximum:
                                  type: number
                                  description: >-
                                    Maximum value of Type.INTEGER and
                                    Type.NUMBER
                                pattern:
                                  type: string
                                  description: >-
                                    Pattern to restrict a string to a regular
                                    expression
                                default:
                                  description: Default value of the data
                                example:
                                  description: >-
                                    Example of the object (only populated when
                                    object is root)
                                anyOf:
                                  type: array
                                  items:
                                    $ref: '#/components/schemas/GeminiSchema'
                                  description: >-
                                    Value should be validated against any of the
                                    subschemas
                                propertyOrdering:
                                  type: array
                                  items:
                                    type: string
                                  description: >-
                                    Order of the properties (not standard
                                    OpenAPI)
                                minProperties:
                                  type: integer
                                  description: Minimum number of properties for Type.OBJECT
                                maxProperties:
                                  type: integer
                                  description: Maximum number of properties for Type.OBJECT
                            parametersJsonSchema:
                              type: object
                              description: >-
                                Alternative to parameters using JSON Schema
                                format
                            response:
                              type: object
                              description: Output schema for the function
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - TYPE_UNSPECIFIED
                                    - STRING
                                    - NUMBER
                                    - INTEGER
                                    - BOOLEAN
                                    - ARRAY
                                    - OBJECT
                                    - 'NULL'
                                  description: The type of the data
                                format:
                                  type: string
                                  description: >-
                                    Format of the data (e.g., float, double,
                                    int32, int64, email, byte)
                                title:
                                  type: string
                                  description: The title of the Schema
                                description:
                                  type: string
                                  description: The description of the data
                                nullable:
                                  type: boolean
                                  description: Indicates if the value may be null
                                enum:
                                  type: array
                                  items:
                                    type: string
                                  description: >-
                                    Possible values for primitive types with
                                    enum format
                                properties:
                                  type: object
                                  additionalProperties:
                                    $ref: '#/components/schemas/GeminiSchema'
                                  description: Properties of Type.OBJECT
                                required:
                                  type: array
                                  items:
                                    type: string
                                  description: Required properties of Type.OBJECT
                                items:
                                  $ref: '#/components/schemas/GeminiSchema'
                                  description: Schema of the elements of Type.ARRAY
                                minItems:
                                  type: integer
                                  description: Minimum number of elements for Type.ARRAY
                                maxItems:
                                  type: integer
                                  description: Maximum number of elements for Type.ARRAY
                                minLength:
                                  type: integer
                                  description: Minimum length of Type.STRING
                                maxLength:
                                  type: integer
                                  description: Maximum length of Type.STRING
                                minimum:
                                  type: number
                                  description: >-
                                    Minimum value of Type.INTEGER and
                                    Type.NUMBER
                                maximum:
                                  type: number
                                  description: >-
                                    Maximum value of Type.INTEGER and
                                    Type.NUMBER
                                pattern:
                                  type: string
                                  description: >-
                                    Pattern to restrict a string to a regular
                                    expression
                                default:
                                  description: Default value of the data
                                example:
                                  description: >-
                                    Example of the object (only populated when
                                    object is root)
                                anyOf:
                                  type: array
                                  items:
                                    $ref: '#/components/schemas/GeminiSchema'
                                  description: >-
                                    Value should be validated against any of the
                                    subschemas
                                propertyOrdering:
                                  type: array
                                  items:
                                    type: string
                                  description: >-
                                    Order of the properties (not standard
                                    OpenAPI)
                                minProperties:
                                  type: integer
                                  description: Minimum number of properties for Type.OBJECT
                                maxProperties:
                                  type: integer
                                  description: Maximum number of properties for Type.OBJECT
                            responseJsonSchema:
                              type: object
                              description: Alternative to response using JSON Schema format
                            behavior:
                              type: string
                              enum:
                                - UNSPECIFIED
                                - BLOCKING
                                - NON_BLOCKING
                              description: >-
                                Function behavior mode. BLOCKING waits for
                                response, NON_BLOCKING continues conversation
                      googleSearch:
                        type: object
                        properties:
                          timeRangeFilter:
                            type: object
                            properties:
                              startTime:
                                type: string
                                format: date-time
                              endTime:
                                type: string
                                format: date-time
                          excludeDomains:
                            type: array
                            items:
                              type: string
                            description: >-
                              List of domains to exclude from search results
                              (max 2000)
                      googleSearchRetrieval:
                        type: object
                        properties:
                          dynamicRetrievalConfig:
                            type: object
                            properties:
                              mode:
                                type: string
                                description: >-
                                  The mode of the predictor for dynamic
                                  retrieval
                              dynamicThreshold:
                                type: number
                                description: Threshold for dynamic retrieval
                      retrieval:
                        type: object
                        properties:
                          disableAttribution:
                            type: boolean
                            deprecated: true
                            description: Deprecated. This option is no longer supported
                          externalApi:
                            type: object
                            properties:
                              endpoint:
                                type: string
                                description: The endpoint of the external API
                              apiSpec:
                                type: string
                                enum:
                                  - API_SPEC_UNSPECIFIED
                                  - SIMPLE_SEARCH
                                  - ELASTIC_SEARCH
                              authConfig:
                                type: object
                                properties:
                                  authType:
                                    type: string
                                    enum:
                                      - AUTH_TYPE_UNSPECIFIED
                                      - NO_AUTH
                                      - API_KEY_AUTH
                                      - HTTP_BASIC_AUTH
                                      - GOOGLE_SERVICE_ACCOUNT_AUTH
                                      - OAUTH
                                      - OIDC_AUTH
                                  apiKeyConfig:
                                    type: object
                                    properties:
                                      apiKeyString:
                                        type: string
                                  googleServiceAccountConfig:
                                    type: object
                                    properties:
                                      serviceAccount:
                                        type: string
                                  httpBasicAuthConfig:
                                    type: object
                                    properties:
                                      credentialSecret:
                                        type: string
                                  oauthConfig:
                                    type: object
                                    properties:
                                      accessToken:
                                        type: string
                                      serviceAccount:
                                        type: string
                                  oidcConfig:
                                    type: object
                                    properties:
                                      idToken:
                                        type: string
                                      serviceAccount:
                                        type: string
                              elasticSearchParams:
                                type: object
                                properties:
                                  index:
                                    type: string
                                    description: The ElasticSearch index to use
                                  numHits:
                                    type: integer
                                    description: Number of hits (chunks) to request
                                  searchTemplate:
                                    type: string
                                    description: The ElasticSearch search template to use
                          vertexAiSearch:
                            type: object
                            properties:
                              datastore:
                                type: string
                                description: >-
                                  Fully-qualified Vertex AI Search data store
                                  resource ID
                              engine:
                                type: string
                                description: >-
                                  Fully-qualified Vertex AI Search engine
                                  resource ID
                              filter:
                                type: string
                                description: Filter strings to be passed to the search API
                              maxResults:
                                type: integer
                                description: >-
                                  Number of search results to return (max 10,
                                  default 10)
                              dataStoreSpecs:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    dataStore:
                                      type: string
                                      description: Full resource name of DataStore
                                    filter:
                                      type: string
                                      description: >-
                                        Filter specification for documents in
                                        the data store
                          vertexRagStore:
                            type: object
                            properties:
                              ragCorpora:
                                type: array
                                items:
                                  type: string
                                deprecated: true
                                description: Deprecated. Use ragResources instead
                              ragResources:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    ragCorpus:
                                      type: string
                                      description: RAGCorpora resource name
                                    ragFileIds:
                                      type: array
                                      items:
                                        type: string
                                      description: >-
                                        rag_file_id. Files should be in the same
                                        rag_corpus
                              ragRetrievalConfig:
                                type: object
                                properties:
                                  topK:
                                    type: integer
                                    description: The number of contexts to retrieve
                                  filter:
                                    type: object
                                    properties:
                                      metadataFilter:
                                        type: string
                                        description: String for metadata filtering
                                      vectorDistanceThreshold:
                                        type: number
                                        description: >-
                                          Only returns contexts with vector
                                          distance smaller than threshold
                                      vectorSimilarityThreshold:
                                        type: number
                                        description: >-
                                          Only returns contexts with vector
                                          similarity larger than threshold
                                  hybridSearch:
                                    type: object
                                    properties:
                                      alpha:
                                        type: number
                                        description: >-
                                          Weight between dense and sparse vector
                                          search (0-1). 0 = sparse only, 1 = dense
                                          only
                                  ranking:
                                    type: object
                                    properties:
                                      llmRanker:
                                        type: object
                                        properties:
                                          modelName:
                                            type: string
                                      rankService:
                                        type: object
                                        properties:
                                          modelName:
                                            type: string
                              similarityTopK:
                                type: integer
                                description: >-
                                  Number of top k results to return from
                                  selected corpora
                              storeContext:
                                type: boolean
                                description: >-
                                  For Gemini Multimodal Live API - memorize
                                  interactions
                              vectorDistanceThreshold:
                                type: number
                                description: >-
                                  Only return results with vector distance
                                  smaller than threshold
                      codeExecution:
                        type: object
                        description: Enables code execution by the model
                      enterpriseWebSearch:
                        type: object
                        properties:
                          excludeDomains:
                            type: array
                            items:
                              type: string
                            description: List of domains to exclude (max 2000)
                      googleMaps:
                        type: object
                        properties:
                          authConfig:
                            type: object
                            properties:
                              authType:
                                type: string
                                enum:
                                  - AUTH_TYPE_UNSPECIFIED
                                  - NO_AUTH
                                  - API_KEY_AUTH
                                  - HTTP_BASIC_AUTH
                                  - GOOGLE_SERVICE_ACCOUNT_AUTH
                                  - OAUTH
                                  - OIDC_AUTH
                              apiKeyConfig:
                                type: object
                                properties:
                                  apiKeyString:
                                    type: string
                              googleServiceAccountConfig:
                                type: object
                                properties:
                                  serviceAccount:
                                    type: string
                              httpBasicAuthConfig:
                                type: object
                                properties:
                                  credentialSecret:
                                    type: string
                              oauthConfig:
                                type: object
                                properties:
                                  accessToken:
                                    type: string
                                  serviceAccount:
                                    type: string
                              oidcConfig:
                                type: object
                                properties:
                                  idToken:
                                    type: string
                                  serviceAccount:
                                    type: string
                      urlContext:
                        type: object
                        description: Tool to support URL context retrieval
                      computerUse:
                        type: object
                        properties:
                          environment:
                            type: string
                            enum:
                              - ENVIRONMENT_UNSPECIFIED
                              - ENVIRONMENT_BROWSER
                            description: The environment being operated
                toolConfig:
                  type: object
                  properties:
                    functionCallingConfig:
                      type: object
                      properties:
                        mode:
                          type: string
                          enum:
                            - MODE_UNSPECIFIED
                            - AUTO
                            - ANY
                            - NONE
                            - VALIDATED
                          description: Function calling mode
                        allowedFunctionNames:
                          type: array
                          items:
                            type: string
                          description: Function names to call when mode is ANY
                    retrievalConfig:
                      type: object
                      properties:
                        latLng:
                          type: object
                          properties:
                            latitude:
                              type: number
                              description: Latitude in degrees [-90.0, +90.0]
                            longitude:
                              type: number
                              description: Longitude in degrees [-180.0, +180.0]
                        languageCode:
                          type: string
                cachedContent:
                  type: string
                  description: Cached content resource name
                labels:
                  type: object
                  additionalProperties:
                    type: string
                  description: Labels for the request
                requests:
                  type: array
                  items:
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
                              The producer of the content. Must be either 'user'
                              or 'model'
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
                                  description: >-
                                    Indicates if the part is thought from the
                                    model
                                thoughtSignature:
                                  type: string
                                  format: byte
                                  description: >-
                                    Opaque signature for thought that can be
                                    reused in subsequent requests
                                inlineData:
                                  type: object
                                  properties:
                                    mimeType:
                                      type: string
                                      description: >-
                                        The IANA standard MIME type of the
                                        source data
                                    data:
                                      type: string
                                      format: byte
                                      description: Base64-encoded raw bytes
                                    displayName:
                                      type: string
                                      description: >-
                                        Display name of the blob (not currently
                                        used in GenerateContent calls)
                                fileData:
                                  type: object
                                  properties:
                                    mimeType:
                                      type: string
                                      description: >-
                                        The IANA standard MIME type of the
                                        source data
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
                                        Unique ID of the function call. If
                                        populated, client should return response
                                        with matching id
                                    name:
                                      type: string
                                      description: >-
                                        The name of the function to call.
                                        Matches FunctionDeclaration.name
                                    args:
                                      type: object
                                      description: >-
                                        Function parameters and values in JSON
                                        object format
                                functionResponse:
                                  type: object
                                  properties:
                                    id:
                                      type: string
                                      description: >-
                                        ID of the function call this response is
                                        for. Matches FunctionCall.id
                                    name:
                                      type: string
                                      description: >-
                                        The name of the function. Matches
                                        FunctionDeclaration.name and
                                        FunctionCall.name
                                    response:
                                      type: object
                                      description: >-
                                        Function response in JSON object format.
                                        Use "output" key for output and "error"
                                        key for error details
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
                                        (NON_BLOCKING only). Defaults to
                                        WHEN_IDLE
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
                                        Contains stdout when successful, stderr
                                        or other description otherwise
                                videoMetadata:
                                  type: object
                                  properties:
                                    fps:
                                      type: number
                                      description: >-
                                        Frame rate of the video. Range is (0.0,
                                        24.0]
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
                  description: Batch embedding requests
                fallbacks:
                  type: array
                  items:
                    type: string
      responses:
        '200':
          description: Successful streaming response
          content:
            text/event-stream:
              schema:
                type: object
                properties:
                  candidates:
                    type: array
                    items:
                      type: object
                      properties:
                        content:
                          type: object
                          properties:
                            role:
                              type: string
                              enum:
                                - user
                                - model
                              description: >-
                                The producer of the content. Must be either
                                'user' or 'model'
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
                                    description: >-
                                      Indicates if the part is thought from the
                                      model
                                  thoughtSignature:
                                    type: string
                                    format: byte
                                    description: >-
                                      Opaque signature for thought that can be
                                      reused in subsequent requests
                                  inlineData:
                                    type: object
                                    properties:
                                      mimeType:
                                        type: string
                                        description: >-
                                          The IANA standard MIME type of the
                                          source data
                                      data:
                                        type: string
                                        format: byte
                                        description: Base64-encoded raw bytes
                                      displayName:
                                        type: string
                                        description: >-
                                          Display name of the blob (not currently
                                          used in GenerateContent calls)
                                  fileData:
                                    type: object
                                    properties:
                                      mimeType:
                                        type: string
                                        description: >-
                                          The IANA standard MIME type of the
                                          source data
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
                                          Unique ID of the function call. If
                                          populated, client should return response
                                          with matching id
                                      name:
                                        type: string
                                        description: >-
                                          The name of the function to call.
                                          Matches FunctionDeclaration.name
                                      args:
                                        type: object
                                        description: >-
                                          Function parameters and values in JSON
                                          object format
                                  functionResponse:
                                    type: object
                                    properties:
                                      id:
                                        type: string
                                        description: >-
                                          ID of the function call this response is
                                          for. Matches FunctionCall.id
                                      name:
                                        type: string
                                        description: >-
                                          The name of the function. Matches
                                          FunctionDeclaration.name and
                                          FunctionCall.name
                                      response:
                                        type: object
                                        description: >-
                                          Function response in JSON object format.
                                          Use "output" key for output and "error"
                                          key for error details
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
                                          (NON_BLOCKING only). Defaults to
                                          WHEN_IDLE
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
                                          Contains stdout when successful, stderr
                                          or other description otherwise
                                  videoMetadata:
                                    type: object
                                    properties:
                                      fps:
                                        type: number
                                        description: >-
                                          Frame rate of the video. Range is (0.0,
                                          24.0]
                                      startOffset:
                                        type: string
                                        description: Start offset of the video
                                      endOffset:
                                        type: string
                                        description: End offset of the video
                              description: List of parts that constitute a single message
                        finishReason:
                          type: string
                          enum:
                            - FINISH_REASON_UNSPECIFIED
                            - STOP
                            - MAX_TOKENS
                            - SAFETY
                            - RECITATION
                            - LANGUAGE
                            - OTHER
                            - BLOCKLIST
                            - PROHIBITED_CONTENT
                            - SPII
                            - MALFORMED_FUNCTION_CALL
                            - IMAGE_SAFETY
                            - UNEXPECTED_TOOL_CALL
                        finishMessage:
                          type: string
                          description: Human-readable finish message
                        tokenCount:
                          type: integer
                          description: Number of tokens for this candidate
                        safetyRatings:
                          type: array
                          items:
                            type: object
                            properties:
                              category:
                                type: string
                                description: Harm category
                              probability:
                                type: string
                                description: Harm probability level
                              probabilityScore:
                                type: number
                                description: Harm probability score
                              severity:
                                type: string
                                description: Harm severity level
                              severityScore:
                                type: number
                                description: Harm severity score
                              blocked:
                                type: boolean
                                description: Whether content was filtered
                              overwrittenThreshold:
                                type: string
                                description: >-
                                  Overwritten threshold for safety category (for
                                  Gemini 2.0 image output with minors detected)
                        citationMetadata:
                          type: object
                          description: Source attribution of the generated content
                        index:
                          type: integer
                          description: Index of the candidate
                        groundingMetadata:
                          type: object
                          description: >-
                            Metadata specifying sources used to ground generated
                            content
                        urlContextMetadata:
                          type: object
                          properties:
                            urlMetadata:
                              type: array
                              items:
                                type: object
                                properties:
                                  retrievedUrl:
                                    type: string
                                  urlRetrievalStatus:
                                    type: string
                        avgLogprobs:
                          type: number
                          description: Average log probability score of the candidate
                        logprobsResult:
                          type: object
                          properties:
                            chosenCandidates:
                              type: array
                              items:
                                type: object
                                properties:
                                  token:
                                    type: string
                                    description: The candidate's token string value
                                  tokenId:
                                    type: integer
                                    description: The candidate's token ID value
                                  logProbability:
                                    type: number
                                    description: The candidate's log probability
                            topCandidates:
                              type: array
                              items:
                                type: object
                                properties:
                                  candidates:
                                    type: array
                                    items:
                                      type: object
                                      properties:
                                        token:
                                          type: string
                                          description: The candidate's token string value
                                        tokenId:
                                          type: integer
                                          description: The candidate's token ID value
                                        logProbability:
                                          type: number
                                          description: The candidate's log probability
                  promptFeedback:
                    type: object
                    properties:
                      blockReason:
                        type: string
                      blockReasonMessage:
                        type: string
                        description: Human-readable block reason message
                      safetyRatings:
                        type: array
                        items:
                          type: object
                          properties:
                            category:
                              type: string
                              description: Harm category
                            probability:
                              type: string
                              description: Harm probability level
                            probabilityScore:
                              type: number
                              description: Harm probability score
                            severity:
                              type: string
                              description: Harm severity level
                            severityScore:
                              type: number
                              description: Harm severity score
                            blocked:
                              type: boolean
                              description: Whether content was filtered
                            overwrittenThreshold:
                              type: string
                              description: >-
                                Overwritten threshold for safety category (for
                                Gemini 2.0 image output with minors detected)
                  usageMetadata:
                    type: object
                    properties:
                      promptTokenCount:
                        type: integer
                        description: >-
                          Number of tokens in the prompt (includes cached
                          content)
                      candidatesTokenCount:
                        type: integer
                        description: Number of tokens in the response(s)
                      totalTokenCount:
                        type: integer
                        description: >-
                          Total token count for prompt, response candidates, and
                          tool-use prompts
                      cachedContentTokenCount:
                        type: integer
                        description: Number of tokens in the cached part of the input
                      thoughtsTokenCount:
                        type: integer
                        description: Number of tokens in thoughts output
                      toolUsePromptTokenCount:
                        type: integer
                        description: Number of tokens in tool-use prompts
                      trafficType:
                        type: string
                        description: Traffic type (Pay-As-You-Go or Provisioned Throughput)
                      cacheTokensDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            modality:
                              type: string
                              description: The modality (TEXT, IMAGE, AUDIO, etc.)
                            tokenCount:
                              type: integer
                        description: Modalities of the cached content in the request input
                      candidatesTokensDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            modality:
                              type: string
                              description: The modality (TEXT, IMAGE, AUDIO, etc.)
                            tokenCount:
                              type: integer
                        description: Modalities returned in the response
                      promptTokensDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            modality:
                              type: string
                              description: The modality (TEXT, IMAGE, AUDIO, etc.)
                            tokenCount:
                              type: integer
                        description: Modalities processed in the request input
                      toolUsePromptTokensDetails:
                        type: array
                        items:
                          type: object
                          properties:
                            modality:
                              type: string
                              description: The modality (TEXT, IMAGE, AUDIO, etc.)
                            tokenCount:
                              type: integer
                        description: Modalities processed for tool-use request inputs
                  modelVersion:
                    type: string
                    description: The model version used to generate the response
                  responseId:
                    type: string
                    description: >-
                      Response ID for identifying each response (encoding of
                      event_id)
                  createTime:
                    type: string
                    format: date-time
                    description: Timestamp when the request was made to the server
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
components:
  schemas:
    GeminiSchema:
      type: object
      description: Schema object for defining input/output data types (OpenAPI 3.0 subset)
      properties:
        type:
          type: string
          enum:
            - TYPE_UNSPECIFIED
            - STRING
            - NUMBER
            - INTEGER
            - BOOLEAN
            - ARRAY
            - OBJECT
            - 'NULL'
          description: The type of the data
        format:
          type: string
          description: Format of the data (e.g., float, double, int32, int64, email, byte)
        title:
          type: string
          description: The title of the Schema
        description:
          type: string
          description: The description of the data
        nullable:
          type: boolean
          description: Indicates if the value may be null
        enum:
          type: array
          items:
            type: string
          description: Possible values for primitive types with enum format
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/GeminiSchema'
          description: Properties of Type.OBJECT
        required:
          type: array
          items:
            type: string
          description: Required properties of Type.OBJECT
        items:
          $ref: '#/components/schemas/GeminiSchema'
          description: Schema of the elements of Type.ARRAY
        minItems:
          type: integer
          description: Minimum number of elements for Type.ARRAY
        maxItems:
          type: integer
          description: Maximum number of elements for Type.ARRAY
        minLength:
          type: integer
          description: Minimum length of Type.STRING
        maxLength:
          type: integer
          description: Maximum length of Type.STRING
        minimum:
          type: number
          description: Minimum value of Type.INTEGER and Type.NUMBER
        maximum:
          type: number
          description: Maximum value of Type.INTEGER and Type.NUMBER
        pattern:
          type: string
          description: Pattern to restrict a string to a regular expression
        default:
          description: Default value of the data
        example:
          description: Example of the object (only populated when object is root)
        anyOf:
          type: array
          items:
            $ref: '#/components/schemas/GeminiSchema'
          description: Value should be validated against any of the subschemas
        propertyOrdering:
          type: array
          items:
            type: string
          description: Order of the properties (not standard OpenAPI)
        minProperties:
          type: integer
          description: Minimum number of properties for Type.OBJECT
        maxProperties:
          type: integer
          description: Maximum number of properties for Type.OBJECT

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt