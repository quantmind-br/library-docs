---
title: Adding a New Guardrail Integration | liteLLM
url: https://docs.litellm.ai/docs/adding_provider/simple_guardrail_tutorial
source: sitemap
fetched_at: 2026-01-21T19:43:56.966630797-03:00
rendered_js: false
word_count: 93
summary: This document provides step-by-step instructions for building and registering a custom guardrail class to validate LLM inputs and outputs within LiteLLM.
tags:
    - litellm
    - guardrails
    - custom-hooks
    - llm-security
    - middleware-development
category: tutorial
---

You're going to create a class that checks text before it goes to the LLM or after it comes back. If it violates your rules, you block it.

## How It Works[​](#how-it-works "Direct link to How It Works")

Request with guardrail:

```
curl --location 'http://localhost:4000/chat/completions' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "How do I hack a system?"}],
    "guardrails": ["my-guardrail"]
}'
```

Your guardrail checks input, then output. If something's wrong, raise an exception.

## Build Your Guardrail[​](#build-your-guardrail "Direct link to Build Your Guardrail")

### Create Your Directory[​](#create-your-directory "Direct link to Create Your Directory")

```
mkdir -p litellm/proxy/guardrails/guardrail_hooks/my_guardrail
cd litellm/proxy/guardrails/guardrail_hooks/my_guardrail
```

Two files: `my_guardrail.py` (main class) and `__init__.py` (initialization).

### Write the Main Class[​](#write-the-main-class "Direct link to Write the Main Class")

`my_guardrail.py`:

Follow from [Custom Guardrail](https://docs.litellm.ai/docs/proxy/guardrails/custom_guardrail#custom-guardrail) tutorial.

### Create the Init File[​](#create-the-init-file "Direct link to Create the Init File")

`__init__.py`:

```
from typing import TYPE_CHECKING

from litellm.types.guardrails import SupportedGuardrailIntegrations

from.my_guardrail import MyGuardrail

if TYPE_CHECKING:
from litellm.types.guardrails import Guardrail, LitellmParams


definitialize_guardrail(litellm_params:"LitellmParams", guardrail:"Guardrail"):
import litellm

    _my_guardrail_callback = MyGuardrail(
        api_base=litellm_params.api_base,
        api_key=litellm_params.api_key,
        guardrail_name=guardrail.get("guardrail_name",""),
        event_hook=litellm_params.mode,
        default_on=litellm_params.default_on,
)

    litellm.logging_callback_manager.add_litellm_callback(_my_guardrail_callback)
return _my_guardrail_callback


guardrail_initializer_registry ={
    SupportedGuardrailIntegrations.MY_GUARDRAIL.value: initialize_guardrail,
}

guardrail_class_registry ={
    SupportedGuardrailIntegrations.MY_GUARDRAIL.value: MyGuardrail,
}
```

### Register Your Guardrail Type[​](#register-your-guardrail-type "Direct link to Register Your Guardrail Type")

Add to `litellm/types/guardrails.py`:

```
classSupportedGuardrailIntegrations(str, Enum):
    LAKERA ="lakera_prompt_injection"
    APORIA ="aporia"
    BEDROCK ="bedrock_guardrails"
    PRESIDIO ="presidio"
    ZSCALER_AI_GUARD ="zscaler_ai_guard"
    MY_GUARDRAIL ="my_guardrail"
```

## Usage[​](#usage "Direct link to Usage")

### Config File[​](#config-file "Direct link to Config File")

```
model_list:
-model_name: gpt-4
litellm_params:
model: gpt-4
api_key: os.environ/OPENAI_API_KEY

litellm_settings:
guardrails:
-guardrail_name: my_guardrail
litellm_params:
guardrail: my_guardrail
mode: during_call
api_key: os.environ/MY_GUARDRAIL_API_KEY
api_base: https://api.myguardrail.com
```

### Per-Request[​](#per-request "Direct link to Per-Request")

```
curl --location 'http://localhost:4000/chat/completions' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Test message"}],
    "guardrails": ["my_guardrail"]
}'
```

## Testing[​](#testing "Direct link to Testing")

Add unit tests inside `test_litellm/` folder.