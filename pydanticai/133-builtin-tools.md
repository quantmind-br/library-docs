---
title: Built-in Tools - Pydantic AI
url: https://ai.pydantic.dev/builtin-tools/
source: sitemap
fetched_at: 2026-01-22T22:23:11.833564995-03:00
rendered_js: false
word_count: 2148
summary: This document explains how to use native built-in tools provided by LLM providers within Pydantic AI, including details on tool types, provider support, and dynamic configuration.
tags:
    - pydantic-ai
    - built-in-tools
    - agent-capabilities
    - dynamic-configuration
    - llm-providers
    - web-search
category: guide
---

Built-in tools are native tools provided by LLM providers that can be used to enhance your agent's capabilities. Unlike [common tools](https://ai.pydantic.dev/common-tools/), which are custom implementations that Pydantic AI executes, built-in tools are executed directly by the model provider.

## Overview

Pydantic AI supports the following built-in tools:

- [**`WebSearchTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebSearchTool "WebSearchTool            dataclass   "): Allows agents to search the web
- [**`CodeExecutionTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.CodeExecutionTool "CodeExecutionTool            dataclass   "): Enables agents to execute code in a secure environment
- [**`ImageGenerationTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool "ImageGenerationTool            dataclass   "): Enables agents to generate images
- [**`WebFetchTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebFetchTool "WebFetchTool            dataclass   "): Enables agents to fetch web pages
- [**`MemoryTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MemoryTool "MemoryTool            dataclass   "): Enables agents to use memory
- [**`MCPServerTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MCPServerTool "MCPServerTool            dataclass   "): Enables agents to use remote MCP servers with communication handled by the model provider
- [**`FileSearchTool`**](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.FileSearchTool "FileSearchTool            dataclass   "): Enables agents to search through uploaded files using vector search (RAG)

These tools are passed to the agent via the `builtin_tools` parameter and are executed by the model provider's infrastructure.

Provider Support

Not all model providers support built-in tools. If you use a built-in tool with an unsupported provider, Pydantic AI will raise a [`UserError`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError") when you try to run the agent.

If a provider supports a built-in tool that is not currently supported by Pydantic AI, please file an issue.

## Dynamic Configuration

Sometimes you need to configure a built-in tool dynamically based on the [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") (e.g., user dependencies), or conditionally omit it. You can achieve this by passing a function to `builtin_tools` that takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") as an argument and returns an [`AbstractBuiltinTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool            dataclass   ") or `None`.

This is particularly useful for tools like [`WebSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebSearchTool "WebSearchTool            dataclass   ") where you might want to set the user's location based on the current request, or disable the tool if the user provides no location.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) dynamic\_builtin\_tool.py

```
frompydantic_aiimport Agent, RunContext, WebSearchTool


async defprepared_web_search(ctx: RunContext[dict]) -> WebSearchTool | None:
    if not ctx.deps.get('location'):
        return None

    return WebSearchTool(
        user_location={'city': ctx.deps['location']},
    )

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[prepared_web_search],
    deps_type=dict,
)

# Run with location
result = agent.run_sync(
    'What is the weather like?',
    deps={'location': 'London'},
)
print(result.output)
#> It's currently raining in London.

# Run without location (tool will be omitted)
result = agent.run_sync(
    'What is the capital of France?',
    deps={'location': None},
)
print(result.output)
#> The capital of France is Paris.
```

dynamic\_builtin\_tool.py

```
frompydantic_aiimport Agent, RunContext, WebSearchTool


async defprepared_web_search(ctx: RunContext[dict]) -> WebSearchTool | None:
    if not ctx.deps.get('location'):
        return None

    return WebSearchTool(
        user_location={'city': ctx.deps['location']},
    )

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[prepared_web_search],
    deps_type=dict,
)

# Run with location
result = agent.run_sync(
    'What is the weather like?',
    deps={'location': 'London'},
)
print(result.output)
#> It's currently raining in London.

# Run without location (tool will be omitted)
result = agent.run_sync(
    'What is the capital of France?',
    deps={'location': None},
)
print(result.output)
#> The capital of France is Paris.
```

The [`WebSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebSearchTool "WebSearchTool            dataclass   ") allows your agent to search the web, making it ideal for queries that require up-to-date data.

### Provider Support

Provider Supported Notes OpenAI Responses ✅ Full feature support. To include search results on the [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") that's available via [`ModelResponse.builtin_tool_calls`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls "builtin_tool_calls            property   "), enable the [`OpenAIResponsesModelSettings.openai_include_web_search_sources`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings.openai_include_web_search_sources "openai_include_web_search_sources            instance-attribute   ") [model setting](https://ai.pydantic.dev/agents/#model-run-settings). Anthropic ✅ Full feature support Google ✅ No parameter support. No [`BuiltinToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart            dataclass   ") or [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") is generated when streaming. Using built-in tools and function tools (including [output tools](https://ai.pydantic.dev/output/#tool-output)) at the same time is not supported; to use structured output, use [`PromptedOutput`](https://ai.pydantic.dev/output/#prompted-output) instead. xAI ✅ Supports `blocked_domains` and `allowed_domains` parameters. Groq ✅ Limited parameter support. To use web search capabilities with Groq, you need to use the [compound models](https://console.groq.com/docs/compound). OpenAI Chat Completions ❌ Not supported Bedrock ❌ Not supported Mistral ❌ Not supported Cohere ❌ Not supported HuggingFace ❌ Not supported Outlines ❌ Not supported

### Usage

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) web\_search\_anthropic.py

```
frompydantic_aiimport Agent, WebSearchTool

agent = Agent('gateway/anthropic:claude-sonnet-4-0', builtin_tools=[WebSearchTool()])

result = agent.run_sync('Give me a sentence with the biggest news in AI this week.')
print(result.output)
#> Scientists have developed a universal AI detector that can identify deepfake videos.
```

web\_search\_anthropic.py

```
frompydantic_aiimport Agent, WebSearchTool

agent = Agent('anthropic:claude-sonnet-4-0', builtin_tools=[WebSearchTool()])

result = agent.run_sync('Give me a sentence with the biggest news in AI this week.')
print(result.output)
#> Scientists have developed a universal AI detector that can identify deepfake videos.
```

*(This example is complete, it can be run "as is")*

With OpenAI, you must use their Responses API to access the web search tool.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) web\_search\_openai.py

```
frompydantic_aiimport Agent, WebSearchTool

agent = Agent('gateway/openai-responses:gpt-5', builtin_tools=[WebSearchTool()])

result = agent.run_sync('Give me a sentence with the biggest news in AI this week.')
print(result.output)
#> Scientists have developed a universal AI detector that can identify deepfake videos.
```

web\_search\_openai.py

```
frompydantic_aiimport Agent, WebSearchTool

agent = Agent('openai-responses:gpt-5', builtin_tools=[WebSearchTool()])

result = agent.run_sync('Give me a sentence with the biggest news in AI this week.')
print(result.output)
#> Scientists have developed a universal AI detector that can identify deepfake videos.
```

*(This example is complete, it can be run "as is")*

### Configuration Options

The `WebSearchTool` supports several configuration parameters:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) web\_search\_configured.py

