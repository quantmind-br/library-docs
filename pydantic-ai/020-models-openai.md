---
title: OpenAI - Pydantic AI
url: https://ai.pydantic.dev/models/openai/
source: sitemap
fetched_at: 2026-01-22T22:26:16.037873971-03:00
rendered_js: false
word_count: 1483
summary: This document provides instructions for installing and configuring OpenAI and Azure OpenAI models within the Pydantic AI framework, including details on the Chat and Responses APIs.
tags:
    - pydantic-ai
    - openai
    - azure-openai
    - llm-integration
    - python-sdk
    - model-configuration
    - ai-agents
category: guide
---

## Install

To use OpenAI models or OpenAI-compatible APIs, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `openai` optional group:

pipuv

```
pipinstall"pydantic-ai-slim[openai]"
```

```
uvadd"pydantic-ai-slim[openai]"
```

## Configuration

To use `OpenAIChatModel` with the OpenAI API, go to [platform.openai.com](https://platform.openai.com/) and follow your nose until you find the place to generate an API key.

## Environment variable

Once you have the API key, you can set it as an environment variable:

```
exportOPENAI_API_KEY='your-api-key'
```

You can then use `OpenAIChatModel` by name:

With Pydantic AI GatewayDirectly to Provider API

```
frompydantic_aiimport Agent

agent = Agent('openai:gpt-5')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel

model = OpenAIChatModel('gpt-5')
agent = Agent(model)
...
```

By default, the `OpenAIChatModel` uses the `OpenAIProvider` with the `base_url` set to `https://api.openai.com/v1`.

## Configure the provider

If you want to pass parameters in code to the provider, you can programmatically instantiate the [OpenAIProvider](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.openai.OpenAIProvider "OpenAIProvider") and pass it to the model:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.openaiimport OpenAIProvider

model = OpenAIChatModel('gpt-5', provider=OpenAIProvider(api_key='your-api-key'))
agent = Agent(model)
...
```

## Custom OpenAI Client

`OpenAIProvider` also accepts a custom `AsyncOpenAI` client via the `openai_client` parameter, so you can customise the `organization`, `project`, `base_url` etc. as defined in the [OpenAI API docs](https://platform.openai.com/docs/api-reference).

custom\_openai\_client.py

```
fromopenaiimport AsyncOpenAI

frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.openaiimport OpenAIProvider

client = AsyncOpenAI(max_retries=3)
model = OpenAIChatModel('gpt-5', provider=OpenAIProvider(openai_client=client))
agent = Agent(model)
...
```

You could also use the [`AsyncAzureOpenAI`](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/switching-endpoints) client to use the Azure OpenAI API. Note that the `AsyncAzureOpenAI` is a subclass of `AsyncOpenAI`.

```
fromopenaiimport AsyncAzureOpenAI

frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.openaiimport OpenAIProvider

client = AsyncAzureOpenAI(
    azure_endpoint='...',
    api_version='2024-07-01-preview',
    api_key='your-api-key',
)

model = OpenAIChatModel(
    'gpt-5',
    provider=OpenAIProvider(openai_client=client),
)
agent = Agent(model)
...
```

## OpenAI Responses API

Pydantic AI also supports OpenAI's [Responses API](https://platform.openai.com/docs/api-reference/responses) through the

You can use [`OpenAIResponsesModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModel "OpenAIResponsesModel            dataclass   ") by name:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
frompydantic_aiimport Agent

agent = Agent('gateway/openai-responses:gpt-5')
...
```

```
frompydantic_aiimport Agent

agent = Agent('openai-responses:gpt-5')
...
```

Or initialise the model directly with just the model name:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIResponsesModel

model = OpenAIResponsesModel('gpt-5')
agent = Agent(model)
...
```

