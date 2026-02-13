---
title: Responses - Python SDK
url: https://openrouter.ai/docs/sdks/python/api-reference/responses.mdx
source: llms
fetched_at: 2026-02-13T15:17:39.757715-03:00
rendered_js: false
word_count: 808
summary: This document provides a technical reference for the beta.responses endpoint in the OpenRouter Python SDK, specifically detailing the send method for generating streaming or non-streaming model responses.
tags:
    - openrouter-sdk
    - python-sdk
    - api-reference
    - streaming-responses
    - ai-integration
    - beta-feature
category: api
---

***

title: Responses - Python SDK
subtitle: Responses method reference
headline: Responses | OpenRouter Python SDK
canonical-url: '[https://openrouter.ai/docs/sdks/python/api-reference/responses](https://openrouter.ai/docs/sdks/python/api-reference/responses)'
'og:site\_name': OpenRouter Documentation
'og:title': Responses | OpenRouter Python SDK
'og:description': >-
Responses method documentation for the OpenRouter Python SDK. Learn how to use
this API endpoint with code examples.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Responses%20-%20Python%20SDK\&description=Responses%20method%20reference](https://openrouter.ai/dynamic-og?title=Responses%20-%20Python%20SDK\&description=Responses%20method%20reference)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

{/* banner:start */}

<Warning>
  The Python SDK and docs are currently in beta.
  Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).
</Warning>

{/* banner:end */}

(*beta.responses*)

## Overview

beta.responses endpoints

### Available Operations

