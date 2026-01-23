---
title: /containers | liteLLM
url: https://docs.litellm.ai/docs/containers
source: sitemap
fetched_at: 2026-01-21T19:44:55.37966941-03:00
rendered_js: false
word_count: 338
summary: This document explains how to manage isolated OpenAI code interpreter sessions using LiteLLM's SDK, Proxy server, and compatible OpenAI client integrations.
tags:
    - litellm
    - openai
    - code-interpreter
    - container-management
    - python-sdk
    - api-proxy
    - isolated-execution
category: guide
---

Manage OpenAI code interpreter containers (sessions) for executing code in isolated environments.

FeatureSupportedCost Tracking✅Logging✅ (Full request/response logging)Load Balancing✅Proxy Server Support✅ Full proxy integration with virtual keysSpend Management✅ Budget tracking and rate limitingSupported Providers`openai`

tip

Containers provide isolated execution environments for code interpreter sessions. You can create, list, retrieve, and delete containers.

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

**Create a Container**

```
import litellm
import os 

# setup env
os.environ["OPENAI_API_KEY"]="sk-.."

container = litellm.create_container(
    name="My Code Interpreter Container",
    custom_llm_provider="openai",
    expires_after={
"anchor":"last_active_at",
"minutes":20
}
)

print(f"Container ID: {container.id}")
print(f"Container Name: {container.name}")
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import acreate_container
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

container =await acreate_container(
    name="My Code Interpreter Container",
    custom_llm_provider="openai",
    expires_after={
"anchor":"last_active_at",
"minutes":20
}
)

print(f"Container ID: {container.id}")
print(f"Container Name: {container.name}")
```

### List Containers[​](#list-containers "Direct link to List Containers")

```
from litellm import list_containers
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

containers = list_containers(
    custom_llm_provider="openai",
    limit=20,
    order="desc"
)

print(f"Found {len(containers.data)} containers")
for container in containers.data:
print(f"  - {container.id}: {container.name}")
```

**Async Usage:**

```
from litellm import alist_containers

containers =await alist_containers(
    custom_llm_provider="openai",
    limit=20,
    order="desc"
)

print(f"Found {len(containers.data)} containers")
for container in containers.data:
print(f"  - {container.id}: {container.name}")
```

### Retrieve a Container[​](#retrieve-a-container "Direct link to Retrieve a Container")

```
from litellm import retrieve_container
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

container = retrieve_container(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)

print(f"Container: {container.name}")
print(f"Status: {container.status}")
print(f"Created: {container.created_at}")
```

**Async Usage:**

```
from litellm import aretrieve_container

container =await aretrieve_container(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)

print(f"Container: {container.name}")
print(f"Status: {container.status}")
print(f"Created: {container.created_at}")
```

### Delete a Container[​](#delete-a-container "Direct link to Delete a Container")

```
from litellm import delete_container
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

result = delete_container(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)

print(f"Deleted: {result.deleted}")
print(f"Container ID: {result.id}")
```

**Async Usage:**

```
from litellm import adelete_container

result =await adelete_container(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)

print(f"Deleted: {result.deleted}")
print(f"Container ID: {result.id}")
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides OpenAI API compatible container endpoints for managing code interpreter sessions:

- `/v1/containers` - Create and list containers
- `/v1/containers/{container_id}` - Retrieve and delete containers

**Setup**

```
$ export OPENAI_API_KEY="sk-..."

$ litellm

# RUNNING on http://0.0.0.0:4000
```

**Custom Provider Specification**

You can specify the custom LLM provider in multiple ways (priority order):

1. Header: `-H "custom-llm-provider: openai"`
2. Query param: `?custom_llm_provider=openai`
3. Request body: `{"custom_llm_provider": "openai", ...}`
4. Defaults to "openai" if not specified

**Create a Container**

```
# Default provider (openai)
curl -X POST "http://localhost:4000/v1/containers" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "My Container",
        "expires_after": {
            "anchor": "last_active_at",
            "minutes": 20
        }
    }'
```

```
# Via header
curl -X POST "http://localhost:4000/v1/containers" \
    -H "Authorization: Bearer sk-1234" \
    -H "custom-llm-provider: openai" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "My Container"
    }'
```

```
# Via query parameter
curl -X POST "http://localhost:4000/v1/containers?custom_llm_provider=openai" \
    -H "Authorization: Bearer sk-1234" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "My Container"
    }'
```

**List Containers**

```
curl "http://localhost:4000/v1/containers?limit=20&order=desc" \
    -H "Authorization: Bearer sk-1234"
```

**Retrieve a Container**

```
curl "http://localhost:4000/v1/containers/cntr_123..." \
    -H "Authorization: Bearer sk-1234"
```

**Delete a Container**

```
curl -X DELETE "http://localhost:4000/v1/containers/cntr_123..." \
    -H "Authorization: Bearer sk-1234"
```

## **Using OpenAI Client with LiteLLM Proxy**[​](#using-openai-client-with-litellm-proxy "Direct link to using-openai-client-with-litellm-proxy")

You can use the standard OpenAI Python client to interact with LiteLLM's container endpoints. This provides a familiar interface while leveraging LiteLLM's proxy features.

### Setup[​](#setup "Direct link to Setup")

First, configure your OpenAI client to point to your LiteLLM proxy:

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",# Your LiteLLM proxy key
    base_url="http://localhost:4000"# LiteLLM proxy URL
)
```

