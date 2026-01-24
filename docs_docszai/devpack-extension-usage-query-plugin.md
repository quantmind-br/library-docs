---
title: Usage Query Plugin
url: https://docs.z.ai/devpack/extension/usage-query-plugin.md
source: llms
fetched_at: 2026-01-24T11:02:34.990471383-03:00
rendered_js: false
word_count: 129
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage Query Plugin

> Query quota and usage statistics for GLM Coding Plan.

The **glm-plan-usage** plugin allows you to query your current quota and usage statistics for the GLM Coding Plan directly within your Claude Code.

**Github Repo**: [zai-coding-plugins](https://github.com/zai-org/zai-coding-plugins)

## Prerequisites

* Node.js 18 or higher
* Install Claude Code CLI (See [Claude Code](/devpack/tool/claude))

## Quick Start

<Note>
  Install the marketplace within Claude Code to access the plugins.
</Note>

<Tabs>
  <Tab title="Method A: Manual Installation">
    Prerequisite: Git environment is set up.

    **1. Install the Marketplace**

    ```shell  theme={null}
    claude plugin marketplace add zai-org/zai-coding-plugins
    ```

    **2. Install Plugin**

    ```shell  theme={null}
    claude plugin install glm-plan-usage@zai-coding-plugins
    ```
  </Tab>

  <Tab title="Method B: Automated Tool">
    Run the `npx @z_ai/coding-helper` tool to manage and install the plugins directly.

    `Start` -> `Coding Tool` -> `Claude Code` -> `Plugin Marketplace`

    ```bash  theme={null}
    npx @z_ai/coding-helper
    ```
  </Tab>
</Tabs>

## Usage

<Steps>
  <Step title="Start Claude Code">
    Navigate to your project and start Claude Code:

    ```bash  theme={null}
    claude
    ```
  </Step>

  <Step title="Query Usage">
    Use the following command to check your current quota and usage:

    ```bash  theme={null}
    /glm-plan-usage:usage-query
    ```
  </Step>
</Steps>

## Build Marketplace Together

<CardGroup cols={2}>
  <Card title="GitHub Repository" icon="github" href="https://github.com/zai-org/zai-coding-plugins">
    View source code, submit issues, contribute
  </Card>

  <Card title="Plugin Marketplace" icon="book" href="https://code.claude.com/docs/en/plugins">
    View how to build the plugin
  </Card>
</CardGroup>