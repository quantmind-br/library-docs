---
title: CLIProxyAPI是什么？ | CLIProxyAPI
url: https://help.router-for.me/cn/introduction/what-is-cliproxyapi
source: crawler
fetched_at: 2026-01-14T22:09:57.25539544-03:00
rendered_js: false
word_count: 128
summary: This document describes CLIProxyAPI, a proxy server that provides OpenAI/Gemini/Claude/Codex compatible API endpoints for command-line interfaces. It supports various models, multi-account management, and features like streaming responses and function calls.
tags:
    - cli-proxy
    - openai-api
    - gemini-api
    - claude-api
    - codex-api
    - llm-proxy
category: guide
---

**CLIProxyAPI** 是一个为 CLI 提供 OpenAI/Gemini/Claude/Codex 兼容 API 接口的代理服务器。

您可以使用本地或多账户的CLI方式，通过任何与 OpenAI（包括Responses）/Gemini/Claude 兼容的客户端和SDK进行访问。

## 功能特性 [​](#%E5%8A%9F%E8%83%BD%E7%89%B9%E6%80%A7)

- 为 CLI 模型提供 OpenAI/Gemini/Claude/Codex 兼容的 API 端点
- Gemini CLI 支持（OAuth 登录）
- 反重力 支持（OAuth 登录）
- OpenAI Codex（GPT 系列）支持（OAuth 登录）
- Claude Code 支持（OAuth 登录）
- Qwen Code 支持（OAuth 登录）
- iFlow 支持（OAuth 登录）
- 支持流式与非流式响应
- 函数调用/工具支持
- 多模态输入（文本、图片）
- 多账户支持与轮询负载均衡（Gemini、OpenAI、Claude、Qwen 与 iFlow）
- 简单的 CLI 身份验证流程（Gemini、OpenAI、Claude、Qwen 与 iFlow）
- 支持 Gemini AIStudio API 密钥
- 支持 AI Studio Build 多账户轮询
- 支持 Gemini CLI 多账户轮询
- 支持 反重力 多账户轮询
- 支持 Claude Code 多账户轮询
- 支持 Qwen Code 多账户轮询
- 支持 iFlow 多账户轮询
- 支持 OpenAI Codex 多账户轮询
- 通过配置接入上游 OpenAI 兼容提供商（例如 OpenRouter）

## 支持的模型 [​](#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A8%A1%E5%9E%8B)

- gemini-3-pro-preview
- gemini-3-pro-image-preview
- gemini-2.5-pro
- gemini-2.5-flash
- gemini-2.5-flash-lite
- gemini-2.5-flash-image
- gemini-2.5-flash-image-preview
- gemini-pro-latest
- gemini-flash-latest
- gemini-flash-lite-latest
- gpt-5
- gpt-5-codex
- claude-opus-4-1-20250805
- claude-opus-4-20250514
- claude-sonnet-4-20250514
- claude-sonnet-4-5-20250929
- claude-haiku-4-5-20251001
- claude-3-7-sonnet-20250219
- claude-3-5-haiku-20241022
- qwen3-coder-plus
- qwen3-coder-flash
- qwen3-max
- qwen3-vl-plus
- deepseek-v3.2
- deepseek-v3.1
- deepseek-r1
- deepseek-v3
- kimi-k2
- glm-4.6
- tstars2.0
- 以及其他 iFlow 支持的模型
- Gemini 模型在需要时自动切换到对应的 preview 版本