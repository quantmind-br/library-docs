---
title: AmpCode食用指南 | CLIProxyAPI
url: https://help.router-for.me/cn/hands-on/tutorial-12
source: crawler
fetched_at: 2026-01-14T22:10:18.607471941-03:00
rendered_js: false
word_count: 238
summary: This document explains how to integrate AmpCode with CLIProxyAPI to use custom models within AmpCode. It covers configuration steps for both CLIProxyAPI and AmpCode clients (CLI and VSCode plugin), along with verification methods.
tags:
    - ampcode
    - cliproxyapi
    - custom-models
    - model-mapping
    - configuration
    - api-integration
category: tutorial
---

今天提到的 **AmpCode** 可能国内很少有人听过（大概是因为没有“白嫖”渠道？）。其实 AmpCode 凭借其独特的理念在 AI 编程领域已占有一席之地。它最核心的特点是**效率优先，成本次之**——用户无需关心模型选择，系统会自动调用当前最佳的模型来完成工作。因此，AmpCode 原生并不支持模型切换，更不用说使用第三方模型了。

AmpCode 主要有两种模式：

- **Free 模式：** 免费使用 Claude Haiku 4.5 模型，代价是包含广告（这可能是目前唯一带广告的 Agent 工具？）。
- **Smart 模式：** 自动选用当下最强的模型组合。在这个时间节点（2025年12月），Smart 模式通常会调用 Claude Opus 4.5 处理复杂任务，Claude Haiku 4.5 负责高频简单响应，并由 GPT 5.1 作为 SubAgent 进行多维度的逻辑补全。

这篇文章将教大家如何搭配 **AmpCode + CLIProxyAPI**，实现“在 AmpCode 中使用自己模型”的目标。

### 1. 配置 CLIProxyAPI [​](#_1-%E9%85%8D%E7%BD%AE-cliproxyapi)

首先我们需要一个配置好的 CLIProxyAPI。具体的部署方法可以参考我之前的 CLIProxyAPI 系列教程，这里不再赘述。

常规配置完 CLIProxyAPI 之后，我们需要在配置文件中加入以下 AmpCode 相关的设置：

```
ampcode:
  upstream-url: "https://ampcode.com"
  restrict-management-to-localhost: false
  upstream-api-key: "sgamp_user_XXXX"
  force-model-mappings: false
  model-mappings:
    - from: claude-opus-4-5-20251101
      to: gemini-claude-sonnet-4-5
    - from: claude-sonnet-4-5-20250929
      to: gemini-claude-sonnet-4-5
    - from: claude-haiku-4-5-20251001
      to: qwen3-coder-flash
```

**配置项说明：**

