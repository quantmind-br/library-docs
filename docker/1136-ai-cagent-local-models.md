---
title: Local models
url: https://docs.docker.com/ai/cagent/local-models/
source: llms
fetched_at: 2026-01-24T14:13:29.118515069-03:00
rendered_js: false
word_count: 460
summary: This document explains how to set up and use Docker Model Runner to execute AI models locally, covering installation, model configuration, and performance optimization techniques.
tags:
    - docker-model-runner
    - local-ai
    - inference
    - rag
    - speculative-decoding
    - embeddings
category: guide
---

## Local models with Docker Model Runner

Docker Model Runner lets you run AI models locally on your machine. No API keys, no recurring costs, and your data stays private.

Docker Model Runner lets you run models locally without API keys or recurring costs. Your data stays on your machine, and you can work offline once models are downloaded. This is an alternative to [cloud model providers](https://docs.docker.com/ai/cagent/model-providers/).

You need Docker Model Runner installed and running:

- Docker Desktop (macOS/Windows) - Enable Docker Model Runner in **Settings &gt; AI &gt; Enable Docker Model Runner**. See [Get started with DMR](https://docs.docker.com/ai/model-runner/get-started/#enable-docker-model-runner) for detailed instructions.
- Docker Engine (Linux) - Install with `sudo apt-get install docker-model-plugin` or `sudo dnf install docker-model-plugin`. See [Get started with DMR](https://docs.docker.com/ai/model-runner/get-started/#docker-engine).

Verify Docker Model Runner is available:

If the command returns version information, you're ready to use local models.

Docker Model Runner can run any compatible model. Models can come from:

- Docker Hub repositories (`docker.io/namespace/model-name`)
- Your own OCI artifacts packaged and pushed to any registry
- HuggingFace models directly (`hf.co/org/model-name`)
- The Docker Model catalog in Docker Desktop

To see models available to the local Docker catalog, run:

To use a model, reference it in your configuration. DMR automatically pulls models on first use if they're not already local.

Configure your agent to use Docker Model Runner with the `dmr` provider:

When you first run your agent, cagent prompts you to pull the model if it's not already available locally:

When you configure an agent to use DMR, cagent automatically connects to your local Docker Model Runner and routes inference requests to it. If a model isn't available locally, cagent prompts you to pull it on first use. No API keys or authentication are required.

For more control over model behavior, define a model configuration:

### [Faster inference with speculative decoding](#faster-inference-with-speculative-decoding)

Speed up model responses using speculative decoding with a smaller draft model:

The draft model generates token candidates, and the main model validates them. This can significantly improve throughput for longer responses.

### [Runtime flags](#runtime-flags)

Pass engine-specific flags to optimize performance:

Common flags:

- `--ngl` - Number of GPU layers
- `--threads` - CPU thread count
- `--repeat-penalty` - Repetition penalty

Docker Model Runner supports both embeddings and reranking for RAG workflows.

### [Embedding with DMR](#embedding-with-dmr)

Use local embeddings for indexing your knowledge base:

### [Reranking with DMR](#reranking-with-dmr)

DMR provides native reranking for improved RAG results:

Native DMR reranking is the fastest option for reranking RAG results.

If cagent can't find Docker Model Runner:

1. Verify Docker Model Runner status:
2. Check available models:
3. Check model logs for errors:
4. Ensure Docker Desktop has Model Runner enabled in settings (macOS/Windows)

<!--THE END-->

- Follow the [tutorial](https://docs.docker.com/ai/cagent/tutorial/) to build your first agent with local models
- Learn about [RAG](https://docs.docker.com/ai/cagent/rag/) to give your agents access to codebases and documentation
- See the [configuration reference](https://docs.docker.com/ai/cagent/reference/config/#docker-model-runner-dmr) for all DMR options