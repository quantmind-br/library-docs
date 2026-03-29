---
title: 叁：NanoBanana实战 | CLIProxyAPI
url: https://help.router-for.me/cn/hands-on/tutorial-3
source: crawler
fetched_at: 2026-01-14T22:10:16.001234125-03:00
rendered_js: false
word_count: 148
summary: This document explains how to integrate the Gemini Web NanoBanana model into CLIProxyAPI by obtaining and using authentication cookies. It provides two methods for acquiring these cookies and outlines the verification steps and important considerations for successful integration.
tags:
    - gemini-web
    - nanobanana
    - cliproxyapi
    - authentication
    - cookie-management
    - image-generation
category: tutorial
---

> **重要通知：因为现在 Gemini CLI 已经完整覆盖了 Gemini Web，并且全免费，所以自 6.2.X 版本起 CLIProxyAPI 将移除 Gemini Web 支持，如果还有想用 Gemini Web 的可以使用 6.1.X 版本，以下教程基于 6.1.X 版本**

经过前两期的实战，我们已成功在 `CLIProxyAPI` 上集成了 `Qwen Code`、`Gemini CLI` 和 `Codex`。本期内容将介绍如何通过添加 Gemini Web 的 Cookie，使 `CLIProxyAPI` 支持 `NanoBanana` 模型。

Gemini 的 `NanoBanana` 模型因其出色的图像处理能力而备受赞誉。然而，Google 并未提供该模型的免费 API。而现在，使用 `CLIProxyAPI`之后，我们就可以通过集成 Gemini Web，从而以免费 API 的形式使用 `NanoBanana` 啦。

我们有两种方法可以获取认证信息：

### 第一种方法 [​](#%E7%AC%AC%E4%B8%80%E7%A7%8D%E6%96%B9%E6%B3%95)

首先，使用您的 Google 账号登录 Gemini 官网 ([https://gemini.google.com/app](https://gemini.google.com/app))。据了解，普通账号每天有 100 次图像生成配额，Pro 账号则有 1000 次。登录成功后，在浏览器中按 F12 打开开发者工具，并切换到“网络” (Network) 选项卡。

![](https://img.072899.xyz/2025/09/074fcf1c455e99185ceeada71a27bd8c.png)

在筛选框中输入 `List`，然后将鼠标悬停在您的用户头像上。片刻之后，下方列表中应出现 `ListAccounts` 的条目。如果未出现，请刷新页面重试。

![](https://img.072899.xyz/2025/09/7cb7104fa93a6b6a6903e0745d3b5573.png)

点击 `ListAccounts`，在“标头” (Headers) -&gt; “请求标头” (Request Headers) 中找到 `Cookie`，并完整复制其值。

![](https://img.072899.xyz/2025/09/c2ba085f10fcb145aff7e9d5081b9382.png)

回到 `CLIProxyAPI` 程序所在的目录，打开终端或命令行，输入命令 `cli-proxy-api --gemini-web-auth`。根据提示，粘贴我们刚才复制的 `Cookie` 值并回车，即可看到验证成功的消息，`Cookie` 已被自动保存。

![](https://img.072899.xyz/2025/09/e149d07875cb8dab12de95f82d2b3e45.png)

### 第二种方法 [​](#%E7%AC%AC%E4%BA%8C%E7%A7%8D%E6%96%B9%E6%B3%95)

如果您使用的是 macOS 系统，或者第一种方法认证失败，那么可能需要手动输入 `__Secure-1PSID` 和 `__Secure-1PSIDTS` 的值。请切换到“应用” (Application) 选项卡，并依次复制图示中的这两个值。

![](https://img.072899.xyz/2025/09/e5b5debae5ec74a31a1b527e506895e7.png)

![](https://img.072899.xyz/2025/09/7767f178e1186358f1a9a498108e5ac0.png)

在命令行执行验证时，根据提示手动填入这两个值即可完成验证。

![](https://img.072899.xyz/2025/09/b02fb7704d5c67385d781f9d9893e0b2.png)

### 验证步骤 [​](#%E9%AA%8C%E8%AF%81%E6%AD%A5%E9%AA%A4)

接下来我们进行验证。需要注意的是，目前程序仅支持通过 OpenAI 兼容接口和 Gemini 原生接口进行文生图或图文生图的操作。因此，我们之前在 `Cherry Studio` 中设置的提供商类型 `OpenAI Response` 需要修改为 `OpenAI`。

![](https://img.072899.xyz/2025/09/48892cc3ce1e3c4379b694afa45c5d35.png)

添加模型 `NanoBanana` (即 `gemini-2.5-flash-image-preview`)。

![](https://img.072899.xyz/2025/09/4674845c6412ec6f5366d109070047fc.png)

现在，在 `Cherry Studio` 中测试一下吧！

![](https://img.072899.xyz/2025/09/fdd35aa92224cd76cbf888ce3ff2cce2.png)

完美地满足了我们的要求，尽情享受“香蕉”吧！

### 注意事项 [​](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

- 现阶段请避免在 `CLIProxyAPI` 中添加多个 Gemini Web 账户。因为当存在多个账户时，程序会轮询调用，这可能会破坏会話的连续性，导致请求失败。 6.0.17版本更新之后，程序支持 Gemini Web 粘性会话，可以添加多个账户了。
- 在 `Cherry Studio` 中，**切勿**在 `OpenAI Response` 提供商类型下添加 `NanoBanana` 模型。已知 `Cherry Studio` 在此情况下存在 Bug，会导致程序崩溃。