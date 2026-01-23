---
title: GitHub Copilot | liteLLM
url: https://docs.litellm.ai/docs/providers/github_copilot
source: sitemap
fetched_at: 2026-01-21T19:49:14.275920672-03:00
rendered_js: false
word_count: 200
summary: This document provides instructions for integrating GitHub Copilot with LiteLLM, covering authentication via OAuth device flow, SDK usage for chat and embeddings, and proxy configuration.
tags:
    - github-copilot
    - litellm
    - authentication
    - python-sdk
    - chat-completion
    - embeddings
    - litellm-proxy
category: guide
---

[https://docs.github.com/en/copilot](https://docs.github.com/en/copilot)

tip

**We support GitHub Copilot Chat API with automatic authentication handling**

PropertyDetailsDescriptionGitHub Copilot Chat API provides access to GitHub's AI-powered coding assistant.Provider Route on LiteLLM`github_copilot/`Supported Endpoints`/chat/completions`, `/embeddings`API Reference[GitHub Copilot docs](https://docs.github.com/en/copilot)

## Authentication[​](#authentication "Direct link to Authentication")

GitHub Copilot uses OAuth device flow for authentication. On first use, you'll be prompted to authenticate via GitHub:

1. LiteLLM will display a device code and verification URL
2. Visit the URL and enter the code to authenticate
3. Your credentials will be stored locally for future use

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Chat Completion[​](#chat-completion "Direct link to Chat Completion")

GitHub Copilot Chat Completion

```
from litellm import completion

response = completion(
    model="github_copilot/gpt-4",
    messages=[{"role":"user","content":"Write a Python function to calculate fibonacci numbers"}],
    extra_headers={
"editor-version":"vscode/1.85.1",
"Copilot-Integration-Id":"vscode-chat"
}
)
print(response)
```

GitHub Copilot Chat Completion - Streaming

```
from litellm import completion

stream = completion(
    model="github_copilot/gpt-4",
    messages=[{"role":"user","content":"Explain async/await in Python"}],
    stream=True,
    extra_headers={
"editor-version":"vscode/1.85.1",
"Copilot-Integration-Id":"vscode-chat"
}
)

for chunk in stream:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

### Responses[​](#responses "Direct link to Responses")

For GPT Codex models, only responses API is supported.

GitHub Copilot Responses

```
import litellm

response =await litellm.aresponses(
    model="github_copilot/gpt-5.1-codex",
input="Write a Python hello world",
    max_output_tokens=500
)

print(response)
```

### Embedding[​](#embedding "Direct link to Embedding")

GitHub Copilot Embedding

```
import litellm

response = litellm.embedding(
    model="github_copilot/text-embedding-3-small",
input=["good morning from litellm"]
)
print(response)
```

## Usage - LiteLLM Proxy[​](#usage---litellm-proxy "Direct link to Usage - LiteLLM Proxy")

Add the following to your LiteLLM Proxy configuration file:

config.yaml

```
model_list:
-model_name: github_copilot/gpt-4
litellm_params:
model: github_copilot/gpt-4
-model_name: github_copilot/gpt-5.1-codex
model_info:
mode: responses
litellm_params:
model: github_copilot/gpt-5.1-codex
-model_name: github_copilot/text-embedding-ada-002
model_info:
mode: embedding
litellm_params:
model: github_copilot/text-embedding-ada-002
```

Start your LiteLLM Proxy server:

Start LiteLLM Proxy

```
litellm --config config.yaml

# RUNNING on http://0.0.0.0:4000
```

- OpenAI SDK
- LiteLLM SDK
- cURL

GitHub Copilot via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="github_copilot/gpt-4",
    messages=[{"role":"user","content":"How do I optimize this SQL query?"}],
    extra_headers={
"editor-version":"vscode/1.85.1",
"Copilot-Integration-Id":"vscode-chat"
}
)

print(response.choices[0].message.content)
```

## Getting Started[​](#getting-started "Direct link to Getting Started")

1. Ensure you have GitHub Copilot access (paid GitHub subscription required)
2. Run your first LiteLLM request - you'll be prompted to authenticate
3. Follow the device flow authentication process
4. Start making requests to GitHub Copilot through LiteLLM

## Configuration[​](#configuration "Direct link to Configuration")

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

You can customize token storage locations:

Environment Variables

```
# Optional: Custom token directory
export GITHUB_COPILOT_TOKEN_DIR="~/.config/litellm/github_copilot"

# Optional: Custom access token file name
export GITHUB_COPILOT_ACCESS_TOKEN_FILE="access-token"

# Optional: Custom API key file name
export GITHUB_COPILOT_API_KEY_FILE="api-key.json"
```

GitHub Copilot supports various editor-specific headers:

Common Headers

```
extra_headers ={
"editor-version":"vscode/1.85.1",# Editor version
"editor-plugin-version":"copilot/1.155.0",# Plugin version
"Copilot-Integration-Id":"vscode-chat",# Integration ID
"user-agent":"GithubCopilot/1.155.0"# User agent
}
```