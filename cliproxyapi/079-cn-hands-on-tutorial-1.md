---
title: 壹：项目介绍+Qwen实战 | CLIProxyAPI
url: https://help.router-for.me/cn/hands-on/tutorial-1
source: crawler
fetched_at: 2026-01-14T22:10:16.24270441-03:00
rendered_js: false
word_count: 242
summary: This document introduces CLIProxyAPI, an open-source AI proxy tool written in Go, that provides an OpenAI/Gemini/Claude/Codex compatible API endpoint for various AI models. It explains the tool's features, benefits, and provides a tutorial on how to convert Qwen Code to an API Key.
tags:
    - ai-proxy
    - cli-proxy-api
    - gemini
    - qwen-code
    - api-key
    - load-balancing
category: tutorial
---

CLIProxyAPI 是一款使用 Go 语言编写的开源 AI 代理工具。也许是因为名字朴实无华，许多人可能对它还很陌生。在遇到它之前，为了能“白嫖” Gemini 模型，我曾先后折腾过 AIStudioProxyAPI、AIStudio-Build-Proxy、Gemini-FastAPI 等多款反代工具，但它们或多或少都有些不尽如人意的地方。

直到我发现了 CLIProxyAPI 并深度使用了几个月，我可以肯定地说：无论是在性能、功能还是适用性上，它都是我用过最出色的 AI 代理工具，没有之一。称之为“神器”也毫不为过。

