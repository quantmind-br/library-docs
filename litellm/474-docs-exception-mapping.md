---
title: Exception Mapping | liteLLM
url: https://docs.litellm.ai/docs/exception_mapping
source: sitemap
fetched_at: 2026-01-21T19:45:10.078565273-03:00
rendered_js: false
word_count: 1040
summary: This document details how LiteLLM maps exceptions from multiple LLM providers to standardized OpenAI-compatible error types for consistent error handling.
tags:
    - litellm
    - exception-handling
    - error-mapping
    - openai-compatibility
    - python-sdk
    - api-errors
category: reference
---

LiteLLM maps exceptions across all providers to their OpenAI counterparts.

All exceptions can be imported from `litellm` - e.g. `from litellm import BadRequestError`

## LiteLLM Exceptions[​](#litellm-exceptions "Direct link to LiteLLM Exceptions")

Status CodeError TypeInherits fromDescription400BadRequestErroropenai.BadRequestError400UnsupportedParamsErrorlitellm.BadRequestErrorRaised when unsupported params are passed400ContextWindowExceededErrorlitellm.BadRequestErrorSpecial error type for context window exceeded error messages - enables context window fallbacks400ContentPolicyViolationErrorlitellm.BadRequestErrorSpecial error type for content policy violation error messages - enables content policy fallbacks400ImageFetchErrorlitellm.BadRequestErrorRaised when there are errors fetching or processing images400InvalidRequestErroropenai.BadRequestErrorDeprecated error, use BadRequestError instead401AuthenticationErroropenai.AuthenticationError403PermissionDeniedErroropenai.PermissionDeniedError404NotFoundErroropenai.NotFoundErrorraise when invalid models passed, example gpt-8408Timeoutopenai.APITimeoutErrorRaised when a timeout occurs422UnprocessableEntityErroropenai.UnprocessableEntityError429RateLimitErroropenai.RateLimitError500APIConnectionErroropenai.APIConnectionErrorIf any unmapped error is returned, we return this error500APIErroropenai.APIErrorGeneric 500-status code error503ServiceUnavailableErroropenai.APIStatusErrorIf provider returns a service unavailable error, this error is raised&gt;=500InternalServerErroropenai.InternalServerErrorIf any unmapped 500-status code error is returned, this error is raisedN/AAPIResponseValidationErroropenai.APIResponseValidationErrorIf Rules are used, and request/response fails a rule, this error is raisedN/ABudgetExceededErrorExceptionRaised for proxy, when budget is exceededN/AJSONSchemaValidationErrorlitellm.APIResponseValidationErrorRaised when response does not match expected json schema - used if `response_schema` param passed in with `enforce_validation=True`N/AMockExceptionExceptionInternal exception, raised by mock\_completion class. Do not use directlyN/AOpenAIErroropenai.OpenAIErrorDeprecated internal exception, inherits from openai.OpenAIError.

Base case we return APIConnectionError

All our exceptions inherit from OpenAI's exception types, so any error-handling you have for that, should work out of the box with LiteLLM.

For all cases, the exception returned inherits from the original OpenAI Exception but contains 3 additional attributes:

- status\_code - the http status code of the exception
- message - the error message
- llm\_provider - the provider raising the exception

## Usage[​](#usage "Direct link to Usage")

```
import litellm
import openai

try:
    response = litellm.completion(
                model="gpt-4",
                messages=[
{
"role":"user",
"content":"hello, write a 20 pageg essay"
}
],
                timeout=0.01,# this will raise a timeout exception
)
except openai.APITimeoutError as e:
print("Passed: Raised correct exception. Got openai.APITimeoutError\nGood Job", e)
print(type(e))
pass
```

## Usage - Catching Streaming Exceptions[​](#usage---catching-streaming-exceptions "Direct link to Usage - Catching Streaming Exceptions")