```
frompydantic_aiimport Agent, WebSearchTool, WebSearchUserLocation

agent = Agent(
    'gateway/anthropic:claude-sonnet-4-0',
    builtin_tools=[
        WebSearchTool(
            search_context_size='high',
            user_location=WebSearchUserLocation(
                city='San Francisco',
                country='US',
                region='CA',
                timezone='America/Los_Angeles',
            ),
            blocked_domains=['example.com', 'spam-site.net'],
            allowed_domains=None,  # Cannot use both blocked_domains and allowed_domains with Anthropic
            max_uses=5,  # Anthropic only: limit tool usage
        )
    ],
)

result = agent.run_sync('Use the web to get the current time.')
print(result.output)
#> In San Francisco, it's 8:21:41 pm PDT on Wednesday, August 6, 2025.
```

web\_search\_configured.py

```
frompydantic_aiimport Agent, WebSearchTool, WebSearchUserLocation

agent = Agent(
    'anthropic:claude-sonnet-4-0',
    builtin_tools=[
        WebSearchTool(
            search_context_size='high',
            user_location=WebSearchUserLocation(
                city='San Francisco',
                country='US',
                region='CA',
                timezone='America/Los_Angeles',
            ),
            blocked_domains=['example.com', 'spam-site.net'],
            allowed_domains=None,  # Cannot use both blocked_domains and allowed_domains with Anthropic
            max_uses=5,  # Anthropic only: limit tool usage
        )
    ],
)

result = agent.run_sync('Use the web to get the current time.')
print(result.output)
#> In San Francisco, it's 8:21:41 pm PDT on Wednesday, August 6, 2025.
```

*(This example is complete, it can be run "as is")*

#### Provider Support

Parameter OpenAI Anthropic xAI Groq `search_context_size` ✅ ❌ ❌ ❌ `user_location` ✅ ✅ ❌ ❌ `blocked_domains` ❌ ✅ ✅ ✅ `allowed_domains` ❌ ✅ ✅ ✅ `max_uses` ❌ ✅ ❌ ❌

Anthropic Domain Filtering

With Anthropic, you can only use either `blocked_domains` or `allowed_domains`, not both.

