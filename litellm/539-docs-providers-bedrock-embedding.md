---
title: Bedrock Embedding | liteLLM
url: https://docs.litellm.ai/docs/providers/bedrock_embedding
source: sitemap
fetched_at: 2026-01-21T19:48:27.878200912-03:00
rendered_js: false
word_count: 573
summary: This document provides a technical reference for using LiteLLM with AWS Bedrock embedding models, including support for synchronous and asynchronous multimodal processing.
tags:
    - aws-bedrock
    - litellm
    - embedding-models
    - async-invoke
    - amazon-nova
    - multimodal-embeddings
category: reference
---

## Supported Embedding Models[​](#supported-embedding-models "Direct link to Supported Embedding Models")

ProviderLiteLLM RouteAWS DocumentationCost TrackingAmazon Titan`bedrock/amazon.titan-*`[Amazon Titan Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html)✅Amazon Nova`bedrock/amazon.nova-*`[Amazon Nova Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/nova-embed.html)✅Cohere`bedrock/cohere.*`[Cohere Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere-embed.html)✅TwelveLabs`bedrock/us.twelvelabs.*`[TwelveLabs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-twelvelabs.html)✅

## Async Invoke Support[​](#async-invoke-support "Direct link to Async Invoke Support")

LiteLLM supports AWS Bedrock's async-invoke feature for embedding models that require asynchronous processing, particularly useful for large media files (video, audio) or when you need to process embeddings in the background.

### Supported Models[​](#supported-models "Direct link to Supported Models")

ProviderAsync Invoke RouteUse CaseAmazon Nova`bedrock/async_invoke/amazon.nova-2-multimodal-embeddings-v1:0`Multimodal embeddings with segmentation for long text, video, and audioTwelveLabs Marengo`bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0`Video, audio, image, and text embeddings

### Required Parameters[​](#required-parameters "Direct link to Required Parameters")

When using async-invoke, you must provide:

ParameterDescriptionRequired`output_s3_uri`S3 URI where the embedding results will be stored✅ Yes`input_type`Type of input: `"text"`, `"image"`, `"video"`, or `"audio"`✅ Yes`aws_region_name`AWS region for the request✅ Yes

### Usage[​](#usage "Direct link to Usage")

#### Basic Async Invoke[​](#basic-async-invoke "Direct link to Basic Async Invoke")

```
from litellm import embedding

# Text embedding with async-invoke
response = embedding(
    model="bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0",
input=["Hello world from LiteLLM async invoke!"],
    aws_region_name="us-east-1",
    input_type="text",
    output_s3_uri="s3://your-bucket/async-invoke-output/"
)

print(f"Job submitted! Invocation ARN: {response._hidden_params._invocation_arn}")
```

#### Video/Audio Embedding[​](#videoaudio-embedding "Direct link to Video/Audio Embedding")

```
# Video embedding (requires async-invoke)
response = embedding(
    model="bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0",
input=["s3://your-bucket/video.mp4"],# S3 URL for video
    aws_region_name="us-east-1",
    input_type="video",
    output_s3_uri="s3://your-bucket/async-invoke-output/"
)

print(f"Video embedding job submitted! ARN: {response._hidden_params._invocation_arn}")
```

#### Image Embedding with Base64[​](#image-embedding-with-base64 "Direct link to Image Embedding with Base64")

```
import base64

# Load and encode image
withopen("image.jpg","rb")as img_file:
    img_data = base64.b64encode(img_file.read()).decode('utf-8')
    img_base64 =f"data:image/jpeg;base64,{img_data}"

response = embedding(
    model="bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0",
input=[img_base64],
    aws_region_name="us-east-1",
    input_type="image",
    output_s3_uri="s3://your-bucket/async-invoke-output/"
)
```

### Retrieving Job Information[​](#retrieving-job-information "Direct link to Retrieving Job Information")

#### Getting Job ID and Invocation ARN[​](#getting-job-id-and-invocation-arn "Direct link to Getting Job ID and Invocation ARN")

The async-invoke response includes the invocation ARN in the hidden parameters:

