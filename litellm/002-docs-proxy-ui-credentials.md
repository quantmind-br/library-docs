---
title: Adding LLM Credentials | liteLLM
url: https://docs.litellm.ai/docs/proxy/ui_credentials
source: sitemap
fetched_at: 2026-01-21T19:53:53.802547236-03:00
rendered_js: false
word_count: 200
summary: This document provides step-by-step instructions for adding, reusing, and managing LLM provider credentials within the user interface. It also explains how these credentials are encrypted and stored for security purposes.
tags:
    - llm-credentials
    - api-keys
    - provider-management
    - encryption
    - litellm
    - ui-configuration
category: guide
---

You can add LLM provider credentials on the UI. Once you add credentials you can reuse them when adding new models

## Add a credential + model[​](#add-a-credential--model "Direct link to Add a credential + model")

### 1. Navigate to LLM Credentials page[​](#1-navigate-to-llm-credentials-page "Direct link to 1. Navigate to LLM Credentials page")

Go to Models -&gt; LLM Credentials -&gt; Add Credential

### 2. Add credentials[​](#2-add-credentials "Direct link to 2. Add credentials")

Select your LLM provider, enter your API Key and click "Add Credential"

**Note: Credentials are based on the provider, if you select Vertex AI then you will see `Vertex Project`, `Vertex Location` and `Vertex Credentials` fields**

### 3. Use credentials when adding a model[​](#3-use-credentials-when-adding-a-model "Direct link to 3. Use credentials when adding a model")

Go to Add Model -&gt; Existing Credentials -&gt; Select your credential in the dropdown

## Create a Credential from an existing model[​](#create-a-credential-from-an-existing-model "Direct link to Create a Credential from an existing model")

Use this if you have already created a model and want to store the model credentials for future use

### 1. Select model to create a credential from[​](#1-select-model-to-create-a-credential-from "Direct link to 1. Select model to create a credential from")

Go to Models -&gt; Select your model -&gt; Credential -&gt; Create Credential

### 2. Use new credential when adding a model[​](#2-use-new-credential-when-adding-a-model "Direct link to 2. Use new credential when adding a model")

Go to Add Model -&gt; Existing Credentials -&gt; Select your credential in the dropdown

## Frequently Asked Questions[​](#frequently-asked-questions "Direct link to Frequently Asked Questions")

How are credentials stored? Credentials in the DB are encrypted/decrypted using `LITELLM_SALT_KEY`, if set. If not, then they are encrypted using `LITELLM_MASTER_KEY`. These keys should be kept secret and not shared with others.