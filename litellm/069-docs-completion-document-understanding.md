---
title: Using PDF Input | liteLLM
url: https://docs.litellm.ai/docs/completion/document_understanding
source: sitemap
fetched_at: 2026-01-21T19:44:21.976224059-03:00
rendered_js: false
word_count: 105
summary: This document explains how to send PDF files and other document types to LLM providers using LiteLLM via URLs, base64 encoding, or file IDs. It includes instructions for checking model support and configuring specific document formats for multi-modal interactions.
tags:
    - litellm
    - pdf-input
    - multimodal-llm
    - chat-completions
    - python-sdk
    - document-analysis
category: tutorial
---

How to send / receive pdf's (other document types) to a `/chat/completions` endpoint

Works for:

- Vertex AI models (Gemini + Anthropic)
- Bedrock Models
- Anthropic API Models
- OpenAI API Models
- Mistral (Only using file ID of already uploaded file, similar to OpenAI file\_id input)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### url[​](#url "Direct link to url")

- SDK
- PROXY

```
from litellm.utils import supports_pdf_input, completion

# set aws credentials
os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""


# pdf url
file_url ="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# model
model ="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"

file_content =[
{"type":"text","text":"What's this file about?"},
{
"type":"file",
"file":{
"file_id": file_url,
}
},
]


ifnot supports_pdf_input(model,None):
print("Model does not support image input")

response = completion(
    model=model,
    messages=[{"role":"user","content": file_content}],
)
assert response isnotNone
```

### base64[​](#base64 "Direct link to base64")

- SDK
- PROXY

```
from litellm.utils import supports_pdf_input, completion

# set aws credentials
os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""


# pdf url
image_url ="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
response = requests.get(url)
file_data = response.content

encoded_file = base64.b64encode(file_data).decode("utf-8")
base64_url =f"data:application/pdf;base64,{encoded_file}"

# model
model ="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"

file_content =[
{"type":"text","text":"What's this file about?"},
{
"type":"file",
"file":{
"file_data": base64_url,
}
},
]


ifnot supports_pdf_input(model,None):
print("Model does not support image input")

response = completion(
    model=model,
    messages=[{"role":"user","content": file_content}],
)
assert response isnotNone
```

## Specifying format[​](#specifying-format "Direct link to Specifying format")

To specify the format of the document, you can use the `format` parameter.

- SDK
- PROXY

```
from litellm.utils import supports_pdf_input, completion

# set aws credentials
os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]=""


# pdf url
file_url ="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# model
model ="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"

file_content =[
{"type":"text","text":"What's this file about?"},
{
"type":"file",
"file":{
"file_id": file_url,
"format":"application/pdf",
}
},
]


ifnot supports_pdf_input(model,None):
print("Model does not support image input")

response = completion(
    model=model,
    messages=[{"role":"user","content": file_content}],
)
assert response isnotNone
```

## Mistral Example[​](#mistral-example "Direct link to Mistral Example")

Here is a sample payload for using the Mistral model for document understanding:

- SDK
- PROXY

```
from litellm.utils import completion

# pdf file_id received from files endpoint
file_id ="fa778e5e-46ec-4562-8418-36623fe25a71"

# model
model ="mistral/mistral-large-latest"

file_content =[
{"type":"text","text":"What's this file about?"},
{
"type":"file",
"file":{
"file_id": file_id,
}
},
]

response = completion(
    model=model,
    messages=[{"role":"user","content": file_content}],
)
assert response isnotNone
```

## Checking if a model supports pdf input[​](#checking-if-a-model-supports-pdf-input "Direct link to Checking if a model supports pdf input")

- SDK
- PROXY

Use `litellm.supports_pdf_input(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0")` -&gt; returns `True` if model can accept pdf input

```
assert litellm.supports_pdf_input(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0")==True
```