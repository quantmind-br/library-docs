---
title: Github Actions：qwen-code-action
url: https://qwenlm.github.io/qwen-code-docs/en/users/integration-github-action
source: github_pages
fetched_at: 2026-04-09T09:03:51.900612521-03:00
rendered_js: true
word_count: 1278
summary: This document explains the qwen-code-action, a GitHub Action that integrates Qwen Code to automate tasks like PR reviews and issue triage. It details setup steps, available features such as on-demand collaboration and tool extensibility, and various configuration inputs for customization.
tags:
    - github-actions
    - ai-integration
    - coding-assistance
    - automation-workflow
    - qwen-code
    - api-key
category: guide
---

## Overview[](#overview)

`qwen-code-action` is a GitHub Action that integrates [Qwen Code](https://github.com/QwenLM/qwen-code)  into your development workflow via the [Qwen Code CLI](https://github.com/QwenLM/qwen-code-action/) . It acts both as an autonomous agent for critical routine coding tasks, and an on-demand collaborator you can quickly delegate work to.

Use it to perform GitHub pull request reviews, triage issues, perform code analysis and modification, and more using [Qwen Code](https://github.com/QwenLM/qwen-code)  conversationally (e.g., `@qwencoder fix this issue`) directly inside your GitHub repositories.

## Features[](#features)

- **Automation**: Trigger workflows based on events (e.g. issue opening) or schedules (e.g. nightly).
- **On-demand Collaboration**: Trigger workflows in issue and pull request comments by mentioning the [Qwen Code CLI](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) (e.g., `@qwencoder /review`).
- **Extensible with Tools**: Leverage [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction/) models’ tool-calling capabilities to interact with other CLIs like the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli)  (`gh`).
- **Customizable**: Use a `QWEN.md` file in your repository to provide project-specific instructions and context to [Qwen Code CLI](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/).

## Quick Start[](#quick-start)

Get started with Qwen Code CLI in your repository in just a few minutes:

### 1. Get a Qwen API Key[](#1-get-a-qwen-api-key)

Obtain your API key from [DashScope](https://help.aliyun.com/zh/model-studio/qwen-code)  (Alibaba Cloud’s AI platform)

### 2. Add it as a GitHub Secret[](#2-add-it-as-a-github-secret)

Store your API key as a secret named `QWEN_API_KEY` in your repository:

- Go to your repository’s **Settings &gt; Secrets and variables &gt; Actions**
- Click **New repository secret**
- Name: `QWEN_API_KEY`, Value: your API key

### 3. Update your .gitignore[](#3-update-your-gitignore)

Add the following entries to your `.gitignore` file:

```
# qwen-code-cli settings
.qwen/

# GitHub App credentials
gha-creds-*.json
```

### 4. Choose a Workflow[](#4-choose-a-workflow)

You have two options to set up a workflow:

**Option A: Use setup command (Recommended)**

1. Start the Qwen Code CLI in your terminal:
2. In Qwen Code CLI in your terminal, type:

**Option B: Manually copy workflows**

1. Copy the pre-built workflows from the [`examples/workflows`](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/) directory to your repository’s `.github/workflows` directory. Note: the `qwen-dispatch.yml` workflow must also be copied, which triggers the workflows to run.

### 5. Try it out[](#5-try-it-out)

**Pull Request Review:**

- Open a pull request in your repository and wait for automatic review
- Comment `@qwencoder /review` on an existing pull request to manually trigger a review

**Issue Triage:**

- Open an issue and wait for automatic triage
- Comment `@qwencoder /triage` on existing issues to manually trigger triaging

**General AI Assistance:**

- In any issue or pull request, mention `@qwencoder` followed by your request
- Examples:
  
  - `@qwencoder explain this code change`
  - `@qwencoder suggest improvements for this function`
  - `@qwencoder help me debug this error`
  - `@qwencoder write unit tests for this component`

## Workflows[](#workflows)

This action provides several pre-built workflows for different use cases. Each workflow is designed to be copied into your repository’s `.github/workflows` directory and customized as needed.

### Qwen Code Dispatch[](#qwen-code-dispatch)

This workflow acts as a central dispatcher for Qwen Code CLI, routing requests to the appropriate workflow based on the triggering event and the command provided in the comment. For a detailed guide on how to set up the dispatch workflow, go to the [Qwen Code Dispatch workflow documentation](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/).

### Issue Triage[](#issue-triage)

This action can be used to triage GitHub Issues automatically or on a schedule. For a detailed guide on how to set up the issue triage system, go to the [GitHub Issue Triage workflow documentation](https://qwenlm.github.io/qwen-code-docs/en/users/examples/workflows/issue-triage/).

### Pull Request Review[](#pull-request-review)

This action can be used to automatically review pull requests when they are opened. For a detailed guide on how to set up the pull request review system, go to the [GitHub PR Review workflow documentation](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/).

### Qwen Code CLI Assistant[](#qwen-code-cli-assistant)

This type of action can be used to invoke a general-purpose, conversational Qwen Code AI assistant within the pull requests and issues to perform a wide range of tasks. For a detailed guide on how to set up the general-purpose Qwen Code CLI workflow, go to the [Qwen Code Assistant workflow documentation](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/).

## Configuration[](#configuration)

### Inputs[](#inputs)

- []()[`qwen*api_key`](#user-content-__input_qwen_api_key): \*(Optional)_ The API key for the Qwen API.
- []()[`qwen*cli_version`](#user-content-__input_qwen_cli_version): \*(Optional, default: `latest`)_ The version of the Qwen Code CLI to install. Can be “latest”, “preview”, “nightly”, a specific version number, or a git branch, tag, or commit. For more information, see [Qwen Code CLI releases](https://github.com/QwenLM/qwen-code-action/blob/main/docs/releases.md) .
- []()[`qwen*debug`](#user-content-__input_qwen_debug): \*(Optional)_ Enable debug logging and output streaming.
- []()[`qwen*model`](#user-content-__input_qwen_model): \*(Optional)_ The model to use with Qwen Code.
- []()[`prompt`](#user-content-__input_prompt): *(Optional, default: `You are a helpful assistant.`)* A string passed to the Qwen Code CLI’s [`--prompt` argument](https://github.com/QwenLM/qwen-code-action/blob/main/docs/cli/configuration.md#command-line-arguments).
- []()[`settings`](#user-content-__input_settings): *(Optional)* A JSON string written to `.qwen/settings.json` to configure the CLI’s *project* settings. For more details, see the documentation on [settings files](https://github.com/QwenLM/qwen-code-action/blob/main/docs/cli/configuration.md#settings-files) .
- []()[`use*qwen_code_assist`](#user-content-__input_use_qwen_code_assist): \*(Optional, default: `false`)_ Whether to use Code Assist for Qwen Code model access instead of the default Qwen Code API key. For more information, see the [Qwen Code CLI documentation](https://github.com/QwenLM/qwen-code-action/blob/main/docs/cli/authentication.md) .
- []()[`use*vertex_ai`](#user-content-__input_use_vertex_ai): \*(Optional, default: `false`)_ Whether to use Vertex AI for Qwen Code model access instead of the default Qwen Code API key. For more information, see the [Qwen Code CLI documentation](https://github.com/QwenLM/qwen-code-action/blob/main/docs/cli/authentication.md) .
- []()[`extensions`](#user-content-__input_extensions): *(Optional)* A list of Qwen Code CLI extensions to install.
- []()[`upload*artifacts`](#user-content-__input_upload_artifacts): \*(Optional, default: `false`)_ Whether to upload artifacts to the github action.
- []()[`use*pnpm`](#user-content-__input_use_pnpm): \*(Optional, default: `false`)_ Whether or not to use pnpm instead of npm to install qwen-code-cli
- []()[`workflow*name`](#user-content-__input_workflow_name): \*(Optional, default: `${{ github.workflow }}`)_ The GitHub workflow name, used for telemetry purposes.

### Outputs[](#outputs)

- []()[`summary`](#user-content-__output_summary): The summarized output from the Qwen Code CLI execution.
- []()[`error`](#user-content-__output_error): The error output from the Qwen Code CLI execution, if any.

### Repository Variables[](#repository-variables)

We recommend setting the following values as repository variables so they can be reused across all workflows. Alternatively, you can set them inline as action inputs in individual workflows or to override repository-level values.

NameDescriptionTypeRequiredWhen Required`DEBUG`Enables debug logging for the Qwen Code CLI.VariableNoNever`QWEN_CLI_VERSION`Controls which version of the Qwen Code CLI is installed.VariableNoPinning the CLI version`APP_ID`GitHub App ID for custom authentication.VariableNoUsing a custom GitHub App

To add a repository variable:

1. Go to your repository’s **Settings &gt; Secrets and variables &gt; Actions &gt; New variable**.
2. Enter the variable name and value.
3. Save.

For details about repository variables, refer to the [GitHub documentation on variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables#creating-configuration-variables-for-a-repository) .

### Secrets[](#secrets)

You can set the following secrets in your repository:

NameDescriptionRequiredWhen Required`QWEN_API_KEY`Your Qwen API key from DashScope.YesRequired for all workflows that call Qwen.`APP_PRIVATE_KEY`Private key for your GitHub App (PEM format).NoUsing a custom GitHub App.

To add a secret:

1. Go to your repository’s **Settings &gt; Secrets and variables &gt;Actions &gt; New repository secret**.
2. Enter the secret name and value.
3. Save.

For more information, refer to the [official GitHub documentation on creating and using encrypted secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) .

## Authentication[](#authentication)

This action requires authentication to the GitHub API and optionally to Qwen Code services.

### GitHub Authentication[](#github-authentication)

You can authenticate with GitHub in two ways:

1. **Default `GITHUB_TOKEN`:** For simpler use cases, the action can use the default `GITHUB_TOKEN` provided by the workflow.
2. **Custom GitHub App (Recommended):** For the most secure and flexible authentication, we recommend creating a custom GitHub App.

For detailed setup instructions for both Qwen and GitHub authentication, go to the [**Authentication documentation**](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/).

## Extensions[](#extensions)

The Qwen Code CLI can be extended with additional functionality through extensions. These extensions are installed from source from their GitHub repositories.

For detailed instructions on how to set up and configure extensions, go to the [Extensions documentation](https://qwenlm.github.io/qwen-code-docs/en/developers/extensions/extension/).

## Best Practices[](#best-practices)

To ensure the security, reliability, and efficiency of your automated workflows, we strongly recommend following our best practices. These guidelines cover key areas such as repository security, workflow configuration, and monitoring.

Key recommendations include:

- **Securing Your Repository:** Implementing branch and tag protection, and restricting pull request approvers.
- **Monitoring and Auditing:** Regularly reviewing action logs and enabling OpenTelemetry for deeper insights into performance and behavior.

For a comprehensive guide on securing your repository and workflows, please refer to our [**Best Practices documentation**](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/).

## Customization[](#customization)

Create a QWEN.md file in the root of your repository to provide project-specific context and instructions to [Qwen Code CLI](https://qwenlm.github.io/qwen-code-docs/en/users/common-workflow/). This is useful for defining coding conventions, architectural patterns, or other guidelines the model should follow for a given repository.

## Contributing[](#contributing)

Contributions are welcome! Check out the Qwen Code CLI **Contributing Guide** for more details on how to get started.