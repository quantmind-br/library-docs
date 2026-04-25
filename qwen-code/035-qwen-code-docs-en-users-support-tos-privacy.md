---
title: 'Qwen Code: Terms of Service and Privacy Notice'
url: https://qwenlm.github.io/qwen-code-docs/en/users/support/tos-privacy
source: github_pages
fetched_at: 2026-04-09T09:04:28.130353982-03:00
rendered_js: true
word_count: 846
summary: This document explains the terms of service and privacy policies governing Qwen Code's use, which vary based on whether the user authenticates via Qwen OAuth, Alibaba Cloud Coding Plan, or a third-party API key. It also details data collection practices regarding usage statistics and telemetry.
tags:
    - terms-of-service
    - privacy-policy
    - authentication-methods
    - data-collection
    - ai-assistant
    - qwen-code
category: guide
---

Qwen Code is an open-source AI coding assistant tool maintained by the Qwen Code team. This document outlines the terms of service and privacy policies that apply when using Qwen Code’s authentication methods and AI model services.

## How to determine your authentication method[](#how-to-determine-your-authentication-method)

Qwen Code supports three authentication methods to access AI models. Your authentication method determines which terms of service and privacy policies apply to your usage:

1. **Qwen OAuth** — Log in with your qwen.ai account (free daily quota)
2. **Alibaba Cloud Coding Plan** — Use an API key from Alibaba Cloud
3. **API Key** — Bring your own API key

For each authentication method, different Terms of Service and Privacy Notices may apply depending on the underlying service provider.

Authentication MethodProviderTerms of ServicePrivacy NoticeQwen OAuthQwen AI[Qwen Terms of Service](https://qwen.ai/termsservice) [Qwen Privacy Policy](https://qwen.ai/privacypolicy) Alibaba Cloud Coding PlanAlibaba CloudSee [details below](#2-if-you-are-using-alibaba-cloud-coding-plan)See [details below](#2-if-you-are-using-alibaba-cloud-coding-plan)API KeyVarious ProvidersDepends on your chosen API provider (OpenAI, Anthropic, etc.)Depends on your chosen API provider

## 1. If you are using Qwen OAuth Authentication[](#1-if-you-are-using-qwen-oauth-authentication)

When you authenticate using your qwen.ai account, these Terms of Service and Privacy Notice documents apply:

- **Terms of Service:** Your use is governed by the [Qwen Terms of Service](https://qwen.ai/termsservice) .
- **Privacy Notice:** The collection and use of your data is described in the [Qwen Privacy Policy](https://qwen.ai/privacypolicy) .

For details about authentication setup, quotas, and supported features, see [Authentication Setup](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/).

## 2. If you are using Alibaba Cloud Coding Plan[](#2-if-you-are-using-alibaba-cloud-coding-plan)

When you authenticate using an API key from Alibaba Cloud, the applicable Terms of Service and Privacy Notice from Alibaba Cloud apply.

Alibaba Cloud Coding Plan is available in two regions:

- **阿里云百炼 (aliyun.com)** — [bailian.console.aliyun.com](https://bailian.console.aliyun.com)
- **Alibaba Cloud (alibabacloud.com)** — [bailian.console.alibabacloud.com](https://bailian.console.alibabacloud.com)

**Important**

When using Alibaba Cloud Coding Plan, you are subject to Alibaba Cloud’s terms and privacy policies. Please review their documentation for specific details about data usage, retention, and privacy practices.

## 3. If you are using your own API Key[](#3-if-you-are-using-your-own-api-key)

When you authenticate using API keys from other providers, the applicable Terms of Service and Privacy Notice depend on your chosen provider.

**Important**

When using your own API key, you are subject to the terms and privacy policies of your chosen API provider, not Qwen Code’s terms. Please review your provider’s documentation for specific details about data usage, retention, and privacy practices.

Qwen Code supports various OpenAI-compatible providers. Please refer to your specific provider’s terms of service and privacy policy for detailed information.

## Usage Statistics and Telemetry[](#usage-statistics-and-telemetry)

Qwen Code may collect anonymous usage statistics and [telemetry](https://qwenlm.github.io/qwen-code-docs/en/developers/development/telemetry/) data to improve the user experience and product quality. This data collection is optional and can be controlled through configuration settings.

### What Data is Collected[](#what-data-is-collected)

When enabled, Qwen Code may collect:

- Anonymous usage statistics (commands run, performance metrics)
- Error reports and crash data
- Feature usage patterns

### Data Collection by Authentication Method[](#data-collection-by-authentication-method)

- **Qwen OAuth:** Usage statistics are governed by Qwen’s privacy policy. You can opt-out through Qwen Code’s configuration settings.
- **Alibaba Cloud Coding Plan:** Usage statistics are governed by Alibaba Cloud’s privacy policy. You can opt-out through Qwen Code’s configuration settings.
- **API Key:** No additional data is collected by Qwen Code beyond what your chosen API provider collects.

## Frequently Asked Questions (FAQ)[](#frequently-asked-questions-faq)

### 1. Is my code, including prompts and answers, used to train AI models?[](#1-is-my-code-including-prompts-and-answers-used-to-train-ai-models)

Whether your code, including prompts and answers, is used to train AI models depends on your authentication method and the specific AI service provider you use:

- **Qwen OAuth**: Data usage is governed by [Qwen’s Privacy Policy](https://qwen.ai/privacy) . Please refer to their policy for specific details about data collection and model training practices.
- **Alibaba Cloud Coding Plan**: Data usage is governed by Alibaba Cloud’s privacy policy. Please refer to their policy for specific details about data collection and model training practices.
- **API Key**: Data usage depends entirely on your chosen API provider. Each provider has their own data usage policies. Please review the privacy policy and terms of service of your specific provider.

**Important**: Qwen Code itself does not use your prompts, code, or responses for model training. Any data usage for training purposes would be governed by the policies of the AI service provider you authenticate with.

### 2. What are Usage Statistics and what does the opt-out control?[](#2-what-are-usage-statistics-and-what-does-the-opt-out-control)

The **Usage Statistics** setting controls optional data collection by Qwen Code for improving the user experience and product quality.

When enabled, Qwen Code may collect:

- Anonymous telemetry (commands run, performance metrics, feature usage)
- Error reports and crash data
- General usage patterns

**What is NOT collected by Qwen Code:**

- Your code content
- Prompts sent to AI models
- Responses from AI models
- Personal information

The Usage Statistics setting only controls data collection by Qwen Code itself. It does not affect what data your chosen AI service provider (Qwen, OpenAI, etc.) may collect according to their own privacy policies.

### 3. How do I switch between authentication methods?[](#3-how-do-i-switch-between-authentication-methods)

You can switch between Qwen OAuth, Alibaba Cloud Coding Plan, and your own API key at any time:

1. **During startup**: Choose your preferred authentication method when prompted
2. **Within the CLI**: Use the `/auth` command to reconfigure your authentication method
3. **Environment variables**: Set up `.env` files for automatic API key authentication

For detailed instructions, see the [Authentication Setup](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/#environment-variables-for-api-access) documentation.