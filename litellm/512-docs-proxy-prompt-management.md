---
title: Prompt Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/prompt_management
source: sitemap
fetched_at: 2026-01-21T19:53:16.845516271-03:00
rendered_js: false
word_count: 596
summary: This document explains how to integrate and manage prompts in LiteLLM by defining them within a configuration file and connecting to external tools like Langfuse and DotPrompt. It covers setup procedures for loading prompts at proxy startup and using them via API endpoints with dynamic variables.
tags:
    - prompt-management
    - litellm-proxy
    - config-yaml
    - langfuse
    - dotprompt
    - prompt-integration
category: configuration
---

Run experiments or change the specific model (e.g. from gpt-4o to gpt4o-mini finetune) from your prompt management tool (e.g. Langfuse) instead of making changes in the application.

Supported IntegrationsLinkNative LiteLLM GitOps (.prompt files)[Get Started](https://docs.litellm.ai/docs/proxy/native_litellm_prompt)Langfuse[Get Started](https://langfuse.com/docs/prompts/get-started)Humanloop[Get Started](https://docs.litellm.ai/docs/observability/humanloop)

## Onboarding Prompts via config.yaml[​](#onboarding-prompts-via-configyaml "Direct link to Onboarding Prompts via config.yaml")

You can onboard and initialize prompts directly in your `config.yaml` file. This allows you to:

- Load prompts at proxy startup
- Manage prompts as code alongside your proxy configuration
- Use any supported prompt integration (dotprompt, Langfuse, BitBucket, GitLab, custom)

### Basic Structure[​](#basic-structure "Direct link to Basic Structure")

Add a `prompts` field to your config.yaml:

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY

prompts:
-prompt_id:"my_prompt_id"
litellm_params:
prompt_id:"my_prompt_id"
prompt_integration:"dotprompt"# or langfuse, bitbucket, gitlab, custom
# integration-specific parameters below
```

### Understanding `prompt_integration`[​](#understanding-prompt_integration "Direct link to understanding-prompt_integration")

The `prompt_integration` field determines where and how prompts are loaded:

- **`dotprompt`** : Load from local `.prompt` files or inline content
- **`langfuse`** : Fetch prompts from Langfuse prompt management
- **`bitbucket`** : Load from BitBucket repository `.prompt` files (team-based access control)
- **`gitlab`** : Load from GitLab repository `.prompt` files (team-based access control)
- **`custom`** : Use your own custom prompt management implementation

Each integration has its own configuration parameters and access control mechanisms.

### Supported Integrations[​](#supported-integrations "Direct link to Supported Integrations")

- DotPrompt (File-based)
- Langfuse
- BitBucket
- GitLab

**Option 1: Using a prompt directory**

```
prompts:
-prompt_id:"hello"
litellm_params:
prompt_id:"hello"
prompt_integration:"dotprompt"
prompt_directory:"./prompts"# Directory containing .prompt files

litellm_settings:
global_prompt_directory:"./prompts"# Global setting for all dotprompt integrations
```

**Option 2: Using inline prompt data**

```
prompts:
-prompt_id:"my_inline_prompt"
litellm_params:
prompt_id:"my_inline_prompt"
prompt_integration:"dotprompt"
prompt_data:
my_inline_prompt:
content:"Hello {{name}}! How can I help you with {{topic}}?"
metadata:
model:"gpt-4"
temperature:0.7
max_tokens:150
```

**Option 3: Using dotprompt\_content for single prompts**

```
prompts:
-prompt_id:"simple_prompt"
litellm_params:
prompt_id:"simple_prompt"
prompt_integration:"dotprompt"
dotprompt_content:|
        ---
        model: gpt-4
        temperature: 0.7
        ---
        System: You are a helpful assistant.

User:{{user_message}}
```

Create `.prompt` files in your prompt directory:

```
# prompts/hello.prompt
---
model: gpt-4
temperature:0.7
---
System: You are a helpful assistant.

User:{{user_message}}
```

### Complete Example[​](#complete-example "Direct link to Complete Example")

Here's a complete example showing multiple prompts with different integrations:

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY

prompts:
# File-based dotprompt
-prompt_id:"coding_assistant"
litellm_params:
prompt_id:"coding_assistant"
prompt_integration:"dotprompt"
prompt_directory:"./prompts"

# Inline dotprompt
-prompt_id:"simple_chat"
litellm_params:
prompt_id:"simple_chat"
prompt_integration:"dotprompt"
prompt_data:
simple_chat:
content:"You are a {{personality}} assistant. User: {{message}}"
metadata:
model:"gpt-4"
temperature:0.8

# Langfuse prompt
-prompt_id:"langfuse_chat"
litellm_params:
prompt_id:"langfuse_chat"
prompt_integration:"langfuse"
langfuse_public_key:"os.environ/LANGFUSE_PUBLIC_KEY"
langfuse_secret_key:"os.environ/LANGFUSE_SECRET_KEY"

litellm_settings:
global_prompt_directory:"./prompts"
```

### How It Works[​](#how-it-works "Direct link to How It Works")

1. **At Startup**: When the proxy starts, it reads the `prompts` field from `config.yaml`
2. **Initialization**: Each prompt is initialized based on its `prompt_integration` type
3. **In-Memory Storage**: Prompts are stored in the `IN_MEMORY_PROMPT_REGISTRY`
4. **Access**: Use these prompts via the `/v1/chat/completions` endpoint with `prompt_id` in the request

### Using Config-Loaded Prompts[​](#using-config-loaded-prompts "Direct link to Using Config-Loaded Prompts")

After loading prompts via config.yaml, use them in your API requests:

```
curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "gpt-4",
    "prompt_id": "coding_assistant",
    "prompt_variables": {
        "language": "python",
        "task": "create a web scraper"
    }
}'
```

### Prompt Schema Reference[​](#prompt-schema-reference "Direct link to Prompt Schema Reference")

Each prompt in the `prompts` list requires:

- **`prompt_id`** (string, required): Unique identifier for the prompt
- **`litellm_params`** (object, required): Configuration for the prompt
  
  - **`prompt_id`** (string, required): Must match the top-level prompt\_id
  - **`prompt_integration`** (string, required): One of: `dotprompt`, `langfuse`, `bitbucket`, `gitlab`, `custom`
  - Additional integration-specific parameters (see tabs above)
- **`prompt_info`** (object, optional): Metadata about the prompt
  
  - **`prompt_type`** (string): Defaults to `"config"` for config-loaded prompts

### Notes[​](#notes "Direct link to Notes")

- Config-loaded prompts have `prompt_type: "config"` and **cannot be updated** via the API
- To update config prompts, modify your `config.yaml` and restart the proxy
- For dynamic prompts that can be updated via API, use the `/prompts` endpoints instead
- All supported integrations work with config-loaded prompts

## Quick Start[​](#quick-start "Direct link to Quick Start")

- SDK
- PROXY

```
import os 
import litellm

os.environ["LANGFUSE_PUBLIC_KEY"]="public_key"# [OPTIONAL] set here or in `.completion`
os.environ["LANGFUSE_SECRET_KEY"]="secret_key"# [OPTIONAL] set here or in `.completion`

litellm.set_verbose =True# see raw request to provider

resp = litellm.completion(
    model="langfuse/gpt-3.5-turbo",
    prompt_id="test-chat-prompt",
    prompt_variables={"user_message":"this is used"},# [OPTIONAL]
    messages=[{"role":"user","content":"<IGNORED>"}],
)
```

**Expected Logs:**

```
POST Request Sent from LiteLLM:
curl -X POST \
https://api.openai.com/v1/ \
-d '{'model': 'gpt-3.5-turbo', 'messages': <YOUR LANGFUSE PROMPT TEMPLATE>}'
```

## How to set model[​](#how-to-set-model "Direct link to How to set model")

### Set the model on LiteLLM[​](#set-the-model-on-litellm "Direct link to Set the model on LiteLLM")

You can do `langfuse/<litellm_model_name>`

- SDK
- PROXY

```
litellm.completion(
    model="langfuse/gpt-3.5-turbo",# or `langfuse/anthropic/claude-3-5-sonnet`
...
)
```

### Set the model in Langfuse[​](#set-the-model-in-langfuse "Direct link to Set the model in Langfuse")

If the model is specified in the Langfuse config, it will be used.

```
model_list:
-model_name: gpt-3.5-turbo
litellm_params:
model: azure/chatgpt-v-2
api_key: os.environ/AZURE_API_KEY
api_base: os.environ/AZURE_API_BASE
```

## What is 'prompt\_variables'?[​](#what-is-prompt_variables "Direct link to What is 'prompt_variables'?")

- `prompt_variables`: A dictionary of variables that will be used to replace parts of the prompt.

## What is 'prompt\_id'?[​](#what-is-prompt_id "Direct link to What is 'prompt_id'?")

- `prompt_id`: The ID of the prompt that will be used for the request.

## What will the formatted prompt look like?[​](#what-will-the-formatted-prompt-look-like "Direct link to What will the formatted prompt look like?")

### `/chat/completions` messages[​](#chatcompletions-messages "Direct link to chatcompletions-messages")

The `messages` field sent in by the client is ignored.

The Langfuse prompt will replace the `messages` field.

To replace parts of the prompt, use the `prompt_variables` field. [See how prompt variables are used](https://github.com/BerriAI/litellm/blob/017f83d038f85f93202a083cf334de3544a3af01/litellm/integrations/langfuse/langfuse_prompt_management.py#L127)

If the Langfuse prompt is a string, it will be sent as a user message (not all providers support system messages).

If the Langfuse prompt is a list, it will be sent as is (Langfuse chat prompts are OpenAI compatible).

## Architectural Overview[​](#architectural-overview "Direct link to Architectural Overview")

## API Reference[​](#api-reference "Direct link to API Reference")

These are the params you can pass to the `litellm.completion` function in SDK and `litellm_params` in config.yaml

```
prompt_id: str # required
prompt_variables: Optional[dict] # optional
prompt_version: Optional[int] # optional
langfuse_public_key: Optional[str] # optional
langfuse_secret: Optional[str] # optional
langfuse_secret_key: Optional[str] # optional
langfuse_host: Optional[str] # optional
```