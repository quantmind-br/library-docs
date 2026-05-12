---
title: Concepts - Fireworks AI Docs
url: https://docs.fireworks.ai/getting-started/concepts
source: sitemap
fetched_at: 2026-04-27T20:18:33.422807924-03:00
rendered_js: false
word_count: 486
summary: This document outlines the fundamental resources within the Fireworks AI platform, detailing concepts like accounts, users, models (including base and LoRA addons), deployments (serverless vs. dedicated), datasets, and fine-tuning jobs. It also describes the API architecture and interaction interfaces.
tags:
    - resources
    - model-management
    - deployment-types
    - account-structure
    - llm-concepts
    - api-architecture
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Resources

### Account

Your account is the top-level resource under which other resources are located. Quotas and billing are enforced at the account level.

- For developer accounts, the account ID is auto-generated from the email address used to sign up.
- Enterprise accounts can optionally choose a custom, unique account ID.

### User

A user is an email address associated with an account. Each user is assigned a role (Admin, User, Contributor, or Inference User) that determines their level of access to resources within the account.

### Models and model types

A model is a set of model weights and metadata. Each model has a globally unique name of the form `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`.

**Base models:** A base model consists of the full set of model weights.

- Fireworks has a library of common base models for [[009-getting-started-quickstart|serverless inference]] and [[070-guides-ondemand-deployments|dedicated deployments]].
- Model IDs for Fireworks models are pre-populated (e.g., `llama-v3p1-70b-instruct`).
- Users can also [[087-models-uploading-custom-models|upload their own]] custom base models.

**LoRA (low-rank adaptation) addons:** A LoRA addon is a small, fine-tuned model that significantly reduces memory required to deploy. Fireworks supports [[011-fine-tuning-finetuning-intro|training]], [[087-models-uploading-custom-models#importing-fine-tuned-models|uploading]], and [[040-fine-tuning-fine-tuning-models#deploying-a-fine-tuned-model|serving]] LoRA addons.

> [!note]
> When retrieving model details via the API, a model may show both `supportsServerless: true` and `supportsLora: true`. However, these are mutually exclusive in deployment — `supportsServerless` applies only to the base model. A LoRA addon requires a dedicated (on-demand) deployment.

### Deployments and deployment types

A model must be deployed before it can be used for inference.

- **Serverless deployments:** Fireworks hosts popular base models on shared deployments. Users pay-per-token without configuring GPUs. See the [[009-getting-started-quickstart|Quickstart - Serverless]].
- **Dedicated deployments:** Configure private deployments with configurable hardware. See [[070-guides-ondemand-deployments|on-demand deployments guide]]. Both LoRA addons and base models can be deployed. Billed by GPU-second basis.

See [[075-guides-querying-text-models|Querying text models guide]] for a comprehensive overview of making LLM inference.

### Deployed model

A "deployed model" name refers to a unique instance of a base model or LoRA addon loaded into a deployment.

### Dataset

A dataset is an immutable set of training examples used to fine-tune a model.

### Fine-tuning job

A fine-tuning job is an offline training job that uses a dataset to train a LoRA addon model.

## Resource names and IDs

A resource name is a globally unique identifier. Resource IDs must satisfy:

- Between 1 and 63 characters (inclusive)
- Consists of `a-z`, `0-9`, and hyphen (`-`)
- Does not begin or end with a hyphen (`-`)
- Does not begin with a digit

## Control plane and data plane

The Fireworks API can be split into:

- **Control plane:** APIs for managing the lifecycle of resources (account, models, deployments).
- **Data plane:** APIs for inference and the backend services that power them.

## Interfaces

Users can interact with Fireworks through:

- **Web app:** [https://app.fireworks.ai](https://app.fireworks.ai)
- **CLI:** [[092-tools-sdks-firectl-firectl|firectl]]
- **API compatibility:**
  - [[093-tools-sdks-openai-compatibility|OpenAI compatible API]]
  - [[089-tools-sdks-anthropic-compatibility|Anthropic compatible API]]
  - [[094-tools-sdks-python-sdk|Python SDK]]
