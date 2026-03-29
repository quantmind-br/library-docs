---
title: AWS Secret Manager | liteLLM
url: https://docs.litellm.ai/docs/secret_managers/aws_secret_manager
source: sitemap
fetched_at: 2026-01-21T19:54:39.193951357-03:00
rendered_js: false
word_count: 158
summary: This document provides instructions for configuring LiteLLM to use AWS Secret Manager for storing and retrieving API keys, virtual keys, and other secrets using various IAM authentication methods.
tags:
    - aws-secret-manager
    - key-management
    - iam-roles
    - security
    - litellm-proxy
    - aws-iam
category: configuration
---

Store your proxy keys in AWS Secret Manager.

FeatureSupportDescriptionReading Secrets✅Read secrets e.g `OPENAI_API_KEY`Writing Secrets✅Store secrets e.g `Virtual Keys`

## Proxy Usage[​](#proxy-usage "Direct link to Proxy Usage")

1. Save AWS Credentials in your environment

```
os.environ["AWS_ACCESS_KEY_ID"] = ""  # Access key
os.environ["AWS_SECRET_ACCESS_KEY"] = "" # Secret access key
os.environ["AWS_REGION_NAME"] = "" # us-east-1, us-east-2, us-west-1, us-west-2
```

2. Enable AWS Secret Manager in config.

<!--THE END-->

- Read Keys from AWS Secret Manager
- Write Virtual Keys to AWS Secret Manager
- Read + Write Keys with AWS Secret Manager

```
general_settings:
master_key: os.environ/litellm_master_key 
key_management_system:"aws_secret_manager"# 👈 KEY CHANGE
key_management_settings:
hosted_keys:["litellm_master_key"]# 👈 Specify which env keys you stored on AWS 

```

3. Run proxy

```
litellm --config /path/to/config.yaml
```

## Using K/V pairs in 1 AWS Secret[​](#using-kv-pairs-in-1-aws-secret "Direct link to Using K/V pairs in 1 AWS Secret")

You can read multiple keys from a single AWS Secret using the `primary_secret_name` parameter:

```
general_settings:
key_management_system:"aws_secret_manager"
key_management_settings:
hosted_keys:[
"OPENAI_API_KEY_MODEL_1",
"OPENAI_API_KEY_MODEL_2",
]
primary_secret_name:"litellm_secrets"# 👈 Read multiple keys from one JSON secret
```

The `primary_secret_name` allows you to read multiple keys from a single AWS Secret as a JSON object. For example, the "litellm\_secrets" would contain:

```
{
"OPENAI_API_KEY_MODEL_1":"sk-key1...",
"OPENAI_API_KEY_MODEL_2":"sk-key2..."
}
```

This reduces the number of AWS Secrets you need to manage.

## IAM Role Assumption[​](#iam-role-assumption "Direct link to IAM Role Assumption")

Use IAM roles instead of static AWS credentials for better security.

### Basic IAM Role[​](#basic-iam-role "Direct link to Basic IAM Role")

```
general_settings:
key_management_system:"aws_secret_manager"
key_management_settings:
store_virtual_keys:true
aws_region_name:"us-east-1"
aws_role_name:"arn:aws:iam::123456789012:role/LiteLLMSecretManagerRole"
aws_session_name:"litellm-session"
```

### Cross-Account Access[​](#cross-account-access "Direct link to Cross-Account Access")

```
general_settings:
key_management_system:"aws_secret_manager"
key_management_settings:
store_virtual_keys:true
aws_region_name:"us-east-1"
aws_role_name:"arn:aws:iam::999999999999:role/CrossAccountRole"
aws_external_id:"unique-external-id"
```

### EKS with IRSA[​](#eks-with-irsa "Direct link to EKS with IRSA")

```
general_settings:
key_management_system:"aws_secret_manager"
key_management_settings:
store_virtual_keys:true
aws_region_name:"us-east-1"
aws_role_name:"arn:aws:iam::123456789012:role/LiteLLMServiceAccountRole"
aws_web_identity_token:"os.environ/AWS_WEB_IDENTITY_TOKEN_FILE"
```

### Configuration Parameters[​](#configuration-parameters "Direct link to Configuration Parameters")

ParameterDescription`aws_region_name`AWS region`aws_role_name`IAM role ARN to assume`aws_session_name`Session name (optional)`aws_external_id`External ID for cross-account`aws_profile_name`AWS profile from `~/.aws/credentials``aws_web_identity_token`OIDC token path for IRSA`aws_sts_endpoint`Custom STS endpoint for VPC