- `upstream-url`, `restrict-management-to-localhost`, `upstream-api-key`： 如果你拥有 AmpCode 账号，并希望在官网后台查看会话信息，请填入这三项。其中 `upstream-api-key` 可以在 AmpCode 后台复制（如下图）。如果你没有 AmpCode 账号，直接删除这三行即可。 **注意：** AmpCode 客户端最近更新后，已强制要求填写上游信息，因此现在此部分为必填项。 ![](https://img.072899.xyz/2025/12/1e6e2eab382f693c3c70c2017e7e7c8f.png)
- `model-mappings` **（重点敲黑板！）**： 这是配置中最关键的部分。我们需要理解 CLIProxyAPI 的处理逻辑： 当 AmpCode 请求某个特定模型（例如 `claude-opus-4-5-20251101`）时，CLIProxyAPI 会优先在已注册的模型列表中查找。
  
  - **情况 A：** 如果该模型存在，直接请求该模型（model-mappings 不生效）。
  - **情况 B：** 如果该模型不存在，CLIProxyAPI 本该报错，但通过配置 model-mappings，我们可以将请求**重定向**到我们指定的模型（例如 `gemini-claude-sonnet-4-5`）。
  
  > **举个栗子帮助理解：**
  > 
  > 假设 AmpCode 请求 `claude-opus-4-5-20251101`，如果在 CLIProxyAPI 里有这个模型，那么 AmpCode 就会使用 CLIProxyAPI 中的 `claude-opus-4-5-20251101` 模型； 如果 CLIProxyAPI 里并没有配置这个模型，系统就会触发 `model-mappings` 规则，把请求转交给 `gemini-claude-sonnet-4-5` 来响应。 通过以上规则，我们就成功实现了“移花接木”，用自己的模型接管了 AmpCode 的请求。
  > 
  > （如果对这个逻辑还有疑问，建议把上面这段话多读几遍~）
- `force-model-mappings`： 这是一个布尔值（`true` 或 `false`），默认为 `false`。 当设置为 `true` 时，CLIProxyAPI 会**强制**应用 `model-mappings` 中的重定向规则，**即使“情况 A”满足**（即 `from` 模型本身存在于 CLIProxyAPI 中）。 这个选项非常适合需要**临时覆盖**或**统一管理**模型请求的场景。例如，即使你的 CLIProxyAPI 中已经配置了 `claude-opus-4-5-20251101`，你依然可以通过开启此选项，将其所有请求强制转到 `gemini-claude-sonnet-4-5`。

完成以上配置，CLIProxyAPI 这一侧就算准备就绪了。

### 2. 配置 AmpCode 客户端 [​](#_2-%E9%85%8D%E7%BD%AE-ampcode-%E5%AE%A2%E6%88%B7%E7%AB%AF)

AmpCode 支持多平台客户端，你可以根据自己的使用习惯选择，以下会讲解配置命令行工具（Amp CLI）与 VSCode 插件两种方式。

#### 方式一：配置 Amp CLI [​](#%E6%96%B9%E5%BC%8F%E4%B8%80-%E9%85%8D%E7%BD%AE-amp-cli)

以下以在 **WSL2 Debian** 中安装 Amp CLI 为例供大家参考。

![](https://img.072899.xyz/2025/12/7979738f3bd96c95c20d06889a74f29e.png)

复制官方提供的安装脚本进行安装： `curl -fsSL https://ampcode.com/install.sh | bash`

**注意：** 安装完成后先不要运行，我们需要编辑环境变量。 输入 `nano ~/.bashrc`，在文件最底部添加如下内容：

```
export AMP_URL="http://你的CPA部署地址:端口"
export AMP_API_KEY="你在CPA中设定的api-keys"
```

保存并退出后，运行 `source ~/.bashrc` 使配置生效。

#### 方式二：配置 VSCode 插件 [​](#%E6%96%B9%E5%BC%8F%E4%BA%8C-%E9%85%8D%E7%BD%AE-vscode-%E6%8F%92%E4%BB%B6)

如果你更习惯在 VSCode 中进行开发，AmpCode 也提供了官方插件。

1. **安装插件**：在 VSCode 扩展商店中搜索并安装 `AmpCode` 插件。 ![](https://img.072899.xyz/2025/12/d62cd472a9e7837929308a732c479ea5.png)
2. **打开设置**：通过命令面板 (`Ctrl+Shift+P`) 搜索 `Preferences: Open User Settings (JSON)`，打开 `settings.json` 文件。
3. **添加配置**：在 `settings.json` 中添加以下配置，将 `amp.url` 指向你的 CLIProxyAPI 服务地址：
   
   json
   
   ```
   {
     // ... 其他配置
     "amp.url": "http://你的CPA部署地址:端口"
   }
   ```
4. **登录**：配置完成后，点击侧边栏的 AmpCode 图标。插件界面会显示你配置的 URL，在红框处输入你在 CLIProxyAPI 中设定的 `api-keys` 即可登录使用（注意不是 AmpCode 官网提供的 Key）。 ![](https://img.072899.xyz/2025/12/98ceb48e3b4c10f0d86a2f138838ff26.png)

### 3. 验证结果 [​](#_3-%E9%AA%8C%E8%AF%81%E7%BB%93%E6%9E%9C)

无论你使用哪种客户端，验证方式都是类似的：

- **对于 Amp CLI 用户：** 输入 `amp` 并尝试发送一段提示词，如果一切顺利，你将看到如下界面： ![](https://img.072899.xyz/2025/12/bba2d9f3010ca2a78db6ac5c63b6645c.png)
- **对于 VSCode 插件用户：** 登录成功后，在 AmpCode 的聊天窗口中发送提示词，插件会正常返回结果。 ![](https://img.072899.xyz/2025/12/c6af979f543fffc6d43b9e88ed7e01c8.png)

同时，在 CLIProxyAPI 的后台日志中，我们也能清晰地看到对应的请求已被成功转发：

![](https://img.072899.xyz/2025/12/3e15d2ef067d8a6deaa8e629465cbfa8.png)

大功告成！