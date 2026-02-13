---
title: Create a chat completion
url: https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request.mdx
source: llms
fetched_at: 2026-02-13T15:18:38.116581-03:00
rendered_js: false
word_count: 33
summary: This document specifies the OpenRouter API endpoint for generating chat completions, detailing both streaming and non-streaming request parameters and response schemas.
tags:
    - openrouter
    - chat-completions
    - api-endpoint
    - llm-api
    - openapi-specification
    - json-schema
category: api
---

# Create a chat completion

POST https://openrouter.ai/api/v1/chat/completions
Content-Type: application/json

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

Reference: https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a chat completion
  version: endpoint_chat.sendChatCompletionRequest
paths:
  /chat/completions:
    post:
      operationId: send-chat-completion-request
      summary: Create a chat completion
      description: >-
        Sends a request for a model response for the given chat conversation.
        Supports both streaming and non-streaming modes.
      tags:
        - - subpackage_chat
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful chat completion response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatResponse'
        '400':
          description: Bad request - invalid parameters
          content: {}
        '401':
          description: Unauthorized - invalid API key
          content: {}
        '429':
          description: Too many requests - rate limit exceeded
          content: {}
        '500':
          description: Internal server error
          content: {}
      requestBody:
        description: Chat completion request parameters
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatGenerationParams'
components:
  schemas:
    __schema1:
      type:
        - boolean
        - 'null'
    Schema3:
      type: string
      enum:
        - value: deny
        - value: allow
    __schema3:
      oneOf:
        - $ref: '#/components/schemas/Schema3'
        - type: 'null'
    Schema5Items0:
      type: string
      enum:
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Ambient
        - value: Amazon Bedrock
        - value: Amazon Nova
        - value: Anthropic
        - value: Arcee AI
        - value: AtlasCloud
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: BytePlus
        - value: Black Forest Labs
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: Inceptron
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: Liquid
        - value: Mara
        - value: Mancer 2
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: Seed
        - value: SiliconFlow
        - value: Sourceful
        - value: StepFun
        - value: Stealth
        - value: StreamLake
        - value: Switchpoint
        - value: Together
        - value: Upstage
        - value: Venice
        - value: WandB
        - value: Xiaomi
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    Schema5Items:
      oneOf:
        - $ref: '#/components/schemas/Schema5Items0'
        - type: string
    __schema5:
      type: array
      items:
        $ref: '#/components/schemas/Schema5Items'
    __schema4:
      oneOf:
        - $ref: '#/components/schemas/__schema5'
        - type: 'null'
    Schema8Items:
      type: string
      enum:
        - value: int4
        - value: int8
        - value: fp4
        - value: fp6
        - value: fp8
        - value: fp16
        - value: bf16
        - value: fp32
        - value: unknown
    __schema8:
      type:
        - array
        - 'null'
      items:
        $ref: '#/components/schemas/Schema8Items'
    ProviderSort:
      type: string
      enum:
        - value: price
        - value: throughput
        - value: latency
    ProviderSortConfigPartition:
      type: string
      enum:
        - value: model
        - value: none
    ProviderSortConfig:
      type: object
      properties:
        by:
          oneOf:
            - $ref: '#/components/schemas/ProviderSort'
            - type: 'null'
        partition:
          oneOf:
            - $ref: '#/components/schemas/ProviderSortConfigPartition'
            - type: 'null'
    ProviderSortUnion:
      oneOf:
        - $ref: '#/components/schemas/ProviderSort'
        - $ref: '#/components/schemas/ProviderSortConfig'
    __schema9:
      oneOf:
        - $ref: '#/components/schemas/ProviderSortUnion'
        - type: 'null'
    __schema11:
      type: number
      format: double
    ModelName:
      type: string
    __schema13:
      description: Any type
    Schema10Prompt:
      oneOf:
        - $ref: '#/components/schemas/__schema11'
        - $ref: '#/components/schemas/ModelName'
        - $ref: '#/components/schemas/__schema13'
    Schema10Completion:
      oneOf:
        - $ref: '#/components/schemas/__schema11'
        - $ref: '#/components/schemas/ModelName'
        - $ref: '#/components/schemas/__schema13'
    __schema14:
      oneOf:
        - $ref: '#/components/schemas/__schema11'
        - $ref: '#/components/schemas/ModelName'
        - $ref: '#/components/schemas/__schema13'
    __schema10:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/Schema10Prompt'
        completion:
          $ref: '#/components/schemas/Schema10Completion'
        image:
          $ref: '#/components/schemas/__schema14'
        audio:
          $ref: '#/components/schemas/__schema14'
        request:
          $ref: '#/components/schemas/__schema14'
    Schema151:
      type: object
      properties:
        p50:
          type:
            - number
            - 'null'
          format: double
        p75:
          type:
            - number
            - 'null'
          format: double
        p90:
          type:
            - number
            - 'null'
          format: double
        p99:
          type:
            - number
            - 'null'
          format: double
    Schema15:
      oneOf:
        - type: number
          format: double
        - $ref: '#/components/schemas/Schema151'
    __schema15:
      oneOf:
        - $ref: '#/components/schemas/Schema15'
        - type: 'null'
    Schema0:
      type: object
      properties:
        allow_fallbacks:
          $ref: '#/components/schemas/__schema1'
          description: >
            Whether to allow backup providers to serve requests

            - true: (default) when the primary provider (or your custom
            providers in "order") is unavailable, use the next best provider.

            - false: use only the primary/custom provider, and return the
            upstream error if it's unavailable.
        require_parameters:
          $ref: '#/components/schemas/__schema1'
          description: >-
            Whether to filter providers to only those that support the
            parameters you've provided. If this setting is omitted or set to
            false, then providers will receive only the parameters they support,
            and ignore the rest.
        data_collection:
          $ref: '#/components/schemas/__schema3'
          description: >-
            Data collection setting. If no available model provider meets the
            requirement, your request will return an error.

            - allow: (default) allow providers which store user data
            non-transiently and may train on it


            - deny: use only providers which do not collect user data.
        zdr:
          type:
            - boolean
            - 'null'
        enforce_distillable_text:
          type:
            - boolean
            - 'null'
        order:
          $ref: '#/components/schemas/__schema4'
          description: >-
            An ordered list of provider slugs. The router will attempt to use
            the first provider in the subset of this list that supports your
            requested model, and fall back to the next if it is unavailable. If
            no providers are available, the request will fail with an error
            message.
        only:
          $ref: '#/components/schemas/__schema4'
          description: >-
            List of provider slugs to allow. If provided, this list is merged
            with your account-wide allowed provider settings for this request.
        ignore:
          $ref: '#/components/schemas/__schema4'
          description: >-
            List of provider slugs to ignore. If provided, this list is merged
            with your account-wide ignored provider settings for this request.
        quantizations:
          $ref: '#/components/schemas/__schema8'
          description: A list of quantization levels to filter the provider by.
        sort:
          $ref: '#/components/schemas/__schema9'
          description: >-
            The sorting strategy to use for this request, if "order" is not
            specified. When set, no load balancing is performed.
        max_price:
          $ref: '#/components/schemas/__schema10'
          description: >-
            The object specifying the maximum price you want to pay for this
            request. USD price per million tokens, for prompt and completion.
        preferred_min_throughput:
          $ref: '#/components/schemas/__schema15'
          description: >-
            Preferred minimum throughput (in tokens per second). Can be a number
            (applies to p50) or an object with percentile-specific cutoffs.
            Endpoints below the threshold(s) may still be used, but are
            deprioritized in routing. When using fallback models, this may cause
            a fallback model to be used instead of the primary model if it meets
            the threshold.
        preferred_max_latency:
          $ref: '#/components/schemas/__schema15'
          description: >-
            Preferred maximum latency (in seconds). Can be a number (applies to
            p50) or an object with percentile-specific cutoffs. Endpoints above
            the threshold(s) may still be used, but are deprioritized in
            routing. When using fallback models, this may cause a fallback model
            to be used instead of the primary model if it meets the threshold.
    __schema0:
      oneOf:
        - $ref: '#/components/schemas/Schema0'
        - type: 'null'
    Schema17Items0:
      type: object
      properties:
        id:
          type: string
          enum:
            - type: stringLiteral
              value: auto-router
        enabled:
          type: boolean
        allowed_models:
          type: array
          items:
            type: string
      required:
        - id
    Schema17Items1:
      type: object
      properties:
        id:
          type: string
          enum:
            - type: stringLiteral
              value: moderation
      required:
        - id
    Schema17ItemsOneOf2Engine:
      type: string
      enum:
        - value: native
        - value: exa
    Schema17Items2:
      type: object
      properties:
        id:
          type: string
          enum:
            - type: stringLiteral
              value: web
        enabled:
          type: boolean
        max_results:
          type: number
          format: double
        search_prompt:
          type: string
        engine:
          $ref: '#/components/schemas/Schema17ItemsOneOf2Engine'
      required:
        - id
    Schema17ItemsOneOf3PdfEngine:
      type: string
      enum:
        - value: mistral-ocr
        - value: pdf-text
        - value: native
    Schema17ItemsOneOf3Pdf:
      type: object
      properties:
        engine:
          $ref: '#/components/schemas/Schema17ItemsOneOf3PdfEngine'
    Schema17Items3:
      type: object
      properties:
        id:
          type: string
          enum:
            - type: stringLiteral
              value: file-parser
        enabled:
          type: boolean
        pdf:
          $ref: '#/components/schemas/Schema17ItemsOneOf3Pdf'
      required:
        - id
    Schema17Items4:
      type: object
      properties:
        id:
          type: string
          enum:
            - type: stringLiteral
              value: response-healing
        enabled:
          type: boolean
      required:
        - id
    Schema17Items:
      oneOf:
        - $ref: '#/components/schemas/Schema17Items0'
        - $ref: '#/components/schemas/Schema17Items1'
        - $ref: '#/components/schemas/Schema17Items2'
        - $ref: '#/components/schemas/Schema17Items3'
        - $ref: '#/components/schemas/Schema17Items4'
    __schema17:
      type: array
      items:
        $ref: '#/components/schemas/Schema17Items'
    ChatGenerationParamsRoute:
      type: string
      enum:
        - value: fallback
        - value: sort
    __schema18:
      type: string
    ChatGenerationParamsTrace:
      type: object
      properties:
        trace_id:
          type: string
        trace_name:
          type: string
        span_name:
          type: string
        generation_name:
          type: string
        parent_span_id:
          type: string
    ChatMessageContentItemCacheControlTtl:
      type: string
      enum:
        - value: 5m
        - value: 1h
    ChatMessageContentItemCacheControl:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: ephemeral
        ttl:
          $ref: '#/components/schemas/ChatMessageContentItemCacheControlTtl'
      required:
        - type
    ChatMessageContentItemText:
      type: object
      properties:
        type:
          type: string
          enum:
            - &ref_0
              type: stringLiteral
              value: text
        text:
          type: string
        cache_control:
          $ref: '#/components/schemas/ChatMessageContentItemCacheControl'
      required:
        - type
        - text
    SystemMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItemText'
    SystemMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/SystemMessageContent1'
    SystemMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: system
        content:
          $ref: '#/components/schemas/SystemMessageContent'
        name:
          type: string
      required:
        - role
        - content
    ChatMessageContentItemImageImageUrlDetail:
      type: string
      enum:
        - value: auto
        - value: low
        - value: high
    ChatMessageContentItemImageImageUrl:
      type: object
      properties:
        url:
          type: string
        detail:
          $ref: '#/components/schemas/ChatMessageContentItemImageImageUrlDetail'
      required:
        - url
    ChatMessageContentItemAudioInputAudio:
      type: object
      properties:
        data:
          type: string
        format:
          type: string
      required:
        - data
        - format
    ChatMessageContentItemVideoOneOf0VideoUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    ChatMessageContentItemVideo0:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: input_video
        video_url:
          $ref: '#/components/schemas/ChatMessageContentItemVideoOneOf0VideoUrl'
      required:
        - type
        - video_url
    ChatMessageContentItemVideoOneOf1VideoUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    ChatMessageContentItemVideo1:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: video_url
        video_url:
          $ref: '#/components/schemas/ChatMessageContentItemVideoOneOf1VideoUrl'
      required:
        - type
        - video_url
    ChatMessageContentItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - *ref_0
            text:
              type: string
            cache_control:
              $ref: '#/components/schemas/ChatMessageContentItemCacheControl'
          required:
            - type
            - text
          description: text variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - type: stringLiteral
                  value: image_url
            image_url:
              $ref: '#/components/schemas/ChatMessageContentItemImageImageUrl'
          required:
            - type
            - image_url
          description: image_url variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - type: stringLiteral
                  value: input_audio
            input_audio:
              $ref: '#/components/schemas/ChatMessageContentItemAudioInputAudio'
          required:
            - type
            - input_audio
          description: input_audio variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - input_video
              description: 'Discriminator value: input_video'
          required:
            - type
          description: input_video variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - video_url
              description: 'Discriminator value: video_url'
          required:
            - type
          description: video_url variant
      discriminator:
        propertyName: type
    UserMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    UserMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/UserMessageContent1'
    UserMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: user
        content:
          $ref: '#/components/schemas/UserMessageContent'
        name:
          type: string
      required:
        - role
        - content
    DeveloperMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItemText'
    DeveloperMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/DeveloperMessageContent1'
    DeveloperMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: developer
        content:
          $ref: '#/components/schemas/DeveloperMessageContent'
        name:
          type: string
      required:
        - role
        - content
    AssistantMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    AssistantMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/AssistantMessageContent1'
    ChatMessageToolCallFunction:
      type: object
      properties:
        name:
          type: string
        arguments:
          type: string
      required:
        - name
        - arguments
    ChatMessageToolCall:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/ChatMessageToolCallFunction'
      required:
        - id
        - type
        - function
    __schema20:
      type:
        - string
        - 'null'
    Schema21:
      type: string
      enum:
        - value: unknown
        - value: openai-responses-v1
        - value: azure-openai-responses-v1
        - value: xai-responses-v1
        - value: anthropic-claude-v1
        - value: google-gemini-v1
    __schema21:
      oneOf:
        - $ref: '#/components/schemas/Schema21'
        - type: 'null'
    Schema190:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: reasoning.summary
        summary:
          type: string
        id:
          $ref: '#/components/schemas/__schema20'
        format:
          $ref: '#/components/schemas/__schema21'
        index:
          $ref: '#/components/schemas/__schema11'
      required:
        - type
        - summary
    Schema191:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: reasoning.encrypted
        data:
          type: string
        id:
          $ref: '#/components/schemas/__schema20'
        format:
          $ref: '#/components/schemas/__schema21'
        index:
          $ref: '#/components/schemas/__schema11'
      required:
        - type
        - data
    Schema192:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: reasoning.text
        text:
          type:
            - string
            - 'null'
        signature:
          type:
            - string
            - 'null'
        id:
          $ref: '#/components/schemas/__schema20'
        format:
          $ref: '#/components/schemas/__schema21'
        index:
          $ref: '#/components/schemas/__schema11'
      required:
        - type
    __schema19:
      oneOf:
        - $ref: '#/components/schemas/Schema190'
        - $ref: '#/components/schemas/Schema191'
        - $ref: '#/components/schemas/Schema192'
    AssistantMessageImagesItemsImageUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
    AssistantMessageImagesItems:
      type: object
      properties:
        image_url:
          $ref: '#/components/schemas/AssistantMessageImagesItemsImageUrl'
      required:
        - image_url
    AssistantMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: assistant
        content:
          oneOf:
            - $ref: '#/components/schemas/AssistantMessageContent'
            - type: 'null'
        name:
          type: string
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ChatMessageToolCall'
        refusal:
          type:
            - string
            - 'null'
        reasoning:
          type:
            - string
            - 'null'
        reasoning_details:
          type: array
          items:
            $ref: '#/components/schemas/__schema19'
        images:
          type: array
          items:
            $ref: '#/components/schemas/AssistantMessageImagesItems'
      required:
        - role
    ToolResponseMessageContent1:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageContentItem'
    ToolResponseMessageContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ToolResponseMessageContent1'
    ToolResponseMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - type: stringLiteral
              value: tool
        content:
          $ref: '#/components/schemas/ToolResponseMessageContent'
        tool_call_id:
          type: string
      required:
        - role
        - content
        - tool_call_id
    Message:
      oneOf:
        - $ref: '#/components/schemas/SystemMessage'
        - $ref: '#/components/schemas/UserMessage'
        - $ref: '#/components/schemas/DeveloperMessage'
        - $ref: '#/components/schemas/AssistantMessage'
        - $ref: '#/components/schemas/ToolResponseMessage'
    ChatGenerationParamsReasoningEffort:
      type: string
      enum:
        - value: xhigh
        - value: high
        - value: medium
        - value: low
        - value: minimal
        - value: none
    ReasoningSummaryVerbosity:
      type: string
      enum:
        - value: auto
        - value: concise
        - value: detailed
    ChatGenerationParamsReasoning:
      type: object
      properties:
        effort:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationParamsReasoningEffort'
            - type: 'null'
        summary:
          oneOf:
            - $ref: '#/components/schemas/ReasoningSummaryVerbosity'
            - type: 'null'
    ChatGenerationParamsResponseFormat0:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: text
      required:
        - type
    ChatGenerationParamsResponseFormat1:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_object
      required:
        - type
    JSONSchemaConfig:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        schema:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ResponseFormatJSONSchema:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: json_schema
        json_schema:
          $ref: '#/components/schemas/JSONSchemaConfig'
      required:
        - type
        - json_schema
    ResponseFormatTextGrammar:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: grammar
        grammar:
          type: string
      required:
        - type
        - grammar
    ChatGenerationParamsResponseFormat4:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: python
      required:
        - type
    ChatGenerationParamsResponseFormat:
      oneOf:
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat0'
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat1'
        - $ref: '#/components/schemas/ResponseFormatJSONSchema'
        - $ref: '#/components/schemas/ResponseFormatTextGrammar'
        - $ref: '#/components/schemas/ChatGenerationParamsResponseFormat4'
    ChatGenerationParamsStop1:
      type: array
      items:
        $ref: '#/components/schemas/ModelName'
    ChatGenerationParamsStop:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ChatGenerationParamsStop1'
    ChatStreamOptions:
      type: object
      properties:
        include_usage:
          type: boolean
    NamedToolChoiceFunction:
      type: object
      properties:
        name:
          type: string
      required:
        - name
    NamedToolChoice:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/NamedToolChoiceFunction'
      required:
        - type
        - function
    ToolChoiceOption:
      oneOf:
        - type: string
          enum:
            - type: stringLiteral
              value: none
        - type: string
          enum:
            - type: stringLiteral
              value: auto
        - type: string
          enum:
            - type: stringLiteral
              value: required
        - $ref: '#/components/schemas/NamedToolChoice'
    ToolDefinitionJsonFunction:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        parameters:
          type: object
          additionalProperties:
            description: Any type
        strict:
          type:
            - boolean
            - 'null'
      required:
        - name
    ToolDefinitionJson:
      type: object
      properties:
        type:
          type: string
          enum:
            - type: stringLiteral
              value: function
        function:
          $ref: '#/components/schemas/ToolDefinitionJsonFunction'
      required:
        - type
        - function
    ChatGenerationParamsDebug:
      type: object
      properties:
        echo_upstream_body:
          type: boolean
    ChatGenerationParamsImageConfig:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: array
          items:
            description: Any type
    ChatGenerationParamsModalitiesItems:
      type: string
      enum:
        - value: text
        - value: image
    ChatGenerationParams:
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/__schema0'
          description: >-
            When multiple model providers are available, optionally indicate
            your routing preference.
        plugins:
          $ref: '#/components/schemas/__schema17'
          description: >-
            Plugins you want to enable for this request, including their
            settings.
        route:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationParamsRoute'
            - type: 'null'
        user:
          type: string
        session_id:
          $ref: '#/components/schemas/__schema18'
          description: >-
            A unique identifier for grouping related requests (e.g., a
            conversation or agent workflow) for observability. If provided in
            both the request body and the x-session-id header, the body value
            takes precedence. Maximum of 128 characters.
        trace:
          $ref: '#/components/schemas/ChatGenerationParamsTrace'
          description: >-
            Metadata for observability and tracing. Known keys (trace_id,
            trace_name, span_name, generation_name, parent_span_id) have special
            handling. Additional keys are passed through as custom metadata to
            configured broadcast destinations.
        messages:
          type: array
          items:
            $ref: '#/components/schemas/Message'
        model:
          $ref: '#/components/schemas/ModelName'
        models:
          type: array
          items:
            $ref: '#/components/schemas/ModelName'
        frequency_penalty:
          type:
            - number
            - 'null'
          format: double
        logit_bias:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
        logprobs:
          type:
            - boolean
            - 'null'
        top_logprobs:
          type:
            - number
            - 'null'
          format: double
        max_completion_tokens:
          type:
            - number
            - 'null'
          format: double
        max_tokens:
          type:
            - number
            - 'null'
          format: double
        metadata:
          type: object
          additionalProperties:
            type: string
        presence_penalty:
          type:
            - number
            - 'null'
          format: double
        reasoning:
          $ref: '#/components/schemas/ChatGenerationParamsReasoning'
        response_format:
          $ref: '#/components/schemas/ChatGenerationParamsResponseFormat'
        seed:
          type:
            - integer
            - 'null'
        stop:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationParamsStop'
            - type: 'null'
        stream:
          type: boolean
          default: false
        stream_options:
          oneOf:
            - $ref: '#/components/schemas/ChatStreamOptions'
            - type: 'null'
        temperature:
          type:
            - number
            - 'null'
          format: double
          default: 1
        tool_choice:
          $ref: '#/components/schemas/ToolChoiceOption'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/ToolDefinitionJson'
        top_p:
          type:
            - number
            - 'null'
          format: double
          default: 1
        debug:
          $ref: '#/components/schemas/ChatGenerationParamsDebug'
        image_config:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ChatGenerationParamsImageConfig'
        modalities:
          type: array
          items:
            $ref: '#/components/schemas/ChatGenerationParamsModalitiesItems'
      required:
        - messages
    ChatCompletionFinishReason:
      type: string
      enum:
        - value: tool_calls
        - value: stop
        - value: length
        - value: content_filter
        - value: error
    __schema25:
      oneOf:
        - $ref: '#/components/schemas/ChatCompletionFinishReason'
        - type: 'null'
    ChatMessageTokenLogprobTopLogprobsItems:
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
      required:
        - token
        - logprob
        - bytes
    ChatMessageTokenLogprob:
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
        top_logprobs:
          type: array
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprobTopLogprobsItems'
      required:
        - token
        - logprob
        - bytes
        - top_logprobs
    ChatMessageTokenLogprobs:
      type: object
      properties:
        content:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprob'
        refusal:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ChatMessageTokenLogprob'
      required:
        - content
        - refusal
    ChatResponseChoice:
      type: object
      properties:
        finish_reason:
          $ref: '#/components/schemas/__schema25'
        index:
          type: number
          format: double
        message:
          $ref: '#/components/schemas/AssistantMessage'
        logprobs:
          oneOf:
            - $ref: '#/components/schemas/ChatMessageTokenLogprobs'
            - type: 'null'
      required:
        - finish_reason
        - index
        - message
    ChatGenerationTokenUsageCompletionTokensDetails:
      type: object
      properties:
        reasoning_tokens:
          type:
            - number
            - 'null'
          format: double
        audio_tokens:
          type:
            - number
            - 'null'
          format: double
        accepted_prediction_tokens:
          type:
            - number
            - 'null'
          format: double
        rejected_prediction_tokens:
          type:
            - number
            - 'null'
          format: double
    ChatGenerationTokenUsagePromptTokensDetails:
      type: object
      properties:
        cached_tokens:
          type: number
          format: double
        cache_write_tokens:
          type: number
          format: double
        audio_tokens:
          type: number
          format: double
        video_tokens:
          type: number
          format: double
    ChatGenerationTokenUsage:
      type: object
      properties:
        completion_tokens:
          type: number
          format: double
        prompt_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        completion_tokens_details:
          oneOf:
            - $ref: >-
                #/components/schemas/ChatGenerationTokenUsageCompletionTokensDetails
            - type: 'null'
        prompt_tokens_details:
          oneOf:
            - $ref: '#/components/schemas/ChatGenerationTokenUsagePromptTokensDetails'
            - type: 'null'
      required:
        - completion_tokens
        - prompt_tokens
        - total_tokens
    ChatResponse:
      type: object
      properties:
        id:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/ChatResponseChoice'
        created:
          type: number
          format: double
        model:
          type: string
        object:
          type: string
          enum:
            - type: stringLiteral
              value: chat.completion
        system_fingerprint:
          type:
            - string
            - 'null'
        usage:
          $ref: '#/components/schemas/ChatGenerationTokenUsage'
      required:
        - id
        - choices
        - created
        - model
        - object

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/chat/completions"

payload = { "messages": [
        {
            "role": "user",
            "content": "Can you explain the theory of relativity in simple terms?"
        }
    ] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/chat/completions';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"messages":[{"role":"user","content":"Can you explain the theory of relativity in simple terms?"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/chat/completions"

	payload := strings.NewReader("{\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you explain the theory of relativity in simple terms?\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/chat/completions")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you explain the theory of relativity in simple terms?\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/chat/completions")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you explain the theory of relativity in simple terms?\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/chat/completions', [
  'body' => '{
  "messages": [
    {
      "role": "user",
      "content": "Can you explain the theory of relativity in simple terms?"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://openrouter.ai/api/v1/chat/completions");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you explain the theory of relativity in simple terms?\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["messages": [
    [
      "role": "user",
      "content": "Can you explain the theory of relativity in simple terms?"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/chat/completions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```