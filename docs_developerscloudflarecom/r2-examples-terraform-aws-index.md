---
title: Terraform (AWS) · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/examples/terraform-aws/index.md
source: llms
fetched_at: 2026-01-24T15:21:22.403721226-03:00
rendered_js: false
word_count: 123
summary: This document provides instructions and configuration examples for managing Cloudflare R2 resources using Terraform and the AWS provider. It details the specific provider settings and S3-compatible resource definitions required for successful integration.
tags:
    - terraform
    - cloudflare-r2
    - aws-provider
    - infrastructure-as-code
    - bucket-configuration
    - s3-compatibility
category: configuration
---

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.



This example shows how to configure R2 with Terraform using the [AWS provider](https://github.com/hashicorp/terraform-provider-aws).

Note for using AWS provider

For using only the Cloudflare provider, see [Terraform](https://developers.cloudflare.com/r2/examples/terraform/).

With [`terraform`](https://developer.hashicorp.com/terraform/downloads) installed:

1. Create `main.tf` file, or edit your existing Terraform configuration
2. Populate the endpoint URL at `endpoints.s3` with your [Cloudflare account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/)
3. Populate `access_key` and `secret_key` with the corresponding [R2 API credentials](https://developers.cloudflare.com/r2/api/tokens/).
4. Ensure that `skip_region_validation = true`, `skip_requesting_account_id = true`, and `skip_credentials_validation = true` are set in the provider configuration.

```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5"
    }
  }
}


provider "aws" {
  region = "us-east-1"


  access_key = <R2 Access Key>
  secret_key = <R2 Secret Key>


  # Required for R2.
  # These options disable S3-specific validation on the client (Terraform) side.
  skip_credentials_validation = true
  skip_region_validation      = true
  skip_requesting_account_id  = true


  endpoints {
    s3 = "https://<account id>.r2.cloudflarestorage.com"
  }
}


resource "aws_s3_bucket" "default" {
  bucket = "<org>-test"
}


resource "aws_s3_bucket_cors_configuration" "default" {
  bucket   = aws_s3_bucket.default.id


  cors_rule {
    allowed_methods = ["GET"]
    allowed_origins = ["*"]
  }
}


resource "aws_s3_bucket_lifecycle_configuration" "default" {
  bucket = aws_s3_bucket.default.id


  rule {
    id     = "expire-bucket"
    status = "Enabled"
    expiration {
      days = 1
    }
  }


  rule {
    id     = "abort-multipart-upload"
    status = "Enabled"
    abort_incomplete_multipart_upload {
      days_after_initiation = 1
    }
  }
}
```

You can then use `terraform plan` to view the changes and `terraform apply` to apply changes.