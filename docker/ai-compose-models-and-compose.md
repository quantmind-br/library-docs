---
title: Use AI models in Compose
url: https://docs.docker.com/ai/compose/models-and-compose/
source: llms
fetched_at: 2026-01-24T14:13:50.227763498-03:00
rendered_js: false
word_count: 607
summary: This document explains how to define and configure AI model dependencies in Docker Compose applications using the models top-level element. It details configuration options, service binding syntax, and integration with Docker Model Runner for portable AI application deployment.
tags:
    - docker-compose
    - ai-models
    - orchestration
    - model-runner
    - container-deployment
    - inference-configuration
category: configuration
---

## Define AI Models in Docker Compose applications

Requires: Docker Compose [2.38.0](https://github.com/docker/compose/releases/tag/v2.38.0) and later

Compose lets you define AI models as core components of your application, so you can declare model dependencies alongside services and run the application on any platform that supports the Compose Specification.

- Docker Compose v2.38 or later
- A platform that supports Compose models such as Docker Model Runner (DMR) or compatible cloud providers. If you are using DMR, see the [requirements](https://docs.docker.com/ai/model-runner/#requirements).

Compose `models` are a standardized way to define AI model dependencies in your application. By using the [`models` top-level element](https://docs.docker.com/reference/compose-file/models/) in your Compose file, you can:

- Declare which AI models your application needs
- Specify model configurations and requirements
- Make your application portable across different platforms
- Let the platform handle model provisioning and lifecycle management

To define models in your Compose application, use the `models` top-level element:

This example defines:

- A service called `chat-app` that uses a model named `llm`
- A model definition for `llm` that references the `ai/smollm2` model image

Models support various configuration options:

Common configuration options include:

- `model` (required): The OCI artifact identifier for the model. This is what Compose pulls and runs via the model runner.
- `context_size`: Defines the maximum token context size for the model.
  
  > Each model has its own maximum context size. When increasing the context length, consider your hardware constraints. In general, try to keep context size as small as feasible for your specific needs.
- `runtime_flags`: A list of raw command-line flags passed to the inference engine when the model is started. See [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) for commonly used parameters and examples.
- Platform-specific options may also be available via extension attributes `x-*`

> See more example in the [Common runtime configurations](#common-runtime-configurations) section.

Services can reference models in two ways: short syntax and long syntax.

### [Short syntax](#short-syntax)

The short syntax is the simplest way to bind a model to a service:

With short syntax, the platform automatically generates environment variables based on the model name:

- `LLM_URL` - URL to access the LLM model
- `LLM_MODEL` - Model identifier for the LLM model
- `EMBEDDING_MODEL_URL` - URL to access the embedding-model
- `EMBEDDING_MODEL_MODEL` - Model identifier for the embedding-model

### [Long syntax](#long-syntax)

The long syntax allows you to customize environment variable names:

With this configuration, your service receives:

- `AI_MODEL_URL` and `AI_MODEL_NAME` for the LLM model
- `EMBEDDING_URL` and `EMBEDDING_NAME` for the embedding model

One of the key benefits of using Compose models is portability across different platforms that support the Compose specification.

### [Docker Model Runner](#docker-model-runner)

When [Docker Model Runner is enabled](https://docs.docker.com/ai/model-runner/):

Docker Model Runner will:

- Pull and run the specified model locally
- Provide endpoint URLs for accessing the model
- Inject environment variables into the service

### [Cloud providers](#cloud-providers)

The same Compose file can run on cloud providers that support Compose models:

Cloud providers might:

- Use managed AI services instead of running models locally
- Apply cloud-specific optimizations and scaling
- Provide additional monitoring and logging capabilities
- Handle model versioning and updates automatically

Below are some example configurations for various use cases.

### [Development](#development)

### [Conservative with disabled reasoning](#conservative-with-disabled-reasoning)

### [Creative with high randomness](#creative-with-high-randomness)

### [Highly deterministic](#highly-deterministic)

### [Concurrent processing](#concurrent-processing)

### [Rich vocabulary model](#rich-vocabulary-model)

### [Embeddings](#embeddings)

When using embedding models with the `/v1/embeddings` endpoint, you must include the `--embeddings` runtime flag for the model to be properly configured.

> This approach is deprecated. Use the [`models` top-level element](#basic-model-definition) instead.

You can also use the `provider` service type, which allows you to declare platform capabilities required by your application. For AI models, you can use the `model` type to declare model dependencies.

To define a model provider:

- [`models` top-level element](https://docs.docker.com/reference/compose-file/models/)
- [`models` attribute](https://docs.docker.com/reference/compose-file/services/#models)
- [Docker Model Runner documentation](https://docs.docker.com/ai/model-runner/)
- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Context size and runtime parameters
- [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) - llama.cpp and vLLM details
- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - OpenAI and Ollama-compatible APIs