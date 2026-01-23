---
title: Bedrock Batches | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_batches
source: sitemap
fetched_at: 2026-01-21T19:48:27.70823701-03:00
rendered_js: false
word_count: 447
summary: This document provides a comprehensive guide on configuring and using LiteLLM to execute asynchronous batch inference jobs through Amazon Bedrock. It covers administrative setup including S3 bucket configuration and IAM roles, alongside developer workflows for file management and batch job execution.
tags:
    - amazon-bedrock
    - litellm
    - batch-inference
    - aws-s3
    - asynchronous-processing
    - api-integration
category: guide
---

Use Amazon Bedrock Batch Inference API through LiteLLM.

PropertyDetailsDescriptionAmazon Bedrock Batch Inference allows you to run inference on large datasets asynchronouslyProvider Doc[AWS Bedrock Batch Inference ↗](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)Cost Tracking✅ Supported

## Overview[​](#overview "Direct link to Overview")

Use this to:

- Run batch inference on large datasets with Bedrock models
- Control batch model access by key/user/team (same as chat completion models)
- Manage S3 storage for batch input/output files

## (Proxy Admin) Usage[​](#proxy-admin-usage "Direct link to (Proxy Admin) Usage")

Here's how to give developers access to your Bedrock Batch models.

### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

- Specify `mode: batch` for each model: Allows developers to know this is a batch model
- Configure S3 bucket and AWS credentials for batch operations

litellm\_config.yaml

```
model_list:
-model_name:"bedrock-batch-claude"
litellm_params:
model: bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0
#########################################################
########## batch specific params ########################
s3_bucket_name: litellm-proxy
s3_region_name: us-west-2
s3_access_key_id: os.environ/AWS_ACCESS_KEY_ID
s3_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_batch_role_arn: arn:aws:iam::888602223428:role/service-role/AmazonBedrockExecutionRoleForAgents_BB9HNW6V4CV
# Optional: Custom KMS encryption key for S3 output
# s3_encryption_key_id: arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012
model_info:
mode: batch # 👈 SPECIFY MODE AS BATCH, to tell user this is a batch model
```

**Required Parameters:**

ParameterDescription`s3_bucket_name`S3 bucket for batch input/output files`s3_region_name`AWS region for S3 bucket`s3_access_key_id`AWS access key for S3 bucket`s3_secret_access_key`AWS secret key for S3 bucket`aws_batch_role_arn`IAM role ARN for Bedrock batch operations. Bedrock Batch APIs require an IAM role ARN to be set.`mode: batch`Indicates to LiteLLM this is a batch model

**Optional Parameters:**

ParameterDescription`s3_encryption_key_id`Custom KMS encryption key ID for S3 output data. If not specified, Bedrock uses AWS managed encryption keys.

### 2. Create Virtual Key[​](#2-create-virtual-key "Direct link to 2. Create Virtual Key")

create\_virtual\_key.sh

```
curl -L -X POST 'https://{PROXY_BASE_URL}/key/generate' \
-H 'Authorization: Bearer ${PROXY_API_KEY}' \
-H 'Content-Type: application/json' \
-d '{"models": ["bedrock-batch-claude"]}'
```

You can now use the virtual key to access the batch models (See Developer flow).

## (Developer) Usage[​](#developer-usage "Direct link to (Developer) Usage")

Here's how to create a LiteLLM managed file and execute Bedrock Batch CRUD operations with the file.

### 1. Create request.jsonl[​](#1-create-requestjsonl "Direct link to 1. Create request.jsonl")

- Check models available via `/model_group/info`
- See all models with `mode: batch`
- Set `model` in .jsonl to the model from `/model_group/info`

bedrock\_batch\_completions.jsonl

```
{"custom_id":"request-1","method":"POST","url":"/v1/chat/completions","body":{"model":"bedrock-batch-claude","messages":[{"role":"system","content":"You are a helpful assistant."},{"role":"user","content":"Hello world!"}],"max_tokens":1000}}
{"custom_id":"request-2","method":"POST","url":"/v1/chat/completions","body":{"model":"bedrock-batch-claude","messages":[{"role":"system","content":"You are an unhelpful assistant."},{"role":"user","content":"Hello world!"}],"max_tokens":1000}}
```

