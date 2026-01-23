---
title: Oracle Cloud Infrastructure (OCI) | liteLLM
url: https://docs.litellm.ai/docs/providers/oci
source: sitemap
fetched_at: 2026-01-21T19:49:55.399684484-03:00
rendered_js: false
word_count: 393
summary: This document provides instructions on integrating LiteLLM with Oracle Cloud Infrastructure (OCI) GenAI services, covering supported models, authentication methods, and configuration for on-demand or dedicated endpoints.
tags:
    - litellm
    - oracle-cloud
    - oci-genai
    - llm-integration
    - api-configuration
    - authentication
category: guide
---

LiteLLM supports the following models for OCI on-demand GenAI API.

Check the [OCI Models List](https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm) to see if the model is available for your region.

## Supported Models[​](#supported-models "Direct link to Supported Models")

### Meta Llama Models[​](#meta-llama-models "Direct link to Meta Llama Models")

- `meta.llama-4-maverick-17b-128e-instruct-fp8`
- `meta.llama-4-scout-17b-16e-instruct`
- `meta.llama-3.3-70b-instruct`
- `meta.llama-3.2-90b-vision-instruct`
- `meta.llama-3.1-405b-instruct`

### xAI Grok Models[​](#xai-grok-models "Direct link to xAI Grok Models")

- `xai.grok-4`
- `xai.grok-3`
- `xai.grok-3-fast`
- `xai.grok-3-mini`
- `xai.grok-3-mini-fast`

### Cohere Models[​](#cohere-models "Direct link to Cohere Models")

- `cohere.command-latest`
- `cohere.command-a-03-2025`
- `cohere.command-plus-latest`

## Authentication[​](#authentication "Direct link to Authentication")

LiteLLM supports two authentication methods for OCI:

### Method 1: Manual Credentials[​](#method-1-manual-credentials "Direct link to Method 1: Manual Credentials")

Provide individual OCI credentials directly to LiteLLM. Follow the [official Oracle tutorial](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm) to create a signing key and obtain the following parameters:

- `user`
- `fingerprint`
- `tenancy`
- `region`
- `key_file` or `key`
- `compartment_id`

This is the default method for LiteLLM AI Gateway (LLM Proxy) access to OCI GenAI models.

### Method 2: OCI SDK Signer[​](#method-2-oci-sdk-signer "Direct link to Method 2: OCI SDK Signer")

Use an OCI SDK `Signer` object for authentication. This method:

- Leverages the official [OCI SDK for signing](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/signing.html)
- Supports additional authentication methods (instance principals, workload identity, etc.)

To use this method, install the OCI SDK:

This method is an alternative when using the LiteLLM SDK on Oracle Cloud Infrastructure (instances or Oracle Kubernetes Engine).

## Usage[​](#usage "Direct link to Usage")

- Manual Credentials
- OCI SDK Signer

Input the parameters obtained from the OCI signing key creation process into the `completion` function:

```
from litellm import completion

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(
    model="oci/xai.grok-4",
    messages=messages,
    oci_region=<your_oci_region>,
    oci_user=<your_oci_user>,
    oci_fingerprint=<your_oci_fingerprint>,
    oci_tenancy=<your_oci_tenancy>,
    oci_serving_mode="ON_DEMAND",# Optional, default is "ON_DEMAND". Other option is "DEDICATED"
# Provide either the private key string OR the path to the key file:
# Option 1: pass the private key as a string
    oci_key=<string_with_content_of_oci_key>,
# Option 2: pass the private key file path
# oci_key_file="<path/to/oci_key.pem>",
    oci_compartment_id=<oci_compartment_id>,
)
print(response)
```

## Usage - Streaming[​](#usage---streaming "Direct link to Usage - Streaming")

Just set `stream=True` when calling completion.

- Manual Credentials
- OCI SDK Signer

```
from litellm import completion

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(
    model="oci/xai.grok-4",
    messages=messages,
    stream=True,
    oci_region=<your_oci_region>,
    oci_user=<your_oci_user>,
    oci_fingerprint=<your_oci_fingerprint>,
    oci_tenancy=<your_oci_tenancy>,
    oci_serving_mode="ON_DEMAND",# Optional, default is "ON_DEMAND". Other option is "DEDICATED"
# Provide either the private key string OR the path to the key file:
# Option 1: pass the private key as a string
    oci_key=<string_with_content_of_oci_key>,
# Option 2: pass the private key file path
# oci_key_file="<path/to/oci_key.pem>",
    oci_compartment_id=<oci_compartment_id>,
)
for chunk in response:
print(chunk["choices"][0]["delta"]["content"])# same as openai format
```