The [`CodeExecutionTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.CodeExecutionTool "CodeExecutionTool            dataclass   ") enables your agent to execute code in a secure environment, making it perfect for computational tasks, data analysis, and mathematical operations.

### Provider Support

Provider Supported Notes OpenAI ✅ To include code execution output on the [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") that's available via [`ModelResponse.builtin_tool_calls`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls "builtin_tool_calls            property   "), enable the [`OpenAIResponsesModelSettings.openai_include_code_execution_outputs`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings.openai_include_code_execution_outputs "openai_include_code_execution_outputs            instance-attribute   ") [model setting](https://ai.pydantic.dev/agents/#model-run-settings). If the code execution generated images, like charts, they will be available on [`ModelResponse.images`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.images "images            property   ") as [`BinaryImage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage") objects. The generated image can also be used as [image output](https://ai.pydantic.dev/output/#image-output) for the agent run. Google ✅ Using built-in tools and function tools (including [output tools](https://ai.pydantic.dev/output/#tool-output)) at the same time is not supported; to use structured output, use [`PromptedOutput`](https://ai.pydantic.dev/output/#prompted-output) instead. Anthropic ✅ xAI ✅ Full feature support. Groq ❌ Bedrock ✅ Only available for Nova 2.0 models. Mistral ❌ Cohere ❌ HuggingFace ❌ Outlines ❌

### Usage

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) code\_execution\_basic.py

```
frompydantic_aiimport Agent, CodeExecutionTool

agent = Agent('gateway/anthropic:claude-sonnet-4-0', builtin_tools=[CodeExecutionTool()])

result = agent.run_sync('Calculate the factorial of 15.')
print(result.output)
#> The factorial of 15 is **1,307,674,368,000**.
print(result.response.builtin_tool_calls)
"""
[
    (
        BuiltinToolCallPart(
            tool_name='code_execution',
            args={
                'code': 'import math\n\n# Calculate factorial of 15\nresult = math.factorial(15)\nprint(f"15! = {result}")\n\n# Let\'s also show it in a more readable format with commas\nprint(f"15! = {result:,}")'
            },
            tool_call_id='srvtoolu_017qRH1J3XrhnpjP2XtzPCmJ',
            provider_name='anthropic',
        ),
        BuiltinToolReturnPart(
            tool_name='code_execution',
            content={
                'content': [],
                'return_code': 0,
                'stderr': '',
                'stdout': '15! = 1307674368000\n15! = 1,307,674,368,000',
                'type': 'code_execution_result',
            },
            tool_call_id='srvtoolu_017qRH1J3XrhnpjP2XtzPCmJ',
            timestamp=datetime.datetime(...),
            provider_name='anthropic',
        ),
    )
]
"""
```

code\_execution\_basic.py

```
frompydantic_aiimport Agent, CodeExecutionTool

agent = Agent('anthropic:claude-sonnet-4-0', builtin_tools=[CodeExecutionTool()])

result = agent.run_sync('Calculate the factorial of 15.')
print(result.output)
#> The factorial of 15 is **1,307,674,368,000**.
print(result.response.builtin_tool_calls)
"""
[
    (
        BuiltinToolCallPart(
            tool_name='code_execution',
            args={
                'code': 'import math\n\n# Calculate factorial of 15\nresult = math.factorial(15)\nprint(f"15! = {result}")\n\n# Let\'s also show it in a more readable format with commas\nprint(f"15! = {result:,}")'
            },
            tool_call_id='srvtoolu_017qRH1J3XrhnpjP2XtzPCmJ',
            provider_name='anthropic',
        ),
        BuiltinToolReturnPart(
            tool_name='code_execution',
            content={
                'content': [],
                'return_code': 0,
                'stderr': '',
                'stdout': '15! = 1307674368000\n15! = 1,307,674,368,000',
                'type': 'code_execution_result',
            },
            tool_call_id='srvtoolu_017qRH1J3XrhnpjP2XtzPCmJ',
            timestamp=datetime.datetime(...),
            provider_name='anthropic',
        ),
    )
]
"""
```

*(This example is complete, it can be run "as is")*

