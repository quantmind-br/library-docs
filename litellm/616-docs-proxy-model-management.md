---
title: Model Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/model_management
source: sitemap
fetched_at: 2026-01-21T19:53:04.800365197-03:00
rendered_js: false
word_count: 166
summary: This document explains how to use specific API endpoints to dynamically add new models and retrieve detailed model metadata without restarting the proxy server.
tags:
    - litellm
    - model-management
    - api-endpoints
    - dynamic-configuration
    - proxy-management
category: api
---

Add new models + Get model info without restarting proxy.

Retrieve detailed information about each model listed in the `/model/info` endpoint, including descriptions from the `config.yaml` file, and additional model info (e.g. max tokens, cost per input token, etc.) pulled from the model\_info you set and the [litellm model cost map](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json). Sensitive details like API keys are excluded for security purposes.

Add a new model to the proxy via the `/model/new` API, to add models without restarting the proxy.

When adding a new model, your JSON payload should conform to the following structure:

Keep in mind that as both endpoints are in \[BETA], you may need to visit the associated GitHub issues linked in the API descriptions to check for updates or provide feedback:

Feedback on the beta endpoints is valuable and helps improve the API for all users.

If you want the ability to add a display name, description, and labels for models, just use `model_info:`

Use a key with access to the model `gpt-4`.

```
{
    "data": [
        {
            "model_name": "gpt-4",
            "litellm_params": {
                "model": "gpt-4"
            },
            "model_info": {
                "id": "e889baacd17f591cce4c63639275ba5e8dc60765d6c553e6ee5a504b19e50ddc",
                "db_model": false,
                "my_custom_key": "my_custom_value", # 👈 CUSTOM INFO
                "key": "gpt-4", # 👈 KEY in LiteLLM MODEL INFO/COST MAP - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
                "max_tokens": 4096,
                "max_input_tokens": 8192,
                "max_output_tokens": 4096,
                "input_cost_per_token": 3e-05,
                "input_cost_per_character": null,
                "input_cost_per_token_above_128k_tokens": null,
                "output_cost_per_token": 6e-05,
                "output_cost_per_character": null,
                "output_cost_per_token_above_128k_tokens": null,
                "output_cost_per_character_above_128k_tokens": null,
                "output_vector_size": null,
                "litellm_provider": "openai",
                "mode": "chat"
            }
        },
    ]
}
```