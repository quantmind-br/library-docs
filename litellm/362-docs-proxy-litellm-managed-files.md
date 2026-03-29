---
title: '[BETA] LiteLLM Managed Files | liteLLM'
url: https://docs.litellm.ai/docs/proxy/litellm_managed_files
source: sitemap
fetched_at: 2026-01-21T19:52:47.10099448-03:00
rendered_js: false
word_count: 402
summary: This document explains how to use LiteLLM Enterprise to manage file uploads across multiple AI providers and implement file-level permissions for secure user access.
tags:
    - litellm
    - file-management
    - access-control
    - cross-provider
    - enterprise-features
    - proxy-server
category: guide
---

- Reuse the same file across different providers.
- Prevent users from seeing files they don't have access to on `list` and `retrieve` calls.

info

This is a free LiteLLM Enterprise feature.

Available via the `litellm[proxy]` package or any `litellm` docker image.

PropertyValueCommentsProxy✅SDK❌Requires postgres DB for storing file ids.Available across all providers✅Supported endpoints`/chat/completions`, `/batch`, `/fine_tuning`, `/responses`

## Usage[​](#usage "Direct link to Usage")

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name:"gemini-2.0-flash"
litellm_params:
model: vertex_ai/gemini-2.0-flash
vertex_project: my-project-id
vertex_location: us-central1
-model_name:"gpt-4o-mini-openai"
litellm_params:
model: gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY

general_settings:
master_key: sk-1234# alternatively use the env var - LITELLM_MASTER_KEY
database_url:"postgresql://<user>:<password>@<host>:<port>/<dbname>"# alternatively use the env var - DATABASE_URL
```

### 2. Start proxy[​](#2-start-proxy "Direct link to 2. Start proxy")

```
litellm --config /path/to/config.yaml
```

### 3. Test it\![​](#3-test-it "Direct link to 3. Test it!")

Specify `target_model_names` to use the same file id across different providers. This is the list of model\_names set via config.yaml (or 'public\_model\_names' on UI).

```
target_model_names="gpt-4o-mini-openai, gemini-2.0-flash"# 👈 Specify model_names
```

Check `/v1/models` to see the list of available model names for a key.

#### **Store a PDF file**[​](#store-a-pdf-file "Direct link to store-a-pdf-file")

```
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)


# Download and save the PDF locally 
url =(
"https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"
)
response = requests.get(url)
response.raise_for_status()

# Save the PDF locally
withopen("2403.05530.pdf","wb")as f:
    f.write(response.content)

file= client.files.create(
file=open("2403.05530.pdf","rb"),
    purpose="user_data",# can be any openai 'purpose' value
    extra_body={"target_model_names":"gpt-4o-mini-openai, gemini-2.0-flash"},# 👈 Specify model_names
)

print(f"file id={file.id}")
```

#### **Use the same file id across different providers**[​](#use-the-same-file-id-across-different-providers "Direct link to use-the-same-file-id-across-different-providers")

- OpenAI
- Vertex AI

```
completion = client.chat.completions.create(
    model="gpt-4o-mini-openai",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"What is in this recording?"},
{
"type":"file",
"file":{
"file_id":file.id,
},
},
],
},
]
)

print(completion.choices[0].message)
```

### Complete Example[​](#complete-example "Direct link to Complete Example")

```
import base64
import requests
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)


# Download and save the PDF locally
url =(
"https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"
)
response = requests.get(url)
response.raise_for_status()

# Save the PDF locally
withopen("2403.05530.pdf","wb")as f:
    f.write(response.content)

# Read the local PDF file
file= client.files.create(
file=open("2403.05530.pdf","rb"),
    purpose="user_data",# can be any openai 'purpose' value
    extra_body={"target_model_names":"gpt-4o-mini-openai, vertex_ai/gemini-2.0-flash"},
)

print(f"file.id: {file.id}")# 👈 Unified file id

## GEMINI CALL ### 
completion = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"What is in this recording?"},
{
"type":"file",
"file":{
"file_id":file.id,
},
},
],
},
]
)

print(completion.choices[0].message)


### OPENAI CALL ### 
completion = client.chat.completions.create(
    model="gpt-4o-mini-openai",
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"What is in this recording?"},
{
"type":"file",
"file":{
"file_id":file.id,
},
},
],
},
],
)

print(completion.choices[0].message)

```

## File Permissions[​](#file-permissions "Direct link to File Permissions")

Prevent users from seeing files they don't have access to on `list` and `retrieve` calls.

### 1. Setup config.yaml[​](#1-setup-configyaml-1 "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name:"gpt-4o-mini-openai"
litellm_params:
model: gpt-4o-mini
api_key: os.environ/OPENAI_API_KEY

general_settings:
master_key: sk-1234# alternatively use the env var - LITELLM_MASTER_KEY
database_url:"postgresql://<user>:<password>@<host>:<port>/<dbname>"# alternatively use the env var - DATABASE_URL
```

