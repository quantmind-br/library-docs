---
title: Amazon Bedrock | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/amazon_bedrock
source: sitemap
fetched_at: 2026-04-26T04:08:59.335312384-03:00
rendered_js: false
word_count: 272
summary: This document provides the requirements and prerequisites for deploying and querying Mistral AI models through the Amazon Bedrock managed service.
tags:
    - amazon-bedrock
    - mistral-ai
    - cloud-deployment
    - aws-sdk
    - boto3
    - model-inference
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI's open and commercial models can be deployed on the Amazon Bedrock cloud platform as fully managed endpoints. Amazon Bedrock is a serverless service so you don't have to manage any infrastructure.

## Available Models

- Mistral Large 3 (25.12)
- Ministral 3 3B, 8B, 14B (25.12)
- Mistral Large (24.07, 24.02)
- Mistral Small (24.02)
- Mixtral 8x7B
- Mistral 7B
- Pixtral Large (25.02)

## Prerequisites

The following items are required:

- Access to an **AWS account** within a region that supports the Amazon Bedrock service and offers access to your model of choice: see [the Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for model availability per region.
- An AWS **IAM principal** (user, role) with sufficient permissions, see [the AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) for more details.
- A local **code environment** set up with the relevant AWS SDK components, namely:
  - the AWS CLI: see [the AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for the installation procedure.
  - the `boto3` Python library: see the [AWS documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) for the installation procedure.

## Model Access

Follow the instructions on [the AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to unlock access to the Mistral model of your choice.

Amazon Bedrock models are accessible through the Converse API.

## Setup

Before running the examples below, make sure to:
- Properly configure the authentication credentials for your development environment. [The AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) provides an in-depth explanation on the required steps.
- Create a Python virtual environment with the `boto3` package (version `>= 1.34.131`).
- Set the following environment variables:
  - `AWS_REGION`: The region where the model is deployed (e.g. `us-west-2`)
  - `AWS_BEDROCK_MODEL_ID`: The model ID (e.g. `mistral.mistral-large-2407-v1:0`)

For more details and examples, refer to the following resources: