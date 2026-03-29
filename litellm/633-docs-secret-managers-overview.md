---
title: Secret Managers Overview | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/overview
source: sitemap
fetched_at: 2026-01-21T19:54:48.309527579-03:00
rendered_js: false
word_count: 58
summary: This document explains how to configure LiteLLM to integrate with external key management systems for reading and writing API secrets and virtual keys.
tags:
    - secret-management
    - litellm-configuration
    - kms-integration
    - aws-secret-manager
    - security
    - virtual-keys
category: configuration
---

LiteLLM supports **reading secrets (eg. `OPENAI_API_KEY`)** and **writing secrets (eg. Virtual Keys)** from Azure Key Vault, Google Secret Manager, Hashicorp Vault, CyberArk Conjur, and AWS Secret Manager.

```
general_settings:
key_management_system:"aws_secret_manager"# REQUIRED
key_management_settings:

# Storing Virtual Keys Settings
store_virtual_keys:true# OPTIONAL. Defaults to False, when True will store virtual keys in secret manager
prefix_for_stored_virtual_keys:"litellm/"# OPTIONAL.I f set, this prefix will be used for stored virtual keys in the secret manager

# Access Mode Settings
access_mode:"write_only"# OPTIONAL. Literal["read_only", "write_only", "read_and_write"]. Defaults to "read_only"

# Hosted Keys Settings
hosted_keys:["litellm_master_key"]# OPTIONAL. Specify which env keys you stored on AWS

# K/V pairs in 1 AWS Secret Settings
primary_secret_name:"litellm_secrets"# OPTIONAL. Read multiple keys from one JSON secret on AWS Secret Manager
```

Team-level secret manager settings let every team bring their own key-management configuration. These settings are used when creating virtual keys tied to the team.

Once saved, LiteLLM will use this configuration.