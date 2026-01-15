---
description: Auto-generated documentation index for CLIProxyAPI
generated: 2026-01-15T01:17:43.852141Z
source: https://help.router-for.me/
total_docs: 90
categories: 9
---

# CLIProxyAPI Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://help.router-for.me/ |
| **Generated** | 2026-01-15T01:17:43.852141Z |
| **Total Documents** | 90 |
| **Organization Method** | Sequential Numbering |
| **Categories** | Introduction & Overview, Core Configuration, Provider Configuration, Compatibility Providers, Management Interfaces, Agent Client Integration, Docker Deployment, Hands-on Tutorials, Chinese Documentation |

---

## Document Index

### 1.. Introduction & Overview (001-003)
*Getting started with CLIProxyAPI - overview, what it is, and quick start guide*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | CLIProxyAPI | This document describes an API service that is compatible with OpenAI, Gemini, a... | api-service, openai-compatible, gemini-compatible, claude-compatible, chat-completions |
| 002 | `002-introduction-what-is-cliproxyapi.md` | What is CLIProxyAPI? | CLIProxyAPI acts as a proxy server, offering OpenAI, Gemini, Claude, and Codex c... | cli, proxy-api, openai-compatible, gemini-api, claude-api |
| 003 | `003-introduction-quick-start.md` | Quick Start | This document provides instructions on how to install and run the CLIProxyAPI on... | installation, macos, linux, windows, docker |

### 2.. Core Configuration (004-011)
*Essential configuration options including basic settings, authentication, storage backends, and hot reloading*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-configuration-basic.md` | Basic Configuration | This document details the configuration options for a server, including settings... | configuration, server-settings, api-keys, providers, logging |
| 005 | `005-configuration-options.md` | Configuration Options | This document details the configuration options available for a proxy API, cover... | configuration, api-settings, provider-credentials, model-routing, proxy-api |
| 006 | `006-configuration-auth-dir.md` | Authentication Directory | This document explains the purpose and function of the `auth-dir` parameter, whi... | authentication, tokens, configuration, auth-dir, google-accounts |
| 007 | `007-configuration-hot-reloading.md` | Hot Reloading | This document explains how the server automatically reloads client configuration... | server-configuration, automatic-reload, client-settings, token-management, dynamic-updates |
| 008 | `008-configuration-thinking.md` | Thinking Budgets via Model Name Parentheses | This document explains how to append values in parentheses to a model name to co... | model-configuration, thinking-budget, reasoning-effort, api-parameters, llm-control |
| 009 | `009-configuration-storage-git.md` | Git-backed Configuration and Token Store | This document explains how to configure an application to use a Git repository f... | git-backed-configuration, token-store, environment-variables, git-repository, centralized-management |
| 010 | `010-configuration-storage-s3.md` | Object Storage-backed Configuration and Token Store | This document explains how to configure an object storage service, like S3, to s... | object-storage, configuration, authentication, s3-compatible, environment-variables |
| 011 | `011-configuration-storage-pgsql.md` | PostgreSQL-backed Configuration and Token Store | This document explains how to configure CLIProxyAPI to use a PostgreSQL database... | postgresql, configuration, token-store, cli-proxy-api, environment-variables |

### 3.. Provider Configuration (012-018)
*OAuth login setup for various AI providers: Gemini, Claude, Codex, Qwen, iFlow, Antigravity, and AI Studio*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-configuration-provider-gemini-cli.md` | Gemini CLI (Gemini via OAuth): | This document explains how to log in to the Gemini Code CLI using the proxy API,... | cli, proxy-api, login, project-id, oauth-callback |
| 013 | `013-configuration-provider-claude-code.md` | Claude Code (Anthropic via OAuth): | This document explains how to use the `cli-proxy-api` command to log in to Claud... | cli, proxy-api, claude-login, oauth, command-line |
| 014 | `014-configuration-provider-codex.md` | Codex (OpenAI via OAuth): | This document provides instructions on how to log into the CLI proxy API using a... | cli-proxy-api, login, oauth, bash, command-line |
| 015 | `015-configuration-provider-qwen-code.md` | Qwen (Qwen Chat via OAuth): | This document explains how to log in to Qwen Chat using the CLI proxy API, offer... | cli-proxy-api, qwen-login, oauth, device-flow, login-url |
| 016 | `016-configuration-provider-iflow.md` | iFlow (iFlow via OAuth): | This document provides instructions on how to log in to the CLI proxy API using ... | cli-proxy-api, login, oauth, bash, command-line |
| 017 | `017-configuration-provider-antigravity.md` | Antigravity (Antigravity via OAuth): | This document explains how to use the cli-proxy-api tool for antigravity login, ... | cli-proxy-api, antigravity-login, oauth-callback, port-configuration, no-browser |
| 018 | `018-configuration-provider-ai-studio.md` | AI Studio Instructions | This document explains how to configure the connection and authentication settin... | aistudio-app, cliproxyapi, connection, authentication, configuration |

### 4.. Compatibility Providers (019-022)
*Upstream provider configuration for Gemini, Claude, Codex, and OpenAI-compatible APIs*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 019 | `019-configuration-provider-gemini-compatibility.md` | Gemini Compatibility Providers | This document explains how to configure upstream Gemini compatible providers usi... | configuration, gemini-api-key, provider-setup, api-key, base-url |
| 020 | `020-configuration-provider-claude-code-compatibility.md` | Claude Code Compatibility Providers | This document explains how to configure upstream Claude Code compatible provider... | claude-api-key, configuration, api-key, base-url, models |
| 021 | `021-configuration-provider-codex-compatibility.md` | Codex Compatibility Providers | This document explains how to configure upstream Codex compatible providers by s... | codex, api-key, configuration, provider, base-url |
| 022 | `022-configuration-provider-openai-compatibility.md` | OpenAI Compatibility Providers | This document explains how to configure upstream OpenAI-compatible providers, su... | openai-compatibility, provider-configuration, api-keys, model-mapping, proxy-configuration |

### 5.. Management Interfaces (023-025)
*Management tools including API, Web UI, and desktop GUI clients*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 023 | `023-management-api.md` | Management API | This document provides a configuration structure for setting up API keys and con... | api-configuration, ai-models, gemini, claude, codex |
| 024 | `024-management-webui.md` | Web UI | This document explains how to use a custom web UI for the CLIProxyAPI management... | cli-proxy-api, management-center, custom-ui, web-ui, github-integration |
| 025 | `025-management-gui.md` | Desktop GUI | This document introduces EasyCLI, a cross-platform desktop GUI client designed t... | gui-client, cli-proxy, desktop-application, cross-platform |

