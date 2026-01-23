---
title: "\U0001F319 Lunary - GenAI Observability | liteLLM"
url: https://docs.litellm.ai/docs/observability/lunary_integration
source: sitemap
fetched_at: 2026-01-21T19:46:19.950533922-03:00
rendered_js: false
word_count: 206
summary: This document provides instructions for integrating Lunary with LiteLLM to enable observability, prompt management, and analytics across various LLM providers. It covers implementation via the Python SDK, LangChain, and the LiteLLM Proxy Server.
tags:
    - lunary
    - litellm
    - observability
    - llm-monitoring
    - prompt-management
    - python-sdk
    - langchain
category: guide
---

[Lunary](https://lunary.ai/) is an open-source platform providing [observability](https://lunary.ai/docs/features/observe), [prompt management](https://lunary.ai/docs/features/prompts), and [analytics](https://lunary.ai/docs/features/observe#analytics) to help team manage and improve LLM chatbots.

You can reach out to us anytime by [email](mailto:hello@lunary.ai) or directly [schedule a Demo](https://lunary.ai/schedule).

## Usage with LiteLLM Python SDK[​](#usage-with-litellm-python-sdk "Direct link to Usage with LiteLLM Python SDK")

### Pre-Requisites[​](#pre-requisites "Direct link to Pre-Requisites")

```
pip install litellm lunary
```

### Quick Start[​](#quick-start "Direct link to Quick Start")

First, get your Lunary public key on the [Lunary dashboard](https://app.lunary.ai/).

Use just 2 lines of code, to instantly log your responses **across all providers** with Lunary:

```
litellm.success_callback =["lunary"]
litellm.failure_callback =["lunary"]
```

Complete code:

```
from litellm import completion

os.environ["LUNARY_PUBLIC_KEY"]="your-lunary-public-key"# from https://app.lunary.ai/)
os.environ["OPENAI_API_KEY"]=""

litellm.success_callback =["lunary"]
litellm.failure_callback =["lunary"]

response = completion(
  model="gpt-4o",
  messages=[{"role":"user","content":"Hi there 👋"}],
  user="ishaan_litellm"
)
```

### Usage with LangChain ChatLiteLLM[​](#usage-with-langchain-chatlitellm "Direct link to Usage with LangChain ChatLiteLLM")

```
import os
from langchain.chat_models import ChatLiteLLM
from langchain.schema import HumanMessage
import litellm

os.environ["LUNARY_PUBLIC_KEY"]=""# from https://app.lunary.ai/settings
os.environ['OPENAI_API_KEY']="sk-..."

litellm.success_callback =["lunary"]
litellm.failure_callback =["lunary"]

chat = ChatLiteLLM(
  model="gpt-4o"
  messages =[
    HumanMessage(
        content="what model are you"
)
]
chat(messages)
```

### Usage with Prompt Templates[​](#usage-with-prompt-templates "Direct link to Usage with Prompt Templates")

You can use Lunary to manage [prompt templates](https://lunary.ai/docs/features/prompts) and use them across all your LLM providers with LiteLLM.

```
from litellm import completion
from lunary

template = lunary.render_template("template-slug",{
"name":"John",# Inject variables
})

litellm.success_callback =["lunary"]

result = completion(**template)
```

### Usage with custom chains[​](#usage-with-custom-chains "Direct link to Usage with custom chains")

You can wrap your LLM calls inside custom chains, so that you can visualize them as traces.

```
import litellm
from litellm import completion
import lunary

litellm.success_callback =["lunary"]
litellm.failure_callback =["lunary"]

@lunary.chain("My custom chain name")
defmy_chain(chain_input):
  chain_run_id = lunary.run_manager.current_run_id
  response = completion(
    model="gpt-4o",
    messages=[{"role":"user","content":"Say 1"}],
    metadata={"parent_run_id": chain_run_id},
)

  response = completion(
    model="gpt-4o",
    messages=[{"role":"user","content":"Say 2"}],
    metadata={"parent_run_id": chain_run_id},
)
  chain_output = response.choices[0].message
return chain_output

my_chain("Chain input")
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

### Step1: Install dependencies and set your environment variables[​](#step1-install-dependencies-and-set-your-environment-variables "Direct link to Step1: Install dependencies and set your environment variables")

Install the dependencies

```
pip install litellm lunary
```

Get you Lunary public key from from [https://app.lunary.ai/settings](https://app.lunary.ai/settings)

```
export LUNARY_PUBLIC_KEY="<your-public-key>"
```

### Step 2: Create a `config.yaml` and set `lunary` callbacks[​](#step-2-create-a-configyaml-and-set-lunary-callbacks "Direct link to step-2-create-a-configyaml-and-set-lunary-callbacks")

```
model_list:
-model_name:"*"
litellm_params:
model:"*"
litellm_settings:
success_callback:["lunary"]
failure_callback:["lunary"]
```

### Step 3: Start the LiteLLM proxy[​](#step-3-start-the-litellm-proxy "Direct link to Step 3: Start the LiteLLM proxy")

```
litellm --config config.yaml
```

### Step 4: Make a request[​](#step-4-make-a-request "Direct link to Step 4: Make a request")

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful math tutor. Guide the user through the solution step by step."
      },
      {
        "role": "user",
        "content": "how can I solve 8x + 7 = -23"
      }
    ]
}'
```

You can find more details about the different ways of making requests to the LiteLLM proxy on [this page](https://docs.litellm.ai/docs/proxy/user_keys)

## Support & Talk to Founders[​](#support--talk-to-founders "Direct link to Support & Talk to Founders")

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
- Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)