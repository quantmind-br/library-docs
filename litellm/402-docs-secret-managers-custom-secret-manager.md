---
title: Custom Secret Manager | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/custom_secret_manager
source: sitemap
fetched_at: 2026-01-21T19:54:42.178700313-03:00
rendered_js: false
word_count: 187
summary: This document provides instructions for integrating custom secret management systems with LiteLLM by implementing a Python class and updating proxy configurations.
tags:
    - litellm
    - secret-management
    - custom-integration
    - python
    - proxy-configuration
    - security
category: guide
---

Integrate your custom secret management system with LiteLLM.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### 1. Create Your Secret Manager Class[​](#1-create-your-secret-manager-class "Direct link to 1. Create Your Secret Manager Class")

Create a new file `my_secret_manager.py` with an in-memory secret store:

my\_secret\_manager.py

```
from typing import Optional, Union
import httpx
from litellm.integrations.custom_secret_manager import CustomSecretManager

classInMemorySecretManager(CustomSecretManager):
def__init__(self):
super().__init__(secret_manager_name="in_memory_secrets")
# Store your secrets in memory
        self.secrets ={
"OPENAI_API_KEY":"sk-...",
"ANTHROPIC_API_KEY":"sk-ant-...",
}

asyncdefasync_read_secret(
        self,
        secret_name:str,
        optional_params: Optional[dict]=None,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
)-> Optional[str]:
"""Read secret asynchronously"""
return self.secrets.get(secret_name)

defsync_read_secret(
        self,
        secret_name:str,
        optional_params: Optional[dict]=None,
        timeout: Optional[Union[float, httpx.Timeout]]=None,
)-> Optional[str]:
"""Read secret synchronously"""
return self.secrets.get(secret_name)
```

### 2. Configure Proxy[​](#2-configure-proxy "Direct link to 2. Configure Proxy")

Reference your custom secret manager in `config.yaml`:

config.yaml

```
general_settings:
master_key: os.environ/LITELLM_MASTER_KEY
key_management_system: custom  # 👈 KEY CHANGE
key_management_settings:
custom_secret_manager: my_secret_manager.InMemorySecretManager  # 👈 KEY CHANGE

model_list:
-model_name: gpt-4
litellm_params:
model: openai/gpt-4
api_key: os.environ/OPENAI_API_KEY  # Read from custom secret manager
```

### 3. Start LiteLLM Proxy[​](#3-start-litellm-proxy "Direct link to 3. Start LiteLLM Proxy")

- Docker
- Python Package

Mount your custom secret manager file on the container:

```
docker run -d \
  -p 4000:4000 \
  -e LITELLM_MASTER_KEY=$LITELLM_MASTER_KEY \
  --name litellm-proxy \
  -v $(pwd)/config.yaml:/app/config.yaml \
  -v $(pwd)/my_secret_manager.py:/app/my_secret_manager.py \
  docker.litellm.ai/berriai/litellm:main-latest \
  --config /app/config.yaml \
  --port 4000 \
  --detailed_debug
```

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

Customize secret manager behavior in your `config.yaml`:

- Read Keys Only
- Store Virtual Keys
- Read + Write

config.yaml

```
general_settings:
key_management_system: custom
key_management_settings:
custom_secret_manager: my_secret_manager.InMemorySecretManager
hosted_keys:["OPENAI_API_KEY","ANTHROPIC_API_KEY"]# Only check these keys
```

### Available Settings[​](#available-settings "Direct link to Available Settings")

SettingDescriptionDefault`custom_secret_manager`Path to your custom secret manager classRequired`access_mode``"read_only"`, `"write_only"`, or `"read_and_write"``"read_only"``hosted_keys`List of specific keys to check in secret managerAll keys`store_virtual_keys`Store LiteLLM virtual keys in secret manager`false``prefix_for_stored_virtual_keys`Prefix for stored virtual keys`"litellm/"``description`Description for stored secrets`None``tags`Tags to apply to stored secrets`None`

## Required Methods[​](#required-methods "Direct link to Required Methods")

Your custom secret manager **must** implement these two methods:

### `async_read_secret()`[​](#async_read_secret "Direct link to async_read_secret")

```
asyncdefasync_read_secret(
    self,
    secret_name:str,
    optional_params: Optional[dict]=None,
    timeout: Optional[Union[float, httpx.Timeout]]=None,
)-> Optional[str]:
"""
    Read a secret asynchronously.

    Returns:
        Secret value if found, None otherwise
    """
pass
```

### `sync_read_secret()`[​](#sync_read_secret "Direct link to sync_read_secret")

```
defsync_read_secret(
    self,
    secret_name:str,
    optional_params: Optional[dict]=None,
    timeout: Optional[Union[float, httpx.Timeout]]=None,
)-> Optional[str]:
"""
    Read a secret synchronously.

    Returns:
        Secret value if found, None otherwise
    """
pass
```

## Optional Methods[​](#optional-methods "Direct link to Optional Methods")

Implement these for additional functionality:

### `async_write_secret()`[​](#async_write_secret "Direct link to async_write_secret")

```
asyncdefasync_write_secret(
    self,
    secret_name:str,
    secret_value:str,
    description: Optional[str]=None,
    optional_params: Optional[dict]=None,
    timeout: Optional[Union[float, httpx.Timeout]]=None,
    tags: Optional[Union[dict,list]]=None,
)->dict:
"""Write a secret to your secret manager"""
pass
```

### `async_delete_secret()`[​](#async_delete_secret "Direct link to async_delete_secret")

```
asyncdefasync_delete_secret(
    self,
    secret_name:str,
    recovery_window_in_days: Optional[int]=7,
    optional_params: Optional[dict]=None,
    timeout: Optional[Union[float, httpx.Timeout]]=None,
)->dict:
"""Delete a secret from your secret manager"""
pass
```

## Use Cases[​](#use-cases "Direct link to Use Cases")

✅ Proprietary vault systems  
✅ Custom authentication (mTLS, OAuth)  
✅ Organization-specific security policies  
✅ Legacy secret storage systems  
✅ Multi-region secret replication  
✅ Secret versioning and rotation  
✅ Compliance requirements (HIPAA, SOC2)

## Example[​](#example "Direct link to Example")

See [cookbook/litellm\_proxy\_server/secret\_manager/my\_secret\_manager.py](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_proxy_server/secret_manager/my_secret_manager.py) for a complete working example with:

- In-memory secret manager implementation
- Integration with LiteLLM Proxy
- Read, write, and delete operations