```
import litellm
try:
    response = litellm.completion(
        model="gpt-3.5-turbo",
        messages=[
{
"role":"user",
"content":"hello, write a 20 pg essay"
}
],
        timeout=0.0001,# this will raise an exception
        stream=True,
)
for chunk in response:
print(chunk)
except openai.APITimeoutError as e:
print("Passed: Raised correct exception. Got openai.APITimeoutError\nGood Job", e)
print(type(e))
pass
except Exception as e:
print(f"Did not raise error `openai.APITimeoutError`. Instead raised error type: {type(e)}, Error: {e}")

```

## Usage - Should you retry exception?[​](#usage---should-you-retry-exception "Direct link to Usage - Should you retry exception?")

```
import litellm
import openai

try:
    response = litellm.completion(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": "hello, write a 20 pageg essay"
                    }
                ],
                timeout=0.01, # this will raise a timeout exception
            )
except openai.APITimeoutError as e:
    should_retry = litellm._should_retry(e.status_code)
    print(f"should_retry: {should_retry}")
```

## Advanced[​](#advanced "Direct link to Advanced")

### Accessing Provider-Specific Error Details[​](#accessing-provider-specific-error-details "Direct link to Accessing Provider-Specific Error Details")

LiteLLM exceptions include a `provider_specific_fields` attribute that contains additional error information specific to each provider. This is particularly useful for Azure OpenAI, which provides detailed content filtering information.

#### Azure OpenAI - Content Policy Violation Inner Error Access[​](#azure-openai---content-policy-violation-inner-error-access "Direct link to Azure OpenAI - Content Policy Violation Inner Error Access")

When Azure OpenAI returns content policy violations, you can access the detailed content filtering results through the `innererror` field:

```
import litellm
from litellm.exceptions import ContentPolicyViolationError

try:
    response = litellm.completion(
        model="azure/gpt-4",
        messages=[
{
"role":"user",
"content":"Some content that might violate policies"
}
]
)
except ContentPolicyViolationError as e:
# Access Azure-specific error details
if e.provider_specific_fields and"innererror"in e.provider_specific_fields:
        innererror = e.provider_specific_fields["innererror"]

# Access content filter results
        content_filter_result = innererror.get("content_filter_result",{})

print(f"Content filter code: {innererror.get('code')}")
print(f"Hate filtered: {content_filter_result.get('hate', {}).get('filtered')}")
print(f"Violence severity: {content_filter_result.get('violence', {}).get('severity')}")
print(f"Sexual content filtered: {content_filter_result.get('sexual', {}).get('filtered')}")
```

**Example Response Structure:**

When calling the LiteLLM proxy, content policy violations will return detailed filtering information:

