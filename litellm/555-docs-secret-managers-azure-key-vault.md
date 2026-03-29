---
title: Azure Key Vault | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/azure_key_vault
source: sitemap
fetched_at: 2026-01-21T19:54:40.366005749-03:00
rendered_js: false
word_count: 30
summary: This document provides instructions for configuring the LiteLLM Proxy Server to use Azure Key Vault for managing API keys and secrets. It covers installation, environment setup, and the necessary configuration file parameters.
tags:
    - litellm
    - proxy-server
    - azure-key-vault
    - secrets-management
    - configuration
category: configuration
---

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

1. Install Proxy dependencies

```
pip install 'litellm[proxy]' 'litellm[extra_proxy]'
```

2. Save Azure details in your environment

```
export["AZURE_CLIENT_ID"]="your-azure-app-client-id"
export["AZURE_CLIENT_SECRET"]="your-azure-app-client-secret"
export["AZURE_TENANT_ID"]="your-azure-tenant-id"
export["AZURE_KEY_VAULT_URI"]="your-azure-key-vault-uri"
```

3. Add to proxy config.yaml

```
model_list:
-model_name:"my-azure-models"# model alias 
litellm_params:
model:"azure/<your-deployment-name>"
api_key:"os.environ/AZURE-API-KEY"# reads from key vault - get_secret("AZURE_API_KEY")
api_base:"os.environ/AZURE-API-BASE"# reads from key vault - get_secret("AZURE_API_BASE")

general_settings:
key_management_system:"azure_key_vault"
```

You can now test this by starting your proxy:

```
litellm --config /path/to/config.yaml
```

[Quick Test Proxy](https://docs.litellm.ai/docs/proxy/quick_start#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js)