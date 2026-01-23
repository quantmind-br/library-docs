---
title: /fine_tuning | liteLLM
url: https://docs.litellm.ai/docs/fine_tuning
source: sitemap
fetched_at: 2026-01-21T19:45:18.277278999-03:00
rendered_js: false
word_count: 406
summary: This document explains how to configure and use LiteLLM to manage files and execute fine-tuning jobs across multiple providers like Azure OpenAI, Vertex AI, and OpenAI.
tags:
    - litellm
    - fine-tuning
    - llm-proxy
    - azure-openai
    - vertex-ai
    - api-configuration
category: guide
---

FeatureSupportedNotesSupported ProvidersOpenAI, Azure OpenAI, Vertex AI-

#### ⚡️See an exhaustive list of supported models and providers at [models.litellm.ai](https://models.litellm.ai/)[​](#%EF%B8%8Fsee-an-exhaustive-list-of-supported-models-and-providers-at-modelslitellmai "Direct link to ️see-an-exhaustive-list-of-supported-models-and-providers-at-modelslitellmai")

| Cost Tracking | 🟡 | [Let us know if you need this](https://github.com/BerriAI/litellm/issues) | | Logging | ✅ | Works across all logging integrations |

Add `finetune_settings` and `files_settings` to your litellm config.yaml to use the fine-tuning endpoints.

## Example config.yaml for `finetune_settings` and `files_settings`[​](#example-configyaml-for-finetune_settings-and-files_settings "Direct link to example-configyaml-for-finetune_settings-and-files_settings")

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/

# For /fine_tuning/jobs endpoints
finetune_settings:
-custom_llm_provider: azure
api_base: https://exampleopenaiendpoint-production.up.railway.app
api_key: os.environ/AZURE_API_KEY
api_version:"2023-03-15-preview"
-custom_llm_provider: openai
api_key: os.environ/OPENAI_API_KEY
-custom_llm_provider:"vertex_ai"
vertex_project:"adroit-crow-413218"
vertex_location:"us-central1"
vertex_credentials:"/Users/ishaanjaffer/Downloads/adroit-crow-413218-a956eef1a2a8.json"

# for /files endpoints
files_settings:
-custom_llm_provider: azure
api_base: https://exampleopenaiendpoint-production.up.railway.app
api_key: fake-key
api_version:"2023-03-15-preview"
-custom_llm_provider: openai
api_key: os.environ/OPENAI_API_KEY
```

## Create File for fine-tuning[​](#create-file-for-fine-tuning "Direct link to Create File for fine-tuning")

- OpenAI Python SDK
- curl

```
client = AsyncOpenAI(api_key="sk-1234", base_url="http://0.0.0.0:4000")# base_url is your litellm proxy url

file_name ="openai_batch_completions.jsonl"
response =await client.files.create(
    extra_headers={"custom-llm-provider":"azure"},# tell litellm proxy which provider to use
file=open(file_name,"rb"),
    purpose="fine-tune",
)
```

## Create fine-tuning job[​](#create-fine-tuning-job "Direct link to Create fine-tuning job")

- Azure OpenAI

<!--THE END-->

- OpenAI Python SDK
- curl

```
ft_job =await client.fine_tuning.jobs.create(
    model="gpt-35-turbo-1106",# Azure OpenAI model you want to fine-tune
    training_file="file-abc123",# file_id from create file response
    extra_headers={"custom-llm-provider":"azure"},# tell litellm proxy which provider to use
)
```

### Request Body[​](#request-body "Direct link to Request Body")

- Supported Params
- Example Request Body

<!--THE END-->

- `model`
  
  **Type:** string  
  **Required:** Yes  
  The name of the model to fine-tune
- `custom_llm_provider`
  
  **Type:** `Literal["azure", "openai", "vertex_ai"]`
  
  **Required:** Yes The name of the model to fine-tune. You can select one of the [**supported providers**](#supported-providers)
- `training_file`
  
  **Type:** string  
  **Required:** Yes  
  The ID of an uploaded file that contains training data.
  
  - See **upload file** for how to upload a file.
  - Your dataset must be formatted as a JSONL file.
- `hyperparameters`
  
  **Type:** object  
  **Required:** No  
  The hyperparameters used for the fine-tuning job.
  
  > #### Supported `hyperparameters`[​](#supported-hyperparameters "Direct link to supported-hyperparameters")
  > 
  > #### batch\_size[​](#batch_size "Direct link to batch_size")
  
  **Type:** string or integer  
  **Required:** No  
  Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.
  
  > #### learning\_rate\_multiplier[​](#learning_rate_multiplier "Direct link to learning_rate_multiplier")
  
  **Type:** string or number  
  **Required:** No  
  Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.
  
  > #### n\_epochs[​](#n_epochs "Direct link to n_epochs")
  
  **Type:** string or integer  
  **Required:** No  
  The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
- `suffix` **Type:** string or null  
  **Required:** No  
  **Default:** null  
  A string of up to 18 characters that will be added to your fine-tuned model name. Example: A `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.
- `validation_file` **Type:** string or null  
  **Required:** No  
  The ID of an uploaded file that contains validation data.
  
  - If provided, this data is used to generate validation metrics periodically during fine-tuning.
- `integrations` **Type:** array or null  
  **Required:** No  
  A list of integrations to enable for your fine-tuning job.
- `seed` **Type:** integer or null  
  **Required:** No  
  The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.

## Cancel fine-tuning job[​](#cancel-fine-tuning-job "Direct link to Cancel fine-tuning job")

- OpenAI Python SDK
- curl

```
# cancel specific fine tuning job
cancel_ft_job =await client.fine_tuning.jobs.cancel(
    fine_tuning_job_id="123",# fine tuning job id
    extra_headers={"custom-llm-provider":"azure"},# tell litellm proxy which provider to use
)

print("response from cancel ft job={}".format(cancel_ft_job))
```

## List fine-tuning jobs[​](#list-fine-tuning-jobs "Direct link to List fine-tuning jobs")

- OpenAI Python SDK
- curl

```
list_ft_jobs =await client.fine_tuning.jobs.list(
    extra_headers={"custom-llm-provider":"azure"}# tell litellm proxy which provider to use
)

print("list of ft jobs={}".format(list_ft_jobs))
```

## [👉 Proxy API Reference](https://litellm-api.up.railway.app/#/fine-tuning)[​](#-proxy-api-reference "Direct link to -proxy-api-reference")