---
title: "[OLD PROXY \U0001F449 [NEW proxy here](./simple_proxy)] Local LiteLLM Proxy Server | liteLLM"
url: https://docs.litellm.ai/docs/proxy_server
source: sitemap
fetched_at: 2026-01-21T19:51:06.880730757-03:00
rendered_js: false
word_count: 308
summary: This document explains how to set up and use LiteLLM Proxy, an OpenAI-compatible server that enables standardized access to over 100 different LLM providers.
tags:
    - litellm
    - openai-compatibility
    - llm-proxy
    - api-gateway
    - model-deployment
    - local-inference
    - python
category: guide
---

A fast, and lightweight OpenAI-compatible server to call 100+ LLM APIs.

info

Docs outdated. New docs 👉 [here](https://docs.litellm.ai/docs/simple_proxy)

## Usage[​](#usage "Direct link to Usage")

```
pip install 'litellm[proxy]'
```

```
$ litellm --model ollama/codellama 

#INFO: Ollama running on http://0.0.0.0:8000
```

### Test[​](#test "Direct link to Test")

In a new shell, run:

### Replace openai base[​](#replace-openai-base "Direct link to Replace openai base")

```
import openai 

openai.api_base ="http://0.0.0.0:8000"

print(openai.ChatCompletion.create(model="test", messages=[{"role":"user","content":"Hey!"}]))
```

#### Other supported models:[​](#other-supported-models "Direct link to Other supported models:")

- VLLM
- OpenAI Compatible Server
- Huggingface
- Anthropic
- TogetherAI
- Replicate
- Petals
- Palm
- Azure OpenAI
- AI21
- Cohere

Assuming you're running vllm locally

```
$ litellm --model vllm/facebook/opt-125m
```

### Tutorial: Use with Multiple LLMs + LibreChat/Chatbot-UI/Auto-Gen/ChatDev/Langroid,etc.[​](#tutorial-use-with-multiple-llms--librechatchatbot-uiauto-genchatdevlangroidetc "Direct link to Tutorial: Use with Multiple LLMs + LibreChat/Chatbot-UI/Auto-Gen/ChatDev/Langroid,etc.")

- Multiple LLMs
- LibreChat
- SmartChatbotUI
- AutoGen
- AutoGen Multi-LLM
- ChatDev
- Langroid

Replace openai base:

```
import openai 

openai.api_key ="any-string-here"
openai.api_base ="http://0.0.0.0:8080"# your proxy url

# call openai
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hey"}])

print(response)

# call cohere
response = openai.ChatCompletion.create(model="command-nightly", messages=[{"role":"user","content":"Hey"}])

print(response)
```

## Local Proxy[​](#local-proxy "Direct link to Local Proxy")

Here's how to use the local proxy to test codellama/mistral/etc. models for different github repos

```
$ ollama pull codellama # OUR Local CodeLlama  

$ litellm --model ollama/codellama --temperature 0.3 --max_tokens 2048
```

### Tutorial: Use with Multiple LLMs + Aider/AutoGen/Langroid/etc.[​](#tutorial-use-with-multiple-llms--aiderautogenlangroidetc "Direct link to Tutorial: Use with Multiple LLMs + Aider/AutoGen/Langroid/etc.")

- Multiple LLMs
- ContinueDev
- Aider
- AutoGen
- AutoGen Multi-LLM
- ChatDev
- Langroid
- GPT-Pilot
- guidance

```
$ litellm

#INFO: litellm proxy running on http://0.0.0.0:8000
```

#### Send a request to your proxy[​](#send-a-request-to-your-proxy "Direct link to Send a request to your proxy")

```
import openai 

openai.api_key ="any-string-here"
openai.api_base ="http://0.0.0.0:8080"# your proxy url

# call gpt-3.5-turbo
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hey"}])

print(response)

# call ollama/llama2
response = openai.ChatCompletion.create(model="ollama/llama2", messages=[{"role":"user","content":"Hey"}])

print(response)
```

note

**Contribute** Using this server with a project? Contribute your tutorial [here!](https://github.com/BerriAI/litellm)

## Advanced[​](#advanced "Direct link to Advanced")

### Logs[​](#logs "Direct link to Logs")

This will return the most recent log (the call that went to the LLM API + the received response).

All logs are saved to a file called `api_logs.json` in the current directory.

### Configure Proxy[​](#configure-proxy "Direct link to Configure Proxy")

If you need to:

- save API keys
- set litellm params (e.g. drop unmapped params, set fallback models, etc.)
- set model-specific params (max tokens, temperature, api base, prompt template)

You can do set these just for that session (via cli), or persist these across restarts (via config file).

#### Save API Keys[​](#save-api-keys "Direct link to Save API Keys")

```
$ litellm --api_key OPENAI_API_KEY=sk-...
```

LiteLLM will save this to a locally stored config file, and persist this across sessions.

LiteLLM Proxy supports all litellm supported api keys. To add keys for a specific provider, check this list:

- Huggingface
- Anthropic
- PerplexityAI
- TogetherAI
- Replicate
- Bedrock
- Palm
- Azure OpenAI
- AI21
- Cohere

```
$ litellm --add_key HUGGINGFACE_API_KEY=my-api-key #[OPTIONAL]
```

E.g.: Set api base, max tokens and temperature.

**For that session**:

```
litellm --model ollama/llama2 \
  --api_base http://localhost:11434 \
  --max_tokens 250 \
  --temperature 0.5

# OpenAI-compatible server running on http://0.0.0.0:8000
```

### Performance[​](#performance "Direct link to Performance")

We load-tested 500,000 HTTP connections on the FastAPI server for 1 minute, using [wrk](https://github.com/wg/wrk).

There are our results:

```
Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   156.38ms   25.52ms 361.91ms   84.73%
    Req/Sec    13.61      5.13    40.00     57.50%
  383625 requests in 1.00m, 391.10MB read
  Socket errors: connect 0, read 1632, write 1, timeout 0
```

## Support/ talk with founders[​](#support-talk-with-founders "Direct link to Support/ talk with founders")

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
- Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)