---
title: /containers/files | liteLLM
url: https://docs.litellm.ai/docs/container_files
source: sitemap
fetched_at: 2026-01-21T19:44:53.100991827-03:00
rendered_js: false
word_count: 224
summary: This document provides a comprehensive guide and API reference for managing files within Code Interpreter containers using the LiteLLM SDK and Proxy. It details endpoints and methods for uploading, listing, retrieving, and deleting files associated with container sessions.
tags:
    - litellm
    - code-interpreter
    - file-management
    - api-reference
    - python-sdk
    - container-files
    - openai-compatibility
category: reference
---

Manage files within Code Interpreter containers. Files are created automatically when code interpreter generates outputs (charts, CSVs, images, etc.).

FeatureSupportedCost Tracking✅Logging✅Supported Providers`openai`

## Endpoints[​](#endpoints "Direct link to Endpoints")

EndpointMethodDescription`/v1/containers/{container_id}/files`POSTUpload file to container`/v1/containers/{container_id}/files`GETList files in container`/v1/containers/{container_id}/files/{file_id}`GETGet file metadata`/v1/containers/{container_id}/files/{file_id}/content`GETDownload file content`/v1/containers/{container_id}/files/{file_id}`DELETEDelete file

## LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

### Upload Container File[​](#upload-container-file "Direct link to Upload Container File")

Upload files directly to a container session. This is useful when `/chat/completions` or `/responses` sends files to the container but the input file type is limited to PDF. This endpoint lets you work with other file types like CSV, Excel, Python scripts, etc.

upload\_container\_file.py

```
from litellm import upload_container_file

# Upload a CSV file
file= upload_container_file(
    container_id="cntr_123...",
file=("data.csv",open("data.csv","rb").read(),"text/csv"),
    custom_llm_provider="openai"
)

print(f"Uploaded: {file.id}")
print(f"Path: {file.path}")
```

**Async:**

aupload\_container\_file.py

```
from litellm import aupload_container_file

file=await aupload_container_file(
    container_id="cntr_123...",
file=("script.py",b"print('hello world')","text/x-python"),
    custom_llm_provider="openai"
)
```

**Supported file formats:**

- CSV (`.csv`)
- Excel (`.xlsx`)
- Python scripts (`.py`)
- JSON (`.json`)
- Markdown (`.md`)
- Text files (`.txt`)
- And more...

### List Container Files[​](#list-container-files "Direct link to List Container Files")

list\_container\_files.py

```
from litellm import list_container_files

files = list_container_files(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)

forfilein files.data:
print(f"  - {file.id}: {file.filename}")
```

**Async:**

alist\_container\_files.py

```
from litellm import alist_container_files

files =await alist_container_files(
    container_id="cntr_123...",
    custom_llm_provider="openai"
)
```

### Retrieve Container File[​](#retrieve-container-file "Direct link to Retrieve Container File")

retrieve\_container\_file.py

```
from litellm import retrieve_container_file

file= retrieve_container_file(
    container_id="cntr_123...",
    file_id="cfile_456...",
    custom_llm_provider="openai"
)

print(f"File: {file.filename}")
print(f"Size: {file.bytes} bytes")
```

### Download File Content[​](#download-file-content "Direct link to Download File Content")

retrieve\_container\_file\_content.py

```
from litellm import retrieve_container_file_content

content = retrieve_container_file_content(
    container_id="cntr_123...",
    file_id="cfile_456...",
    custom_llm_provider="openai"
)

# content is raw bytes
withopen("output.png","wb")as f:
    f.write(content)
```

### Delete Container File[​](#delete-container-file "Direct link to Delete Container File")

delete\_container\_file.py

```
from litellm import delete_container_file

result = delete_container_file(
    container_id="cntr_123...",
    file_id="cfile_456...",
    custom_llm_provider="openai"
)

print(f"Deleted: {result.deleted}")
```

## LiteLLM AI Gateway (Proxy)[​](#litellm-ai-gateway-proxy "Direct link to LiteLLM AI Gateway (Proxy)")

### Upload File[​](#upload-file "Direct link to Upload File")

- OpenAI SDK
- curl

upload\_file.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

file= client.containers.files.create(
    container_id="cntr_123...",
file=open("data.csv","rb")
)

print(f"Uploaded: {file.id}")
print(f"Path: {file.path}")
```

### List Files[​](#list-files "Direct link to List Files")

- OpenAI SDK
- curl

list\_files.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

files = client.containers.files.list(
    container_id="cntr_123..."
)

forfilein files.data:
print(f"  - {file.id}: {file.filename}")
```

### Retrieve File Metadata[​](#retrieve-file-metadata "Direct link to Retrieve File Metadata")

- OpenAI SDK
- curl

retrieve\_file.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

file= client.containers.files.retrieve(
    container_id="cntr_123...",
    file_id="cfile_456..."
)

print(f"File: {file.filename}")
print(f"Size: {file.bytes} bytes")
```

### Download File Content[​](#download-file-content-1 "Direct link to Download File Content")

- OpenAI SDK
- curl

download\_content.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

content = client.containers.files.content(
    container_id="cntr_123...",
    file_id="cfile_456..."
)

withopen("output.png","wb")as f:
    f.write(content.read())
```

### Delete File[​](#delete-file "Direct link to Delete File")

- OpenAI SDK
- curl

delete\_file.py

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

result = client.containers.files.delete(
    container_id="cntr_123...",
    file_id="cfile_456..."
)

print(f"Deleted: {result.deleted}")
```

## Parameters[​](#parameters "Direct link to Parameters")

### Upload File[​](#upload-file-1 "Direct link to Upload File")

ParameterTypeRequiredDescription`container_id`stringYesContainer ID`file`FileTypesYesFile to upload. Can be a tuple of (filename, content, content\_type), file-like object, or bytes

### List Files[​](#list-files-1 "Direct link to List Files")

ParameterTypeRequiredDescription`container_id`stringYesContainer ID`after`stringNoPagination cursor`limit`integerNoItems to return (1-100, default: 20)`order`stringNoSort order: `asc` or `desc`

### Retrieve/Delete File[​](#retrievedelete-file "Direct link to Retrieve/Delete File")

ParameterTypeRequiredDescription`container_id`stringYesContainer ID`file_id`stringYesFile ID

## Response Objects[​](#response-objects "Direct link to Response Objects")

### ContainerFileObject[​](#containerfileobject "Direct link to ContainerFileObject")

ContainerFileObject

```
{
"id":"cfile_456...",
"object":"container.file",
"container_id":"cntr_123...",
"bytes":12345,
"created_at":1234567890,
"filename":"chart.png",
"path":"/mnt/data/chart.png",
"source":"code_interpreter"
}
```

### ContainerFileListResponse[​](#containerfilelistresponse "Direct link to ContainerFileListResponse")

ContainerFileListResponse

```
{
"object":"list",
"data":[...],
"first_id":"cfile_456...",
"last_id":"cfile_789...",
"has_more":false
}
```

### DeleteContainerFileResponse[​](#deletecontainerfileresponse "Direct link to DeleteContainerFileResponse")

DeleteContainerFileResponse

```
{
"id":"cfile_456...",
"object":"container.file.deleted",
"deleted":true
}
```

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

ProviderStatusOpenAI✅ Supported

- [Containers API](https://docs.litellm.ai/docs/containers) - Manage containers
- [Code Interpreter Guide](https://docs.litellm.ai/docs/guides/code_interpreter) - Using Code Interpreter with LiteLLM