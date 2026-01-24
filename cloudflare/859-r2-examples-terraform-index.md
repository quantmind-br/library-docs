---
title: Terraform · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/examples/terraform/index.md
source: llms
fetched_at: 2026-01-24T15:21:22.974961419-03:00
rendered_js: false
word_count: 107
summary: This document provides instructions and code examples for managing Cloudflare R2 buckets using Terraform and the Cloudflare provider.
tags:
    - cloudflare-r2
    - terraform
    - infrastructure-as-code
    - cloud-storage
    - bucket-management
    - cloudflare-provider
category: tutorial
---

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.



This example shows how to configure R2 with Terraform using the [Cloudflare provider](https://github.com/cloudflare/terraform-provider-cloudflare).

Note for using AWS provider

When using the Cloudflare Terraform provider, you can only manage buckets. To configure items such as CORS and object lifecycles, you will need to use the [AWS Provider](https://developers.cloudflare.com/r2/examples/terraform-aws/).

With [`terraform`](https://developer.hashicorp.com/terraform/downloads) installed, create `main.tf` and copy the content below replacing with your API Token.

```hcl
terraform {
  required_providers {
    cloudflare = {
      source = "cloudflare/cloudflare"
      version = "~> 4"
    }
  }
}


provider "cloudflare" {
  api_token = "<YOUR_API_TOKEN>"
}


resource "cloudflare_r2_bucket" "cloudflare-bucket" {
  account_id = "<YOUR_ACCOUNT_ID>"
  name       = "my-tf-test-bucket"
  location   = "WEUR"
}
```

You can then use `terraform plan` to view the changes and `terraform apply` to apply changes.