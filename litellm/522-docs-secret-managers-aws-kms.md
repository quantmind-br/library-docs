---
title: AWS Key Management V1 | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/aws_kms
source: sitemap
fetched_at: 2026-01-21T19:54:38.941354608-03:00
rendered_js: false
word_count: 51
summary: This document explains how to use AWS Key Management Service (KMS) to store and decrypt a hashed copy of the Proxy Master Key for secure key management.
tags:
    - aws-kms
    - key-management
    - security
    - enterprise-feature
    - environment-variables
category: configuration
---

info

✨ **This is an Enterprise Feature**

[Enterprise Pricing](https://www.litellm.ai/#pricing)

[Contact us here to get a free trial](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat)

tip

\[BETA] AWS Key Management v2 is on the enterprise tier. Go [here for docs](https://docs.litellm.ai/docs/proxy/enterprise#beta-aws-key-manager---key-decryption)

Use AWS KMS to storing a hashed copy of your Proxy Master Key in the environment.

```
export LITELLM_MASTER_KEY="djZ9xjVaZ..." # 👈 ENCRYPTED KEY
export AWS_REGION_NAME="us-west-2"
```

```
general_settings:
key_management_system:"aws_kms"
key_management_settings:
hosted_keys:["LITELLM_MASTER_KEY"]# 👈 WHICH KEYS ARE STORED ON KMS
```

[**See Decryption Code**](https://github.com/BerriAI/litellm/blob/a2da2a8f168d45648b61279d4795d647d94f90c9/litellm/utils.py#L10182)