```
{
"error":{
"message":"litellm.ContentPolicyViolationError: AzureException - The response was filtered due to the prompt triggering Azure OpenAI's content management policy...",
"type":null,
"param":null,
"code":"400",
"provider_specific_fields":{
"innererror":{
"code":"ResponsibleAIPolicyViolation",
"content_filter_result":{
"hate":{
"filtered":true,
"severity":"high"
},
"jailbreak":{
"filtered":false,
"detected":false
},
"self_harm":{
"filtered":false,
"severity":"safe"
},
"sexual":{
"filtered":false,
"severity":"safe"
},
"violence":{
"filtered":true,
"severity":"medium"
}
}
}
}
}
}

## Details 

To see how it's implemented - [check out the code](https://github.com/BerriAI/litellm/blob/a42c197e5a6de56ea576c73715e6c7c6b19fa249/litellm/utils.py#L1217)

[Create an issue](https://github.com/BerriAI/litellm/issues/new) **or** [make a PR](https://github.com/BerriAI/litellm/pulls) if you want to improve the exception mapping. 

**Note** For OpenAI and Azure we return the original exception (since they're of the OpenAI Error type). But we add the 'llm_provider' attribute to them. [See code](https://github.com/BerriAI/litellm/blob/a42c197e5a6de56ea576c73715e6c7c6b19fa249/litellm/utils.py#L1221)

## Custom mapping list

Base case - we return `litellm.APIConnectionError` exception (inherits from openai's APIConnectionError exception).

| custom_llm_provider        | Timeout | ContextWindowExceededError | BadRequestError | NotFoundError | ContentPolicyViolationError | AuthenticationError | APIError | RateLimitError | ServiceUnavailableError | PermissionDeniedError | UnprocessableEntityError |
|----------------------------|---------|----------------------------|------------------|---------------|-----------------------------|---------------------|----------|----------------|-------------------------|-----------------------|-------------------------|
| openai                     | ✓       | ✓                          | ✓                |               | ✓                           | ✓                   |          |                |                         |                       |                           |
| watsonx                     |       | | | | | | |✓| | | |
| text-completion-openai     | ✓       | ✓                          | ✓                |               | ✓                           | ✓                   |          |                |                         |                       |                           |
| custom_openai              | ✓       | ✓                          | ✓                |               | ✓                           | ✓                   |          |                |                         |                       |                           |
| openai_compatible_providers| ✓       | ✓                          | ✓                |               | ✓                           | ✓                   |          |                |                         |                       |                           |
| anthropic                  | ✓       | ✓                          | ✓                | ✓             |                             | ✓                   |          |                | ✓                       | ✓                     |                           |
| replicate                  | ✓       | ✓                          | ✓                | ✓             |                             | ✓                   |          | ✓              | ✓                       |                       |                           |
| bedrock                    | ✓       | ✓                          | ✓                | ✓             |                             | ✓                   |          | ✓              | ✓                       | ✓                     |                           |
| sagemaker                  |         | ✓                          | ✓                |               |                             |                     |          |                |                         |                       |                           |
| vertex_ai                  | ✓       |                            | ✓                |               |                             |                     | ✓        |                |                         |                       | ✓                         |
| palm                       | ✓       | ✓                          |                  |               |                             |                     | ✓        |                |                         |                       |                           |
| gemini                     | ✓       | ✓                          |                  |               |                             |                     | ✓        |                |                         |                       |                           |
| cloudflare                 |         |                            | ✓                |               |                             | ✓                   |          |                |                         |                       |                           |
| cohere                     |         | ✓                          | ✓                |               |                             | ✓                   |          |                | ✓                       |                       |                           |
| cohere_chat                |         | ✓                          | ✓                |               |                             | ✓                   |          |                | ✓                       |                       |                           |
| huggingface                | ✓       | ✓                          | ✓                |               |                             | ✓                   |          | ✓              | ✓                       |                       |                           |
| ai21                       | ✓       | ✓                          | ✓                | ✓             |                             | ✓                   |          | ✓              |                         |                       |                           |
| nlp_cloud                  | ✓       | ✓                          | ✓                |               |                             | ✓                   | ✓        | ✓              | ✓                       |                       |                           |
| together_ai                | ✓       | ✓                          | ✓                |               |                             | ✓                   |          |                |                         |                       |                           |
| aleph_alpha                |         |                            | ✓                |               |                             | ✓                   |          |                |                         |                       |                           |
| ollama                     | ✓       |                            | ✓                |               |                             |                     |          |                | ✓                       |                       |                           |
| ollama_chat                | ✓       |                            | ✓                |               |                             |                     |          |                | ✓                       |                       |                           |
| vllm                       |         |                            |                  |               |                             | ✓                   | ✓        |                |                         |                       |                           |
| azure                      | ✓       | ✓                          | ✓                | ✓             | ✓                           | ✓                   |          |                | ✓                       |                       |                           |

- "✓" indicates that the specified `custom_llm_provider` can raise the corresponding exception.
- Empty cells indicate the lack of association or that the provider does not raise that particular exception type as indicated by the function.


> For a deeper understanding of these exceptions, you can check out [this](https://github.com/BerriAI/litellm/blob/d7e58d13bf9ba9edbab2ab2f096f3de7547f35fa/litellm/utils.py#L1544) implementation for additional insights.

The `ContextWindowExceededError` is a sub-class of `InvalidRequestError`. It was introduced to provide more granularity for exception-handling scenarios. Please refer to [this issue to learn more](https://github.com/BerriAI/litellm/issues/228).

Contributions to improve exception mapping are [welcome](https://github.com/BerriAI/litellm#contributing)
```