Expectation:

- LiteLLM translates this to the bedrock deployment specific value (e.g. `bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0`)

### 2. Upload File[​](#2-upload-file "Direct link to 2. Upload File")

Specify `target_model_names: "<model-name>"` to enable LiteLLM managed files and request validation.

model-name should be the same as the model-name in the request.jsonl

- Python
- Curl

bedrock\_batch.py

```
from openai import OpenAI

client = OpenAI(
    base_url="http://0.0.0.0:4000",
    api_key="sk-1234",
)

# Upload file
batch_input_file = client.files.create(
file=open("./bedrock_batch_completions.jsonl","rb"),# {"model": "bedrock-batch-claude"} <-> {"model": "bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0"}
    purpose="batch",
    extra_body={"target_model_names":"bedrock-batch-claude"}
)
print(batch_input_file)
```

**Where is the file written?**:

The file is written to S3 bucket specified in your config and prepared for Bedrock batch inference.

### 3. Create the batch[​](#3-create-the-batch "Direct link to 3. Create the batch")

- Python
- Curl

bedrock\_batch.py

```
...
# Create batch
batch = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={"description":"Test batch job"},
)
print(batch)
```

### 4. Retrieve batch results[​](#4-retrieve-batch-results "Direct link to 4. Retrieve batch results")

Once the batch job is completed, download the results from S3:

- Python
- Curl
- LiteLLM Direct

bedrock\_batch.py

```
...
# Wait for batch completion (check status periodically)
batch_status = client.batches.retrieve(batch_id=batch.id)

if batch_status.status =="completed":
# Download the output file
    result = client.files.content(
        file_id=batch_status.output_file_id,
        extra_headers={"custom-llm-provider":"bedrock"}
)

# Save or process the results
withopen("batch_output.jsonl","wb")as f:
        f.write(result.content)

# Parse JSONL results
for line in result.text.strip().split('\n'):
        record = json.loads(line)
print(f"Record ID: {record['recordId']}")
print(f"Output: {record.get('modelOutput', {})}")
```

**Output Format:**

The batch output file is in JSONL format with each line containing:

```
{
"recordId":"request-1",
"modelInput":{
"messages":[...],
"max_tokens":1000
},
"modelOutput":{
"content":[...],
"id":"msg_abc123",
"model":"claude-3-5-sonnet-20240620-v1:0",
"role":"assistant",
"stop_reason":"end_turn",
"usage":{
"input_tokens":15,
"output_tokens":10
}
}
}
```

## FAQ[​](#faq "Direct link to FAQ")

### Where are my files written?[​](#where-are-my-files-written "Direct link to Where are my files written?")

When a `target_model_names` is specified, the file is written to the S3 bucket configured in your Bedrock batch model configuration.

### What models are supported?[​](#what-models-are-supported "Direct link to What models are supported?")

LiteLLM only supports Bedrock Anthropic Models for Batch API. If you want other bedrock models file an issue [here](https://github.com/BerriAI/litellm/issues/new/choose).

### How do I use a custom KMS encryption key?[​](#how-do-i-use-a-custom-kms-encryption-key "Direct link to How do I use a custom KMS encryption key?")

If your S3 bucket requires a custom KMS encryption key, you can specify it in your configuration using `s3_encryption_key_id`. This is useful for enterprise customers with specific encryption requirements.

You can set the encryption key in 2 ways:

1. **In config.yaml** (recommended):

```
model_list:
-model_name:"bedrock-batch-claude"
litellm_params:
model: bedrock/us.anthropic.claude-3-5-sonnet-20240620-v1:0
s3_encryption_key_id: arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012
# ... other params
```

2. **As an environment variable**:

```
export AWS_S3_ENCRYPTION_KEY_ID=arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012
```

## Further Reading[​](#further-reading "Direct link to Further Reading")

- [AWS Bedrock Batch Inference Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)
- [LiteLLM Managed Batches](https://docs.litellm.ai/docs/proxy/managed_batches)
- [LiteLLM Authentication to Bedrock](https://docs.litellm.ai/docs/providers/bedrock#boto3---authentication)