## Usage Examples by Model Type[​](#usage-examples-by-model-type "Direct link to Usage Examples by Model Type")

### Using Cohere Models[​](#using-cohere-models "Direct link to Using Cohere Models")

- Manual Credentials
- OCI SDK Signer

```
from litellm import completion

messages =[{"role":"user","content":"Explain quantum computing"}]
response = completion(
    model="oci/cohere.command-latest",
    messages=messages,
    oci_region="us-chicago-1",
    oci_user=<your_oci_user>,
    oci_fingerprint=<your_oci_fingerprint>,
    oci_tenancy=<your_oci_tenancy>,
    oci_key=<string_with_content_of_oci_key>,
    oci_compartment_id=<oci_compartment_id>,
)
print(response)
```

## Using Dedicated Endpoints[​](#using-dedicated-endpoints "Direct link to Using Dedicated Endpoints")

OCI supports dedicated endpoints for hosting models. Use the `oci_serving_mode="DEDICATED"` parameter along with `oci_endpoint_id` to specify the endpoint ID.

- Manual Credentials
- OCI SDK Signer

```
from litellm import completion

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(
    model="oci/xai.grok-4",# Must match the model type hosted on the endpoint
    messages=messages,
    oci_region=<your_oci_region>,
    oci_user=<your_oci_user>,
    oci_fingerprint=<your_oci_fingerprint>,
    oci_tenancy=<your_oci_tenancy>,
    oci_serving_mode="DEDICATED",
    oci_endpoint_id="ocid1.generativeaiendpoint.oc1...",# Your dedicated endpoint OCID
    oci_key=<string_with_content_of_oci_key>,
    oci_compartment_id=<oci_compartment_id>,
)
print(response)
```

**Important:** When using `oci_serving_mode="DEDICATED"`:

- The `model` parameter **must match the type of model hosted on your dedicated endpoint** (e.g., use `"oci/cohere.command-latest"` for Cohere models, `"oci/xai.grok-4"` for Grok models)
- The model name determines the API format and vendor-specific handling (Cohere vs Generic)
- The `oci_endpoint_id` parameter specifies your dedicated endpoint's OCID
- If `oci_endpoint_id` is not provided, the `model` parameter will be used as the endpoint ID (for backward compatibility)

**Example with Cohere Dedicated Endpoint:**

```
# For a dedicated endpoint hosting a Cohere model
response = completion(
    model="oci/cohere.command-latest",# Use Cohere model name to get Cohere API format
    messages=messages,
    oci_region="us-chicago-1",
    oci_user=<your_oci_user>,
    oci_fingerprint=<your_oci_fingerprint>,
    oci_tenancy=<your_oci_tenancy>,
    oci_serving_mode="DEDICATED",
    oci_endpoint_id="ocid1.generativeaiendpoint.oc1...",# Your Cohere endpoint OCID
    oci_key=<string_with_content_of_oci_key>,
    oci_compartment_id=<oci_compartment_id>,
)
```

## Optional Parameters[​](#optional-parameters "Direct link to Optional Parameters")

ParameterTypeDefaultDescription`oci_region`string`us-ashburn-1`OCI region where the GenAI service is deployed`oci_serving_mode`string`ON_DEMAND`Service mode: `ON_DEMAND` for managed models or `DEDICATED` for dedicated endpoints`oci_endpoint_id`stringSame as `model`(For DEDICATED mode) The OCID of your dedicated endpoint`oci_compartment_id`string**Required**The OCID of the OCI compartment containing your resources`oci_user`string-(Manual auth) The OCID of the OCI user`oci_fingerprint`string-(Manual auth) The fingerprint of the API signing key`oci_tenancy`string-(Manual auth) The OCID of your OCI tenancy`oci_key`string-(Manual auth) The private key content as a string`oci_key_file`string-(Manual auth) Path to the private key file`oci_signer`object-(SDK auth) OCI SDK Signer object for authentication