> **官方仓库地址**：[https://github.com/router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)

### **它究竟能做什么？** [​](#%E5%AE%83%E7%A9%B6%E7%AB%9F%E8%83%BD%E5%81%9A%E4%BB%80%E4%B9%88)

软件功能特性支持的模型为 CLI 模型提供 OpenAI/Gemini/Claude/Codex 兼容的 API 端点gemini-2.5-pro新增 OpenAI Codex（GPT 系列）支持（OAuth 登录）gemini-2.5-flash新增 Claude Code 支持（OAuth 登录）gemini-2.5-flash-lite新增 Qwen Code 支持（OAuth 登录）gemini-2.5-flash-image-preview新增 iFlow 支持（OAuth 登录）gpt-5新增 Gemini Web 支持（通过 Cookie 登录）gpt-5-codex支持流式与非流式响应claude-opus-4-1-20250805函数调用/工具支持claude-opus-4-20250514多模态输入（文本、图片）claude-sonnet-4-20250514多账户支持与轮询负载均衡（Gemini、OpenAI、Claude、Qwen 与 iFlow）claude-sonnet-4-5-20250929简单的 CLI 身份验证流程（Gemini、OpenAI、Claude、Qwen 与 iFlow）claude-3-7-sonnet-20250219支持 Gemini AIStudio API 密钥claude-3-5-haiku-20241022支持 Gemini CLI 多账户轮询qwen3-coder-plus支持 Claude Code 多账户轮询qwen3-coder-flash支持 Qwen Code 多账户轮询qwen3-max支持 iFlow 多账户轮询qwen3-vl-plus支持 OpenAI Codex 多账户轮询deepseek-v3.2通过配置接入上游 OpenAI 兼容提供商（例如 OpenRouter）deepseek-v3.1可复用的 Go SDKdeepseek-r1deepseek-v3kimi-k2glm-4.6tstars2.0以及其他 iFlow 支持的模型

简单来说，CLIProxyAPI 的核心优势包括：

- **无需安装 Gemini CLI**，即可将其授权转换为通用的 API Key，从而在任何应用中调用功能完整的 Gemini 2.5 Pro、Gemini 2.5 Flash、Gemini 2.5 Flash Lite 模型。当正式版模型配额用尽后，它会自动切换到 Preview 模型（如 `gemini-2.5-pro-preview-05-06`），基本能用足每天 1000 次的调用配额，轻松实现“Gemini 自由”。
- **无需安装 Qwen Code**，即可将其授权转换为通用的 API Key，在任何地方调用 Qwen3 Coder Plus、Qwen3 Coder Flash 模型，实现“Qwen3 Coder 自由”。
- **无需安装 Codex**，即可将其授权转换为通用的 API Key，在任何地方调用 GPT-5、GPT-5-Codex 模型。尤其在目前可以免费开设 Team 账户的活动下，轻松实现“GPT 自由”。
- **将 Gemini 网页版转换为 API Key**，在任何地方调用 Nano Banana 等网页版模型（需客户端支持。据网友分享，免费版 Gemini 网页账户每天可调用约 100 次，而 Gemini Pro 用户则高达 1000 次）。
- **强大的负载均衡能力**。CLIProxyAPI 支持将不同来源（无论是 API Key 还是 OAuth 授权）的多个账户整合在一起进行负载均衡轮询，这意味着你可以轻松地将调用配额翻倍。
- **极低的资源消耗**。值得一提的是，该程序对系统资源的消耗极低。程序本身仅 10MB 左右，启动时内存占用不到 10MB，长时间峰值内存占用也仅有 100MB 左右，几乎任何电脑都能流畅运行。

程序的使用非常简单。官方不仅提供了适用于各平台的二进制文件和 Docker 部署方式，还提供了 EasyCLI 和 WebUI，对新手十分友好。所有设置均通过 `config.yaml` 配置文件管理，且支持热重载——修改配置后即时生效，无需重启程序。完整的配置项解说详见《零：配置详细解说》。

### **实战教程：转换 Qwen Code 为 API Key** [​](#%E5%AE%9E%E6%88%98%E6%95%99%E7%A8%8B-%E8%BD%AC%E6%8D%A2-qwen-code-%E4%B8%BA-api-key)

下面，我们以在 Windows 平台下将 Qwen Code 转换为 API Key 为例，演示 CLIProxyAPI 的具体使用方法。

1. **下载并解压**
   
   首先，从官方仓库下载预编译的可执行文件，并将其解压到任意文件夹。在本例中，我将其放在 `Z:\CLIProxyAPI` 目录下。我们只需要用到图中的两个文件。
   
   ![](https://img.072899.xyz/2025/09/b247eb98e0172c799c452d647ab09836.png)
2. **编辑配置文件**
   
   将 `config.example.yaml` 重命名为 `config.yaml`，然后用文本编辑器打开，仅需保留并修改以下基础配置项：
   
   yaml
   
   ```
   port: 8317
   
   # 文件夹位置请根据你的实际情况填写
   auth-dir: "Z:\\CLIProxyAPI\\auths"
   
   request-retry: 3
   
   quota-exceeded:
     switch-project: true
     switch-preview-model: true
   
   api-keys:
   # Key请自行设置，用于客户端访问代理
   - "ABC-123456"
   ```
3. **获取授权**
   
   在 `CLIProxyAPI` 目录下打开终端，输入 `cli-proxy-api --qwen-login` 后回车。程序会自动打开浏览器，请在浏览器中登录你的 Qwen 账户并完成授权。
   
   ![](https://img.072899.xyz/2025/09/ec2e867f5a8de1d24969cb5225cdaa9e.png)
   
   完成授权后，回到终端，程序会尝试获取认证信息。成功后，会要求输入邮箱或昵称（如图中红色箭头所示）。这只是一个用于标识账户的别名，可以随意填写。我这里填的是 `qwen-example`。回车后，可以看到认证文件已成功生成，并保存到了配置文件 `auth-dir` 指定的位置。
   
   ![](https://img.072899.xyz/2025/09/8d37d893884910db77bd4498373a4922.png)
   
   > **提示**：如果系统没有自动弹出浏览器，请不必担心。手动复制终端中红框标出的网址，粘贴到浏览器中打开即可完成授权。
4. **启动代理服务**
   
   以上步骤完成了账户认证。现在，我们来正式启动代理服务。直接双击可执行文件 (`cli-proxy-api.exe`)，出现以下窗口即代表启动成功。
   
   ![](https://img.072899.xyz/2025/09/9e75a484a7f0713c6b56f1fd9a749195.png)
5. **在客户端中配置和测试**
   
   至此，一切准备就绪。下面我们使用 Cherry Studio 来进行测试。
   
   - 在 Cherry Studio 中添加一个新的模型提供商。
   
   <!--THE END-->
   
   ![](https://img.072899.xyz/2025/09/2a2d401e75d02421861e136a6e377f5b.png)
   
   - 模型提供商类型可以选择除 Azure 之外的任意类型。这里我们以 `OpenAI-Response` 为例，供应商名称可自定义，例如 `CLIProxyAPI`。
   
   <!--THE END-->
   
   ![](https://img.072899.xyz/2025/09/3161b549ee3877342f178b2828a30dc6.png)
   
   - **API密钥**：填写我们在 `config.yaml` 中自己设置的 Key，本例中为 `ABC-123456`。
   - **API地址**：填写我们本地服务的地址和端口。还记得配置文件中的端口号 `8317` 吗？这里我们填入 `http://127.0.0.1:8317`。
   
   <!--THE END-->
   
   ![](https://img.072899.xyz/2025/09/5f9638b5f5e5c14d4a818b7362167083.png)
   
   - 点击“管理模型”，你就可以看到通过代理加载的 Qwen Code 模型了。
   
   <!--THE END-->
   
   ![](https://img.072899.xyz/2025/09/9a5d68865bfd1d5fa1cf7778860e6a76.png)
   
   - 添加模型后，我们来测试一下。
   
   ![](https://img.072899.xyz/2025/09/83fd73b257efa9e50ce11bf03cb597d6.png)

可以看到，模型已成功返回消息。整个配置过程是不是很简单？