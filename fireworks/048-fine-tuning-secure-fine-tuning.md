---
title: Secure Training (BYOB) - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/secure-fine-tuning
source: sitemap
fetched_at: 2026-04-27T20:18:38.037158855-03:00
rendered_js: false
word_count: 300
summary: This document explains how users can enable secure model fine-tuning by connecting their proprietary datasets and infrastructure to Fireworks, detailing integration methods for Google Cloud Storage (GCS), AWS S3, and Azure Blob Storage.
tags:
    - secure-fine-tuning
    - data-storage
    - gcs-integration
    - aws-s3
    - azure-blob
    - byob
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Secure Training (BYOB)

Maintain full control over sensitive components and data while fine-tuning on Fireworks. Your training data never persists on the platform beyond active workflows.

## GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning. Fireworks creates proxy datasets referencing your external buckets — data is accessed only during fine-tuning within a secure, isolated cluster.

### Required Permissions

Grant access to three service accounts:

| Service Account | Required Role |
|-----------------|---------------|
| `fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com` | Custom role with `storage.buckets.getIamPolicy` |
| `inference@fw-ai-cp-prod.iam.gserviceaccount.com` | Storage Object Viewer |
| Your company's Fireworks account email | Storage Object Viewer |

```bash
# Fireworks Control Plane
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com \
  --role=projects/<YOUR_PROJECT>/roles/<YOUR_CUSTOM_ROLE>

# Inference Service Account
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer

# Your Company's Fireworks Service Account (get email with firectl account get)
gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
  --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
  --role=roles/storage.objectViewer
```

### Usage

```bash
# Create dataset referencing your GCS bucket
firectl dataset create {DATASET_NAME} --external-url gs://bucket-name/path/to/data.jsonl

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME}
```

## AWS S3 Bucket Integration

Access S3 data using GCP-to-AWS OIDC federation — no long-lived credentials stored.

### IAM Role Setup

Create an IAM role with a trust policy allowing Fireworks to assume it via web identity federation:

- **Federated Principal:** `accounts.google.com`
- **Action:** `sts:AssumeRoleWithWebIdentity`
- **Condition:** `accounts.google.com:aud` equals `117388763667264115668`

Attach a policy granting `s3:GetObject` and `s3:ListBucket` on your bucket. See [AWS OIDC federation documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html) for detailed steps.

### Usage

```bash
# Create dataset referencing your S3 bucket
firectl dataset create {DATASET_NAME} --external-url s3://bucket-name/path/to/data.jsonl

# Use in fine-tuning job with IAM role
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --aws-iam-role "arn:aws:iam::{AWS_ACCOUNT_ID}:role/{ROLE_NAME}"
```

### Alternative: Credentials Secret

Use static AWS access keys stored in a Fireworks secret instead of IAM federation:

```bash
# Create secret
firectl secret create --name aws-creds \
  --aws-access-key-id "AKIA..." \
  --aws-secret-access-key "..."

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --aws-credentials-secret "accounts/{ACCOUNT}/secrets/aws-creds"
```

## Azure Blob Storage Integration

Access Azure data using GCP-to-Azure Workload Identity Federation — no long-lived credentials stored.

### Federated Identity Setup

Create an App Registration (or user-assigned Managed Identity) in Azure AD with a federated credential trusting the Fireworks GCP service account:

- **Issuer:** `https://accounts.google.com`
- **Subject identifier:** `117388763667264115668`
- **Audience:** `api://AzureADTokenExchange`

Assign the **Storage Blob Data Reader** role on your storage account or container. See [Azure workload identity federation documentation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust) for detailed steps.

### Usage

```bash
# Create dataset referencing your Azure Blob container
firectl dataset create {DATASET_NAME} \
  --external-url https://{STORAGE_ACCOUNT}.blob.core.windows.net/{CONTAINER}/path/to/data.jsonl

# Use in fine-tuning job with managed identity federation
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --azure-managed-identity-client-id "{MANAGED_IDENTITY_CLIENT_ID}" \
  --azure-tenant-id "{AZURE_TENANT_ID}"
```

### Alternative: Credentials Secret

Store Azure credentials in a Fireworks secret. The secret value must be a JSON object containing `connection_string`, `sas_token`, or `account_key`:

```bash
# Create secret with Azure credentials
firectl secret create --name azure-creds \
  --value '{"sas_token": "sv=2023-01-03&ss=b&srt=o&sp=rl&se=..."}'

# Use in fine-tuning job
firectl sftj create \
  --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
  --base-model "accounts/fireworks/models/{MODEL}" \
  --output-model {TRAINED_MODEL_NAME} \
  --azure-credentials-secret "accounts/{ACCOUNT}/secrets/azure-creds"
```

#secure-fine-tuning #data-storage #gcs-integration #aws-s3 #azure-blob #byob