In addition to text output, code execution with OpenAI can generate images as part of their response. Accessing this image via [`ModelResponse.images`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.images "images            property   ") or [image output](https://ai.pydantic.dev/output/#image-output) requires the [`OpenAIResponsesModelSettings.openai_include_code_execution_outputs`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings.openai_include_code_execution_outputs "openai_include_code_execution_outputs            instance-attribute   ") [model setting](https://ai.pydantic.dev/agents/#model-run-settings) to be enabled.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) code\_execution\_openai.py

```
frompydantic_aiimport Agent, BinaryImage, CodeExecutionTool
frompydantic_ai.models.openaiimport OpenAIResponsesModelSettings

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[CodeExecutionTool()],
    output_type=BinaryImage,
    model_settings=OpenAIResponsesModelSettings(openai_include_code_execution_outputs=True),
)

result = agent.run_sync('Generate a chart of y=x^2 for x=-5 to 5.')
assert isinstance(result.output, BinaryImage)
```

code\_execution\_openai.py

```
frompydantic_aiimport Agent, BinaryImage, CodeExecutionTool
frompydantic_ai.models.openaiimport OpenAIResponsesModelSettings

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[CodeExecutionTool()],
    output_type=BinaryImage,
    model_settings=OpenAIResponsesModelSettings(openai_include_code_execution_outputs=True),
)

result = agent.run_sync('Generate a chart of y=x^2 for x=-5 to 5.')
assert isinstance(result.output, BinaryImage)
```

*(This example is complete, it can be run "as is")*

The [`ImageGenerationTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool "ImageGenerationTool            dataclass   ") enables your agent to generate images.

### Provider Support

Provider Supported Notes OpenAI Responses ✅ Full feature support. Only supported by models newer than `gpt-5`. Metadata about the generated image, like the [`revised_prompt`](https://platform.openai.com/docs/guides/tools-image-generation#revised-prompt) sent to the underlying image model, is available on the [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") that's available via [`ModelResponse.builtin_tool_calls`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls "builtin_tool_calls            property   "). Google ✅ Limited parameter support. Only supported by [image generation models](https://ai.google.dev/gemini-api/docs/image-generation) like `gemini-2.5-flash-image` and `gemini-3-pro-image-preview`. These models do not support [function tools](https://ai.pydantic.dev/tools/) and will always have the option of generating images, even if this built-in tool is not explicitly specified. Anthropic ❌ xAI ❌ Groq ❌ Bedrock ❌ Mistral ❌ Cohere ❌ HuggingFace ❌

### Usage

Generated images are available on [`ModelResponse.images`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.images "images            property   ") as [`BinaryImage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage") objects:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_openai.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent('gateway/openai-responses:gpt-5', builtin_tools=[ImageGenerationTool()])

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

assert isinstance(result.response.images[0], BinaryImage)
```

image\_generation\_openai.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent('openai-responses:gpt-5', builtin_tools=[ImageGenerationTool()])

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

assert isinstance(result.response.images[0], BinaryImage)
```

*(This example is complete, it can be run "as is")*

Image generation with Google [image generation models](https://ai.google.dev/gemini-api/docs/image-generation) does not require the `ImageGenerationTool` built-in tool to be explicitly specified:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_google.py

```
frompydantic_aiimport Agent, BinaryImage

agent = Agent('gateway/gemini:gemini-2.5-flash-image')

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

assert isinstance(result.response.images[0], BinaryImage)
```

image\_generation\_google.py

```
frompydantic_aiimport Agent, BinaryImage

agent = Agent('google-gla:gemini-2.5-flash-image')

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

assert isinstance(result.response.images[0], BinaryImage)
```

*(This example is complete, it can be run "as is")*

The `ImageGenerationTool` can be used together with `output_type=BinaryImage` to get [image output](https://ai.pydantic.dev/output/#image-output). If the `ImageGenerationTool` built-in tool is not explicitly specified, it will be enabled automatically:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_output.py

```
frompydantic_aiimport Agent, BinaryImage

agent = Agent('gateway/openai-responses:gpt-5', output_type=BinaryImage)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

image\_generation\_output.py

```
frompydantic_aiimport Agent, BinaryImage

agent = Agent('openai-responses:gpt-5', output_type=BinaryImage)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

*(This example is complete, it can be run "as is")*

### Configuration Options

The `ImageGenerationTool` supports several configuration parameters:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_configured.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[
        ImageGenerationTool(
            background='transparent',
            input_fidelity='high',
            moderation='low',
            output_compression=100,
            output_format='png',
            partial_images=3,
            quality='high',
            size='1024x1024',
        )
    ],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

image\_generation\_configured.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[
        ImageGenerationTool(
            background='transparent',
            input_fidelity='high',
            moderation='low',
            output_compression=100,
            output_format='png',
            partial_images=3,
            quality='high',
            size='1024x1024',
        )
    ],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

*(This example is complete, it can be run "as is")*

OpenAI Responses models also respect the `aspect_ratio` parameter. Because the OpenAI API only exposes discrete image sizes, Pydantic AI maps `'1:1'` -&gt; `1024x1024`, `'2:3'` -&gt; `1024x1536`, and `'3:2'` -&gt; `1536x1024`. Providing any other aspect ratio results in an error, and if you also set `size` it must match the computed value.

To control the aspect ratio when using Gemini image models, include the `ImageGenerationTool` explicitly:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_google\_aspect\_ratio.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'gateway/gemini:gemini-2.5-flash-image',
    builtin_tools=[ImageGenerationTool(aspect_ratio='16:9')],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate a wide illustration of an axolotl city skyline.')
assert isinstance(result.output, BinaryImage)
```

image\_generation\_google\_aspect\_ratio.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'google-gla:gemini-2.5-flash-image',
    builtin_tools=[ImageGenerationTool(aspect_ratio='16:9')],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate a wide illustration of an axolotl city skyline.')
assert isinstance(result.output, BinaryImage)
```

*(This example is complete, it can be run "as is")*

To control the image resolution with Google image generation models (starting with Gemini 3 Pro Image), use the `size` parameter:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) image\_generation\_google\_resolution.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'gateway/gemini:gemini-3-pro-image-preview',
    builtin_tools=[ImageGenerationTool(aspect_ratio='16:9', size='4K')],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate a high-resolution wide landscape illustration of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

image\_generation\_google\_resolution.py

```
frompydantic_aiimport Agent, BinaryImage, ImageGenerationTool

agent = Agent(
    'google-gla:gemini-3-pro-image-preview',
    builtin_tools=[ImageGenerationTool(aspect_ratio='16:9', size='4K')],
    output_type=BinaryImage,
)

result = agent.run_sync('Generate a high-resolution wide landscape illustration of an axolotl.')
assert isinstance(result.output, BinaryImage)
```

*(This example is complete, it can be run "as is")*

For more details, check the [API documentation](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool "ImageGenerationTool            dataclass   ").

#### Provider Support

Parameter OpenAI Google `background` ✅ ❌ `input_fidelity` ✅ ❌ `moderation` ✅ ❌ `output_compression` ✅ (100 (default), jpeg or webp only) ✅ (75 (default), jpeg only, Vertex AI only) `output_format` ✅ ✅ (Vertex AI only) `partial_images` ✅ ❌ `quality` ✅ ❌ `size` ✅ (auto (default), 1024x1024, 1024x1536, 1536x1024) ✅ (1K (default), 2K, 4K) `aspect_ratio` ✅ (1:1, 2:3, 3:2) ✅ (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)

Notes

- **OpenAI**: `auto` lets the model select the value.
- **Google (Vertex AI)**: Setting `output_compression` will default `output_format` to `jpeg` if not specified.

The [`WebFetchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebFetchTool "WebFetchTool            dataclass   ") enables your agent to pull URL contents into its context, allowing it to pull up-to-date information from the web.

### Provider Support

Provider Supported Notes Anthropic ✅ Full feature support. Uses Anthropic's [Web Fetch Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool) internally to retrieve URL contents. Google ✅ No parameter support. The limits are fixed at 20 URLs per request with a maximum of 34MB per URL. Using built-in tools and function tools (including [output tools](https://ai.pydantic.dev/output/#tool-output)) at the same time is not supported; to use structured output, use [`PromptedOutput`](https://ai.pydantic.dev/output/#prompted-output) instead. xAI ❌ Web browsing is implemented as part of [`WebSearchTool`](#web-search-tool) with xAI. OpenAI ❌ Groq ❌ Bedrock ❌ Mistral ❌ Cohere ❌ HuggingFace ❌ Outlines ❌

### Usage

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) web\_fetch\_basic.py

```
frompydantic_aiimport Agent, WebFetchTool

agent = Agent('gateway/gemini:gemini-2.5-flash', builtin_tools=[WebFetchTool()])

result = agent.run_sync('What is this? https://ai.pydantic.dev')
print(result.output)
#> A Python agent framework for building Generative AI applications.
```

web\_fetch\_basic.py

```
frompydantic_aiimport Agent, WebFetchTool

agent = Agent('google-gla:gemini-2.5-flash', builtin_tools=[WebFetchTool()])

result = agent.run_sync('What is this? https://ai.pydantic.dev')
print(result.output)
#> A Python agent framework for building Generative AI applications.
```

*(This example is complete, it can be run "as is")*

### Configuration Options

The `WebFetchTool` supports several configuration parameters:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) web\_fetch\_configured.py

```
frompydantic_aiimport Agent, WebFetchTool

agent = Agent(
    'gateway/anthropic:claude-sonnet-4-0',
    builtin_tools=[
        WebFetchTool(
            allowed_domains=['ai.pydantic.dev', 'docs.pydantic.dev'],
            max_uses=10,
            enable_citations=True,
            max_content_tokens=50000,
        )
    ],
)

result = agent.run_sync(
    'Compare the documentation at https://ai.pydantic.dev and https://docs.pydantic.dev'
)
print(result.output)
"""
Both sites provide comprehensive documentation for Pydantic projects. ai.pydantic.dev focuses on PydanticAI, a framework for building AI agents, while docs.pydantic.dev covers Pydantic, the data validation library. They share similar documentation styles and both emphasize type safety and developer experience.
"""
```

web\_fetch\_configured.py

```
frompydantic_aiimport Agent, WebFetchTool

agent = Agent(
    'anthropic:claude-sonnet-4-0',
    builtin_tools=[
        WebFetchTool(
            allowed_domains=['ai.pydantic.dev', 'docs.pydantic.dev'],
            max_uses=10,
            enable_citations=True,
            max_content_tokens=50000,
        )
    ],
)

result = agent.run_sync(
    'Compare the documentation at https://ai.pydantic.dev and https://docs.pydantic.dev'
)
print(result.output)
"""
Both sites provide comprehensive documentation for Pydantic projects. ai.pydantic.dev focuses on PydanticAI, a framework for building AI agents, while docs.pydantic.dev covers Pydantic, the data validation library. They share similar documentation styles and both emphasize type safety and developer experience.
"""
```

*(This example is complete, it can be run "as is")*

#### Provider Support

Parameter Anthropic Google `max_uses` ✅ ❌ `allowed_domains` ✅ ❌ `blocked_domains` ✅ ❌ `enable_citations` ✅ ❌ `max_content_tokens` ✅ ❌

Anthropic Domain Filtering

With Anthropic, you can only use either `blocked_domains` or `allowed_domains`, not both.

The [`MemoryTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MemoryTool "MemoryTool            dataclass   ") enables your agent to use memory.

### Provider Support

Provider Supported Notes Anthropic ✅ Requires a tool named `memory` to be defined that implements [specific sub-commands](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool#tool-commands). You can use a subclass of [`anthropic.lib.tools.BetaAbstractMemoryTool`](https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/lib/tools/_beta_builtin_memory_tool.py) as documented below. Google ❌ OpenAI ❌ Groq ❌ Bedrock ❌ Mistral ❌ Cohere ❌ HuggingFace ❌

### Usage

The Anthropic SDK provides an abstract [`BetaAbstractMemoryTool`](https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/lib/tools/_beta_builtin_memory_tool.py) class that you can subclass to create your own memory storage solution (e.g., database, cloud storage, encrypted files, etc.). Their [`LocalFilesystemMemoryTool`](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py) example can serve as a starting point.

The following example uses a subclass that hard-codes a specific memory. The bits specific to Pydantic AI are the `MemoryTool` built-in tool and the `memory` tool definition that forwards commands to the `call` method of the `BetaAbstractMemoryTool` subclass.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) anthropic\_memory.py

```
fromtypingimport Any

fromanthropic.lib.toolsimport BetaAbstractMemoryTool
fromanthropic.types.betaimport (
    BetaMemoryTool20250818CreateCommand,
    BetaMemoryTool20250818DeleteCommand,
    BetaMemoryTool20250818InsertCommand,
    BetaMemoryTool20250818RenameCommand,
    BetaMemoryTool20250818StrReplaceCommand,
    BetaMemoryTool20250818ViewCommand,
)

frompydantic_aiimport Agent, MemoryTool


classFakeMemoryTool(BetaAbstractMemoryTool):
    defview(self, command: BetaMemoryTool20250818ViewCommand) -> str:
        return 'The user lives in Mexico City.'

    defcreate(self, command: BetaMemoryTool20250818CreateCommand) -> str:
        return f'File created successfully at {command.path}'

    defstr_replace(self, command: BetaMemoryTool20250818StrReplaceCommand) -> str:
        return f'File {command.path} has been edited'

    definsert(self, command: BetaMemoryTool20250818InsertCommand) -> str:
        return f'Text inserted at line {command.insert_line} in {command.path}'

    defdelete(self, command: BetaMemoryTool20250818DeleteCommand) -> str:
        return f'File deleted: {command.path}'

    defrename(self, command: BetaMemoryTool20250818RenameCommand) -> str:
        return f'Renamed {command.old_path} to {command.new_path}'

    defclear_all_memory(self) -> str:
        return 'All memory cleared'

fake_memory = FakeMemoryTool()

agent = Agent('gateway/anthropic:claude-sonnet-4-5', builtin_tools=[MemoryTool()])


@agent.tool_plain
defmemory(**command: Any) -> Any:
    return fake_memory.call(command)


result = agent.run_sync('Remember that I live in Mexico City')
print(result.output)
"""
Got it! I've recorded that you live in Mexico City. I'll remember this for future reference.
"""

result = agent.run_sync('Where do I live?')
print(result.output)
#> You live in Mexico City.
```

anthropic\_memory.py

```
fromtypingimport Any

fromanthropic.lib.toolsimport BetaAbstractMemoryTool
fromanthropic.types.betaimport (
    BetaMemoryTool20250818CreateCommand,
    BetaMemoryTool20250818DeleteCommand,
    BetaMemoryTool20250818InsertCommand,
    BetaMemoryTool20250818RenameCommand,
    BetaMemoryTool20250818StrReplaceCommand,
    BetaMemoryTool20250818ViewCommand,
)

frompydantic_aiimport Agent, MemoryTool


classFakeMemoryTool(BetaAbstractMemoryTool):
    defview(self, command: BetaMemoryTool20250818ViewCommand) -> str:
        return 'The user lives in Mexico City.'

    defcreate(self, command: BetaMemoryTool20250818CreateCommand) -> str:
        return f'File created successfully at {command.path}'

    defstr_replace(self, command: BetaMemoryTool20250818StrReplaceCommand) -> str:
        return f'File {command.path} has been edited'

    definsert(self, command: BetaMemoryTool20250818InsertCommand) -> str:
        return f'Text inserted at line {command.insert_line} in {command.path}'

    defdelete(self, command: BetaMemoryTool20250818DeleteCommand) -> str:
        return f'File deleted: {command.path}'

    defrename(self, command: BetaMemoryTool20250818RenameCommand) -> str:
        return f'Renamed {command.old_path} to {command.new_path}'

    defclear_all_memory(self) -> str:
        return 'All memory cleared'

fake_memory = FakeMemoryTool()

agent = Agent('anthropic:claude-sonnet-4-5', builtin_tools=[MemoryTool()])


@agent.tool_plain
defmemory(**command: Any) -> Any:
    return fake_memory.call(command)


result = agent.run_sync('Remember that I live in Mexico City')
print(result.output)
"""
Got it! I've recorded that you live in Mexico City. I'll remember this for future reference.
"""

result = agent.run_sync('Where do I live?')
print(result.output)
#> You live in Mexico City.
```

*(This example is complete, it can be run "as is")*

The [`MCPServerTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MCPServerTool "MCPServerTool            dataclass   ") allows your agent to use remote MCP servers with communication handled by the model provider.

This requires the MCP server to live at a public URL the provider can reach and does not support many of the advanced features of Pydantic AI's agent-side [MCP support](https://ai.pydantic.dev/mcp/client/), but can result in optimized context use and caching, and faster performance due to the lack of a round-trip back to Pydantic AI.

### Provider Support

Provider Supported Notes OpenAI Responses ✅ Full feature support. [Connectors](https://platform.openai.com/docs/guides/tools-connectors-mcp#connectors) can be used by specifying a special `x-openai-connector:<connector_id>` URL. Anthropic ✅ Full feature support xAI ✅ Full feature support Google ❌ Not supported Groq ❌ Not supported OpenAI Chat Completions ❌ Not supported Bedrock ❌ Not supported Mistral ❌ Not supported Cohere ❌ Not supported HuggingFace ❌ Not supported

### Usage

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) mcp\_server\_anthropic.py

```
frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'gateway/anthropic:claude-sonnet-4-5',
    builtin_tools=[
        MCPServerTool(
            id='deepwiki',
            url='https://mcp.deepwiki.com/mcp',  # (1)
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [DeepWiki MCP server](https://docs.devin.ai/work-with-devin/deepwiki-mcp) does not require authorization.

mcp\_server\_anthropic.py

```
frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'anthropic:claude-sonnet-4-5',
    builtin_tools=[
        MCPServerTool(
            id='deepwiki',
            url='https://mcp.deepwiki.com/mcp',  # (1)
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [DeepWiki MCP server](https://docs.devin.ai/work-with-devin/deepwiki-mcp) does not require authorization.

*(This example is complete, it can be run "as is")*

With OpenAI, you must use their Responses API to access the MCP server tool:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) mcp\_server\_openai.py

```
frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='deepwiki',
            url='https://mcp.deepwiki.com/mcp',  # (1)
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [DeepWiki MCP server](https://docs.devin.ai/work-with-devin/deepwiki-mcp) does not require authorization.

mcp\_server\_openai.py

```
frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='deepwiki',
            url='https://mcp.deepwiki.com/mcp',  # (1)
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [DeepWiki MCP server](https://docs.devin.ai/work-with-devin/deepwiki-mcp) does not require authorization.

*(This example is complete, it can be run "as is")*

### Configuration Options

The `MCPServerTool` supports several configuration parameters for custom MCP servers:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) mcp\_server\_configured\_url.py

```
importos

frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='github',
            url='https://api.githubcopilot.com/mcp/',
            authorization_token=os.getenv('GITHUB_ACCESS_TOKEN', 'mock-access-token'),  # (1)
            allowed_tools=['search_repositories', 'list_commits'],
            description='GitHub MCP server',
            headers={'X-Custom-Header': 'custom-value'},
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [GitHub MCP server](https://github.com/github/github-mcp-server) requires an authorization token.

mcp\_server\_configured\_url.py

```
importos

frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='github',
            url='https://api.githubcopilot.com/mcp/',
            authorization_token=os.getenv('GITHUB_ACCESS_TOKEN', 'mock-access-token'),  # (1)
            allowed_tools=['search_repositories', 'list_commits'],
            description='GitHub MCP server',
            headers={'X-Custom-Header': 'custom-value'},
        )
    ]
)

result = agent.run_sync('Tell me about the pydantic/pydantic-ai repo.')
print(result.output)
"""
The pydantic/pydantic-ai repo is a Python agent framework for building Generative AI applications.
"""
```

1. The [GitHub MCP server](https://github.com/github/github-mcp-server) requires an authorization token.

For OpenAI Responses, you can use a [connector](https://platform.openai.com/docs/guides/tools-connectors-mcp#connectors) by specifying a special `x-openai-connector:` URL:

*(This example is complete, it can be run "as is")*

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) mcp\_server\_configured\_connector\_id.py

```
importos

frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'gateway/openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='google-calendar',
            url='x-openai-connector:connector_googlecalendar',
            authorization_token=os.getenv('GOOGLE_API_KEY', 'mock-api-key'), # (1)
        )
    ]
)

result = agent.run_sync('What do I have on my calendar today?')
print(result.output)
#> You're going to spend all day playing with Pydantic AI.
```

1. OpenAI's Google Calendar connector requires an [authorization token](https://platform.openai.com/docs/guides/tools-connectors-mcp#authorizing-a-connector).

mcp\_server\_configured\_connector\_id.py

```
importos

frompydantic_aiimport Agent, MCPServerTool

agent = Agent(
    'openai-responses:gpt-5',
    builtin_tools=[
        MCPServerTool(
            id='google-calendar',
            url='x-openai-connector:connector_googlecalendar',
            authorization_token=os.getenv('GOOGLE_API_KEY', 'mock-api-key'), # (1)
        )
    ]
)

result = agent.run_sync('What do I have on my calendar today?')
print(result.output)
#> You're going to spend all day playing with Pydantic AI.
```

1. OpenAI's Google Calendar connector requires an [authorization token](https://platform.openai.com/docs/guides/tools-connectors-mcp#authorizing-a-connector).

*(This example is complete, it can be run "as is")*

#### Provider Support

Parameter OpenAI Anthropic xAI `authorization_token` ✅ ✅ ✅ `allowed_tools` ✅ ✅ ✅ `description` ✅ ❌ ✅ `headers` ✅ ❌ ✅

The [`FileSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.FileSearchTool "FileSearchTool            dataclass   ") enables your agent to search through uploaded files using vector search, providing a fully managed Retrieval-Augmented Generation (RAG) system. This tool handles file storage, chunking, embedding generation, and context injection into prompts.

### Provider Support

Provider Supported Notes OpenAI Responses ✅ Full feature support. Requires files to be uploaded to vector stores via the [OpenAI Files API](https://platform.openai.com/docs/api-reference/files). To include search results on the [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") available via [`ModelResponse.builtin_tool_calls`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.builtin_tool_calls "builtin_tool_calls            property   "), enable the [`OpenAIResponsesModelSettings.openai_include_file_search_results`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings.openai_include_file_search_results "openai_include_file_search_results            instance-attribute   ") [model setting](https://ai.pydantic.dev/agents/#model-run-settings). Google (Gemini) ✅ Requires files to be uploaded via the [Gemini Files API](https://ai.google.dev/gemini-api/docs/files). Files are automatically deleted after 48 hours. Supports up to 2 GB per file and 20 GB per project. Using built-in tools and function tools (including [output tools](https://ai.pydantic.dev/output/#tool-output)) at the same time is not supported; to use structured output, use [`PromptedOutput`](https://ai.pydantic.dev/output/#prompted-output) instead. Google (Vertex AI) ❌ Anthropic ❌ Not supported Groq ❌ Not supported OpenAI Chat Completions ❌ Not supported Bedrock ❌ Not supported Mistral ❌ Not supported Cohere ❌ Not supported HuggingFace ❌ Not supported Outlines ❌ Not supported

### Usage

#### OpenAI Responses

With OpenAI, you need to first [upload files to a vector store](https://platform.openai.com/docs/assistants/tools/file-search), then reference the vector store IDs when using the `FileSearchTool`.

file\_search\_openai\_upload.py

```
importasyncio

frompydantic_aiimport Agent, FileSearchTool
frompydantic_ai.models.openaiimport OpenAIResponsesModel


async defmain():
    model = OpenAIResponsesModel('gpt-5')

    with open('my_document.txt', 'rb') as f:
        file = await model.client.files.create(file=f, purpose='assistants')

    vector_store = await model.client.vector_stores.create(name='my-docs')
    await model.client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=file.id
    )

    agent = Agent(
        model,
        builtin_tools=[FileSearchTool(file_store_ids=[vector_store.id])]
    )

    result = await agent.run('What information is in my documents about pydantic?')
    print(result.output)
    #> Based on your documents, Pydantic is a data validation library for Python...

asyncio.run(main())
```

#### Google (Gemini)

With Gemini, you need to first [create a file search store via the Files API](https://ai.google.dev/gemini-api/docs/files), then reference the file search store names.

file\_search\_google\_upload.py

```
importasyncio

frompydantic_aiimport Agent, FileSearchTool
frompydantic_ai.models.googleimport GoogleModel


async defmain():
    model = GoogleModel('gemini-2.5-flash')

    store = await model.client.aio.file_search_stores.create(
        config={'display_name': 'my-docs'}
    )

    with open('my_document.txt', 'rb') as f:
        await model.client.aio.file_search_stores.upload_to_file_search_store(
            file_search_store_name=store.name,
            file=f,
            config={'mime_type': 'text/plain'}
        )

    agent = Agent(
        model,
        builtin_tools=[FileSearchTool(file_store_ids=[store.name])]
    )

    result = await agent.run('Summarize the key points from my uploaded documents.')
    print(result.output)
    #> The documents discuss the following key points: ...

asyncio.run(main())
```

## API Reference

For complete API documentation, see the [API Reference](https://ai.pydantic.dev/api/builtin_tools/).