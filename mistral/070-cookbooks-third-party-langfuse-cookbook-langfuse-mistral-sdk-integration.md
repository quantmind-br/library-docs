---
title: Mistral AI SDK Integration with Langfuse - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-langfuse-cookbook_langfuse_mistral_sdk_integration
source: crawler
fetched_at: 2026-01-29T07:33:56.304007823-03:00
rendered_js: false
word_count: 871
---

This cookbook provides step-by-step examples of integrating Langfuse with the Mistral AI SDK (v1) in Python. By following these examples, you'll learn how to seamlessly log and trace interactions with Mistral's language models, enhancing the transparency, debuggability, and performance monitoring of your AI-driven applications.

* * *

Note: Langfuse is also natively integrated with [LangChain](https://langfuse.com/docs/integrations/langchain/tracing), [LlamaIndex](https://langfuse.com/docs/integrations/llama-index/get-started), [LiteLLM](https://langfuse.com/docs/integrations/litellm/tracing), and [other frameworks](https://langfuse.com/docs/integrations/overview). If you use one of them, any use of Mistral models is instrumented right away.

* * *

## Overview

In this notebook, we will explore various use cases where Langfuse can be integrated with Mistral AI SDK, including:

- **Basic LLM Calls:** Learn how to wrap standard Mistral model interactions with Langfuse's @observe decorator for comprehensive logging.
- **Chained Function Calls:** See how to manage and observe complex workflows where multiple model interactions are linked together to produce a final result.
- **Async and Streaming Support:** Discover how to use Langfuse with asynchronous and streaming responses from Mistral models, ensuring that real-time and concurrent interactions are fully traceable.
- **Function Calling:** Understand how to implement and observe external tool integrations with Mistral, allowing the model to interact with custom functions and APIs.

For more detailed guidance on the Mistral SDK or the **@observe** decorator from Langfuse, please refer to the [Mistral SDK repo](https://github.com/mistralai/client-python) and the [Langfuse Documentation](https://langfuse.com/docs/sdk/python/decorators#log-any-llm-call).

## What is Langfuse?

[Langfuse](https://langfuse.com/) is an open-source LLM engineering platform. It includes features such as [traces](https://langfuse.com/docs/tracing), [evals](https://langfuse.com/docs/scores/overview), and [prompt management](https://langfuse.com/docs/prompts/get-started) to help you debug and improve your LLM app.

## Setup

[Sign up](https://cloud.langfuse.com/auth/sign-up) for Langfuse if you haven't already. Copy your [API keys](https://langfuse.com/faq/all/where-are-langfuse-api-keys) from your project settings and add them to your environment.

Set your Mistral API key as an environment variable. If you haven't already, [sign up for a Mistral acccount](https://console.mistral.ai/). Then [subscribe](https://console.mistral.ai/billing/) to a free trial or billing plan, after which you'll be able to [generate an API key](https://console.mistral.ai/api-keys/).

## Examples

### 1. Completions

We are integrating the Mistral AI SDK with Langfuse using the [@observe decorator](https://langfuse.com/docs/sdk/python/decorators), which is crucial for logging and tracing interactions with large language models (LLMs). The @observe(as\_type="generation") decorator specifically logs LLM interactions, capturing inputs, outputs, and model parameters. The resulting `mistral_completion` method can then be used across your project.

Optionally, other functions (api handlers, retrieval functions, ...) can be also decorated.

#### 1.1 Simple Example

In the following example, we also added the decorator to the top-level function `find_best_painter_from`. This function calls the mistral\_completion function, which is decorated with @observe(as\_type="generation"). This hierarchical setup hels to trace more complex applications which involve multiple LLM calls and other non-llm methods which are decorated with @observe.

You can use langfuse\_context.update\_current\_observation or langfuse\_context.update\_current\_trace to add additional details such as input, output, and model parameters to the trace.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/836a9585-cfcc-47f7-881f-85ebdd9f601b](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/836a9585-cfcc-47f7-881f-85ebdd9f601b)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-1.png)

#### 1.2 Chained Completions

This example demonstrates chaining multiple LLM calls using the @observe decorator. The first call identifies the best painter from a specified country, and the second call uses that painter's name to find their most famous painting. Both interactions are logged by Langfuse as we use the wrapped `mistral_completion` method created above, ensuring full traceability across the chained requests.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/a3360c6f-24ad-455c-aae7-eb9d5c6f5dac](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/a3360c6f-24ad-455c-aae7-eb9d5c6f5dac)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-2.png)

### 2. Streaming Completions

The following example demonstrates how to handle streaming responses from the Mistral model using the @observe(as\_type="generation") decorator. The process is similar to the *Completion* example but includes handling streamed data in real-time.

Just like in the previous example, we wrap the streaming function with the @observe decorator to capture the input, model parameters, and usage details. Additionally, the function processes the streamed output incrementally, updating the Langfuse context as each chunk is received.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/75a2a4fe-088d-4134-9797-ba9c21be01b2](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/75a2a4fe-088d-4134-9797-ba9c21be01b2)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-3.png)

### 3. Async Completion

This example showcases the use of the @observe decorator in an asynchronous context. It wraps an async function that interacts with the Mistral model, ensuring that both the request and the response are logged by Langfuse. The async function allows for non-blocking LLM calls, making it suitable for applications that require concurrency while maintaining full observability of the interactions.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/1f7d91ce-45dd-41bf-8e6f-1875086ed32f](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/1f7d91ce-45dd-41bf-8e6f-1875086ed32f)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-4.png)

### 4. Async Streaming

This example demonstrates the use of the @observe decorator in an asynchronous streaming context. It wraps an async function that streams responses from the Mistral model, logging each chunk of data in real-time.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/36608110-f6cf-4566-a080-7c18777e2dbf](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/36608110-f6cf-4566-a080-7c18777e2dbf)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-5.png)

### 5. Tool Calling

This snippet introduces Mistral's function-calling capability, where you can define custom functions to retrieve specific data, like payment status and date, based on a transaction ID. These functions are then registered with the Mistral model, allowing it to call them when processing queries. For a deeper dive into function calling with Mistral, refer to the official [Mistral documentation](https://docs.mistral.ai/capabilities/function_calling/).

The *check\_transaction\_status* function demonstrates the use of Mistral's function-calling capabilities. The function's result is then incorporated into the LLM's response, which is logged and traced in Langfuse. This example illustrates how external function calls can be seamlessly integrated into a Langfuse by using the the wrapped *mistral\_completion* function, ensuring that every step — from tool selection to final output - is captured for thorough observability.

Example trace in Langfuse: [https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/e986408a-f96b-40dc-8278-5d0eb0286f82](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/e986408a-f96b-40dc-8278-5d0eb0286f82)

![Example trace in Langfuse UI](https://docs.mistral.ai/cookbooks/third_party/Langfuse/images/trace-example-6.png)

## Feedback

* * *

If you have any feedback or requests, please create a GitHub [Issue](https://langfuse.com/issue) or share your idea with the community on [Discord](https://discord.langfuse.com/).