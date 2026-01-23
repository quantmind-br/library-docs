---
title: /ocr | liteLLM
url: https://docs.litellm.ai/docs/ocr
source: sitemap
fetched_at: 2026-01-21T19:46:43.14031781-03:00
rendered_js: false
word_count: 195
summary: This document provides technical documentation for implementing Optical Character Recognition (OCR) using LiteLLM, covering Python SDK integration, proxy configuration, and detailed API request and response specifications.
tags:
    - litellm
    - ocr
    - python-sdk
    - api-reference
    - mistral-ai
    - document-processing
category: api
---

FeatureSupportedCost Tracking✅Logging✅ (Basic Logging not supported)Load Balancing✅Supported Providers`mistral`, `azure_ai`, `vertex_ai`

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import ocr
import os

os.environ["MISTRAL_API_KEY"]="sk-.."

response = ocr(
    model="mistral/mistral-ocr-latest",
    document={
"type":"document_url",
"document_url":"https://arxiv.org/pdf/2201.04234"
}
)

# Access extracted text
for page in response.pages:
print(f"Page {page.index}:")
print(page.markdown)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import aocr
import os, asyncio

os.environ["MISTRAL_API_KEY"]="sk-.."

asyncdeftest_async_ocr():
    response =await aocr(
        model="mistral/mistral-ocr-latest",
        document={
"type":"document_url",
"document_url":"https://arxiv.org/pdf/2201.04234"
}
)

# Access extracted text
for page in response.pages:
print(f"Page {page.index}:")
print(page.markdown)

asyncio.run(test_async_ocr())
```

### Using Base64 Encoded Documents[​](#using-base64-encoded-documents "Direct link to Using Base64 Encoded Documents")

```
import base64
from litellm import ocr

# Encode PDF to base64
withopen("document.pdf","rb")as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

response = ocr(
    model="mistral/mistral-ocr-latest",
    document={
"type":"document_url",
"document_url":f"data:application/pdf;base64,{base64_pdf}"
}
)
```

### Optional Parameters[​](#optional-parameters "Direct link to Optional Parameters")

```
response = ocr(
    model="mistral/mistral-ocr-latest",
    document={
"type":"document_url",
"document_url":"https://example.com/doc.pdf"
},
# Optional Mistral parameters
    pages=[0,1,2],# Only process specific pages
    include_image_base64=True,# Include extracted images
    image_limit=10,# Max images to return
    image_min_size=100# Min image size to include
)
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides a Mistral API compatible `/ocr` endpoint for OCR calls.

**Setup**

Add this to your litellm proxy config.yaml

```
model_list:
-model_name: mistral-ocr
litellm_params:
model: mistral/mistral-ocr-latest
api_key: os.environ/MISTRAL_API_KEY
```

Start litellm

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

Test request

```
curl http://0.0.0.0:4000/v1/ocr \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistral-ocr",
    "document": {
        "type": "document_url",
        "document_url": "https://arxiv.org/pdf/2201.04234"
    }
  }'
```

## **Request/Response Format**[​](#requestresponse-format "Direct link to requestresponse-format")

### Example Request[​](#example-request "Direct link to Example Request")

```
{
"model":"mistral/mistral-ocr-latest",
"document":{
"type":"document_url",
"document_url":"https://arxiv.org/pdf/2201.04234"
},
"pages":[0,1,2],# Optional: specific pages to process
"include_image_base64":True,# Optional: include extracted images
"image_limit":10,# Optional: max images to return
"image_min_size":100# Optional: min image size in pixels
}
```

### Request Parameters[​](#request-parameters "Direct link to Request Parameters")

ParameterTypeRequiredDescription`model`stringYesThe OCR model to use (e.g., `"mistral/mistral-ocr-latest"`)`document`objectYesDocument to process. Must contain `type` and URL field`document.type`stringYesEither `"document_url"` for PDFs/docs or `"image_url"` for images`document.document_url`stringConditionalURL to the document (required if `type` is `"document_url"`)`document.image_url`stringConditionalURL to the image (required if `type` is `"image_url"`)`pages`arrayNoList of specific page indices to process (0-indexed)`include_image_base64`booleanNoWhether to include extracted images as base64 strings`image_limit`integerNoMaximum number of images to return`image_min_size`integerNoMinimum size (in pixels) for images to include

#### Document Format Examples[​](#document-format-examples "Direct link to Document Format Examples")

**For PDFs and documents:**

```
{
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
```

**For images:**

```
{
"type":"image_url",
"image_url":"https://example.com/image.png"
}
```

**For base64-encoded content:**

```
{
"type":"document_url",
"document_url":"data:application/pdf;base64,JVBERi0xLjQKJ..."
}
```

### Response Format[​](#response-format "Direct link to Response Format")

The response follows Mistral's OCR format with the following structure:

```
{
"pages":[
{
"index":0,
"markdown":"# Document Title\n\nExtracted text content...",
"dimensions":{
"dpi":200,
"height":2200,
"width":1700
},
"images":[
{
"image_base64":"base64string...",
"bbox":{
"x":100,
"y":200,
"width":300,
"height":400
}
}
]
}
],
"model":"mistral-ocr-2505-completion",
"usage_info":{
"pages_processed":29,
"doc_size_bytes":3002783
},
"document_annotation":null,
"object":"ocr"
}
```

#### Response Fields[​](#response-fields "Direct link to Response Fields")

FieldTypeDescription`pages`arrayList of processed pages with extracted content`pages[].index`integerPage number (0-indexed)`pages[].markdown`stringExtracted text in Markdown format`pages[].dimensions`objectPage dimensions (dpi, height, width in pixels)`pages[].images`arrayExtracted images from the page (if `include_image_base64=true`)`model`stringThe model used for OCR processing`usage_info`objectProcessing statistics (pages processed, document size)`document_annotation`objectOptional document-level annotations`object`stringAlways `"ocr"` for OCR responses

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderLink to UsageMistral AI[Usage](#quick-start)Azure AI[Usage](https://docs.litellm.ai/docs/providers/azure_ocr)Vertex AI[Usage](https://docs.litellm.ai/docs/providers/vertex_ocr)