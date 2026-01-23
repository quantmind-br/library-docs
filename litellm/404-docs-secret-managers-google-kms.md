---
title: Google Key Management Service | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/google_kms
source: sitemap
fetched_at: 2026-01-21T19:54:45.135968277-03:00
rendered_js: false
word_count: 32
summary: This guide explains how to configure and use Google KMS for managing encrypted environment variables and database URLs within the LiteLLM proxy server.
tags:
    - google-kms
    - litellm
    - encryption
    - proxy-configuration
    - security
    - key-management
category: guide
---

Use encrypted keys from Google KMS on the proxy

Step 1. Add keys to env

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"
export GOOGLE_KMS_RESOURCE_NAME="projects/*/locations/*/keyRings/*/cryptoKeys/*"
export PROXY_DATABASE_URL_ENCRYPTED=b'\n$\x00D\xac\xb4/\x8e\xc...'
```

Step 2: Update Config

```
general_settings:
key_management_system:"google_kms"
database_url:"os.environ/PROXY_DATABASE_URL_ENCRYPTED"
master_key: sk-1234
```

Step 3: Start + test proxy

```
$ litellm --config /path/to/config.yaml
```

And in another terminal

[Quick Test Proxy](https://docs.litellm.ai/docs/proxy/user_keys)