### 2. Start proxy[​](#2-start-proxy-1 "Direct link to 2. Start proxy")

```
litellm --config /path/to/config.yaml
```

### 3. Issue a key to the user[​](#3-issue-a-key-to-the-user "Direct link to 3. Issue a key to the user")

Let's create a user with the id `user_123`.

```
curl -L -X POST 'http://0.0.0.0:4000/user/new' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{"models": ["gpt-4o-mini-openai"], "user_id": "user_123"}'
```

Get the key from the response.

### 4. User creates a file[​](#4-user-creates-a-file "Direct link to 4. User creates a file")

#### 4a. Create a file[​](#4a-create-a-file "Direct link to 4a. Create a file")

```
{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}
{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who wrote 'Romeo and Juliet'?"}, {"role": "assistant", "content": "Oh, just some guy named William Shakespeare. Ever heard of him?"}]}
```

#### 4b. Upload the file[​](#4b-upload-the-file "Direct link to 4b. Upload the file")

```
from openai import OpenAI

client = OpenAI(
    base_url="http://0.0.0.0:4000",
    api_key="sk-...",# 👈 Use the key you generated in step 3
    max_retries=0
)

# Upload file
finetuning_input_file = client.files.create(
file=open("./fine_tuning.jsonl","rb"),# {"model": "azure-gpt-4o"} <-> {"model": "gpt-4o-my-special-deployment"}
    purpose="fine-tune",
    extra_body={"target_model_names":"gpt-4.1-openai"}# 👈 Tells litellm which regions/projects to write the file in. 
)
print(finetuning_input_file)# file.id = "litellm_proxy/..." = {"model_name": {"deployment_id": "deployment_file_id"}}
```

### 5. User retrieves a file[​](#5-user-retrieves-a-file "Direct link to 5. User retrieves a file")

- User created file
- User did not create file

```
from openai import OpenAI

...# User created file (3b)

file= client.files.retrieve(
    file_id=finetuning_input_file.id
)

print(file)# File retrieved successfully
```

## Supported Endpoints[​](#supported-endpoints "Direct link to Supported Endpoints")

#### Create a file - `/files`[​](#create-a-file---files "Direct link to create-a-file---files")

```
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)

# Download and save the PDF locally
url =(
"https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"
)
response = requests.get(url)
response.raise_for_status()

# Save the PDF locally
withopen("2403.05530.pdf","wb")as f:
    f.write(response.content)

# Read the local PDF file
file= client.files.create(
file=open("2403.05530.pdf","rb"),
    purpose="user_data",# can be any openai 'purpose' value
    extra_body={"target_model_names":"gpt-4o-mini-openai, vertex_ai/gemini-2.0-flash"},
)
```

#### Retrieve a file - `/files/{file_id}`[​](#retrieve-a-file---filesfile_id "Direct link to retrieve-a-file---filesfile_id")

```
client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)

file= client.files.retrieve(file_id=file.id)
```

#### Delete a file - `/files/{file_id}/delete`[​](#delete-a-file---filesfile_iddelete "Direct link to delete-a-file---filesfile_iddelete")

```
client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)

file= client.files.delete(file_id=file.id)
```

#### List files - `/files`[​](#list-files---files "Direct link to list-files---files")

```
client = OpenAI(base_url="http://0.0.0.0:4000", api_key="sk-1234", max_retries=0)

files = client.files.list(extra_body={"target_model_names":"gpt-4o-mini-openai"})

print(files)# All files user has created
```

Pre-GA Limitations on List Files:

- No multi-model support: Just 1 model name is supported for now.
- No multi-deployment support: Just 1 deployment of the model is supported for now (e.g. if you have 2 deployments with the `gpt-4o-mini-openai` public model name, it will pick one and return all files on that deployment).

Pre-GA Limitations will be fixed before GA of the Managed Files feature.

## FAQ[​](#faq "Direct link to FAQ")

**1. Does LiteLLM store the file?**

No, LiteLLM does not store the file. It only stores the file id's in the postgres DB.

**2. How does LiteLLM know which file to use for a given file id?**

LiteLLM stores a mapping of the litellm file id to the model-specific file id in the postgres DB. When a request comes in, LiteLLM looks up the model-specific file id and uses it in the request to the provider.

**3. How do file deletions work?**

When a file is deleted, LiteLLM deletes the mapping from the postgres DB, and the files on each provider.

**4. Can a user call a file id that was created by another user?**

No, as of `v1.71.2` users can only view/edit/delete files they have created.

## Architecture[​](#architecture "Direct link to Architecture")

## See Also[​](#see-also "Direct link to See Also")

- [Managed Files w/ Finetuning APIs](https://docs.litellm.ai/docs/proxy/managed_finetuning)
- [Managed Files w/ Batch APIs](https://docs.litellm.ai/docs/proxy/managed_batches)