* [send](#send) - Create a response

## send

Creates a streaming or non-streaming response using OpenResponses API format

### Example Usage

{/* UsageSnippet language="python" operationID="createResponses" method="post" path="/responses" */}

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.beta.responses.send(service_tier="auto", stream=False)

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter              | Type                                                                                                                                 | Required             | Description                                                                                                                                                                                                                                                                                          | Example                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `input`                | [Optional\[components.OpenResponsesInput\]](../../components/openresponsesinput.md)                                                  | :heavy\_minus\_sign: | Input for a response request - can be a string or array of items                                                                                                                                                                                                                                     | \[<br />`{"role": "user","content": "What is the weather today?"}`<br />] |
| `instructions`         | *OptionalNullable\[str]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `metadata`             | Dict\[str, *str*]                                                                                                                    | :heavy\_minus\_sign: | Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed.                                                                                                                                         | `{"user_id": "123","session_id": "abc-def-ghi"}`                          |
| `tools`                | List\[[components.OpenResponsesRequestToolUnion](/docs/sdks/python/api-reference/components/openresponsesrequesttoolunion)]          | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `tool_choice`          | [Optional\[components.OpenAIResponsesToolChoiceUnion\]](../../components/openairesponsestoolchoiceunion.md)                          | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `parallel_tool_calls`  | *OptionalNullable\[bool]*                                                                                                            | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `model`                | *Optional\[str]*                                                                                                                     | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `models`               | List\[*str*]                                                                                                                         | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `text`                 | [Optional\[components.OpenResponsesResponseText\]](../../components/openresponsesresponsetext.md)                                    | :heavy\_minus\_sign: | Text output configuration including format and verbosity                                                                                                                                                                                                                                             | `{"format": {"type": "text"}`,<br />"verbosity": "medium"<br />}          |
| `reasoning`            | [OptionalNullable\[components.OpenResponsesReasoningConfig\]](../../components/openresponsesreasoningconfig.md)                      | :heavy\_minus\_sign: | Configuration for reasoning mode in the response                                                                                                                                                                                                                                                     | `{"summary": "auto","enabled": true}`                                     |
| `max_output_tokens`    | *OptionalNullable\[float]*                                                                                                           | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `temperature`          | *OptionalNullable\[float]*                                                                                                           | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `top_p`                | *OptionalNullable\[float]*                                                                                                           | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `top_logprobs`         | *OptionalNullable\[int]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `max_tool_calls`       | *OptionalNullable\[int]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `presence_penalty`     | *OptionalNullable\[float]*                                                                                                           | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `frequency_penalty`    | *OptionalNullable\[float]*                                                                                                           | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `top_k`                | *Optional\[float]*                                                                                                                   | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `image_config`         | Dict\[str, [components.OpenResponsesRequestImageConfig](/docs/sdks/python/api-reference/components/openresponsesrequestimageconfig)] | :heavy\_minus\_sign: | Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/features/multimodal/image-generation](https://openrouter.ai/docs/features/multimodal/image-generation) for more details.                                                      | `{"aspect_ratio": "16:9"}`                                                |
| `modalities`           | List\[[components.ResponsesOutputModality](/docs/sdks/python/api-reference/components/responsesoutputmodality)]                      | :heavy\_minus\_sign: | Output modalities for the response. Supported values are "text" and "image".                                                                                                                                                                                                                         | \[<br />"text",<br />"image"<br />]                                       |
| `prompt_cache_key`     | *OptionalNullable\[str]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `previous_response_id` | *OptionalNullable\[str]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `prompt`               | [OptionalNullable\[components.OpenAIResponsesPrompt\]](../../components/openairesponsesprompt.md)                                    | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `include`              | List\[[components.OpenAIResponsesIncludable](/docs/sdks/python/api-reference/components/openairesponsesincludable)]                  | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `background`           | *OptionalNullable\[bool]*                                                                                                            | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `safety_identifier`    | *OptionalNullable\[str]*                                                                                                             | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `service_tier`         | [Optional\[components.ServiceTier\]](../../components/servicetier.md)                                                                | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `truncation`           | [OptionalNullable\[components.Truncation\]](../../components/truncation.md)                                                          | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  | auto                                                                      |
| `stream`               | *Optional\[bool]*                                                                                                                    | :heavy\_minus\_sign: | N/A                                                                                                                                                                                                                                                                                                  |                                                                           |
| `provider`             | [OptionalNullable\[components.OpenResponsesRequestProvider\]](../../components/openresponsesrequestprovider.md)                      | :heavy\_minus\_sign: | When multiple model providers are available, optionally indicate your routing preference.                                                                                                                                                                                                            |                                                                           |
| `plugins`              | List\[[components.OpenResponsesRequestPluginUnion](/docs/sdks/python/api-reference/components/openresponsesrequestpluginunion)]      | :heavy\_minus\_sign: | Plugins you want to enable for this request, including their settings.                                                                                                                                                                                                                               |                                                                           |
| `user`                 | *Optional\[str]*                                                                                                                     | :heavy\_minus\_sign: | A unique identifier representing your end-user, which helps distinguish between different users of your app. This allows your app to identify specific users in case of abuse reports, preventing your entire app from being affected by the actions of individual users. Maximum of 128 characters. |                                                                           |
| `session_id`           | *Optional\[str]*                                                                                                                     | :heavy\_minus\_sign: | A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 128 characters.                                                          |                                                                           |
| `retries`              | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.md)                                                                   | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                           |

### Response

**[operations.CreateResponsesResponse](/docs/sdks/python/api-reference/operations/createresponsesresponse)**

### Errors

| Error Type                              | Status Code | Content Type     |
| --------------------------------------- | ----------- | ---------------- |
| errors.BadRequestResponseError          | 400         | application/json |
| errors.UnauthorizedResponseError        | 401         | application/json |
| errors.PaymentRequiredResponseError     | 402         | application/json |
| errors.NotFoundResponseError            | 404         | application/json |
| errors.RequestTimeoutResponseError      | 408         | application/json |
| errors.PayloadTooLargeResponseError     | 413         | application/json |
| errors.UnprocessableEntityResponseError | 422         | application/json |
| errors.TooManyRequestsResponseError     | 429         | application/json |
| errors.InternalServerResponseError      | 500         | application/json |
| errors.BadGatewayResponseError          | 502         | application/json |
| errors.ServiceUnavailableResponseError  | 503         | application/json |
| errors.EdgeNetworkTimeoutResponseError  | 524         | application/json |
| errors.ProviderOverloadedResponseError  | 529         | application/json |
| errors.OpenRouterDefaultError           | 4XX, 5XX    | \*/\*            |