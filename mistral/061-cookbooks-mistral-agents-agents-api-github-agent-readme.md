---
title: Github Automation with Mistral AI Agents - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-github_agent-readme
source: crawler
fetched_at: 2026-01-29T07:33:46.585105178-03:00
rendered_js: false
word_count: 239
summary: This cookbook provides a guide for building a GitHub agent using Mistral Medium and the Model Context Protocol (MCP) to automate repository management and pull requests. It covers environment setup with Docker, GitHub token configuration, and tool integration using Chainlit.
tags:
    - mistral-ai
    - github-api
    - mcp-server
    - ai-agents
    - docker
    - automation
    - chainlit
category: tutorial
---

This cookbook show how to create an Agent that use mistral Medium to perform some actions on your github.

> WIP: This cookbook is minimal working example and will still evolve in the near future.

[![Github Agent](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/gif/Github_PR.gif)](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-github_agent-readme)

## Use Case

- Create a New Repo.
- Manage PRs.
- Collaborate with the AI to create some code and upload some code to an existing repo.

## Installation

## Environment Setup

In this example, we are relying on the docker mcp :

hence you will to make sure that :

1. you have docker on your computer.
2. you pull the associated images:

3)You have created a token for github. You can do so [HERE](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-github_agent-readme)

> **Disclaimer:** The coding is done by AI, hence when creating your GitHub token, for enhanced security, it is strongly recommended to create a [fine-grained personal access token](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-github_agent-readme) with only the minimum necessary permissions for the tasks you intend to perform.

Set your MistralAI API key and your Github key:

## Usage

Run the application:

Ask questions like:

- "Create a repo under my username : called ..."
- "Generate the files for a todo app and push them to repo ... under branch name ..."

## MCP Usage

There is two type of MCPs.

STDIO : Local usage of tools. SSE : Remote usage of tools.

In this example, we leverage the chainlit integration of MCP tools, and directly convert them in our API ! Hence do not hesitate to test other MCP Servers yourself. ![MCP from chainlit](https://docs.mistral.ai/cookbooks/mistral/agents/agents_api/github_agent/public/sse_mcp.png)