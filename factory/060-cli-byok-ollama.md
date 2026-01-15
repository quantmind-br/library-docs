---
title: Ollama - Factory Documentation
url: https://docs.factory.ai/cli/byok/ollama
source: sitemap
fetched_at: 2026-01-13T19:03:23.37386809-03:00
rendered_js: false
word_count: 200
summary: Instructions for integrating local and cloud-hosted Ollama models into the Factory application, including configuration settings, hardware requirements, and troubleshooting steps.
tags:
    - ollama
    - local-models
    - custom-models
    - ai-integration
    - hardware-requirements
category: configuration
---

Run models locally on your hardware with Ollama, or use Ollama Cloud for hosted inference.

## Local Ollama

Run models entirely on your machine with no internet required.

### Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "qwen2.5-coder:32b",
      "displayName": "Qwen 2.5 Coder 32B [Local]",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16000
    },
    {
      "model": "qwen2.5-coder:7b",
      "displayName": "Qwen 2.5 Coder 7B [Local]",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 4000
    }
  ]
}
```

### Setup

1. Install Ollama from [ollama.com/download](https://ollama.com/download)
2. Pull desired models:
   
   ```
   # Recommended models
   ollama pull qwen2.5-coder:32b
   ollama pull qwen2.5-coder:7b
   ```
3. Start the Ollama server with extra context:
   
   ```
   OLLAMA_CONTEXT_LENGTH=32000 ollama serve
   ```
4. Add configurations to Factory config

### Approximate Hardware Requirements

Model SizeRAM RequiredVRAM (GPU)3B params4GB3GB7B params8GB6GB13B params16GB10GB30B params32GB20GB70B params64GB40GB

## Ollama Cloud

Use Ollama’s cloud service for hosted model inference without local hardware requirements

### Recommended Cloud Model

The best performance for agentic coding has been observed with **qwen3-coder:480b**. For a full list of available cloud models, visit: [ollama.com/search?c=cloud](https://ollama.com/search?c=cloud)

### Configuration

```
{
  "customModels": [
    {
      "model": "qwen3-coder:480b-cloud",
      "displayName": "qwen3-coder [Online]",
      "baseUrl": "http://localhost:11434/v1/",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 128000
    }
  ]
}
```

### Getting Started with Cloud Models

1. Ensure Ollama is installed and running locally
2. Cloud models are accessed through your local Ollama instance - no API key needed
3. Add the configuration above to your Factory config
4. The model will automatically use cloud compute when requested

## Troubleshooting

### Local server not connecting

- Ensure Ollama is running: `ollama serve`
- Check if port 11434 is available
- Try `curl http://localhost:11434/api/tags` to test

### Model not found

- Pull the model first: `ollama pull model-name`
- Check exact model name with `ollama list`

## Notes

- Local API doesn’t require authentication (use any placeholder for `api_key`)
- Models are stored in `~/.ollama/models/`