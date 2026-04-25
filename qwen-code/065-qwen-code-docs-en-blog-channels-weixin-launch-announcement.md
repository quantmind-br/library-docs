---
title: 'Qwen Code Beta: Use AI to Write Code in Your WeChat Channel!'
url: https://qwenlm.github.io/qwen-code-docs/en/blog/channels-weixin-launch-announcement
source: github_pages
fetched_at: 2026-04-09T09:05:17.973350101-03:00
rendered_js: true
word_count: 596
summary: This document details how developers can utilize Qwen Code for coding assistance directly within WeChat channels, eliminating the need for traditional IDEs or terminals. It provides a comprehensive guide covering prerequisites, step-by-step configuration (connecting via QR code and editing settings), testing procedures, and advanced customization tips.
tags:
    - qwen-code
    - wechat-integration
    - ai-coding-assistant
    - development-workflow
    - configuration-guide
    - chatbot
category: tutorial
---

## Qwen Code Beta: Use AI to Write Code in Your WeChat Channel!

> **Great news for developers!** Starting today, Qwen Code officially supports WeChat channel functionality. No need to open a terminal or IDE—just send a message in WeChat, and let the AI assistant help you write code, check documentation, and solve technical problems. Attention, attention! This is not crayfish, this is Qwen Code’s Channel feature! Fresh out of the oven: [https://github.com/QwenLM/qwen-code/pull/2628](https://github.com/QwenLM/qwen-code/pull/2628)

* * *

## 💡 Real-World Scenario Testing, Just to Spark Ideas\![](#-real-world-scenario-testing-just-to-spark-ideas)

While eating in the cafeteria, I suddenly received a new GitHub issue notification. With the channel feature, I can just take a screenshot and send it to WeChat, then WeChat starts my local Qwen Code, and I begin a pleasant journey of community Q&A!

![](https://img.alicdn.com/imgextra/i1/O1CN01UsiEbV1iFT5QGXI7m_!!6000000004383-2-tps-3340-1640.png)

## 🎯 Why Do You Need a WeChat Channel?[](#-why-do-you-need-a-wechat-channel)

![WeChat Channel Core Concept Diagram](https://img.alicdn.com/imgextra/i4/O1CN01p9WUdg27Z2P6L8UTB_!!6000000007810-0-tps-1376-768.jpg)

As a developer, do you often encounter these scenarios:

- **During your commute**, you suddenly think of a bug solution and want AI to help verify your approach immediately
- **Between meetings**, you need to quickly check API usage but don’t want to open your computer
- **Late at night**, inspiration strikes while lying in bed, and you want AI to generate a code framework for you
- **While traveling**, you encounter an urgent online issue and need to help colleagues troubleshoot remotely

Previously, you had to open your computer and start a terminal to use Qwen Code. Now, **your WeChat is your development environment**.

* * *

## 🚀 Quick Start Guide[](#-quick-start-guide)

### Prerequisites[](#prerequisites)

Make sure you have:

- ✅ Installed the preview version of Qwen Code `npm i @qwen-code/qwen-code@0.14.0-preview.0 -g`
- ✅ Prepared a WeChat account that can receive messages

> In the AI era, who still configures parameters manually? You just need `npx skills add https://github.com/QwenLM/qwen-code-examples --skill weixin-channel-setup` to install this weixin-channel-setup Skill, then open Qwen and ask it: `{'/'}skills weixin-channel-setup Please help me configure`

If you prefer the traditional configuration method, refer to the three steps below:

![Three-step Configuration Flowchart](https://img.alicdn.com/imgextra/i4/O1CN01aWJWAF1YwqRJ6ryra_!!6000000003124-0-tps-1376-768.jpg)

### Step 1: Scan to Connect[](#step-1-scan-to-connect)

Run in terminal:

```
qwen channel configure-weixin
```

There’s a “QR code URL” in the terminal. Copy the link and open it in your browser, then scan with WeChat.

- You may be prompted to install WeChat After successful scanning, you’ll see:

```
Connected to WeChat successfully!
Credentials saved. You can now start a weixin channel with:
  qwen channel start <name>
```

At this point, your WeChat credentials have been securely saved locally.

### Step 2: Configure Channel[](#step-2-configure-channel)

Edit `~/.qwen/settings.json` and add the following configuration:

```
"channels": {
    "my-weixin": {
      "type": "weixin",
      "senderPolicy": "open",
      "sessionScope": "user",
      "model": "qwen3.5-plus",
      "instructions": "You are a concise coding assistant responding via WeChat. Keep responses under 500 characters. Use plain text only."
    }
  }
```

### Step 3: Start and Test[](#step-3-start-and-test)

```
qwen channel start my-weixin
```

After seeing the `[Channel] "my-weixin" is running.` prompt, open WeChat:

1. Find your bot assistant (the one you just scanned)
2. Send a message: “Hello, help me write a Python Hello World”
3. Wait for the response…

🎉 **Congratulations! You can now write code using WeChat!**

* * *

## 🔧 Advanced Tips[](#-advanced-tips)

### 1. Customize AI Persona[](#1-customize-ai-persona)

Through the `instructions` field, you can create your own AI assistant:

```
{
  "instructions": "You are a senior TypeScript engineer. When answering questions:\n1. Prioritize runnable code examples\n2. Explain key design decisions\n3. Point out potential edge cases\n4. Keep a professional but friendly tone"
}
```

### 2. Auto-start on Boot[](#2-auto-start-on-boot)

Honestly, asking Qwen Code about this might work better—let it help you configure~

More features await your contribution!

* * *

## 📢 Feedback and Suggestions[](#-feedback-and-suggestions)

We value your experience! If you encounter any issues or have new feature suggestions during use, feel free to provide feedback through:

- 🐛 **Report Bugs**: [GitHub Issues](https://github.com/QwenLM/qwen-code/issues)
- 💡 **Feature Suggestions**: [GitHub Discussions](https://github.com/QwenLM/qwen-code/discussions)
- 💬 **Community Discussion**: Join our developer community

* * *

## 🎁 Conclusion[](#-conclusion)

![](https://img.alicdn.com/imgextra/i2/O1CN01LLNV5D1Wz15PztdB3_!!6000000002858-2-tps-2642-996.png)

Our vision is to create a group of truly autonomous AI employees in the AI era—omnipotent beings that can completely liberate our productivity, allowing us to enjoy life and create fun in grasslands, mountains, valleys, meadows, and beaches.

**In the future, we also plan to support:**

- 📱 DingTalk, Feishu, and other enterprise IM platforms
- 🤖 Voice input support, more media format processing

These features are important but may not be our priority. We heavily rely on community co-building. We look forward to your participation!