```
response = embedding(
    model="bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0",
input=["Hello world"],
    aws_region_name="us-east-1",
    input_type="text",
    output_s3_uri="s3://your-bucket/async-invoke-output/"
)

# Access invocation ARN
invocation_arn = response._hidden_params._invocation_arn
print(f"Invocation ARN: {invocation_arn}")

# Extract job ID from ARN (last part after the last slash)
job_id = invocation_arn.split("/")[-1]
print(f"Job ID: {job_id}")
```

#### Checking Job Status[​](#checking-job-status "Direct link to Checking Job Status")

Use LiteLLM's `retrieve_batch` function to check if your job is still processing:

```
from litellm import retrieve_batch

defcheck_async_job_status(invocation_arn, aws_region_name="us-east-1"):
"""Check the status of an async invoke job using LiteLLM batch API"""
try:
        response = retrieve_batch(
            batch_id=invocation_arn,# Pass the invocation ARN here
            custom_llm_provider="bedrock",
            aws_region_name=aws_region_name
)
return response
except Exception as e:
print(f"Error checking job status: {e}")
returnNone

# Check status
status = check_async_job_status(invocation_arn,"us-east-1")
if status:
print(f"Job Status: {status.status}")# "in_progress", "completed", or "failed"
print(f"Output Location: {status.metadata['output_file_id']}")# S3 URI where results are stored
```

#### Polling Until Complete[​](#polling-until-complete "Direct link to Polling Until Complete")

Here's a complete example of polling for job completion:

```
defwait_for_async_job(invocation_arn, aws_region_name="us-east-1", max_wait=3600):
"""Poll job status until completion"""
    start_time = time.time()

whileTrue:
        status = retrieve_batch(
            batch_id=invocation_arn,
            custom_llm_provider="bedrock",
            aws_region_name=aws_region_name,
)

if status.status =="completed":
print("✅ Job completed!")
return status
elif status.status =="failed":
            error_msg = status.metadata.get('failure_message','Unknown error')
raise Exception(f"❌ Job failed: {error_msg}")
else:
            elapsed = time.time()- start_time
if elapsed > max_wait:
raise TimeoutError(f"Job timed out after {max_wait} seconds")

print(f"⏳ Job still processing... (elapsed: {elapsed:.0f}s)")
            time.sleep(10)# Wait 10 seconds before checking again

# Wait for completion
completed_status = wait_for_async_job(invocation_arn)
output_s3_uri = completed_status.metadata['output_file_id']
print(f"Results available at: {output_s3_uri}")
```

**Note:** The actual embedding results are stored in S3. When the job is completed, download the results from the S3 location specified in `status.metadata['output_file_id']`. The results will be in JSON/JSONL format containing the embedding vectors.

## Amazon Nova Multimodal Embeddings[​](#amazon-nova-multimodal-embeddings "Direct link to Amazon Nova Multimodal Embeddings")

Amazon Nova supports multimodal embeddings for text, images, video, and audio. It offers flexible embedding dimensions and purposes optimized for different use cases.

### Supported Features[​](#supported-features "Direct link to Supported Features")

- **Modalities**: Text, Image, Video, Audio
- **Dimensions**: 256, 384, 1024, 3072 (default: 3072)
- **Embedding Purposes**:
  
  - `GENERIC_INDEX` (default)
  - `GENERIC_RETRIEVAL`
  - `TEXT_RETRIEVAL`
  - `IMAGE_RETRIEVAL`
  - `VIDEO_RETRIEVAL`
  - `AUDIO_RETRIEVAL`
  - `CLASSIFICATION`
  - `CLUSTERING`

### Text Embedding[​](#text-embedding "Direct link to Text Embedding")

```
from litellm import embedding

response = embedding(
    model="bedrock/amazon.nova-2-multimodal-embeddings-v1:0",
input=["Hello, world!"],
    aws_region_name="us-east-1",
    dimensions=1024,# Optional: 256, 384, 1024, or 3072
)

print(response.data[0].embedding)
```

### Image Embedding with Base64[​](#image-embedding-with-base64-1 "Direct link to Image Embedding with Base64")

Amazon Nova accepts images in base64 format using the standard data URL format:

```
import base64
from litellm import embedding

# Method 1: Load image from file
withopen("image.jpg","rb")as image_file:
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
# Create data URL with proper format
    image_base64 =f"data:image/jpeg;base64,{image_data}"

response = embedding(
    model="bedrock/amazon.nova-2-multimodal-embeddings-v1:0",
input=[image_base64],
    aws_region_name="us-east-1",
    dimensions=1024,
)

print(f"Image embedding: {response.data[0].embedding[:10]}...")# First 10 dimensions
```