### Create a Container[​](#create-a-container "Direct link to Create a Container")

```
container = client.containers.create(
    name="test-container",
    expires_after={
"anchor":"last_active_at",
"minutes":20
},
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Container ID: {container.id}")
print(f"Container Name: {container.name}")
print(f"Created at: {container.created_at}")
```

### List Containers[​](#list-containers-1 "Direct link to List Containers")

```
containers = client.containers.list(
    limit=20,
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Found {len(containers.data)} containers")
for container in containers.data:
print(f"  - {container.id}: {container.name}")
```

### Retrieve a Container[​](#retrieve-a-container-1 "Direct link to Retrieve a Container")

```
container = client.containers.retrieve(
    container_id="cntr_6901d28b3c8881908b702815828a5bde0380b3408aeae8c7",
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Container: {container.name}")
print(f"Status: {container.status}")
print(f"Last active: {container.last_active_at}")
```

### Delete a Container[​](#delete-a-container-1 "Direct link to Delete a Container")

```
result = client.containers.delete(
    container_id="cntr_6901d28b3c8881908b702815828a5bde0380b3408aeae8c7",
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Deleted: {result.deleted}")
print(f"Container ID: {result.id}")
```

### Complete Workflow Example[​](#complete-workflow-example "Direct link to Complete Workflow Example")

Here's a complete example showing the full container management workflow:

```
from openai import OpenAI

# Initialize client
client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

# 1. Create a container
print("Creating container...")
container = client.containers.create(
    name="My Code Interpreter Session",
    expires_after={
"anchor":"last_active_at",
"minutes":20
},
    extra_body={"custom_llm_provider":"openai"}
)

container_id = container.id
print(f"Container created. ID: {container_id}")

# 2. List all containers
print("\nListing containers...")
containers = client.containers.list(
    extra_body={"custom_llm_provider":"openai"}
)

for c in containers.data:
print(f"  - {c.id}: {c.name} (Status: {c.status})")

# 3. Retrieve specific container
print(f"\nRetrieving container {container_id}...")
retrieved = client.containers.retrieve(
    container_id=container_id,
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Container: {retrieved.name}")
print(f"Status: {retrieved.status}")
print(f"Last active: {retrieved.last_active_at}")

# 4. Delete container
print(f"\nDeleting container {container_id}...")
result = client.containers.delete(
    container_id=container_id,
    extra_body={"custom_llm_provider":"openai"}
)

print(f"Deleted: {result.deleted}")
```

## Container Parameters[​](#container-parameters "Direct link to Container Parameters")

### Create Container Parameters[​](#create-container-parameters "Direct link to Create Container Parameters")

ParameterTypeRequiredDescription`name`stringYesName of the container`expires_after`objectNoContainer expiration settings`expires_after.anchor`stringNoAnchor point for expiration (e.g., "last\_active\_at")`expires_after.minutes`integerNoMinutes until expiration from anchor`file_ids`arrayNoList of file IDs to include in the container`custom_llm_provider`stringNoLLM provider to use (default: "openai")

### List Container Parameters[​](#list-container-parameters "Direct link to List Container Parameters")

ParameterTypeRequiredDescription`after`stringNoCursor for pagination`limit`integerNoNumber of items to return (1-100, default: 20)`order`stringNoSort order: "asc" or "desc" (default: "desc")`custom_llm_provider`stringNoLLM provider to use (default: "openai")

### Retrieve/Delete Container Parameters[​](#retrievedelete-container-parameters "Direct link to Retrieve/Delete Container Parameters")

ParameterTypeRequiredDescription`container_id`stringYesID of the container to retrieve/delete`custom_llm_provider`stringNoLLM provider to use (default: "openai")

## Response Objects[​](#response-objects "Direct link to Response Objects")

### ContainerObject[​](#containerobject "Direct link to ContainerObject")

```
{
"id":"cntr_123...",
"object":"container",
"created_at":1234567890,
"name":"My Container",
"status":"active",
"last_active_at":1234567890,
"expires_at":1234569090,
"file_ids":[]
}
```

### ContainerListResponse[​](#containerlistresponse "Direct link to ContainerListResponse")

```
{
"object":"list",
"data":[
{
"id":"cntr_123...",
"object":"container",
"created_at":1234567890,
"name":"My Container",
"status":"active"
}
],
"first_id":"cntr_123...",
"last_id":"cntr_456...",
"has_more":false
}
```

### DeleteContainerResult[​](#deletecontainerresult "Direct link to DeleteContainerResult")

```
{
"id":"cntr_123...",
"object":"container.deleted",
"deleted":true
}
```

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderSupport StatusNotesOpenAI✅ SupportedFull support for all container operations

info

Currently, only OpenAI supports container management for code interpreter sessions. Support for additional providers may be added in the future.

- [Container Files API](https://docs.litellm.ai/docs/container_files) - Manage files within containers
- [Code Interpreter Guide](https://docs.litellm.ai/docs/guides/code_interpreter) - Using Code Interpreter with LiteLLM