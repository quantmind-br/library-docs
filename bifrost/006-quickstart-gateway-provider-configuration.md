---
title: Provider Configuration
url: https://docs.getbifrost.ai/quickstart/gateway/provider-configuration.md
source: llms
fetched_at: 2026-01-21T19:44:50.405610298-03:00
rendered_js: false
word_count: 1214
summary: This document explains how to set up and manage multiple AI model providers using the Web UI, API, or configuration files. It covers advanced settings such as weighted load balancing, network configurations, and environment variable management for API keys.
tags:
    - provider-configuration
    - ai-models
    - load-balancing
    - api-keys
    - environment-variables
    - multi-provider
category: configuration
---

# Provider Configuration

> Configure multiple AI providers for custom concurrency, queue sizes, proxy settings, and more.

## Multi-Provider Setup

Configure multiple providers to seamlessly switch between them. This example shows how to configure OpenAI, Anthropic, and Mistral providers.

<Tabs group="provider-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=ac7f272948b57a362066fc98f6e26bf5" alt="Provider Configuration Interface" data-og-width="3002" width="3002" data-og-height="2147" height="2147" data-path="media/ui-provider-configs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=280&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=8509b4603bcbec88c3f651b08d087e5f 280w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=560&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=33925983d03514c7ea026c323b5fb8b6 560w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=840&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=063361edca41f680753b3d5be71bddc3 840w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=1100&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=6914883bce09a9773efa731cad64e79c 1100w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=1650&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=6ae67cf6f4b95da43a3ced286463ec76 1650w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-provider-configs.png?w=2500&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=2404c77a5ab78c5c3820f8a6e3d626aa 2500w" />

    1. Go to **[http://localhost:8080](http://localhost:8080)**
    2. Navigate to **"Model Providers"** in the sidebar
    3. Select provider and configure keys
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    # Add OpenAI provider
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ]
    }'

    # Add Anthropic provider
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "anthropic",
        "keys": [
            {
                "name": "anthropic-key-1",
                "value": "env.ANTHROPIC_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ]
    }'

    # Add vLLM (self-hosted OpenAI-compatible server)
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "vllm-local",
        "keys": [
            {
                "name": "vllm-key-1",
                "value": "dummy",
                "models": [],
                "weight": 1.0
            }
        ],
        "network_config": {
            "base_url": "http://vllm-endpoint:8000",
            "default_request_timeout_in_seconds": 60
        },
        "custom_provider_config": {
            "base_provider_type": "openai",
            "allowed_requests": {
                "chat_completion": true,
                "chat_completion_stream": true
            }
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    <Note>
      Each key in a provider needs to have a unique name.
    </Note>

    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ]
            },
            "anthropic": {
                "keys": [
                    {
                        "name": "anthropic-key",
                        "value": "env.ANTHROPIC_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ]
            },
            "vllm-local": {
                "keys": [
                    {
                        "name": "vllm-key",
                        "value": "dummy",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "network_config": {
                    "base_url": "http://vllm-endpoint:8000",
                    "default_request_timeout_in_seconds": 60
                },
                "custom_provider_config": {
                    "base_provider_type": "openai",
                    "allowed_requests": {
                        "chat_completion": true,
                        "chat_completion_stream": true
                    }
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

<Tip>
  **Kubernetes DNS (only for custom endpoint):** When running in Kubernetes, use fully qualified domain names (FQDN) like `http://<service>.<namespace>.svc.cluster.local:8000` for cross-namespace custom endpoints. Short names like `http://<service>:8000` only work within the same namespace.
</Tip>

## Making Requests

Once providers are configured, you can make requests to any specific provider. This example shows how to send a request directly to OpenAI's GPT-4o Mini model. Bifrost handles the provider-specific API formatting automatically.

```bash  theme={null}
curl --location 'http://localhost:8080/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
    "model": "openai/gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Hello!"}
    ]
}'
```

## Environment Variables

Set up your API keys for the providers you want to use. Bifrost supports both direct key values and environment variable references with the `env.` prefix:

```bash  theme={null}
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export MISTRAL_API_KEY="your-mistral-api-key"
export CEREBRAS_API_KEY="your-cerebras-api-key"
export GROQ_API_KEY="your-groq-api-key"
export COHERE_API_KEY="your-cohere-api-key"
```

**Environment Variable Handling:**

* Use `"value": "env.VARIABLE_NAME"` to reference environment variables
* Use `"value": "sk-proj-xxxxxxxxx"` to pass keys directly
* All sensitive data is automatically redacted in GET requests and UI responses for security

## Advanced Configuration

### Weighted Load Balancing

Distribute requests across multiple API keys or providers based on custom weights. This example shows how to split traffic 70/30 between two OpenAI keys, useful for managing rate limits or costs across different accounts.

<Tabs group="load-balancing">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=9a681769557df343eb4e66fb427a0598" alt="Weighted Load Balancing Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-multi-key-for-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=528e0455f52e55c5356fb1ef03ed4435 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=f3660535d633e0b0876cbab8ec8bb21e 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=3687ef50a1e54c94e11daee7461543ff 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=aabd0160842b9e0c68b4879af828f813 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=af53871b3224679959462e15f27e852c 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=249b3c3b66f00f08ee75c3032ab121bb 2500w" />

    1. Navigate to **"Model Providers"** → **"OpenAI"**
    2. Click **"Add Key"** to add multiple keys
    3. Set weight values (0.7 and 0.3)
    4. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY_1",
                "models": [],
                "weight": 0.7
            },
            {
                "name": "openai-key-2",
                "value": "env.OPENAI_API_KEY_2", 
                "models": [],
                "weight": 0.3
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY_1",
                        "models": [],
                        "weight": 0.7
                    },
                    {
                        "name": "openai-key-2",
                        "value": "env.OPENAI_API_KEY_2",
                        "models": [],
                        "weight": 0.3
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

### Model-Specific Keys

Use different API keys for specific models, allowing you to manage access controls and billing separately. This example uses a premium key for advanced reasoning models (o1-preview, o1-mini) and a standard key for regular GPT models.

<Tabs group="model-keys">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=9a681769557df343eb4e66fb427a0598" alt="Model-Specific Keys Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-multi-key-for-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=528e0455f52e55c5356fb1ef03ed4435 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=f3660535d633e0b0876cbab8ec8bb21e 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=3687ef50a1e54c94e11daee7461543ff 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=aabd0160842b9e0c68b4879af828f813 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=af53871b3224679959462e15f27e852c 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-multi-key-for-models.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=249b3c3b66f00f08ee75c3032ab121bb 2500w" />

    1. Navigate to **"Model Providers"** → **"OpenAI"**
    2. Add first key with models: `["gpt-4o", "gpt-4o-mini"]`
    3. Add premium key with models: `["o1-preview", "o1-mini"]`
    4. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": ["gpt-4o", "gpt-4o-mini"],
                "weight": 1.0
            },
            {
                "name": "openai-key-2",
                "value": "env.OPENAI_API_KEY_PREMIUM",
                "models": ["o1-preview", "o1-mini"],
                "weight": 1.0
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": ["gpt-4o", "gpt-4o-mini"],
                        "weight": 1.0
                    },
                    {
                        "name": "openai-key-2",
                        "value": "env.OPENAI_API_KEY_PREMIUM",
                        "models": ["o1-preview", "o1-mini"],
                        "weight": 1.0
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

### Custom Base URL

Override the default API endpoint for a provider. This is useful for connecting to self-hosted models, local development servers, or OpenAI-compatible APIs like vLLM, Ollama, or LiteLLM.

<Tabs group="base-url-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=d23ca8ea0061a9f23c8921973311e1b9" alt="Base URL Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-base-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=280&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=2af14bba03f8a71061287017087405da 280w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=560&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=9cdd284d2501e59c92e9c6c8038b4e36 560w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=840&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=885834ef52aefe16fc09b9fb870a6af3 840w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=1100&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=9253ac324265b6ca752317e4d4d5c80f 1100w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=1650&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=0f2666c02bdfbaeec2123208fe8486c0 1650w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-base-url.png?w=2500&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=0e41c93e1cda205d2bb60445eb86536a 2500w" />

    1. Navigate to **"Model Providers"** → **"OpenAI"** → **"Provider level configuration"** → **"Network config"**
    2. Set **Base URL**: `http://localhost:8000/v1`
    3. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "network_config": {
            "base_url": "http://localhost:8000/v1"
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "network_config": {
                    "base_url": "http://localhost:8000/v1"
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

<Note>
  For self-hosted providers like Ollama and SGL, `base_url` is required. For standard providers, it's optional and overrides the default endpoint.
</Note>

### Managing Retries

Configure retry behavior for handling temporary failures and rate limits. This example sets up exponential backoff with up to 5 retries, starting with 1ms delay and capping at 10 seconds - ideal for handling transient network issues.

<Tabs group="retry-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=49801ff84f24b2847b5de83c9afa1d7e" alt="Retry Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-concurrency-timeout.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=91b02eb49527c68f09b6af424cab4978 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=dc103588252a132acd49d10536325134 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=537dc509001b7d354f6c9a9936d37836 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=192e77e0f46541e9d6ef8db262635a9f 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=db35d063a224f28663791738ff0053ec 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-timeout.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=37e83cb3bed547a6b3b7729fed884f4e 2500w" />

    1. Navigate to **"Model Providers"** → **"OpenAI"** → **"Provider level configuration"** → **"Network config"**
    2. Set **Max Retries**: `5`
    3. Set **Initial Backoff**: `1` ms
    4. Set **Max Backoff**: `10000` ms
    5. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "network_config": {
            "max_retries": 5,
            "retry_backoff_initial_ms": 1,
            "retry_backoff_max_ms": 10000
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "network_config": {
                    "max_retries": 5,
                    "retry_backoff_initial_ms": 1,
                    "retry_backoff_max_ms": 10000
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

### Custom Concurrency and Buffer Size

Fine-tune performance by adjusting worker concurrency and queue sizes per provider (defaults are 1000 workers and 5000 queue size). This example gives OpenAI higher limits (100 workers, 500 queue) for high throughput, while Anthropic gets conservative limits to respect their rate limits.

<Tabs group="concurrency-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=2c56cb51da2fc0ed83584ccb833b34d6" alt="Concurrency Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-concurrency-buffer-size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=20329410572adb1d3c623ee6b8e97794 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=a1d14faef3ff48229e911f4f6c9a6107 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=0e0c7520a0fb8956c1f976cdebfeab16 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=880cb3056a95a6d2b0b7e12432e03c5a 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=4583f8c0c1b89135bc3a1f9cae77c8f6 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-concurrency-buffer-size.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=d3c05ca5ef9721912608331d9be91daa 2500w" />

    1. Navigate to **"Model Providers"** → **{Provider}** → **"Provider level configuration"** → **"Performance tuning"**
    2. Set **Concurrency**: Worker count (100 for OpenAI, 25 for Anthropic)
    3. Set **Buffer Size**: Queue size (500 for OpenAI, 100 for Anthropic)
    4. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    # OpenAI with high throughput settings
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "concurrency_and_buffer_size": {
            "concurrency": 100,
            "buffer_size": 500
        }
    }'

    # Anthropic with conservative settings
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "anthropic", 
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.ANTHROPIC_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "concurrency_and_buffer_size": {
            "concurrency": 25,
            "buffer_size": 100
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "concurrency_and_buffer_size": {
                    "concurrency": 100,
                    "buffer_size": 500
                }
            },
            "anthropic": {
                "keys": [
                    {
                        "name": "anthropic-key-1",
                        "value": "env.ANTHROPIC_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "concurrency_and_buffer_size": {
                    "concurrency": 25,
                    "buffer_size": 100
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

### Custom Headers

Bifrost supports two ways to add custom headers to provider requests: **static headers** configured at the provider level, and **dynamic headers** passed per-request.

#### Static Headers (Provider Level)

Configure headers that are automatically included in every request to a specific provider. This is useful for provider-specific requirements, API versioning, or organizational metadata.

<Tabs group="static-headers">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=d29e2ae76e64af57804eb07444ff131a" alt="Extra Headers Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-extra-headers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=280&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=85d7e9fd34ba5e3068ae759c65fafc04 280w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=560&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=65b14cec085be05b62c1926660fbb046 560w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=840&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=4f839efeadfe924a555280e65d911b19 840w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=1100&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=d76bc5a08da1ff309ee0f937493ee204 1100w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=1650&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=e03a64b855f5d8b44a33ab063ecda3a6 1650w, https://mintcdn.com/bifrost/CnHgWKmYLXfJ0GEc/media/ui-extra-headers.png?w=2500&fit=max&auto=format&n=CnHgWKmYLXfJ0GEc&q=85&s=630d95e5ace5bd52b0da215a94e273f2 2500w" />

    1. Navigate to **"Model Providers"** → **"OpenAI"** → **"Provider level configuration"** → **"Network config"**
    2. Add headers in the **"Extra Headers"** section
    3. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "network_config": {
            "extra_headers": {
                "x-custom-org": "my-organization",
                "x-environment": "production"
            }
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "network_config": {
                    "extra_headers": {
                        "x-custom-org": "my-organization",
                        "x-environment": "production"
                    }
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

#### Dynamic Headers (Per Request)

Send custom headers with individual requests using the `x-bf-eh-*` prefix. Headers are automatically propagated to the provider after stripping the prefix. This is useful for request-specific metadata, user identification, or custom tracking information.

```bash  theme={null}
curl --location 'http://localhost:8080/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'x-bf-eh-user-id: user-123' \
--header 'x-bf-eh-tracking-id: trace-456' \
--data '{
    "model": "openai/gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Hello!"}
    ]
}'
```

The `x-bf-eh-` prefix is stripped before forwarding, so `x-bf-eh-user-id` becomes `user-id` in the request to the provider.

**Example use cases:**

* User identification: `x-bf-eh-user-id`, `x-bf-eh-tenant-id`
* Request tracking: `x-bf-eh-correlation-id`, `x-bf-eh-trace-id`
* Custom metadata: `x-bf-eh-department`, `x-bf-eh-cost-center`
* A/B testing: `x-bf-eh-experiment-id`, `x-bf-eh-variant`

#### Security Denylist

Bifrost maintains a security denylist of headers that are never forwarded to providers, regardless of configuration:

```go  theme={null}
denylist := map[string]bool{
    "proxy-authorization": true,
    "cookie":              true,
    "host":                true,
    "content-length":      true,
    "connection":          true,
    "transfer-encoding":   true,

    // prevent auth/key overrides via x-bf-eh-*
    "x-api-key":      true,
    "x-goog-api-key": true,
    "x-bf-api-key":   true,
    "x-bf-vk":        true,
}
```

This denylist is applied to both static and dynamic headers to prevent security vulnerabilities.

### Setting Up a Proxy

Route requests through proxies for compliance, security, or geographic requirements. This example shows both HTTP proxy for OpenAI and authenticated SOCKS5 proxy for Anthropic, useful for corporate environments or regional access.

<Tabs group="proxy-config">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=de55ac1effe8b49c4ac60079f987e5ed" alt="Proxy Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-proxy-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=280&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=6e17f75355716054b062d2b4281c12ec 280w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=560&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=9894720d9cd719f60783b27fb7ecfcd0 560w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=840&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=012d561202e7e99d6dc5d3baae7ed0b6 840w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=1100&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=4709e3f998986cf7edd6c8f457eeb5a2 1100w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=1650&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=975e3d6d41d34aa3deb29cd379d504a4 1650w, https://mintcdn.com/bifrost/haPSvjWru9cl-Jd-/media/ui-proxy-setup.png?w=2500&fit=max&auto=format&n=haPSvjWru9cl-Jd-&q=85&s=76837e350931b5247e53026edb8bd0ee 2500w" />

    1. Navigate to **"Model Providers"** → **{Provider}** → **"Provider level configuration"** → **"Proxy config"**
    2. Select **Proxy Type**: HTTP or SOCKS5
    3. Set **Proxy URL**: `http://localhost:8000`
    4. Add credentials if needed (username/password)
    5. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    # HTTP proxy for OpenAI
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "proxy_config": {
            "type": "http",
            "url": "http://localhost:8000"
        }
    }'

    # SOCKS5 proxy with authentication for Anthropic
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "anthropic",
        "keys": [
            {
                "name": "anthropic-key-1",
                "value": "env.ANTHROPIC_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "proxy_config": {
            "type": "socks5",
            "url": "http://localhost:8000",
            "username": "user",
            "password": "password"
        }
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "proxy_config": {
                    "type": "http",
                    "url": "http://localhost:8000"
                }
            },
            "anthropic": {
                "keys": [
                    {
                        "name": "anthropic-key-1",
                        "value": "env.ANTHROPIC_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "proxy_config": {
                    "type": "socks5",
                    "url": "http://localhost:8000",
                    "username": "user",
                    "password": "password"
                }
            }
        }
    }
    ```
  </Tab>
</Tabs>

### Send Back Raw Response

Include the original provider response alongside Bifrost's standardized response format. Useful for debugging and accessing provider-specific metadata.

<Tabs group="raw-response">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=ea6a5fb31847f99883b68ab33d847353" alt="Raw Response Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-raw-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=280&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=37a561e71be14d6dab5550f54cd81ea3 280w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=560&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=25afd6398ce081df20ccebcbec7755fb 560w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=840&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=553d4d77d1890a453fdef0f3322ee1b8 840w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=1100&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=23cf3686ea9bace23da51bba891af3ae 1100w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=1650&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=b9c53413820a9d3b2459326c53c25460 1650w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-response.png?w=2500&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=bb9e6dbb6573df152efe4a7c4973983f 2500w" />

    1. Navigate to **"Model Providers"** → **{Provider}** → **"Provider level configuration"** → **"Performance tuning"**
    2. Toggle **"Include Raw Response"** to enabled
    3. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "send_back_raw_response": true
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "send_back_raw_response": true
            }
        }
    }
    ```
  </Tab>
</Tabs>

When enabled, the raw provider response appears in `extra_fields.raw_response`:

```json  theme={null}
{
    "choices": [...],
    "usage": {...},
    "extra_fields": {
        "provider": "openai",
        "raw_response": {
            // Original OpenAI response here
        }
    }
}
```

### Send Back Raw Request

Include the original request sent to the provider alongside Bifrost's response. Useful for debugging request transformations and verifying what was actually sent to the provider.

<Tabs group="raw-request">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=2f009a76cf0acd1dc237513eaffb912e" alt="Raw Request Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-raw-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=280&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=1dad5fad4afa7f98b78220bd175d49bc 280w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=560&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=1cd0201186d2be9f3ab744ecd0d5beb8 560w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=840&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=92370b03995526a85be5d908800977e9 840w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=1100&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=2dc4723d1ba3d6fb8288f283684c8745 1100w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=1650&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=d6fc0b9459e811d4db22a8064c3de49c 1650w, https://mintcdn.com/bifrost/NXcbzch8DxxqGB-u/media/ui-raw-request.png?w=2500&fit=max&auto=format&n=NXcbzch8DxxqGB-u&q=85&s=a8511f91a5d2e8d3bac57f1933915baa 2500w" />

    1. Navigate to **"Model Providers"** → **{Provider}** → **"Provider level configuration"** → **"Performance tuning"**
    2. Toggle **"Include Raw Request"** to enabled
    3. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "openai",
        "keys": [
            {
                "name": "openai-key-1",
                "value": "env.OPENAI_API_KEY",
                "models": [],
                "weight": 1.0
            }
        ],
        "send_back_raw_request": true
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "openai": {
                "keys": [
                    {
                        "name": "openai-key-1",
                        "value": "env.OPENAI_API_KEY",
                        "models": [],
                        "weight": 1.0
                    }
                ],
                "send_back_raw_request": true
            }
        }
    }
    ```
  </Tab>
</Tabs>

When enabled, the raw provider request appears in `extra_fields.raw_request`:

```json  theme={null}
{
    "choices": [...],
    "usage": {...},
    "extra_fields": {
        "provider": "openai",
        "raw_request": {
            // Original request sent to OpenAI here
        }
    }
}
```

<Tip>
  You can enable both `send_back_raw_request` and `send_back_raw_response` together to see the complete request-response cycle for debugging purposes.
</Tip>

## Provider-Specific Authentication

Enterprise cloud providers require additional configuration beyond API keys. Configure Azure, AWS Bedrock, and Google Vertex with platform-specific authentication details.

### Azure

Azure supports two authentication methods:

#### Azure Entra ID (Service Principal)

<Tabs group="azure-entra-auth">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=0da4867c5eb1abb6ac5549b7a8aa0666" alt="Azure Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-azure-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=280&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=17e572fb7d1e35b96ca42921a2fd0a90 280w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=560&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=24845e859ef049a8b33a712778096c30 560w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=840&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=511ccabc2b5dcbac688abe0f04e1b9fc 840w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=1100&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=7f31384b6c229d1b41c768527afd57f4 1100w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=1650&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=35bd6af0c0739c6b1f9bd174b396fa69 1650w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=2500&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=2180a231e99f9831e99ea66f3ed0bfa7 2500w" />

    1. Navigate to **"Model Providers"** → **"Azure"**
    2. Leave **API Key** empty for Service Principal auth
    3. Set **Client ID**: Your Azure Entra ID client ID
    4. Set **Client Secret**: Your Azure Entra ID client secret
    5. Set **Tenant ID**: Your Azure Entra ID tenant ID
    6. Set **Endpoint**: Your Azure endpoint URL
    7. Configure **Deployments**: Map model names to deployment names
    8. Set **API Version**: e.g., `2024-08-01-preview`
    9. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "azure",
        "keys": [
            {
                "name": "azure-key-1",
                "value": "",
                "models": ["gpt-4o", "gpt-4o-mini"],
                "weight": 1.0,
                "azure_key_config": {
                    "endpoint": "env.AZURE_ENDPOINT",
                    "client_id": "env.AZURE_CLIENT_ID",
                    "client_secret": "env.AZURE_CLIENT_SECRET",
                    "tenant_id": "env.AZURE_TENANT_ID",
                    "deployments": {
                        "gpt-4o": "gpt-4o-deployment",
                        "gpt-4o-mini": "gpt-4o-mini-deployment"
                    },
                    "api_version": "2024-08-01-preview"
                }
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "azure": {
                "keys": [
                    {
                        "name": "azure-key-1",
                        "value": "",
                        "models": ["gpt-4o", "gpt-4o-mini"],
                        "weight": 1.0,
                        "azure_key_config": {
                            "endpoint": "env.AZURE_ENDPOINT",
                            "client_id": "env.AZURE_CLIENT_ID",
                            "client_secret": "env.AZURE_CLIENT_SECRET",
                            "tenant_id": "env.AZURE_TENANT_ID",
                            "deployments": {
                                "gpt-4o": "gpt-4o-deployment",
                                "gpt-4o-mini": "gpt-4o-mini-deployment"
                            },
                            "api_version": "2024-08-01-preview"
                        }
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

#### Direct Authentication

For simpler use cases, provide the authentication credential directly in the `value` field:

<Tabs group="azure-direct-auth">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=0da4867c5eb1abb6ac5549b7a8aa0666" alt="Azure Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-azure-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=280&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=17e572fb7d1e35b96ca42921a2fd0a90 280w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=560&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=24845e859ef049a8b33a712778096c30 560w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=840&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=511ccabc2b5dcbac688abe0f04e1b9fc 840w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=1100&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=7f31384b6c229d1b41c768527afd57f4 1100w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=1650&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=35bd6af0c0739c6b1f9bd174b396fa69 1650w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-azure-config.png?w=2500&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=2180a231e99f9831e99ea66f3ed0bfa7 2500w" />

    1. Navigate to **"Model Providers"** → **"Azure"**
    2. Set **API Key**: Your Azure API key
    3. Set **Endpoint**: Your Azure endpoint URL
    4. Configure **Deployments**: Map model names to deployment names
    5. Set **API Version**: e.g., `2024-08-01-preview`
    6. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "azure",
        "keys": [
            {
                "name": "azure-key-1",
                "value": "env.AZURE_API_KEY",
                "models": ["gpt-4o", "gpt-4o-mini"],
                "weight": 1.0,
                "azure_key_config": {
                    "endpoint": "env.AZURE_ENDPOINT",
                    "deployments": {
                        "gpt-4o": "gpt-4o-deployment",
                        "gpt-4o-mini": "gpt-4o-mini-deployment"
                    },
                    "api_version": "2024-08-01-preview"
                }
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "azure": {
                "keys": [
                    {
                        "name": "azure-key-1",
                        "value": "env.AZURE_API_KEY",
                        "models": ["gpt-4o", "gpt-4o-mini"],
                        "weight": 1.0,
                        "azure_key_config": {
                            "endpoint": "env.AZURE_ENDPOINT",
                            "deployments": {
                                "gpt-4o": "gpt-4o-deployment",
                                "gpt-4o-mini": "gpt-4o-mini-deployment"
                            },
                            "api_version": "2024-08-01-preview"
                        }
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

<Note>
  If `client_id`, `client_secret`, and `tenant_id` are configured, Service Principal authentication is used. Otherwise, direct authentication with the `value` field is used.
</Note>

### AWS Bedrock

AWS Bedrock supports both explicit credentials and IAM role authentication:

<Tabs group="bedrock-auth">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=739f6946560b27b7a26e1fe480b97b31" alt="AWS Bedrock Configuration Interface" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-bedrock-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=280&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=f7c8c6a960850a69eed26d4199c31461 280w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=560&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=cd25c8fa6947f0af6d0b71b9d785f054 560w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=840&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=cea0ef54cd352894af64dd33fdd2350f 840w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=1100&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=26fbfe901a4e08e5d1a823587d48d96a 1100w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=1650&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=6f73cc27155dda6aa825d126b3300a1d 1650w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-bedrock-config.png?w=2500&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=94f253c3d53a43b541aea075f683574c 2500w" />

    1. Navigate to **"Model Providers"** → **"AWS Bedrock"**
    2. Set **API Key**: AWS API Key (or leave empty if using IAM role authentication)
    3. Set **Access Key**: AWS Access Key ID (or leave empty to use IAM in environment)
    4. Set **Secret Key**: AWS Secret Access Key (or leave empty to use IAM in environment)
    5. Set **Region**: e.g., `us-east-1`
    6. Configure **Deployments**: Map model names to inference profiles
    7. Set **ARN**: Required for deployments mapping
    8. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "bedrock",
        "keys": [
            {
                "name": "bedrock-key-1",
                "models": ["anthropic.claude-3-sonnet-20240229-v1:0", "anthropic.claude-v2:1"],
                "weight": 1.0,
                "bedrock_key_config": {
                    "access_key": "env.AWS_ACCESS_KEY_ID",
                    "secret_key": "env.AWS_SECRET_ACCESS_KEY",
                    "session_token": "env.AWS_SESSION_TOKEN",
                    "region": "us-east-1",
                    "deployments": {
                        "claude-3-sonnet": "us.anthropic.claude-3-sonnet-20240229-v1:0"
                    },
                    "arn": "arn:aws:bedrock:us-east-1:123456789012:inference-profile"
                }
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "bedrock": {
                "keys": [
                    {
                        "name": "bedrock-key-1",
                        "models": ["anthropic.claude-3-sonnet-20240229-v1:0", "anthropic.claude-v2:1"],
                        "weight": 1.0,
                        "bedrock_key_config": {
                            "access_key": "env.AWS_ACCESS_KEY_ID",
                            "secret_key": "env.AWS_SECRET_ACCESS_KEY",
                            "session_token": "env.AWS_SESSION_TOKEN",
                            "region": "us-east-1",
                            "deployments": {
                                "claude-3-sonnet": "us.anthropic.claude-3-sonnet-20240229-v1:0"
                            },
                            "arn": "arn:aws:bedrock:us-east-1:123456789012:inference-profile"
                        }
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

**Notes:**

* If using API Key authentication, set `value` field to the API key, else leave it empty for IAM role authentication.
* In IAM role authentication, if both `access_key` and `secret_key` are empty, Bifrost uses IAM role authentication from the environment.
* `arn` is required for URL formation - `deployments` mapping is ignored without it.
* When using `arn` + `deployments`, Bifrost uses model profiles; otherwise forms path with incoming model name directly.

### Google Vertex

Google Vertex requires project configuration and authentication credentials:

<Tabs group="vertex-auth">
  <Tab title="Using Web UI">
        <img src="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=e3fff8f539e76191e7e3c9a731e13e3e" alt="Google Vertex Configuration Interface" data-og-width="4308" width="4308" data-og-height="2628" height="2628" data-path="media/ui-vertex-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=280&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=147dab9a1409041f60545cff7d160a8b 280w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=560&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=a964d67ca626004fed79d20b1bb8c0f8 560w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=840&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=261bda1043a87f22f6212f4010559fc9 840w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=1100&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=fb87e42e9a411d3b9c11ed58f2e38b77 1100w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=1650&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=dc696a466321fa7fb132b2de1db4e022 1650w, https://mintcdn.com/bifrost/pkxFwnRqDiNNj2Yw/media/ui-vertex-config.png?w=2500&fit=max&auto=format&n=pkxFwnRqDiNNj2Yw&q=85&s=5cc0f7cf0888d05699591be09448b9bc 2500w" />

    1. Navigate to **"Model Providers"** → **"Google Vertex"**
    2. Set **API Key**: Your Vertex API key
    3. Set **Project ID**: Your Google Cloud project ID
    4. Set **Region**: e.g., `us-central1`
    5. Set **Auth Credentials**: Service account credentials JSON
    6. Save configuration
  </Tab>

  <Tab title="Using API">
    ```bash  theme={null}
    curl --location 'http://localhost:8080/api/providers' \
    --header 'Content-Type: application/json' \
    --data '{
        "provider": "vertex",
        "keys": [
            {
                "name": "vertex-key-1",
                "value": "env.VERTEX_API_KEY",
                "models": ["gemini-pro", "gemini-pro-vision"],
                "weight": 1.0,
                "vertex_key_config": {
                    "project_id": "env.VERTEX_PROJECT_ID",
                    "region": "us-central1",
                    "auth_credentials": "env.VERTEX_CREDENTIALS",
                    "deployments": {
                        "fine-tuned-gemini-2.5-pro": "123456789"
                    }
                }
            }
        ]
    }'
    ```
  </Tab>

  <Tab title="Using config.json">
    ```json  theme={null}
    {
        "providers": {
            "vertex": {
                "keys": [
                    {
                        "name": "vertex-key-1",
                        "value": "env.VERTEX_API_KEY",
                        "models": ["gemini-pro", "gemini-pro-vision"],
                        "weight": 1.0,
                        "vertex_key_config": {
                            "project_id": "env.VERTEX_PROJECT_ID",
                            "region": "us-central1",
                            "auth_credentials": "env.VERTEX_CREDENTIALS",
                            "deployments": {
                                "fine-tuned-gemini-2.5-pro": "123456789"
                            }
                        }
                    }
                ]
            }
        }
    }
    ```
  </Tab>
</Tabs>

**Notes:**

* You can leave both API Key and Auth Credentials empty to use service account authentication from the environment.
* You must set Project Number in Key config if using fine-tuned models.
* API Key Authentication is only supported for Gemini and fine-tuned models.
* You can use custom fine-tuned models by passing `vertex/<your-fine-tuned-model-id>` or `vertex/<model-deployment-alias>` if you have set the deployments in the key config.

<Note>
  Vertex AI support for fine-tuned models is currently in beta. Requests to non-Gemini fine-tuned models may fail, so please test and report any issues.
</Note>

## Next Steps

Now that you understand provider configuration, explore these related topics:

### Essential Topics

* **[Streaming Responses](./streaming)** - Real-time response generation
* **[Tool Calling](./tool-calling)** - Enable AI to use external functions
* **[Multimodal AI](./multimodal)** - Process images, audio, and text
* **[Integrations](./integrations)** - Drop-in compatibility with existing SDKs

### Advanced Topics

* **[Core Features](../../features/)** - Advanced Bifrost capabilities
* **[Architecture](../../architecture/)** - How Bifrost works internally
* **[Deployment](../../deployment-guides)** - Production setup and scaling


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt