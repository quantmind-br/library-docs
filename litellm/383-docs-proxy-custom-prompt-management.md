---
title: Custom Prompt Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/custom_prompt_management
source: sitemap
fetched_at: 2026-01-21T19:51:34.825921529-03:00
rendered_js: false
word_count: 97
summary: This document explains how to integrate custom prompt management systems with LiteLLM by implementing and registering a custom hook class for automated prompt retrieval and formatting.
tags:
    - litellm
    - prompt-management
    - custom-hooks
    - python-sdk
    - llm-integration
    - callbacks
category: guide
---

Connect LiteLLM to your prompt management system with custom hooks.

Create a class that inherits from `CustomPromptManagement` to handle prompt retrieval and formatting:

Create a new file called `custom_prompt.py` and add this code. The key method here is `get_chat_completion_prompt` you can implement custom logic to retrieve and format prompts based on the `prompt_id` and `prompt_variables`.

```
from typing import List, Tuple, Optional
from litellm.integrations.custom_prompt_management import CustomPromptManagement
from litellm.types.llms.openai import AllMessageValues
from litellm.types.utils import StandardCallbackDynamicParams

classMyCustomPromptManagement(CustomPromptManagement):
defget_chat_completion_prompt(
        self,
        model:str,
        messages: List[AllMessageValues],
        non_default_params:dict,
        prompt_id:str,
        prompt_variables: Optional[dict],
        dynamic_callback_params: StandardCallbackDynamicParams,
)-> Tuple[str, List[AllMessageValues],dict]:
"""
        Retrieve and format prompts based on prompt_id.

        Returns:
            - model: The model to use
            - messages: The formatted messages
            - non_default_params: Optional parameters like temperature
        """
# Example matching the diagram: Add system message for prompt_id "1234"
if prompt_id =="1234":
# Prepend system message while preserving existing messages
            new_messages =[
{"role":"system","content":"Be a good Bot!"},
]+ messages
return model, new_messages, non_default_params

# Default: Return original messages if no prompt_id match
return model, messages, non_default_params

prompt_management = MyCustomPromptManagement()
```

When you pass `prompt_id="1234"`, the custom prompt manager will add a system message "Be a good Bot!" to your conversation:

If you call `litellm.completion()` from a Python script (without going through the proxy), register your custom prompt manager before making the request:

```

import litellm
from custom_prompt import prompt_management

litellm.callbacks =[prompt_management]
litellm.use_litellm_proxy =True

response = litellm.completion(
    model="gpt-4",
    messages=[{"role":"user","content":"hi"}],
    prompt_id="1234",
    prompt_variables={"user_message":"hi"},
)
```