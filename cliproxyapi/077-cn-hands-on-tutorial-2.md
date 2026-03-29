---
title: 贰：Gemini CLI+Codex实战 | CLIProxyAPI
url: https://help.router-for.me/cn/hands-on/tutorial-2
source: crawler
fetched_at: 2026-01-14T22:10:16.405892999-03:00
rendered_js: false
word_count: 138
summary: This tutorial explains how to integrate Codex and Gemini CLI with CLIProxyAPI, building upon a previous setup for Qwen Code. It provides step-by-step instructions for configuring authentication for both models, including setting up a Google Cloud project for Gemini.
tags:
    - codex
    - gemini
    - cli-proxy-api
    - oauth
    - authentication
    - tutorial
category: tutorial
---

在之前的文章中，我们通过在 CLIProxyAPI 上的简单配置，成功将 Qwen Code 转换成了 API 并在 Cherry Studio 中调用。相信读到这里的你，已经对这款工具的强大功能和便捷性有了初步认识。

在本篇教程中，我们将继续探讨，并把 Codex 和 Gemini CLI 也集成进来。

需要说明的是，本次操作所使用的配置文件与上一篇 Qwen 教程中的是同一个

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

### 配置 Codex [​](#%E9%85%8D%E7%BD%AE-codex)

首先，我们来配置 Codex。Codex 的 OAuth 授权流程与之前的 Qwen 非常相似。在终端命令行中输入 `cli-proxy-api --codex-login`，系统会自动打开 ChatGPT 的授权页面，请使用你的 ChatGPT 账号登录。

![](https://img.072899.xyz/2025/09/8d78b93fcfb3e111a93f6437f9a6acfa.png)

如果是 ChatGPT Team 账号，则需要选择对应的工作空间。授权成功的页面如下：

![](https://img.072899.xyz/2025/09/86518a31294a769281c7c5ef8946550e.png)

回到终端命令行，可以看到认证文件已成功生成并保存。

![](https://img.072899.xyz/2025/09/c4c9613c9b086a9d8af70d0cf31d75f9.png)

如果你有多个 ChatGPT 账号，只需重复几次同样的操作即可。

需要注意的是，目前 Codex 需要付费的 ChatGPT 会员才能够使用，免费用户并没有权限哦。

### 配置 Gemini CLI [​](#%E9%85%8D%E7%BD%AE-gemini-cli)

接下来，我们来添加 Gemini CLI。Gemini CLI 是完全免费的，但有些用户在配置过程中可能会遇到问题。因此，在这里我将从创建 Google Cloud 项目开始，一步步带你完成整个授权认证过程。

首先，请用你的 Google 账号登录 [https://console.cloud.google.com/。登录成功后，点击图中所示位置：](https://console.cloud.google.com/%E3%80%82%E7%99%BB%E5%BD%95%E6%88%90%E5%8A%9F%E5%90%8E%EF%BC%8C%E7%82%B9%E5%87%BB%E5%9B%BE%E4%B8%AD%E6%89%80%E7%A4%BA%E4%BD%8D%E7%BD%AE%EF%BC%9A)

![](https://img.072899.xyz/2025/09/75416d68babdacc8ddd9bfd652a49b38.png)

点击“新建项目”。

![](https://img.072899.xyz/2025/09/566e57546c8bcd73d7ce41e56581b4a5.png)

给项目命名后，点击“创建”。

![](https://img.072899.xyz/2025/09/9e90a699265fc1dcfb7755f7c1858b73.png)

按照第一步的位置，选择刚刚创建的项目。

![](https://img.072899.xyz/2025/09/a84803f955e057f34723227bdf55b145.png)

先把红框内的项目 ID 复制下来备用，然后点击左上角箭头所指的位置。

![](https://img.072899.xyz/2025/09/c1d1617812ecea50c3a63dfb76eb5c04.png)

依次点击“API和服务” -&gt; “已启用的API和服务”。

![](https://img.072899.xyz/2025/09/782d8096de6276f24fc8ca444ee2910d.png)

点击“启用API和服务”。

![](https://img.072899.xyz/2025/09/1c0e48d7434bc76d37ef769d86684595.png)

在图示的搜索框内输入 `cloudaicompanion.googleapis.com`，然后点击搜索到的“Gemini for Google Cloud”。

![](https://img.072899.xyz/2025/09/a52b17b80635df9e46b8d5b49957e3d6.png)

点击“启用”。

![](https://img.072899.xyz/2025/09/58afcf1004138c4c1d63474030d49dff.png)

至此，Google Cloud 前期的准备工作就全部完成了。现在，我们回到 CLIProxyAPI 程序所在的目录，打开终端命令行，输入 `cli-proxy-api --login --project_id [你的项目ID]`。例如，在本例中就是 `cli-proxy-api --login --project_id mimetic-planet-473413-v7`。

随后会弹出授权页面，请使用刚才完成准备工作的 Google 账号登录。

![](https://img.072899.xyz/2025/09/51ca74eb061751336d110b3421c43548.png)

验证成功的页面如下：

![](https://img.072899.xyz/2025/09/346f6add9a943f0c324afbad856cc3bf.png)

回到终端命令行，可以看到认证文件已被成功保存。

![](https://img.072899.xyz/2025/09/8682dc8a08bffd34d7900819e1073960.png)

有些读者可能会好奇，为什么 Codex 和 Gemini CLI 在验证成功后的命令行信息，与 Qwen 有所不同？答案是，在验证 Codex 和 Gemini CLI 时，CLIProxyAPI 会在本地监听一个特定端口以接收回调，因此验证总是一次成功。而在验证 Qwen 时，CLIProxyAPI 会直接从 Qwen 的验证服务器来获取授权信息，因此最多会有 60 次的尝试请求。

### 验证模型 [​](#%E9%AA%8C%E8%AF%81%E6%A8%A1%E5%9E%8B)

我们再来验证一下刚才通过 OAuth 添加的 Codex 和 Gemini CLI。在 Cherry Studio 中添加模型，如下所示：

![](https://img.072899.xyz/2025/09/db8e65c9548213303da43cc214ee5000.png)

试试 Gemini-2.5-Pro：

![](https://img.072899.xyz/2025/09/a2fc6ce45adcf334a2908984a8db428d.png)

再来问问 GPT-5-Codex：

![](https://img.072899.xyz/2025/09/c07a3dbd57f728186ad835fa5afdde6d.png)

至此，所有模型都已成功集成。你学会了吗？