#### Supported Image Formats[​](#supported-image-formats "Direct link to Supported Image Formats")

Nova supports the following image formats:

- JPEG: `data:image/jpeg;base64,...`
- PNG: `data:image/png;base64,...`
- GIF: `data:image/gif;base64,...`
- WebP: `data:image/webp;base64,...`

#### Complete Example with Error Handling[​](#complete-example-with-error-handling "Direct link to Complete Example with Error Handling")

```
import base64
from litellm import embedding

defget_image_embedding(image_path, dimensions=1024):
"""
    Get embedding for an image file.

    Args:
        image_path: Path to the image file
        dimensions: Embedding dimension (256, 384, 1024, or 3072)

    Returns:
        List of embedding values
    """
try:
# Determine image format from file extension
if image_path.lower().endswith('.png'):
            mime_type ="image/png"
elif image_path.lower().endswith(('.jpg','.jpeg')):
            mime_type ="image/jpeg"
elif image_path.lower().endswith('.gif'):
            mime_type ="image/gif"
elif image_path.lower().endswith('.webp'):
            mime_type ="image/webp"
else:
raise ValueError(f"Unsupported image format: {image_path}")

# Read and encode image
withopen(image_path,"rb")as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            image_base64 =f"data:{mime_type};base64,{image_data}"

# Get embedding
        response = embedding(
            model="bedrock/amazon.nova-2-multimodal-embeddings-v1:0",
input=[image_base64],
            aws_region_name="us-east-1",
            dimensions=dimensions,
)

return response.data[0].embedding

except Exception as e:
print(f"Error getting image embedding: {e}")
raise

# Example usage
image_embedding = get_image_embedding("photo.jpg", dimensions=1024)
print(f"Got embedding with {len(image_embedding)} dimensions")
```

### Error Handling[​](#error-handling "Direct link to Error Handling")

#### Common Errors[​](#common-errors "Direct link to Common Errors")

ErrorCauseSolution`ValueError: output_s3_uri cannot be empty`Missing S3 output URIProvide a valid S3 URI`ValueError: Input type 'video' requires async_invoke route`Using video/audio without async-invokeUse `bedrock/async_invoke/` model prefix`ValueError: input_type is required`Missing input type parameterSpecify `input_type` parameter

#### Example Error Handling[​](#example-error-handling "Direct link to Example Error Handling")

```
try:
    response = embedding(
        model="bedrock/async_invoke/us.twelvelabs.marengo-embed-2-7-v1:0",
input=["Hello world"],
        aws_region_name="us-east-1",
        input_type="text",
        output_s3_uri="s3://your-bucket/output/"# Required for async-invoke
)
print("Job submitted successfully!")

except ValueError as e:
if"output_s3_uri cannot be empty"instr(e):
print("Error: Please provide a valid S3 output URI")
elif"requires async_invoke route"instr(e):
print("Error: Use async_invoke model for video/audio inputs")
else:
print(f"Error: {e}")
except Exception as e:
print(f"Unexpected error: {e}")
```

### Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Use async-invoke for large files**: Video and audio files are better processed asynchronously
2. **Use LiteLLM batch API**: Use `retrieve_batch()` instead of direct Bedrock API calls for status checking
3. **Monitor job status**: Check job status periodically using the batch API to know when results are ready
4. **Handle errors gracefully**: Implement proper error handling for network issues and job failures
5. **Set appropriate timeouts**: Consider the processing time for large files
6. **Use S3 for large inputs**: For video/audio, use S3 URLs instead of base64 encoding

### Limitations[​](#limitations "Direct link to Limitations")

- Async-invoke is supported for TwelveLabs Marengo and Amazon Nova models
- Results are stored in S3 and must be retrieved separately using the output file ID
- Job status checking requires using LiteLLM's `retrieve_batch()` function
- No built-in polling mechanism in LiteLLM (must implement your own status checking loop)

### API keys[​](#api-keys "Direct link to API keys")

This can be set as env variables or passed as **params to litellm.embedding()**