### 6.. Agent Client Integration (026-030)
*Integration guides for Gemini CLI, Claude Code, Codex, Factory Droid, and Amp CLI*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-agent-client-gemini-cli.md` | Gemini CLI | This document explains how to configure the CLIProxyAPI server for two authentic... | cliproxyapi, authentication, google-oauth, gemini-api-key, configuration |
| 027 | `027-agent-client-claude-code.md` | Claude Code | This document explains how to configure environment variables for the CLIProxyAP... | cli-proxy, api-configuration, environment-variables, model-selection, anthropic-api |
| 028 | `028-agent-client-codex.md` | Codex | This document explains how to configure the Codex CLIProxyAPI server by editing ... | codex, cliproxyapi, configuration, toml, auth |
| 029 | `029-agent-client-droid.md` | Factory Droid | This document explains how to configure custom models for the CLIProxyAPI server... | cli-proxy, api-configuration, custom-models, json-config |
| 030 | `030-agent-client-amp-cli.md` | Amp CLI | This document explains how to integrate Amp CLI and IDE extensions with CLIProxy... | ampt-cli, ide-extensions, cliproxyapi, oauth, ai-providers |

### 7.. Docker Deployment (031-032)
*Docker and Docker Compose deployment instructions*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 031 | `031-docker-docker.md` | Run with Docker | This document provides Docker commands to run the CLIProxyAPI, including instruc... | docker, cli-proxy-api, oauth, login, server-start |
| 032 | `032-docker-docker-compose.md` | Run with Docker Compose | This document provides instructions on how to set up and run the CLIProxyAPI usi... | docker-compose, cli-proxy-api, setup, configuration, authentication |

### 8.. Hands-on Tutorials (033-045)
*Practical tutorials covering configuration, deployment, and integration scenarios*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 033 | `033-hands-on-tutorial-0.md` | Zero: Detailed Configuration Explanation | This document explains the various configuration items available in the CLIProxy... | configuration, cli-proxy-api, settings, api-keys, remote-management |
| 034 | `034-hands-on-tutorial-1.md` | One: Project Introduction + Qwen Hands-on | This document introduces CLIProxyAPI, an open-source AI proxy tool written in Go... | ai-proxy, cli-proxy-api, qwen-code, api-key, tutorial |
| 035 | `035-hands-on-tutorial-2.md` | Two: Gemini CLI + Codex Hands-on | This tutorial explains how to configure and integrate Codex and Gemini CLI with ... | codex, gemini, cli, api-integration, authentication |
| 036 | `036-hands-on-tutorial-3.md` | Three: NanoBanana Hands-on | This document explains how to integrate Gemini Web's NanoBanana model with CLIPr... | gemini-web, nanobana-model, cliproxyapi, authentication, cookies |
| 037 | `037-hands-on-tutorial-4.md` | Four: Relay Forwarding Integration | This document explains how to configure CLIProxyAPI to integrate various AI rela... | configuration, cli-proxy-api, ai-relay-services, api-keys, base-url |
| 038 | `038-hands-on-tutorial-5.md` | Five: Docker Server Deployment | This document explains how to deploy the CLIProxyAPI on a server using Docker, c... | docker, deployment, server, cliproxyapi, oauth |
| 039 | `039-hands-on-tutorial-6.md` | Six: The Beginner's Favorite GUI | This document explains how to enable and access the WebUI for CLIProxyAPI, a web... | webui, cli-proxy-api, configuration, remote-management, access |
| 040 | `040-hands-on-tutorial-7.md` | Zero-Cost Deployment: ClawCloud (Built-in Storage) | This tutorial explains how to deploy the CLIProxyAPI on a container cloud platfo... | cli-proxy-api, container-cloud, deployment, clawcloud-run, oauth-authentication |
| 041 | `041-hands-on-tutorial-8.md` | Zero-Cost Deployment: HuggingFace (Database Storage) | This document guides users on how to deploy CLIProxyAPI on HuggingFace by persis... | cli-proxy-api, huggingface, postgresql, deployment, persistence |
| 042 | `042-hands-on-tutorial-9.md` | Zero-Cost Deployment: Railway (Object Storage) | This document guides users on deploying the CLIProxyAPI program using Railway an... | deployment, railway, clawcloud, s3-bucket, docker |
| 043 | `043-hands-on-tutorial-10.md` | Zero-Cost Deployment: Render (Git Storage) | This document provides a step-by-step guide on how to deploy the CLIProxyAPI on ... | cli-proxy-api, render, persistent-storage, github-integration, deployment-guide |
| 044 | `044-hands-on-tutorial-11.md` | Zero-Cost Deployment (AIStudio Reverse Proxy) | This document explains how to deploy AIStudioBuild as a WebSocket proxy for CLIP... | aistudio, cli-proxy-api, websocket, docker, huggingface |
| 045 | `045-hands-on-tutorial-12.md` | AmpCode Usage Guide | This document explains how to configure AmpCode to use custom models by integrat... | ampcode, cliproxyapi, custom-models, model-mapping, configuration |

### 9.. Chinese Documentation (046-090)
*Chinese language versions of all documentation (中文文档)*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 046 | `046-cn.md` | CLIProxyAPI | This document describes CLIProxyAPI, a service that provides a unified API endpo... | api-service, llm-integration, openai-api, gemini-api, claude-api |
| 047 | `047-cn-introduction-what-is-cliproxyapi.md` | CLIProxyAPI是什么？ | This document describes CLIProxyAPI, a proxy server that provides OpenAI/Gemini/... | cli-proxy, openai-api, gemini-api, claude-api, codex-api |
| 048 | `048-cn-introduction-quick-start.md` | 快速开始 | This document provides instructions on how to install and run the CLIProxyAPI to... | installation, macos, linux, windows, docker |
| 049 | `049-cn-configuration-basic.md` | 基础配置 | This document details the configuration options for the CLI Proxy API, including... | configuration, api-keys, tls, proxy, model-routing |
| 050 | `050-cn-configuration-options.md` | 配置选项 | This document details the configuration options for a CLI proxy API, covering ba... | configuration, cli-proxy-api, api-settings, provider-credentials, model-mapping |
| 051 | `051-cn-configuration-auth-dir.md` | 凭证目录 | This document explains the `auth-dir` parameter, which specifies the location wh... | authentication, credentials, auth-dir, token-storage, google-accounts |
| 052 | `052-cn-configuration-hot-reloading.md` | 热更新 | This document explains how the service automatically reloads client configuratio... | hot-update, configuration-reload, client-tokens, service-restart, auth-dir |
| 053 | `053-cn-configuration-thinking.md` | 通过模型名括号设置思考量 | This document explains how to control the thinking budget or reasoning level for... | model-configuration, thinking-budget, reasoning-level, api-parameters, llm-control |
| 054 | `054-cn-configuration-storage-git.md` | Git 支持的配置与令牌存储 | This document explains how to configure an application to use a Git repository a... | git-store, configuration, authentication, environment-variables, version-control |
| 055 | `055-cn-configuration-storage-s3.md` | 对象存储驱动的配置与令牌存储 | This document explains how to configure object storage, specifically S3-compatib... | object-storage, s3-compatible, configuration, authentication, environment-variables |
| 056 | `056-cn-configuration-storage-pgsql.md` | PostgreSQL 支持的配置与令牌存储 | This document explains how to use PostgreSQL to store configuration and tokens i... | postgresql, configuration-storage, token-storage, hosted-environment, environment-variables |
| 057 | `057-cn-configuration-provider-gemini-cli.md` | Gemini CLI (Gemini OAuth 登录): | This document explains how to log in to the Gemini Code CLI using the `--login` ... | cli, login, authentication, project-id, oauth |
| 058 | `058-cn-configuration-provider-claude-code.md` | Claude Code (Anthropic OAuth 登录): | This document explains how to use the `cli-proxy-api` command with the `--claude... | cli-proxy-api, claude-login, authentication, oauth, command-line |
| 059 | `059-cn-configuration-provider-codex.md` | Codex (OpenAI OAuth 登录): | This document explains how to use the `cli-proxy-api` command with the `--codex-... | cli-proxy-api, codex-login, oauth, command-line |
| 060 | `060-cn-configuration-provider-qwen-code.md` | Qwen (Qwen Chat OAuth 登录): | This document explains how to use the Qwen Chat OAuth device login flow via the ... | cli-proxy-api, qwen-chat, oauth, device-login, bash |
| 061 | `061-cn-configuration-provider-iflow.md` | iFlow (iFlow OAuth 登录): | This document explains how to use the `cli-proxy-api` command with the `--iflow-... | cli-proxy-api, authentication, login, oauth, callback-port |
| 062 | `062-cn-configuration-provider-antigravity.md` | 反重力 (反重力 OAuth 登录): | This document explains how to use the cli-proxy-api command with the --antigravi... | cli-proxy-api, oauth-login, command-line-interface, local-port, browser-option |
| 063 | `063-cn-configuration-provider-ai-studio.md` | AI Studio 使用说明 | This document explains how to configure the AI Studio application to connect to ... | aistudio, cliproxyapi, configuration, websocket, authentication |
| 064 | `064-cn-configuration-provider-gemini-compatibility.md` | Gemini 兼容供应商 | This document explains how to configure upstream Gemini-compatible providers usi... | gemini-api-key, configuration, api-key, base-url, proxy-url |
| 065 | `065-cn-configuration-provider-claude-code-compatibility.md` | Claude Code 兼容供应商 | This document explains how to configure upstream Claude Code compatible provider... | claude-api-key, configuration, api-key, base-url, proxy-url |
| 066 | `066-cn-configuration-provider-codex-compatibility.md` | Codex 兼容供应商 | This document explains how to configure an upstream Codex-compatible provider us... | codex, api-key, configuration, provider, upstream |
| 067 | `067-cn-configuration-provider-openai-compatibility.md` | OpenAI 兼容供应商 | This document explains how to configure an upstream OpenAI-compatible provider u... | openai-compatibility, upstream-provider, configuration, api-key, proxy-settings |
| 068 | `068-cn-management-api.md` | 管理 API | This document provides a JSON configuration example for setting up various API k... | api-keys, configuration, json, proxy, models |
| 069 | `069-cn-management-webui.md` | Web UI | This document explains how to configure and use a custom web UI for the CLI Prox... | cli-proxy, api-management, web-ui, customization, github-releases |
| 070 | `070-cn-management-gui.md` | 桌面客户端 | This document introduces EasyCLI, a cross-platform desktop client for CLIProxyAP... | desktop-client, cli, proxy, api, cross-platform |
| 071 | `071-cn-agent-client-gemini-cli.md` | Gemini CLI | This document explains how to configure and start the CLIProxyAPI server, detail... | cliproxyapi, authentication, google-oauth, gemini-api-key, configuration |
| 072 | `072-cn-agent-client-claude-code.md` | Claude Code | This document explains how to configure system environment variables to run the ... | cli-proxy-api, environment-variables, configuration, ai-models, gemini |
| 073 | `073-cn-agent-client-codex.md` | Codex | This document explains how to start the CLIProxyAPI server and configure the `co... | cliproxyapi, configuration, server-setup, toml, json |
| 074 | `074-cn-agent-client-droid.md` | Factory Droid | This document defines custom models for AI services, including model names, base... | custom-models, ai-configuration, openai, anthropic, api-settings |
| 075 | `075-cn-agent-client-amp-cli.md` | Amp CLI | This guide explains how to integrate the CLIProxyAPI with the Amp CLI and Amp ID... | amr-cli, cli-proxy-api, oauth, configuration, api-integration |
| 076 | `076-cn-docker-docker.md` | 使用 Docker 运行 | This document provides Docker commands to run a CLI proxy API, including instruc... | docker, cli-proxy-api, oauth, gemini, openai |
| 077 | `077-cn-docker-docker-compose.md` | 使用 Docker Compose 运行 | This document explains how to use Docker Compose to set up and run the CLIProxyA... | docker-compose, cli-proxy-api, deployment, configuration, ai-models |
| 078 | `078-cn-hands-on-tutorial-0.md` | 零：配置详细解说 | This document provides a detailed configuration guide for the CLIProxyAPI, expla... | configuration, cli-proxy-api, api-keys, remote-management, logging |
| 079 | `079-cn-hands-on-tutorial-1.md` | 壹：项目介绍+Qwen实战 | This document introduces CLIProxyAPI, an open-source AI proxy tool written in Go... | ai-proxy, cli-proxy-api, gemini, qwen-code, api-key |
| 080 | `080-cn-hands-on-tutorial-2.md` | 贰：Gemini CLI+Codex实战 | This tutorial explains how to integrate Codex and Gemini CLI with CLIProxyAPI, b... | codex, gemini, cli-proxy-api, oauth, authentication |
| 081 | `081-cn-hands-on-tutorial-3.md` | 叁：NanoBanana实战 | This document explains how to integrate the Gemini Web NanoBanana model into CLI... | gemini-web, nanobanana, cliproxyapi, authentication, cookie-management |
| 082 | `082-cn-hands-on-tutorial-4.md` | 肆：中转转发接入篇 | This tutorial explains how to integrate various AI proxy services, including Cla... | cli-proxy-api, configuration, ai-proxy, claude, codex |
| 083 | `083-cn-hands-on-tutorial-5.md` | 伍：Docker服务器部署 | This document explains how to deploy the CLIProxyAPI on a server using Docker, i... | docker, deployment, server, cli-proxy-api, oauth |
| 084 | `084-cn-hands-on-tutorial-6.md` | 陆：新人最爱GUI | This document explains how to enable and access the WebUI for CLIProxyAPI, which... | cli-proxy-api, webui, configuration, remote-management, access |
| 085 | `085-cn-hands-on-tutorial-7.md` | 零成本部署：ClawCloud (自带存储) | This document provides a step-by-step tutorial on deploying the CLIProxyAPI on a... | container-cloud, deployment-tutorial, cli-proxy-api, oauth-authentication, easy-cli |
| 086 | `086-cn-hands-on-tutorial-8.md` | 零成本部署：HuggingFace (数据库存储) | This tutorial explains how to persist configuration and authentication informati... | postgresql, huggingface, deployment, cli-proxy-api, configuration |
| 087 | `087-cn-hands-on-tutorial-9.md` | 零成本部署：Railway (对象存储) | This document provides a tutorial on deploying the CLIProxyAPI program using Rai... | railway, clawcloud, s3-storage, docker, deployment |
| 088 | `088-cn-hands-on-tutorial-10.md` | 零成本部署：Render (Git存储) | This document provides a step-by-step guide on how to deploy the CLIProxyAPI on ... | cli-proxy-api, render, github, persistent-storage, deployment |
| 089 | `089-cn-hands-on-tutorial-11.md` | 零成本部署AIStudio反代 | This tutorial explains how to deploy AIStudioBuild using Docker on HuggingFace o... | aistudiobuild, cli-proxy-api, websocket, docker, huggingface |
| 090 | `090-cn-hands-on-tutorial-12.md` | AmpCode食用指南 | This document explains how to integrate AmpCode with CLIProxyAPI to use custom m... | ampcode, cliproxyapi, custom-models, model-mapping, configuration |

---

## Quick Reference

### By Topic

| Topic | File Range | Description |
|-------|------------|-------------|
| **Getting Started** | 001-003 | Overview, introduction, and quick start |
| **Basic Setup** | 004-011 | Core configuration, auth, storage |
| **Provider Setup** | 012-022 | OAuth and compatibility providers |
| **Management** | 023-025 | API, WebUI, and GUI management tools |
| **Client Integration** | 026-030 | AI agent client configurations |
| **Deployment** | 031-032 | Docker deployment |
| **Tutorials** | 033-045 | Hands-on guides and deployment scenarios |
| **中文文档** | 046-090 | Chinese documentation |

### By Provider

| Provider | Files | Type |
|----------|-------|------|
| **Gemini** | 012, 019, 026, 057, 064, 071 | OAuth, Compatibility, Client |
| **Claude** | 013, 020, 027, 058, 065, 072 | OAuth, Compatibility, Client |
| **Codex** | 014, 021, 028, 059, 066, 073 | OAuth, Compatibility, Client |
| **OpenAI** | 022, 067 | Compatibility providers |
| **Qwen** | 015, 060, 079 | OAuth, Tutorial |
| **iFlow** | 016, 061 | OAuth |
| **Amp** | 018, 030, 063, 075, 090 | Studio, Client, Tutorial |

---

## Learning Path

### Level 1: Foundation (Start Here)
- **Read files 001-003** for introduction, overview, and quick start guide
- Understand what CLIProxyAPI is and how it works

### Level 2: Core Configuration
- **Complete files 004-011** for basic configuration setup
- Configure authentication directories, storage backends (Git, S3, PostgreSQL)
- Enable hot reloading for dynamic updates

### Level 3: Provider Integration
- **Configure providers from files 012-018**
- Set up OAuth for Gemini, Claude, Codex, Qwen, iFlow, Antigravity
- Configure AI Studio integration
- **Add compatibility providers from files 019-022**
- Connect upstream OpenAI/Gemini/Claude/Codex-compatible APIs

### Level 4: Management & Clients
- **Explore management tools in files 023-025**
- Set up Management API, Web UI, and desktop GUI
- **Integrate agent clients from files 026-030**
- Configure Gemini CLI, Claude Code, Codex, Factory Droid, Amp CLI

### Level 5: Deployment
- **Deploy with Docker from files 031-032**
- Use Docker or Docker Compose for production

### Level 6: Advanced Tutorials
- **Follow hands-on tutorials 033-045**
- Detailed configuration explanations
- Provider integration tutorials (Qwen, Gemini, Codex, NanoBanana)
- Relay forwarding integration
- Server deployment with Docker
- WebUI management
- Zero-cost deployment guides (ClawCloud, HuggingFace, Railway, Render, AIStudio)
- AmpCode usage guide

### Level 7: Chinese Documentation
- **中文文档 available in files 046-090**
- Complete Chinese translations of all documentation

---

## Key Features

### Multi-Provider Support
- OAuth authentication for Gemini, Claude, Codex, Qwen, iFlow, Antigravity
- OpenAI/Gemini/Claude/Codex-compatible upstream providers
- AI Studio WebSocket proxy support

### Storage Backends
- Local file system (default)
- Git repository for version control
- S3-compatible object storage
- PostgreSQL database

### Management Interfaces
- RESTful Management API
- Web UI for browser-based management
- Desktop GUI (EasyCLI) for cross-platform usage

### Client Integration
- Gemini CLI
- Claude Code (Anthropic)
- Codex (OpenAI)
- Factory Droid
- Amp CLI and IDE extensions

### Deployment Options
- Standalone binary (macOS, Linux, Windows)
- Docker container
- Docker Compose
- Zero-cost deployment platforms (ClawCloud, HuggingFace, Railway, Render)

---

## Architecture Overview

CLIProxyAPI acts as a **unified proxy server** that:

1. **Wraps CLI tools** (Gemini CLI, ChatGPT Codex, Claude Code, Qwen Code, iFlow)
2. **Provides standard APIs** (OpenAI/Gemini/Claude/Codex compatible)
3. **Supports multiple accounts** for load balancing
4. **Enables free access** to premium models (Gemini 2.5 Pro, GPT 5, Claude, Qwen)

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the CLIProxyAPI documentation structure.*