You can learn more about the differences between the Responses API and Chat Completions API in the [OpenAI API docs](https://platform.openai.com/docs/guides/migrate-to-responses).

### Built-in tools

The Responses API has built-in tools that you can use instead of building your own:

- [Web search](https://platform.openai.com/docs/guides/tools-web-search): allow models to search the web for the latest information before generating a response.
- [Code interpreter](https://platform.openai.com/docs/guides/tools-code-interpreter): allow models to write and run Python code in a sandboxed environment before generating a response.
- [Image generation](https://platform.openai.com/docs/guides/tools-image-generation): allow models to generate images based on a text prompt.
- [File search](https://platform.openai.com/docs/guides/tools-file-search): allow models to search your files for relevant information before generating a response.
- [Computer use](https://platform.openai.com/docs/guides/tools-computer-use): allow models to use a computer to perform tasks on your behalf.

Web search, Code interpreter, Image generation, and File search are natively supported through the [Built-in tools](https://ai.pydantic.dev/builtin-tools/) feature.

Computer use can be enabled by passing an [`openai.types.responses.ComputerToolParam`](https://github.com/openai/openai-python/blob/main/src/openai/types/responses/computer_tool_param.py) in the `openai_builtin_tools` setting on [`OpenAIResponsesModelSettings`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings "OpenAIResponsesModelSettings"). It doesn't currently generate [`BuiltinToolCallPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart            dataclass   ") or [`BuiltinToolReturnPart`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart            dataclass   ") parts in the message history, or streamed events; please submit an issue if you need native support for this built-in tool.

computer\_use\_tool.py

```
fromopenai.types.responsesimport ComputerToolParam

frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIResponsesModel, OpenAIResponsesModelSettings

model_settings = OpenAIResponsesModelSettings(
    openai_builtin_tools=[
        ComputerToolParam(
            type='computer_use',
        )
    ],
)
model = OpenAIResponsesModel('gpt-5')
agent = Agent(model=model, model_settings=model_settings)

result = agent.run_sync('Open a new browser tab')
print(result.output)
```

#### Referencing earlier responses

The Responses API supports referencing earlier model responses in a new request using a `previous_response_id` parameter, to ensure the full [conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses#passing-context-from-the-previous-response) including [reasoning items](https://platform.openai.com/docs/guides/reasoning#keeping-reasoning-items-in-context) are kept in context. This is available through the `openai_previous_response_id` field in [`OpenAIResponsesModelSettings`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings "OpenAIResponsesModelSettings").

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIResponsesModel, OpenAIResponsesModelSettings

model = OpenAIResponsesModel('gpt-5')
agent = Agent(model=model)

result = agent.run_sync('The secret is 1234')
model_settings = OpenAIResponsesModelSettings(
    openai_previous_response_id=result.all_messages()[-1].provider_response_id
)
result = agent.run_sync('What is the secret code?', model_settings=model_settings)
print(result.output)
#> 1234
```

By passing the `provider_response_id` from an earlier run, you can allow the model to build on its own prior reasoning without needing to resend the full message history.

##### Automatically referencing earlier responses

When the `openai_previous_response_id` field is set to `'auto'`, Pydantic AI will automatically select the most recent `provider_response_id` from message history and omit messages that came before it, letting the OpenAI API leverage server-side history instead for improved efficiency.

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIResponsesModel, OpenAIResponsesModelSettings

model = OpenAIResponsesModel('gpt-5')
agent = Agent(model=model)

result1 = agent.run_sync('Tell me a joke.')
print(result1.output)
#> Did you hear about the toothpaste scandal? They called it Colgate.

# When set to 'auto', the most recent provider_response_id
# and messages after it are sent as request.
model_settings = OpenAIResponsesModelSettings(openai_previous_response_id='auto')
result2 = agent.run_sync(
    'Explain?',
    message_history=result1.new_messages(),
    model_settings=model_settings
)
print(result2.output)
#> This is an excellent joke invented by Samuel Colvin, it needs no explanation.
```

## OpenAI-compatible Models

Many providers and models are compatible with the OpenAI API, and can be used with `OpenAIChatModel` in Pydantic AI. Before getting started, check the [installation and configuration](#install) instructions above.

To use another OpenAI-compatible API, you can make use of the `base_url` and `api_key` arguments from `OpenAIProvider`:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.openaiimport OpenAIProvider

model = OpenAIChatModel(
    'model_name',
    provider=OpenAIProvider(
        base_url='https://<openai-compatible-api-endpoint>', api_key='your-api-key'
    ),
)
agent = Agent(model)
...
```

Various providers also have their own provider classes so that you don't need to specify the base URL yourself and you can use the standard `<PROVIDER>_API_KEY` environment variable to set the API key. When a provider has its own provider class, you can use the `Agent("<provider>:<model>")` shorthand, e.g. `Agent("deepseek:deepseek-chat")` or `Agent("moonshotai:kimi-k2-0711-preview")`, instead of building the `OpenAIChatModel` explicitly. Similarly, you can pass the provider name as a string to the `provider` argument on `OpenAIChatModel` instead of building instantiating the provider class explicitly.

#### Model Profile

Sometimes, the provider or model you're using will have slightly different requirements than OpenAI's API or models, like having different restrictions on JSON schemas for tool definitions, or not supporting tool definitions to be marked as strict.

When using an alternative provider class provided by Pydantic AI, an appropriate model profile is typically selected automatically based on the model name. If the model you're using is not working correctly out of the box, you can tweak various aspects of how model requests are constructed by providing your own [`ModelProfile`](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile) (for behaviors shared among all model classes) or [`OpenAIModelProfile`](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.openai.OpenAIModelProfile "OpenAIModelProfile            dataclass   ") (for behaviors specific to `OpenAIChatModel`):

```
frompydantic_aiimport Agent, InlineDefsJsonSchemaTransformer
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.profiles.openaiimport OpenAIModelProfile
frompydantic_ai.providers.openaiimport OpenAIProvider

model = OpenAIChatModel(
    'model_name',
    provider=OpenAIProvider(
        base_url='https://<openai-compatible-api-endpoint>.com', api_key='your-api-key'
    ),
    profile=OpenAIModelProfile(
        json_schema_transformer=InlineDefsJsonSchemaTransformer,  # Supported by any model class on a plain ModelProfile
        openai_supports_strict_tool_definition=False  # Supported by OpenAIModel only, requires OpenAIModelProfile
    )
)
agent = Agent(model)
```

### DeepSeek

To use the [DeepSeek](https://deepseek.com) provider, first create an API key by following the [Quick Start guide](https://api-docs.deepseek.com/).

You can then set the `DEEPSEEK_API_KEY` environment variable and use [`DeepSeekProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.deepseek.DeepSeekProvider "DeepSeekProvider") by name:

```
frompydantic_aiimport Agent

agent = Agent('deepseek:deepseek-chat')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.deepseekimport DeepSeekProvider

model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key='your-deepseek-api-key'),
)
agent = Agent(model)
...
```

You can also customize any provider with a custom `http_client`:

```
fromhttpximport AsyncClient

frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.deepseekimport DeepSeekProvider

custom_http_client = AsyncClient(timeout=30)
model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(
        api_key='your-deepseek-api-key', http_client=custom_http_client
    ),
)
agent = Agent(model)
...
```

### Alibaba Cloud Model Studio (DashScope)

To use Qwen models via [Alibaba Cloud Model Studio (DashScope)](https://www.alibabacloud.com/en/product/modelstudio), you can set the `ALIBABA_API_KEY` (or `DASHSCOPE_API_KEY`) environment variable and use [`AlibabaProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.alibaba.AlibabaProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('alibaba:qwen-max')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.alibabaimport AlibabaProvider

model = OpenAIChatModel(
    'qwen-max',
    provider=AlibabaProvider(api_key='your-api-key'),
)
agent = Agent(model)
...
```

The `AlibabaProvider` uses the international DashScope compatible endpoint `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` by default. You can override this by passing a custom `base_url`:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.alibabaimport AlibabaProvider

model = OpenAIChatModel(
    'qwen-max',
    provider=AlibabaProvider(
        api_key='your-api-key',
        base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',  # China region
    ),
)
agent = Agent(model)
...
```

### Ollama

Pydantic AI supports both self-hosted [Ollama](https://ollama.com/) servers (running locally or remotely) and [Ollama Cloud](https://ollama.com/cloud).

For servers running locally, use the `http://localhost:11434/v1` base URL. For Ollama Cloud, use `https://ollama.com/v1` and ensure an API key is set.

You can set the `OLLAMA_BASE_URL` and (optionally) `OLLAMA_API_KEY` environment variables and use [`OllamaProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.ollama.OllamaProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('ollama:gpt-oss:20b')
...
```

Or initialise the model and provider directly:

```
frompydanticimport BaseModel

frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.ollamaimport OllamaProvider


classCityLocation(BaseModel):
    city: str
    country: str


ollama_model = OpenAIChatModel(
    model_name='gpt-oss:20b',
    provider=OllamaProvider(base_url='http://localhost:11434/v1'),  # (1)!
)
agent = Agent(ollama_model, output_type=CityLocation)

result = agent.run_sync('Where were the olympics held in 2012?')
print(result.output)
#> city='London' country='United Kingdom'
print(result.usage())
#> RunUsage(input_tokens=57, output_tokens=8, requests=1)
```

1. For Ollama Cloud, use the `base_url='https://ollama.com/v1'` and set the `OLLAMA_API_KEY` environment variable.

### Azure AI Foundry

To use [Azure AI Foundry](https://ai.azure.com/) as your provider, you can set the `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, and `OPENAI_API_VERSION` environment variables and use [`AzureProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.azure.AzureProvider "AzureProvider") by name:

```
frompydantic_aiimport Agent

agent = Agent('azure:gpt-5')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.azureimport AzureProvider

model = OpenAIChatModel(
    'gpt-5',
    provider=AzureProvider(
        azure_endpoint='your-azure-endpoint',
        api_version='your-api-version',
        api_key='your-api-key',
    ),
)
agent = Agent(model)
...
```

### Vercel AI Gateway

To use [Vercel's AI Gateway](https://vercel.com/docs/ai-gateway), first follow the [documentation](https://vercel.com/docs/ai-gateway) instructions on obtaining an API key or OIDC token.

You can set the `VERCEL_AI_GATEWAY_API_KEY` and `VERCEL_OIDC_TOKEN` environment variables and use [`VercelProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.vercel.VercelProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('vercel:anthropic/claude-4-sonnet')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.vercelimport VercelProvider

model = OpenAIChatModel(
    'anthropic/claude-4-sonnet',
    provider=VercelProvider(api_key='your-vercel-ai-gateway-api-key'),
)
agent = Agent(model)
...
```

### MoonshotAI

Create an API key in the [Moonshot Console](https://platform.moonshot.ai/console).

You can set the `MOONSHOTAI_API_KEY` environment variable and use [`MoonshotAIProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.moonshotai.MoonshotAIProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('moonshotai:kimi-k2-0711-preview')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.moonshotaiimport MoonshotAIProvider

model = OpenAIChatModel(
    'kimi-k2-0711-preview',
    provider=MoonshotAIProvider(api_key='your-moonshot-api-key'),
)
agent = Agent(model)
...
```

### GitHub Models

To use [GitHub Models](https://docs.github.com/en/github-models), you'll need a GitHub personal access token with the `models: read` permission.

You can set the `GITHUB_API_KEY` environment variable and use [`GitHubProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.github.GitHubProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('github:xai/grok-3-mini')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.githubimport GitHubProvider

model = OpenAIChatModel(
    'xai/grok-3-mini',  # GitHub Models uses prefixed model names
    provider=GitHubProvider(api_key='your-github-token'),
)
agent = Agent(model)
...
```

GitHub Models supports various model families with different prefixes. You can see the full list on the [GitHub Marketplace](https://github.com/marketplace?type=models) or the public [catalog endpoint](https://models.github.ai/catalog/models).

### Perplexity

Follow the Perplexity [getting started](https://docs.perplexity.ai/guides/getting-started) guide to create an API key.

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.openaiimport OpenAIProvider

model = OpenAIChatModel(
    'sonar-pro',
    provider=OpenAIProvider(
        base_url='https://api.perplexity.ai',
        api_key='your-perplexity-api-key',
    ),
)
agent = Agent(model)
...
```

### Fireworks AI

Go to [Fireworks.AI](https://fireworks.ai/) and create an API key in your account settings.

You can set the `FIREWORKS_API_KEY` environment variable and use [`FireworksProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.fireworks.FireworksProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('fireworks:accounts/fireworks/models/qwq-32b')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.fireworksimport FireworksProvider

model = OpenAIChatModel(
    'accounts/fireworks/models/qwq-32b',  # model library available at https://fireworks.ai/models
    provider=FireworksProvider(api_key='your-fireworks-api-key'),
)
agent = Agent(model)
...
```

### Together AI

Go to [Together.ai](https://www.together.ai/) and create an API key in your account settings.

You can set the `TOGETHER_API_KEY` environment variable and use [`TogetherProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.together.TogetherProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('together:meta-llama/Llama-3.3-70B-Instruct-Turbo-Free')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.togetherimport TogetherProvider

model = OpenAIChatModel(
    'meta-llama/Llama-3.3-70B-Instruct-Turbo-Free',  # model library available at https://www.together.ai/models
    provider=TogetherProvider(api_key='your-together-api-key'),
)
agent = Agent(model)
...
```

### Heroku AI

To use [Heroku AI](https://www.heroku.com/ai), first create an API key.

You can set the `HEROKU_INFERENCE_KEY` and (optionally )`HEROKU_INFERENCE_URL` environment variables and use [`HerokuProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.heroku.HerokuProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('heroku:claude-sonnet-4-5')
...
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.herokuimport HerokuProvider

model = OpenAIChatModel(
    'claude-sonnet-4-5',
    provider=HerokuProvider(api_key='your-heroku-inference-key'),
)
agent = Agent(model)
...
```

### LiteLLM

To use [LiteLLM](https://www.litellm.ai/), set the configs as outlined in the [doc](https://docs.litellm.ai/docs/set_keys). In `LiteLLMProvider`, you can pass `api_base` and `api_key`. The value of these configs will depend on your setup. For example, if you are using OpenAI models, then you need to pass `https://api.openai.com/v1` as the `api_base` and your OpenAI API key as the `api_key`. If you are using a LiteLLM proxy server running on your local machine, then you need to pass `http://localhost:<port>` as the `api_base` and your LiteLLM API key (or a placeholder) as the `api_key`.

To use custom LLMs, use `custom/` prefix in the model name.

Once you have the configs, use the [`LiteLLMProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.litellm.LiteLLMProvider) as follows:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.litellmimport LiteLLMProvider

model = OpenAIChatModel(
    'openai/gpt-5',
    provider=LiteLLMProvider(
        api_base='<api-base-url>',
        api_key='<api-key>'
    )
)
agent = Agent(model)

result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
...
```

### Nebius AI Studio

Go to [Nebius AI Studio](https://studio.nebius.com/) and create an API key.

You can set the `NEBIUS_API_KEY` environment variable and use [`NebiusProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.nebius.NebiusProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('nebius:Qwen/Qwen3-32B-fast')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.nebiusimport NebiusProvider

model = OpenAIChatModel(
    'Qwen/Qwen3-32B-fast',
    provider=NebiusProvider(api_key='your-nebius-api-key'),
)
agent = Agent(model)
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

### OVHcloud AI Endpoints

To use OVHcloud AI Endpoints, you need to create a new API key. To do so, go to the [OVHcloud manager](https://ovh.com/manager), then in Public Cloud &gt; AI Endpoints &gt; API keys. Click on `Create a new API key` and copy your new key.

You can explore the [catalog](https://endpoints.ai.cloud.ovh.net/catalog) to find which models are available.

You can set the `OVHCLOUD_API_KEY` environment variable and use [`OVHcloudProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.ovhcloud.OVHcloudProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('ovhcloud:gpt-oss-120b')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

If you need to configure the provider, you can use the [`OVHcloudProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.ovhcloud.OVHcloudProvider) class:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.ovhcloudimport OVHcloudProvider

model = OpenAIChatModel(
    'gpt-oss-120b',
    provider=OVHcloudProvider(api_key='your-api-key'),
)
agent = Agent(model)
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

### SambaNova

To use [SambaNova Cloud](https://cloud.sambanova.ai/), you need to obtain an API key from the [SambaNova Cloud dashboard](https://cloud.sambanova.ai/dashboard).

SambaNova provides access to multiple model families including Meta Llama, DeepSeek, Qwen, and Mistral models with fast inference speeds.

You can set the `SAMBANOVA_API_KEY` environment variable and use [`SambaNovaProvider`](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.sambanova.SambaNovaProvider) by name:

```
frompydantic_aiimport Agent

agent = Agent('sambanova:Meta-Llama-3.1-8B-Instruct')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

Or initialise the model and provider directly:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.sambanovaimport SambaNovaProvider

model = OpenAIChatModel(
    'Meta-Llama-3.1-8B-Instruct',
    provider=SambaNovaProvider(api_key='your-api-key'),
)
agent = Agent(model)
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
```

For a complete list of available models, see the [SambaNova supported models documentation](https://docs.sambanova.ai/docs/en/models/sambacloud-models).

You can customize the base URL if needed:

```
frompydantic_aiimport Agent
frompydantic_ai.models.openaiimport OpenAIChatModel
frompydantic_ai.providers.sambanovaimport SambaNovaProvider

model = OpenAIChatModel(
    'DeepSeek-R1-0528',
    provider=SambaNovaProvider(
        api_key='your-api-key',
        base_url='https://custom.endpoint.com/v1',
    ),
)
agent = Agent(model)
...
```