```
import os
os.environ["AWS_ACCESS_KEY_ID"]=""# Access key
os.environ["AWS_SECRET_ACCESS_KEY"]=""# Secret access key
os.environ["AWS_REGION_NAME"]=""# us-east-1, us-east-2, us-west-1, us-west-2
```

## Usage[​](#usage-1 "Direct link to Usage")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

```
from litellm import embedding
response = embedding(
    model="bedrock/amazon.titan-embed-text-v1",
input=["good morning from litellm"],
)
print(response)
```

### LiteLLM Proxy Server[​](#litellm-proxy-server "Direct link to LiteLLM Proxy Server")

#### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: titan-embed-v1
litellm_params:
model: bedrock/amazon.titan-embed-text-v1
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-east-1
-model_name: titan-embed-v2
litellm_params:
model: bedrock/amazon.titan-embed-text-v2:0
aws_access_key_id: os.environ/AWS_ACCESS_KEY_ID
aws_secret_access_key: os.environ/AWS_SECRET_ACCESS_KEY
aws_region_name: us-east-1
```

#### 2. Start Proxy[​](#2-start-proxy "Direct link to 2. Start Proxy")

```
litellm --config /path/to/config.yaml
```

#### 3. Use with OpenAI Python SDK[​](#3-use-with-openai-python-sdk "Direct link to 3. Use with OpenAI Python SDK")

```
import openai
client = openai.OpenAI(
    api_key="anything",
    base_url="http://0.0.0.0:4000"
)

response = client.embeddings.create(
input=["good morning from litellm"],
    model="titan-embed-v1"
)
print(response)
```

#### 4. Use with LiteLLM Python SDK[​](#4-use-with-litellm-python-sdk "Direct link to 4. Use with LiteLLM Python SDK")

```
import litellm
response = litellm.embedding(
    model="titan-embed-v1",# model alias from config.yaml
input=["good morning from litellm"],
    api_base="http://0.0.0.0:4000",
    api_key="anything"
)
print(response)
```

## Supported AWS Bedrock Embedding Models[​](#supported-aws-bedrock-embedding-models "Direct link to Supported AWS Bedrock Embedding Models")

Model NameUsageSupported Additional OpenAI params**Amazon Nova Multimodal Embeddings**`embedding(model="bedrock/amazon.nova-2-multimodal-embeddings-v1:0", input=input)`Supports multimodal input (text, image, video, audio), multiple purposes, dimensions (256, 384, 1024, 3072)Titan Embeddings V2`embedding(model="bedrock/amazon.titan-embed-text-v2:0", input=input)`[here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_v2_transformation.py#L59)Titan Embeddings - V1`embedding(model="bedrock/amazon.titan-embed-text-v1", input=input)`[here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_g1_transformation.py#L53)Titan Multimodal Embeddings`embedding(model="bedrock/amazon.titan-embed-image-v1", input=input)`[here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/amazon_titan_multimodal_transformation.py#L28)TwelveLabs Marengo Embed 2.7`embedding(model="bedrock/us.twelvelabs.marengo-embed-2-7-v1:0", input=input)`Supports multimodal input (text, video, audio, image)Cohere Embeddings - English`embedding(model="bedrock/cohere.embed-english-v3", input=input)`[here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/cohere_transformation.py#L18)Cohere Embeddings - Multilingual`embedding(model="bedrock/cohere.embed-multilingual-v3", input=input)`[here](https://github.com/BerriAI/litellm/blob/f5905e100068e7a4d61441d7453d7cf5609c2121/litellm/llms/bedrock/embed/cohere_transformation.py#L18)Cohere Embed v4`embedding(model="bedrock/cohere.embed-v4:0", input=input)`Supports text and image input, configurable dimensions (256, 512, 1024, 1536), 128k context length

### Advanced - [Drop Unsupported Params](https://docs.litellm.ai/docs/completion/drop_params#openai-proxy-usage)[​](#advanced---drop-unsupported-params "Direct link to advanced---drop-unsupported-params")

### Advanced - [Pass model/provider-specific Params](https://docs.litellm.ai/docs/completion/provider_specific_params#proxy-usage)[​](#advanced---pass-modelprovider-specific-params "Direct link to advanced---pass-modelprovider-specific-params")