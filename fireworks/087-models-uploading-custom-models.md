---
title: Custom Models - Fireworks AI Docs
url: https://docs.fireworks.ai/models/uploading-custom-models
source: sitemap
fetched_at: 2026-04-27T20:18:08.005401139-03:00
rendered_js: false
word_count: 548
summary: This document outlines how users can upload custom or fine-tuned AI models to a platform like Fireworks, detailing various methods including local file uploads, S3 and Azure Blob Storage transfers, required file formats, model customization options, and the subsequent steps for deployment and publishing.
tags:
    - model-upload
    - huggingface-models
    - cloud-storage
    - deployment-workflow
    - architecture-support
    - lora-adapters
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Upload your own models from Hugging Face or elsewhere to deploy fine-tuned or custom-trained models optimized for your use case. Multiple upload options are available: local files, S3 buckets, or Azure Blob Storage. All uploads are encrypted and models remain private to your account by default.

## Requirements

### Supported Architectures

Fireworks supports most popular model architectures:

- [DeepSeek V1, V2 & V3](https://huggingface.co/deepseek-ai)
- [Qwen, Qwen2, Qwen2.5, Qwen2.5-VL, Qwen3](https://huggingface.co/Qwen)
- [Kimi K2 family](https://huggingface.co/moonshotai)
- [GLM 4.X family](https://huggingface.co/zai-org)
- [Llama 1, 2, 3, 3.1, 4](https://huggingface.co/docs/transformers/en/model_doc/llama2)
- [Mistral & Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mistral)
- [Gemma](https://huggingface.co/docs/transformers/en/model_doc/gemma)
- [GPT-OSS 120B and 20B](https://huggingface.co/openai/gpt-oss-120b)
- [DBRX](https://huggingface.co/docs/transformers/en/model_doc/dbrx)
- [Falcon](https://huggingface.co/docs/transformers/en/model_doc/falcon)
- [GPT NeoX](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
- [Idefics3](https://huggingface.co/docs/transformers/en/model_doc/idefics3)
- [LLaVA](https://huggingface.co/docs/transformers/main/en/model_doc/llava)
- [Phi, Phi-3, Phi-3V, Phi-4](https://huggingface.co/docs/transformers/en/model_doc/phi)
- [Pythia](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
- [Solar](https://huggingface.co/upstage/SOLAR-10.7B-v1.0)
- [StableLM](https://huggingface.co/docs/transformers/main/en/model_doc/stablelm)
- [Starcoder (GPTBigCode)](https://huggingface.co/docs/transformers/en/model_doc/gpt_bigcode) & [Starcoder2](https://huggingface.co/docs/transformers/main/en/model_doc/starcoder2)
- [Vision Llama](https://huggingface.co/docs/transformers/en/model_doc/llama2)

### Required Files

| File | Description |
|---|---|
| `config.json` | Model configuration |
| `*.safetensors` or `*.bin` | Model weights |
| `*.index.json` | Weights index |
| `tokenizer.model` / `tokenizer.json` / `tokenizer_config.json` | Tokenizer files |

If the requisite files are not present, model deployment may fail.

### Customizing Base Model Configuration

For base models (not LoRA adapters), customize the chat template and generation defaults:

- **Chat template**: Add or modify the `chat_template` field in `tokenizer_config.json`. See the Hugging Face guide on [Templates for Chat Models](https://huggingface.co/docs/transformers/main/en/chat_templating) for details.
- **Generation defaults**: Modify `generation_config.json` to set `max_new_tokens`, `temperature`, `top_p`, etc.

You can also use a `fireworks.json` file with base models. If present, `fireworks.json` takes priority over `generation_config.json`. See [Customizing generation defaults with fireworks.json](#customizing-generation-defaults-with-fireworksjson) for the full schema.

## Uploading Your Model

- Local files (CLI)
- S3 bucket (CLI)
- Azure Blob Storage (CLI)
- REST API

### Local Upload

```bash
firectl model create <MODEL_ID> /path/to/files/
```

### S3 Upload

```bash
firectl model create <MODEL_ID> s3://<BUCKET_NAME>/<PATH_TO_MODEL>/ \
  --aws-access-key-id <ACCESS_KEY_ID> \
  --aws-secret-access-key <SECRET_ACCESS_KEY>
```

See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) for how to generate an access key ID and secret access key pair.

### Azure Blob Storage Upload

**SAS token:**

```bash
# First create a Fireworks secret containing your Azure SAS token
firectl secret create --name <SECRET_NAME> --value <SAS_TOKEN>

# Then upload the model using the secret
firectl model create <MODEL_ID> https://<STORAGE_ACCOUNT>.blob.core.windows.net/<CONTAINER>/<PATH> \
  --azure-sas-token-secret accounts/<ACCOUNT_ID>/secrets/<SECRET_NAME>
```

See the [Azure documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for how to generate a SAS token.

**Federated identity:**

```bash
firectl model create <MODEL_ID> https://<STORAGE_ACCOUNT>.blob.core.windows.net/<CONTAINER>/<PATH> \
  --azure-client-id <CLIENT_ID> \
  --azure-tenant-id <TENANT_ID>
```

### REST API Upload

For programmatic uploads (automation, CI/CD pipelines), use the Fireworks REST API: create model → get upload URLs → upload files → validate. See the REST API upload guide for a complete Python example.

## Verifying Your Upload

```bash
firectl model get accounts/<ACCOUNT_ID>/models/<MODEL_NAME>
```

Look for `State: READY` in the output.

## Deploying Your Model

```bash
firectl deployment create accounts/<ACCOUNT_ID>/models/<MODEL_NAME> --wait
```

See [[070-guides-ondemand-deployments]] for configuration options like GPU types, autoscaling, and quantization.

## Publishing Your Model

By default, models are private to your account. Publish a model to make it available to other Fireworks users:

- Listed in the public model catalog
- Deployable by anyone with a Fireworks account
- Still hosted and controlled by your account

```bash
# Publish
firectl model update <MODEL_ID> --public

# Unpublish
firectl model update <MODEL_ID> --public=false
```

## Importing Fine-Tuned Models (LoRA Adapters)

Upload your own custom fine-tuned models as LoRA adapters.

### Requirements

Your custom LoRA addon must contain:

| File | Description |
|---|---|
| `adapter_config.json` | Hugging Face adapter configuration |
| `adapter_model.bin` or `adapter_model.safetensors` | Saved addon file |

The `adapter_config.json` must contain:

- `r` — LoRA rank (integer between 4 and 64, inclusive)
- `target_modules` — List of supported modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `up_proj` (or `w1`), `down_proj` (or `w2`), `gate_proj` (or `w3`), `block_sparse_moe.gate`

### Customizing Generation Defaults with fireworks.json

For LoRA adapters, use a `fireworks.json` file to customize generation defaults. Adapters inherit configuration from their base model—modifying `generation_config.json` in the adapter folder won't work.

```json
{
  "defaults": {
    "stop": ["<|im_end|>", "</s>"],
    "max_tokens": 1024,
    "temperature": 0.7,
    "top_k": 50,
    "top_p": 0.9,
    "min_p": 0.0,
    "typical_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "repetition_penalty": 1.0
  },
  "model_arch": null,
  "model_config_name": null,
  "has_lora": true,
  "has_teft": false
}
```

### Uploading the LoRA Adapter

```bash
firectl model create <MODEL_ID> /path/to/files/ --base-model "accounts/fireworks/models/<BASE_MODEL_ID>"
```

#model-upload #lora-adapters #huggingface #cloud-storage
