---
title: Vertex AI OCR | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_ocr
source: sitemap
fetched_at: 2026-01-21T19:50:46.36683072-03:00
rendered_js: false
word_count: 220
summary: This document provides a comprehensive guide for implementing Vertex AI OCR using LiteLLM, covering authentication methods, SDK and proxy configurations, and document processing for PDFs and images.
tags:
    - vertex-ai
    - ocr
    - litellm
    - mistral
    - document-processing
    - python-sdk
    - data-extraction
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionVertex AI OCR provides document intelligence capabilities powered by Mistral, enabling text extraction from PDFs and imagesProvider Route on LiteLLM`vertex_ai/`Supported Operations`/ocr`Link to Provider Doc[Vertex AI ↗](https://cloud.google.com/vertex-ai)

Extract text from documents and images using Vertex AI's OCR models, powered by Mistral.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### **LiteLLM SDK**[​](#litellm-sdk "Direct link to litellm-sdk")

SDK Usage

```
import litellm
import os

# Set environment variables
os.environ["VERTEXAI_PROJECT"]="your-project-id"
os.environ["VERTEXAI_LOCATION"]="us-central1"

# OCR with PDF URL
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)

# Access extracted text
for page in response.pages:
print(page.text)
```

### **LiteLLM PROXY**[​](#litellm-proxy "Direct link to litellm-proxy")

proxy\_config.yaml

```
model_list:
-model_name: vertex-ocr
litellm_params:
model: vertex_ai/mistral-ocr-2505
vertex_project: os.environ/VERTEXAI_PROJECT
vertex_location: os.environ/VERTEXAI_LOCATION
vertex_credentials: path/to/service-account.json  # Optional
model_info:
mode: ocr
```

**Start Proxy**

```
litellm --config proxy_config.yaml
```

**Call OCR via Proxy**

cURL Request

```
curl -X POST http://localhost:4000/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "vertex-ocr",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2201.04234"
    }
  }'
```

## Authentication[​](#authentication "Direct link to Authentication")

Vertex AI OCR supports multiple authentication methods:

### Service Account JSON[​](#service-account-json "Direct link to Service Account JSON")

Service Account Auth

```
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={"type":"document_url","document_url":"https://..."},
    vertex_project="your-project-id",
    vertex_location="us-central1",
    vertex_credentials="path/to/service-account.json"
)
```

### Application Default Credentials[​](#application-default-credentials "Direct link to Application Default Credentials")

Default Credentials

```
# Relies on GOOGLE_APPLICATION_CREDENTIALS environment variable
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={"type":"document_url","document_url":"https://..."},
    vertex_project="your-project-id",
    vertex_location="us-central1"
)
```

## Document Types[​](#document-types "Direct link to Document Types")

Vertex AI OCR supports both PDFs and images.

### PDF Documents[​](#pdf-documents "Direct link to PDF Documents")

PDF OCR

```
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
},
    vertex_project="your-project-id",
    vertex_location="us-central1"
)
```

### Image Documents[​](#image-documents "Direct link to Image Documents")

Image OCR

```
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={
"type":"image_url",
"image_url":"https://example.com/image.png"
},
    vertex_project="your-project-id",
    vertex_location="us-central1"
)
```

### Base64 Encoded Documents[​](#base64-encoded-documents "Direct link to Base64 Encoded Documents")

Base64 PDF

```
import base64

# Read and encode PDF
withopen("document.pdf","rb")as f:
    pdf_base64 = base64.b64encode(f.read()).decode()

response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",# This doesn't work for deepseek
    document={
"type":"document_url",
"document_url":f"data:application/pdf;base64,{pdf_base64}"
},
    vertex_project="your-project-id",
    vertex_location="us-central1"
)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

All Parameters

```
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={# Required: Document to process
"type":"document_url",
"document_url":"https://..."
},
    vertex_project="your-project-id",# Required: GCP project ID
    vertex_location="us-central1",# Optional: Defaults to us-central1
    vertex_credentials="path/to/key.json",# Optional: Service account key
    include_image_base64=True,# Optional: Include base64 images
    pages=[0,1,2],# Optional: Specific pages to process
    image_limit=10# Optional: Limit number of images
)
```

## Response Format[​](#response-format "Direct link to Response Format")

Response Structure

```
# Response has the following structure
response.pages          # List of pages with extracted text
response.model          # Model used
response.object# "ocr"
response.usage_info     # Token usage information

# Access page content
for page in response.pages:
print(f"Page {page.page_number}:")
print(page.text)
```

## Async Support[​](#async-support "Direct link to Async Support")

Async Usage

```
import litellm

response =await litellm.aocr(
    model="vertex_ai/mistral-ocr-2505",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
},
    vertex_project="your-project-id",
    vertex_location="us-central1"
)
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks costs for Vertex AI OCR:

- **Cost per page**: $0.0005 (based on $1.50 per 1,000 pages)

View Cost

```
response = litellm.ocr(
    model="vertex_ai/mistral-ocr-2505",
    document={"type":"document_url","document_url":"https://..."},
    vertex_project="your-project-id"
)

# Access cost information
print(f"Cost: ${response._hidden_params.get('response_cost',0)}")
```

## Important Notes[​](#important-notes "Direct link to Important Notes")

URL Conversion

Vertex AI Mistral OCR endpoints don't have internet access. LiteLLM automatically converts public URLs to base64 data URIs before sending requests to Vertex AI.

Regional Availability

Mistral OCR is available in multiple regions. Specify `vertex_location` to use a region closer to your data:

- `us-central1` (default)
- `europe-west1`
- `asia-southeast1`

Deepseek OCR is only available in global region.

## Supported Models[​](#supported-models "Direct link to Supported Models")

- `mistral-ocr-2505` - Latest Mistral OCR model on Vertex AI
- `deepseek-ocr-maas` - Lates Deepseek OCR model on Vertex AI

Use the Vertex AI provider prefix: `vertex_ai/<model-name>`