---
title: Google Secret Manager | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/google_secret_manager
source: sitemap
fetched_at: 2026-01-21T19:54:45.388547132-03:00
rendered_js: false
word_count: 31
summary: This document explains how to configure and integrate Google Secret Manager as a key management system for the LiteLLM proxy.
tags:
    - google-secret-manager
    - litellm-proxy
    - key-management
    - security-configuration
    - environment-variables
category: configuration
---

Support for [Google Secret Manager](https://cloud.google.com/security/products/secret-manager)

1. Save Google Secret Manager details in your environment

```
GOOGLE_SECRET_MANAGER_PROJECT_ID="your-project-id-on-gcp" # example: adroit-crow-413218
```

Optional Params

```
export GOOGLE_SECRET_MANAGER_REFRESH_INTERVAL = ""            # (int) defaults to 86400
export GOOGLE_SECRET_MANAGER_ALWAYS_READ_SECRET_MANAGER = ""  # (str) set to "true" if you want to always read from google secret manager without using in memory caching. NOT RECOMMENDED in PROD
```

2. Add to proxy config.yaml

```
model_list:
-model_name: fake-openai-endpoint
litellm_params:
model: openai/fake
api_base: https://exampleopenaiendpoint-production.up.railway.app/
api_key: os.environ/OPENAI_API_KEY # this will be read from Google Secret Manager

general_settings:
key_management_system:"google_secret_manager"
```

You can now test this by starting your proxy:

```
litellm --config /path/to/config.yaml
```

[Quick Test Proxy](https://docs.litellm.ai/docs/proxy/quick_start#using-litellm-proxy---curl-request-openai-package-langchain-langchain-js)