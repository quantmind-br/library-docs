---
title: DMR REST API
url: https://docs.docker.com/ai/model-runner/api-reference/
source: llms
fetched_at: 2026-01-24T14:14:08.932938632-03:00
rendered_js: false
word_count: 599
summary: This document explains how to interact with Docker Model Runner programmatically through its support for OpenAI, Anthropic, and Ollama API formats. It provides details on base URLs, supported parameters, and specific endpoints for model inference and management.
tags:
    - docker-model-runner
    - openai-compatibility
    - anthropic-api
    - ollama-api
    - api-endpoints
    - model-inference
category: api
---

Once Model Runner is enabled, new API endpoints are available. You can use these endpoints to interact with a model programmatically. Docker Model Runner provides compatibility with OpenAI, Anthropic, and Ollama API formats.

The base URL to interact with the endpoints depends on how you run Docker and which API format you're using.

Access fromBase URLContainers`http://model-runner.docker.internal`Host processes (TCP)`http://localhost:12434`

> TCP host access must be enabled. See [Enable Docker Model Runner](https://docs.docker.com/ai/model-runner/get-started/#enable-docker-model-runner-in-docker-desktop).

Access fromBase URLContainers`http://172.17.0.1:12434`Host processes`http://localhost:12434`

> The `172.17.0.1` interface may not be available by default to containers within a Compose project. In this case, add an `extra_hosts` directive to your Compose service YAML:
> 
> Then you can access the Docker Model Runner APIs at `http://model-runner.docker.internal:12434/`

### [Base URLs for third-party tools](#base-urls-for-third-party-tools)

When configuring third-party tools that expect OpenAI-compatible APIs, use these base URLs:

Tool typeBase URL formatOpenAI SDK / clients`http://localhost:12434/engines/v1`Anthropic SDK / clients`http://localhost:12434`Ollama-compatible clients`http://localhost:12434`

See [IDE and tool integrations](https://docs.docker.com/ai/model-runner/ide-integrations/) for specific configuration examples.

Docker Model Runner supports multiple API formats:

APIDescriptionUse case[OpenAI API](#openai-compatible-api)OpenAI-compatible chat completions, embeddingsMost AI frameworks and tools[Anthropic API](#anthropic-compatible-api)Anthropic-compatible messages endpointTools built for Claude[Ollama API](#ollama-compatible-api)Ollama-compatible endpointsTools built for Ollama[DMR API](#dmr-native-endpoints)Native Docker Model Runner endpointsModel management

DMR implements the OpenAI API specification for maximum compatibility with existing tools and frameworks.

### [Endpoints](#endpoints)

> You can optionally include the engine name in the path: `/engines/llama.cpp/v1/chat/completions`. This is useful when running multiple inference engines.

### [Model name format](#model-name-format)

When specifying a model in API requests, use the full model identifier including the namespace:

Common model name formats:

- Docker Hub models: `ai/smollm2`, `ai/llama3.2`, `ai/qwen2.5-coder`
- Tagged versions: `ai/smollm2:360M-Q4_K_M`
- Custom models: `myorg/mymodel`

### [Supported parameters](#supported-parameters)

The following OpenAI API parameters are supported:

ParameterTypeDescription`model`stringRequired. The model identifier.`messages`arrayRequired for chat completions. The conversation history.`prompt`stringRequired for completions. The prompt text.`max_tokens`integerMaximum tokens to generate.`temperature`floatSampling temperature (0.0-2.0).`top_p`floatNucleus sampling parameter (0.0-1.0).`stream`BooleanEnable streaming responses.`stop`string/arrayStop sequences.`presence_penalty`floatPresence penalty (-2.0 to 2.0).`frequency_penalty`floatFrequency penalty (-2.0 to 2.0).

### [Limitations and differences from OpenAI](#limitations-and-differences-from-openai)

Be aware of these differences when using DMR's OpenAI-compatible API:

FeatureDMR behaviorAPI keyNot required. DMR ignores the `Authorization` header.Function callingSupported with llama.cpp for compatible models.VisionSupported for multi-modal models (e.g., LLaVA).JSON modeSupported via `response_format: {"type": "json_object"}`.LogprobsSupported.Token countingUses the model's native token encoder, which may differ from OpenAI's.

DMR provides [Anthropic Messages API](https://platform.claude.com/docs/en/api/messages) compatibility for tools and frameworks built for Claude.

### [Endpoints](#endpoints-1)

### [Supported parameters](#supported-parameters-1)

The following Anthropic API parameters are supported:

ParameterTypeDescription`model`stringRequired. The model identifier.`messages`arrayRequired. The conversation messages.`max_tokens`integerMaximum tokens to generate.`temperature`floatSampling temperature (0.0-1.0).`top_p`floatNucleus sampling parameter.`top_k`integerTop-k sampling parameter.`stream`BooleanEnable streaming responses.`stop_sequences`arrayCustom stop sequences.`system`stringSystem prompt.

### [Example: Chat with Anthropic API](#example-chat-with-anthropic-api)

### [Example: Streaming response](#example-streaming-response)

DMR also provides Ollama-compatible endpoints for tools and frameworks built for Ollama.

### [Endpoints](#endpoints-2)

EndpointMethodDescription`/api/tags`GETList available models`/api/show`POSTShow model information`/api/chat`POSTGenerate chat completion`/api/generate`POSTGenerate completion`/api/embeddings`POSTGenerate embeddings

### [Example: Chat with Ollama API](#example-chat-with-ollama-api)

### [Example: List models](#example-list-models)

These endpoints are specific to Docker Model Runner for model management:

EndpointMethodDescription`/models/create`POSTPull/create a model`/models`GETList local models`/models/{namespace}/{name}`GETGet model details`/models/{namespace}/{name}`DELETEDelete a local model

### [Request from within a container](#request-from-within-a-container)

To call the `chat/completions` OpenAI endpoint from within another container using `curl`:

### [Request from the host using TCP](#request-from-the-host-using-tcp)

To call the `chat/completions` OpenAI endpoint from the host via TCP:

1. Enable the host-side TCP support from the Docker Desktop GUI, or via the [Docker Desktop CLI](https://docs.docker.com/desktop/features/desktop-cli/). For example: `docker desktop enable model-runner --tcp <port>`.
   
   If you are running on Windows, also enable GPU-backed inference. See [Enable Docker Model Runner](https://docs.docker.com/ai/model-runner/get-started/#enable-docker-model-runner-in-docker-desktop).
2. Interact with it as documented in the previous section using `localhost` and the correct port.

### [Request from the host using a Unix socket](#request-from-the-host-using-a-unix-socket)

To call the `chat/completions` OpenAI endpoint through the Docker socket from the host using `curl`:

### [Streaming responses](#streaming-responses)

To receive streaming responses, set `stream: true`:

### [Python](#python)

### [Node.js](#nodejs)

- [IDE and tool integrations](https://docs.docker.com/ai/model-runner/ide-integrations/) - Configure Cline, Continue, Cursor, and other tools
- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Adjust context size and runtime parameters
- [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) - Learn about llama.cpp and vLLM options